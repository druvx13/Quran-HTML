# Qur'an PDF Generator

This script generates a high-quality, print-ready PDF book containing the complete Holy Qur'an with the Pickthall English Translation and Romanized Transliteration.

## Features

- **Complete Text**: All 114 Surahs with 6,236 verses
- **Dual Format**: 
  - Pickthall English Translation (elegant serif typography)
  - Romanized Transliteration (distinct font for easy pronunciation)
- **Professional Layout**:
  - A5 page size (standard book format)
  - Table of Contents with all Surah names
  - Clear Surah headers (Arabic name + English meaning + Number)
  - Verse numbers inline with text
  - Page numbers in footer
  - Visual hierarchy between transliteration and translation

## Usage

Simply run the Python script:

```bash
python3 generate_quran_pdf.py
```

The PDF will be generated as `Qur'an_Pickthall_Transliteration_Complete.pdf` in the repository root directory.

## Requirements

- Python 3.6+
- reportlab
- beautifulsoup4
- lxml

Install dependencies with:

```bash
pip3 install reportlab beautifulsoup4 lxml
```

## Output

- **File**: `Qur'an_Pickthall_Transliteration_Complete.pdf`
- **Size**: ~1 MB
- **Pages**: ~666 pages
- **Format**: A5 (148 × 210 mm / 5.83 × 8.27 inches)

## Data Sources

The script parses data from:
- `/translations/pickthall/*.html` - Pickthall English translations
- `/*.html` - Arabic text with romanized transliteration

## Design Philosophy

The PDF is designed for readability and beauty:
- **Transliteration**: Bold Courier font, indented, with verse numbers
- **Translation**: Regular Times-Roman serif font, justified alignment
- **Headers**: Centered, bold, with clear hierarchy
- **Spacing**: Generous margins and line spacing for comfortable reading

## Data Integrity

The script includes validation to ensure:
- All 114 Surahs are loaded
- All verses are properly extracted and numbered
- UTF-8 encoding is preserved for special characters
- No data is omitted or altered from source files
