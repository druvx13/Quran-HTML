#!/usr/bin/env python3
"""
Generate a complete PDF of the Quran from the unified translation directory.
Includes Arabic text, IPA transliteration, romanization, and English translation.
"""

import os
from pathlib import Path
from weasyprint import HTML, CSS
from bs4 import BeautifulSoup
import html

# English names for all 114 surahs
SURAH_ENGLISH_NAMES = {
    1: "Fātiḥa, or the Opening Chapter",
    2: "Baqara, or the Heifer",
    3: "Āl-i-'Imrān, or The Family of 'Imrān",
    4: "Nisāa, or The Women",
    5: "Māïda, or The Table Spread",
    6: "An'ām, or Cattle",
    7: "A'rāf, or the Heights",
    8: "Anfāl, or the Spoils of War",
    9: "Tauba (Repentance) or Barāat (Immunity)",
    10: "Yūnus, or Jonah",
    11: "Hūd (The Prophet Hūd)",
    12: "Yūsuf, or Joseph",
    13: "Ra'd or Thunder",
    14: "Ibrāhīm, or Abraham",
    15: "Al-Hijr, or The Rocky Tract",
    16: "Naḥl or The Bee",
    17: "Banī Isrā-īl, or the Children of Israel",
    18: "Kahf, or the Cave",
    19: "Maryam, or Mary",
    20: "Ṭā-Hā (Mystic Letters, Ṭ. H.)",
    21: "Anbiyāa, or The Prophets",
    22: "Ḥajj, or The Pilgrimage",
    23: "Mū-minūn",
    24: "Nūr, or Light",
    25: "Furqān, or The Criterion",
    26: "Shu'arāa, or The Poets",
    27: "Naml, or the Ants",
    28: "Qaṣaṣ, or the Narration",
    29: "'Ankabūt, or the Spider",
    30: "Rūm, or The Roman Empire",
    31: "Luqmān (the Wise)",
    32: "Sajda, or Adoration",
    33: "Aḥzāb, or The Confederates",
    34: "Sabā, or the City of Sabā",
    35: "Fāṭir, or The Originator of Creation; or Malāïka, or The Angels",
    36: "Yā-Sīn (being Abbreviated Letters)",
    37: "Ṣāffāt, or Those Ranged in Ranks",
    38: "Ṣād (being one of the Abbreviated Letters)",
    39: "Zumar, or the Crowds",
    40: "Mū-min, or The Believer",
    41: "Hā-mīm (Abbreviated Letters), or Ḥā-Mīm Sajda, or Fuṣṣilat",
    42: "Shūrā, or Consultation",
    43: "Zukhruf, or Gold Adornments",
    44: "Dukhān, or Smoke (or Mist)",
    45: "Jathiya, or Bowing the Knee",
    46: "Aḥqāf, or Winding Sand-tracts",
    47: "Muḥammad (the Prophet)",
    48: "Fat-ḥ or Victory",
    49: "Ḥujurāt, or the Inner Apartments",
    50: "Qāf",
    51: "Zāriyāt, or the Winds That Scatter",
    52: "Ṭūr, or the Mount",
    53: "Najm, or the Star",
    54: "Qamar, or the Moon",
    55: "Raḥmān, or (God) Most Gracious",
    56: "Wāqi'a, or The Inevitable Event",
    57: "Ḥadīd, or Iron",
    58: "Mujādila, or The Woman who Pleads",
    59: "Ḥashr, or the Gathering",
    60: "Mumtaḥana, or the Woman to be Examined",
    61: "Ṣaff, or Battle Array",
    62: "Jumu'a, or the Assembly (Friday) Prayer",
    63: "Munāfiqūn, or the Hypocrites",
    64: "Tagābun, or Mutual Loss and Gain",
    65: "Ṭalāq, or Divorce",
    66: "Taḥrīm, or Holding (something) to be Forbidden",
    67: "Mulk, or Dominion",
    68: "Qalam, or the Pen, or Nūn",
    69: "Ḥāqqa, or the Sure Reality",
    70: "Ma'ārij, or the Ways of Ascent",
    71: "Nūḥ, or Noah",
    72: "Jinn, or the Spirits",
    73: "Muzzammil, or Folded in Garments",
    74: "Muddaththir, or One Wrapped Up",
    75: "Qiyāmat, or the Resurrection",
    76: "Dahr, or Time, or Insān, or Man",
    77: "Mursalāt, or Those Sent Forth",
    78: "Nabaa, or The (Great) News",
    79: "Nāzi'āt, or Those Who Tear Out",
    80: "'Abasa, or He Frowned",
    81: "Takwīr, or the Folding Up",
    82: "Infiṭār, or The Cleaving Asunder",
    83: "Taṭfīf, or Dealing in Fraud",
    84: "Inshiqāq, or The Rending Asunder",
    85: "Burūj, or The Zodiacal Signs",
    86: "Ṭāriq, or The Night-Visitant",
    87: "A'lā, or the Most High",
    88: "Gāshiya, or the Overwhelming Event",
    89: "Fajr, or the Break of Day",
    90: "Balad, or The City",
    91: "Shams, or The Sun",
    92: "Lail, or The Night",
    93: "Duhā, or The Glorious Morning Light",
    94: "Inshirāḥ, or The Expansion",
    95: "Tīn, or The Fig",
    96: "Iqraa, or Read! or Proclaim! Or 'Alaq, or The Clot of Congealed Blood",
    97: "Qadr, or The Night of Power (or Honour)",
    98: "Baiyina, or The Clear Evidence",
    99: "Zilzāl, or The Convulsion",
    100: "'Adiyāt, or Those that run",
    101: "Al-Qāri'a, or The Day of Noise and Clamour",
    102: "Takathur or Piling Up",
    103: "'Aṣr, or Time through the Ages",
    104: "Humaza, or the Scandal-monger",
    105: "Fīl, or The Elephant",
    106: "The Quraish, (Custodians of the Ka'ba)",
    107: "Mā'ūn, or Neighbourly Needs",
    108: "Kauthar, or Abundance",
    109: "Kāfirūn, or Those who reject Faith",
    110: "Naṣr, or Help",
    111: "Lahab, or (the Father of) Flame",
    112: "Ikhlāṣ, or Purity (of Faith)",
    113: "Falaq, or The Dawn",
    114: "Nās, or Mankind"
}

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
        /* Override any font specifications to allow system fonts for proper Arabic rendering */
        * {{
            font-family: inherit !important;
        }}
        
        {css_content}
        
        /* Additional PDF-specific styles - NO FONT RESTRICTIONS for proper Arabic rendering */
        body {{
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
            margin-bottom: 10pt;
        }}
        
        h3 {{
            text-align: center;
            font-size: 14pt;
            margin-bottom: 20pt;
            font-style: italic;
            color: #555;
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
                english_name = SURAH_ENGLISH_NAMES.get(i, "")
                if title:
                    # Extract surah name from title
                    title_text = title.get_text(strip=True)
                    # Remove just the number at the start if present
                    if '. ' in title_text:
                        title_text = title_text.split('. ', 1)[1] if '. ' in title_text else title_text
                    if english_name:
                        html_content += f'            <li>{i}. {title_text} — {english_name}</li>\n'
                    else:
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
        english_name = SURAH_ENGLISH_NAMES.get(i, "")
        
        if title:
            html_content += f"    <h1>{title.get_text(strip=True)}</h1>\n"
        
        if english_name:
            html_content += f"    <h3>{english_name}</h3>\n"
        
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
