#!/usr/bin/env python3
"""
Generate a complete PDF of the Quran from the unified translation directory.
Includes Arabic text, IPA transliteration, romanization, and English translation.
"""

import os
from pathlib import Path
from weasyprint import HTML, CSS
from bs4 import BeautifulSoup

def extract_surah_content(html_file):
    """Extract the surah content from an HTML file."""
    with open(html_file, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
    
    # Extract the title
    title = soup.find('h1')
    subtitle = soup.find('h2')
    
    # Extract the table with verses
    table = soup.find('table', {'width': '100%', 'border': '1'})
    
    return title, subtitle, table

def create_combined_html():
    """Create a combined HTML file from all surahs in the unified directory."""
    unified_dir = Path('/home/runner/work/Quran-HTML/Quran-HTML/translations/unified')
    css_path = Path('/home/runner/work/Quran-HTML/Quran-HTML/css/marg.css')
    
    # Read the CSS file
    css_content = ""
    if css_path.exists():
        with open(css_path, 'r', encoding='utf-8') as f:
            css_content = f.read()
    
    # Start building the HTML
    html_content = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>The Holy Quran - Complete Unified Translation</title>
    <style>
        {css_content}
        
        /* Additional PDF-specific styles */
        body {{
            font-family: 'Amiri', 'Arial Unicode MS', Arial, sans-serif;
            margin: 2cm;
            line-height: 1.6;
        }}
        
        h1 {{
            text-align: center;
            font-size: 24pt;
            margin-top: 20pt;
            page-break-before: always;
        }}
        
        h1:first-of-type {{
            page-break-before: avoid;
        }}
        
        h2 {{
            text-align: center;
            font-size: 18pt;
            margin-bottom: 20pt;
        }}
        
        table {{
            width: 100%;
            border-collapse: collapse;
            margin-bottom: 10pt;
            page-break-inside: avoid;
        }}
        
        td {{
            padding: 8pt;
            border: 1px solid #ccc;
        }}
        
        .cover {{
            text-align: center;
            padding: 100pt 0;
            page-break-after: always;
        }}
        
        .cover h1 {{
            font-size: 36pt;
            margin-bottom: 20pt;
            page-break-before: avoid;
        }}
        
        .cover h2 {{
            font-size: 24pt;
            margin-bottom: 10pt;
        }}
        
        .cover p {{
            font-size: 14pt;
            margin: 10pt 0;
        }}
        
        .toc {{
            page-break-after: always;
        }}
        
        .toc h2 {{
            font-size: 28pt;
            margin-bottom: 30pt;
        }}
        
        .toc ul {{
            list-style-type: none;
            padding: 0;
        }}
        
        .toc li {{
            margin: 5pt 0;
            font-size: 12pt;
        }}
        
        /* Ensure Arabic text displays correctly */
        [dir="rtl"] {{
            direction: rtl;
            text-align: right;
        }}
        
        /* Keep verse groups together */
        .verse-group {{
            page-break-inside: avoid;
        }}
    </style>
</head>
<body>
    <div class="cover">
        <h1>The Holy Quran</h1>
        <h2>القرآن الكريم</h2>
        <p><b>Complete Unified Translation</b></p>
        <p>Arabic Text • IPA Transliteration • Romanization • English Translation</p>
        <p style="margin-top: 40pt; font-size: 12pt;">
            This edition contains the complete text of all 114 surahs of the Holy Quran<br>
            with parallel Arabic text, International Phonetic Alphabet (IPA) transliteration,<br>
            romanization, and English translation.
        </p>
    </div>
"""
    
    # Add table of contents
    html_content += '    <div class="toc">\n        <h2>Table of Contents</h2>\n        <ul>\n'
    
    # Generate TOC entries by reading each file
    for i in range(1, 115):
        html_file = unified_dir / f"{i:03d}.html"
        if html_file.exists():
            with open(html_file, 'r', encoding='utf-8') as f:
                soup = BeautifulSoup(f.read(), 'html.parser')
                title = soup.find('h1')
                if title:
                    # Extract surah name from title
                    title_text = title.get_text(strip=True)
                    # Remove just the number at the start if present
                    if '. ' in title_text:
                        title_text = title_text.split('. ', 1)[1] if '. ' in title_text else title_text
                    html_content += f'            <li>{i}. {title_text}</li>\n'
    
    html_content += '        </ul>\n    </div>\n\n'
    
    # Process each surah file
    for i in range(1, 115):
        html_file = unified_dir / f"{i:03d}.html"
        
        if not html_file.exists():
            print(f"Warning: {html_file} not found, skipping...")
            continue
        
        print(f"Processing Surah {i}...")
        
        title, subtitle, table = extract_surah_content(html_file)
        
        if title:
            html_content += f"    <h1>{title.get_text(strip=True)}</h1>\n"
        
        if subtitle:
            html_content += f"    <h2>{subtitle.get_text(strip=True)}</h2>\n"
        
        if table:
            # Modify the table to group verse rows together
            rows = table.find_all('tr')
            html_content += '    <table>\n'
            
            # Process rows in groups of 4 (Arabic, IPA, Romanization, English)
            for j in range(0, len(rows), 4):
                if j + 3 < len(rows):
                    html_content += '    <tbody class="verse-group">\n'
                    for k in range(4):
                        row = rows[j + k]
                        html_content += '        ' + str(row) + '\n'
                    html_content += '    </tbody>\n'
                else:
                    # Handle remaining rows
                    for k in range(j, min(j + 4, len(rows))):
                        if k < len(rows):
                            html_content += '        ' + str(rows[k]) + '\n'
            
            html_content += '    </table>\n\n'
    
    html_content += """</body>
</html>"""
    
    # Save the combined HTML
    output_html = Path('/home/runner/work/Quran-HTML/Quran-HTML/translations/unified/quran-complete.html')
    with open(output_html, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"Combined HTML saved to: {output_html}")
    return output_html

def generate_pdf(html_file):
    """Generate PDF from HTML file."""
    pdf_file = html_file.with_suffix('.pdf')
    
    print(f"Generating PDF: {pdf_file}")
    print("This may take a few minutes...")
    
    # Generate the PDF
    HTML(filename=str(html_file)).write_pdf(pdf_file)
    
    print(f"PDF generated successfully: {pdf_file}")
    return pdf_file

def main():
    print("Creating combined HTML from all surahs...")
    html_file = create_combined_html()
    
    print("\nGenerating PDF...")
    pdf_file = generate_pdf(html_file)
    
    print(f"\n✓ Complete!")
    print(f"  HTML: {html_file}")
    print(f"  PDF:  {pdf_file}")
    
    # Print file size
    pdf_size = os.path.getsize(pdf_file) / (1024 * 1024)  # MB
    print(f"  Size: {pdf_size:.2f} MB")

if __name__ == '__main__':
    main()
