#!/usr/bin/env python3
"""
Generate a high-quality PDF book of the Qur'an with Pickthall Translation and Romanized Transliteration
"""

import os
import sys
from bs4 import BeautifulSoup
from reportlab.lib.pagesizes import A5
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT, TA_RIGHT
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus.tableofcontents import TableOfContents

# Paths
BASE_DIR = '/home/runner/work/Quran-HTML/Quran-HTML'
TRANSLATION_DIR = os.path.join(BASE_DIR, 'translations', 'pickthall')
TRANSLITERATION_DIR = BASE_DIR

class QuranData:
    """Class to parse and hold Qur'an data"""
    
    def __init__(self):
        self.surahs = []
    
    def parse_pickthall_translation(self, surah_num):
        """Parse Pickthall translation from HTML"""
        filename = os.path.join(TRANSLATION_DIR, f"{surah_num:03d}.html")
        
        if not os.path.exists(filename):
            print(f"Warning: Translation file not found: {filename}")
            return None
        
        with open(filename, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f.read(), 'html.parser')
        
        # Extract Surah name from H1 tag
        h1 = soup.find('h1')
        surah_info = {}
        if h1:
            text = h1.get_text()
            # Format: "1. al-Fatihah: The Opening"
            parts = text.split('.', 1)
            if len(parts) > 1:
                surah_info['number'] = int(parts[0].strip())
                rest = parts[1].strip()
                if ':' in rest:
                    arabic_name, english_name = rest.split(':', 1)
                    surah_info['arabic_name'] = arabic_name.strip()
                    surah_info['english_name'] = english_name.strip()
                else:
                    surah_info['name'] = rest
        
        # Extract verses
        ayahs = []
        for p in soup.find_all('p'):
            # Look for verse anchors
            anchor = p.find('a', {'name': lambda x: x and x.startswith('an_')})
            if anchor:
                verse_num = anchor.get_text().strip()
                # Get text after the anchor
                text = p.get_text()
                # Remove verse number from beginning
                text = text[len(verse_num):].strip()
                if text:
                    ayahs.append({
                        'number': int(verse_num),
                        'text': text
                    })
        
        surah_info['ayahs'] = ayahs
        return surah_info
    
    def parse_transliteration(self, surah_num):
        """Parse transliteration from HTML"""
        filename = os.path.join(TRANSLITERATION_DIR, f"{surah_num:03d}.html")
        
        if not os.path.exists(filename):
            print(f"Warning: Transliteration file not found: {filename}")
            return None
        
        with open(filename, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f.read(), 'html.parser')
        
        # Extract Surah name from H2 (transliterated name)
        h2 = soup.find('h2')
        translit_name = h2.get_text().strip() if h2 else ""
        
        # Extract transliterations - they are in italic tags within table cells
        ayahs = []
        table = soup.find('table')
        if table:
            rows = table.find_all('tr')
            current_ayah = None
            
            for row in rows:
                cell = row.find('td')
                if not cell:
                    continue
                
                # Check if this row has a verse anchor
                anchor = cell.find('a', {'name': lambda x: x and x.startswith('an_')})
                if anchor:
                    # This is the start of a new verse (Arabic text row)
                    if current_ayah:
                        ayahs.append(current_ayah)
                    verse_num = anchor.get_text().strip()
                    current_ayah = {
                        'number': int(verse_num),
                        'transliteration': ''
                    }
                elif current_ayah:
                    # Check if this row contains transliteration (italic tag)
                    italic = cell.find('i')
                    if italic:
                        current_ayah['transliteration'] = italic.get_text().strip()
            
            # Add last ayah
            if current_ayah:
                ayahs.append(current_ayah)
        
        return {
            'transliterated_name': translit_name,
            'ayahs': ayahs
        }
    
    def load_all_data(self):
        """Load all 114 Surahs"""
        print("Loading Qur'an data...")
        
        for surah_num in range(1, 115):
            print(f"  Loading Surah {surah_num}/114...", end='\r')
            
            # Parse translation
            translation_data = self.parse_pickthall_translation(surah_num)
            if not translation_data:
                continue
            
            # Parse transliteration
            translit_data = self.parse_transliteration(surah_num)
            
            # Merge data
            surah = {
                'number': translation_data.get('number', surah_num),
                'arabic_name': translation_data.get('arabic_name', ''),
                'english_name': translation_data.get('english_name', ''),
                'transliterated_name': translit_data.get('transliterated_name', '') if translit_data else '',
                'ayahs': []
            }
            
            # Merge ayahs
            translation_ayahs = {a['number']: a for a in translation_data.get('ayahs', [])}
            translit_ayahs = {a['number']: a for a in translit_data.get('ayahs', [])} if translit_data else {}
            
            all_verse_nums = sorted(set(list(translation_ayahs.keys()) + list(translit_ayahs.keys())))
            
            for verse_num in all_verse_nums:
                ayah = {
                    'number': verse_num,
                    'transliteration': translit_ayahs.get(verse_num, {}).get('transliteration', ''),
                    'translation': translation_ayahs.get(verse_num, {}).get('text', '')
                }
                surah['ayahs'].append(ayah)
            
            self.surahs.append(surah)
        
        print(f"\nLoaded {len(self.surahs)} Surahs successfully")
        
        # Validate
        total_ayahs = sum(len(s['ayahs']) for s in self.surahs)
        print(f"Total verses: {total_ayahs}")
        
        return True


class NumberedCanvas(canvas.Canvas):
    """Custom canvas for page numbers"""
    
    def __init__(self, *args, **kwargs):
        canvas.Canvas.__init__(self, *args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_number(num_pages)
            canvas.Canvas.showPage(self)
        canvas.Canvas.save(self)

    def draw_page_number(self, page_count):
        page_num = self._pageNumber
        text = f"Page {page_num} of {page_count}"
        self.setFont("Times-Roman", 9)
        self.drawCentredString(A5[0] / 2, 0.5 * inch, text)


class QuranPDFGenerator:
    """Generate PDF book of the Qur'an"""
    
    def __init__(self, quran_data):
        self.data = quran_data
        self.styles = getSampleStyleSheet()
        self.setup_styles()
        self.toc = TableOfContents()
    
    def setup_styles(self):
        """Setup custom styles for the document"""
        
        # Surah title style
        self.styles.add(ParagraphStyle(
            name='SurahTitle',
            parent=self.styles['Heading1'],
            fontSize=16,
            textColor=colors.HexColor('#2C3E50'),
            spaceAfter=12,
            alignment=TA_CENTER,
            fontName='Times-Bold'
        ))
        
        # Surah subtitle (transliterated name)
        self.styles.add(ParagraphStyle(
            name='SurahSubtitle',
            parent=self.styles['Heading2'],
            fontSize=12,
            textColor=colors.HexColor('#7F8C8D'),
            spaceAfter=20,
            alignment=TA_CENTER,
            fontName='Times-Italic'
        ))
        
        # Verse number style
        self.styles.add(ParagraphStyle(
            name='VerseNumber',
            parent=self.styles['Normal'],
            fontSize=9,
            textColor=colors.HexColor('#95A5A6'),
            fontName='Times-Bold'
        ))
        
        # Transliteration style (will use Courier as fallback for Gentium Plus)
        self.styles.add(ParagraphStyle(
            name='Transliteration',
            parent=self.styles['Normal'],
            fontSize=10,
            fontName='Courier-Bold',
            textColor=colors.HexColor('#34495E'),
            spaceAfter=6,
            leftIndent=20,
            rightIndent=20,
            alignment=TA_JUSTIFY
        ))
        
        # Translation style (elegant serif)
        self.styles.add(ParagraphStyle(
            name='Translation',
            parent=self.styles['Normal'],
            fontSize=11,
            fontName='Times-Roman',
            textColor=colors.black,
            spaceAfter=12,
            leftIndent=20,
            rightIndent=20,
            alignment=TA_JUSTIFY
        ))
        
        # TOC heading
        self.styles.add(ParagraphStyle(
            name='TOCHeading',
            parent=self.styles['Heading1'],
            fontSize=18,
            textColor=colors.HexColor('#2C3E50'),
            spaceAfter=30,
            alignment=TA_CENTER,
            fontName='Times-Bold'
        ))
    
    def create_toc_entry(self, surah):
        """Create a table of contents entry"""
        return f"{surah['number']}. {surah['arabic_name']}: {surah['english_name']}"
    
    def generate_pdf(self, output_filename):
        """Generate the complete PDF"""
        print(f"\nGenerating PDF: {output_filename}")
        
        # Create PDF document
        doc = SimpleDocTemplate(
            output_filename,
            pagesize=A5,
            rightMargin=0.75*inch,
            leftMargin=0.75*inch,
            topMargin=1*inch,
            bottomMargin=0.75*inch,
            title="The Holy Qur'an - Pickthall Translation with Transliteration",
            author="M.M. Pickthall (Translation)"
        )
        
        # Story elements
        story = []
        
        # Title page
        story.append(Spacer(1, 2*inch))
        title = Paragraph(
            "<b>The Holy Qur'an</b>",
            ParagraphStyle(
                name='MainTitle',
                fontSize=24,
                alignment=TA_CENTER,
                fontName='Times-Bold',
                textColor=colors.HexColor('#2C3E50'),
                spaceAfter=12
            )
        )
        story.append(title)
        
        subtitle = Paragraph(
            "Complete Arabic Text<br/>Pickthall English Translation<br/>with Romanized Transliteration",
            ParagraphStyle(
                name='Subtitle',
                fontSize=14,
                alignment=TA_CENTER,
                fontName='Times-Italic',
                textColor=colors.HexColor('#34495E')
            )
        )
        story.append(subtitle)
        story.append(PageBreak())
        
        # Table of Contents
        toc_title = Paragraph("Table of Contents", self.styles['TOCHeading'])
        story.append(toc_title)
        story.append(Spacer(1, 0.3*inch))
        
        # Add TOC entries
        for surah in self.data.surahs:
            toc_entry = Paragraph(
                f'<a href="#{surah["number"]}">{self.create_toc_entry(surah)}</a>',
                ParagraphStyle(
                    name='TOCEntry',
                    fontSize=10,
                    fontName='Times-Roman',
                    leftIndent=20,
                    spaceAfter=4
                )
            )
            story.append(toc_entry)
        
        story.append(PageBreak())
        
        # Add all Surahs
        for idx, surah in enumerate(self.data.surahs):
            print(f"  Adding Surah {surah['number']}/114 to PDF...", end='\r')
            
            # Surah title with bookmark
            title_text = f"<a name='{surah['number']}'/>{surah['number']}. {surah['arabic_name']}: {surah['english_name']}"
            story.append(Paragraph(title_text, self.styles['SurahTitle']))
            
            # Transliterated name
            if surah['transliterated_name']:
                story.append(Paragraph(surah['transliterated_name'], self.styles['SurahSubtitle']))
            
            story.append(Spacer(1, 0.2*inch))
            
            # Add verses
            for ayah in surah['ayahs']:
                # Transliteration (if available) with verse number
                if ayah['transliteration']:
                    translit = Paragraph(
                        f"<b>[{ayah['number']}]</b> <i>{ayah['transliteration']}</i>",
                        self.styles['Transliteration']
                    )
                    story.append(translit)
                
                # Translation with verse number if no transliteration
                if ayah['translation']:
                    if ayah['transliteration']:
                        # If we have transliteration, don't repeat verse number
                        translation = Paragraph(ayah['translation'], self.styles['Translation'])
                    else:
                        # If no transliteration, add verse number to translation
                        translation = Paragraph(f"<b>[{ayah['number']}]</b> {ayah['translation']}", self.styles['Translation'])
                    story.append(translation)
            
            # Page break after each Surah (except the last one)
            if idx < len(self.data.surahs) - 1:
                story.append(PageBreak())
        
        print(f"\n  Building PDF document...")
        
        # Build PDF with custom canvas for page numbers
        doc.build(story, canvasmaker=NumberedCanvas)
        
        print(f"✓ PDF generated successfully: {output_filename}")
        print(f"  File size: {os.path.getsize(output_filename) / 1024 / 1024:.2f} MB")


def main():
    """Main execution function"""
    print("="*60)
    print("Qur'an PDF Generator")
    print("Pickthall Translation with Romanized Transliteration")
    print("="*60)
    
    # Load data
    quran_data = QuranData()
    success = quran_data.load_all_data()
    
    if not success or len(quran_data.surahs) != 114:
        print(f"ERROR: Failed to load all 114 Surahs. Only {len(quran_data.surahs)} loaded.")
        return 1
    
    # Verify data integrity
    print("\nData Integrity Check:")
    for surah in quran_data.surahs:
        if not surah['ayahs']:
            print(f"  WARNING: Surah {surah['number']} has no verses!")
    
    # Generate PDF
    output_file = os.path.join(BASE_DIR, 'Qur\'an_Pickthall_Transliteration_Complete.pdf')
    generator = QuranPDFGenerator(quran_data)
    generator.generate_pdf(output_file)
    
    print("\n" + "="*60)
    print("PDF Generation Complete!")
    print("="*60)
    
    return 0


if __name__ == '__main__':
    sys.exit(main())
