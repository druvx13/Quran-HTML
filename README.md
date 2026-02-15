# Unicode Qur'an

This is an independent website presenting the complete Holy Qur'an in Unicode Arabic with IPA (International Phonetic Alphabet) transliteration.

## Contents

- **index.html** - Main index page with links to all 114 surahs and English translations
- **001.html - 114.html** - Individual surahs (chapters) of the Qur'an with Arabic Unicode and IPA transliteration
- **xlit.html** - Transliteration table explaining the IPA system used
- **arabic.jpg** - Arabic calligraphy image
- **css/marg.css** - Stylesheet for the website
- **fonts/** - Directory containing Amiri font files for beautiful Arabic typography
- **translations/** - English translations of the Qur'an:
  - **pickthall/** - Pickthall translation (1938)
  - **yusuf-ali/** - Yusuf Ali translation with commentary
  - **rodwell/** - Rodwell translation (1876)
  - **palmer/** - Palmer translation (1880, Sacred Books of the East)
- **Quran_Pickthall_Translation.pdf** - Complete Pickthall translation in PDF format (all 114 surahs)
- **Quran_Palmer_Translation.pdf** - Complete Palmer translation in PDF format (Sacred Books of the East, Volumes 6 & 9)

## Features

- **Amiri Font**: Uses the beautiful Amiri typeface, a classical Arabic font in Naskh style specifically designed for Quranic text
- **Unicode Arabic Text**: The Qur'an is displayed using Unicode characters for proper Arabic rendering
- **IPA Transliteration**: Each verse includes a mechanical letter-by-letter transliteration into International Phonetic Alphabet
- **Multiple English Translations**: Four complete English translations included:
  - **Pickthall** (1938) - The Meaning of the Glorious Qur'ân by M.M. Pickthall
  - **Yusuf Ali** - The Holy Qur'ân: Text, Translation and Commentary
  - **Rodwell** (1876) - The Koran translated by J.M. Rodwell
  - **Palmer** (1880) - The Qur'ân from Sacred Books of the East by E.H. Palmer
- **Simple Navigation**: Navigate between surahs using Previous/Next links and the main index
- **Clean Layout**: Minimal design focused on the content without external advertisements or tracking

## PDF Downloads

Complete PDF books of English translations are available:

### Pickthall Translation (1938)
**[Download Quran_Pickthall_Translation.pdf](Quran_Pickthall_Translation.pdf)** (1.1 MB)

This PDF contains "The Meaning of the Glorious Qur'ân" translated by Mohammed Marmaduke Pickthall (1938), formatted for easy reading and printing. Includes all 114 surahs.

### Palmer Translation (1880)
**[Download Quran_Palmer_Translation.pdf](Quran_Palmer_Translation.pdf)** (1.6 MB)

This PDF contains the complete E.H. Palmer translation from the Sacred Books of the East (Volumes 6 & 9), published in 1880. Includes:
- Part I and Part II title pages
- Complete introduction by E.H. Palmer
- Abstract of the contents of the Qur'ân
- All 114 surahs (chapters)
- Comprehensive index
- Errata

Both PDFs are professionally formatted for reading, studying, and printing.

## Usage

To view the website locally:

1. Open `index.html` in a web browser
2. Or serve the directory with any HTTP server:
   ```bash
   python3 -m http.server 8080
   ```
   Then visit http://localhost:8080

## Note on Transliteration

The IPA transliteration is NOT a pronunciation guide. Rather, it is a mechanical conversion of the Arabic, letter by letter, into equivalent IPA characters. The Arabic text should be treated as primary, and the transliteration as a study aid.

## Typography

This website uses the **Amiri font** (أميري), a classical Arabic typeface in Naskh style designed specifically for typesetting the Quran. Amiri is a revival of the beautiful typeface pioneered by Bulaq Press (Amiria Press) in early 20th century Cairo.

The Amiri font is included in the `fonts/` directory and is automatically loaded when you view the website. The font is licensed under the [SIL Open Font License (OFL)](fonts/OFL.txt), making it free to use and distribute.

**Font Features:**
- Classical Naskh calligraphic style
- Optimized for Quranic text with proper diacritical marks
- Excellent balance between traditional beauty and modern readability
- Includes AmiriQuran variant specifically designed for Quranic verses

## Source

This content was extracted from the Internet Sacred Text Archive's Unicode Qur'an collection and adapted to be a standalone, independent website.

## License

This project is licensed under the [MIT No Attribution (MIT-0) License](LICENSE).

**License Summary:**
- The **website code and compilation** are licensed under MIT-0, allowing unrestricted use without attribution requirements
- The **Amiri font files** in the `fonts/` directory are licensed under the [SIL Open Font License (OFL)](fonts/OFL.txt)
- The **Qur'anic text** and **historical translations** (Pickthall, Yusuf Ali, Rodwell, Palmer) are in the public domain

You are free to use, modify, and distribute this work for any purpose without restriction.
