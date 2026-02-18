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
  - **unified/** - Unified translation with Arabic, IPA, romanization, and English (Yusuf Ali)
    - **[quran-complete.pdf](translations/unified/quran-complete.pdf)** - Complete Quran as a single PDF (6.8 MB)
    - **[quran-complete.html](translations/unified/quran-complete.html)** - Complete Quran as a single HTML file
  - **pickthall/** - Pickthall translation (1938)
  - **yusuf-ali/** - Yusuf Ali translation with commentary
  - **rodwell/** - Rodwell translation (1876)
  - **palmer/** - Palmer translation (1880, Sacred Books of the East)

## Features

- **Complete PDF Version**: Download the entire Quran with Arabic text (using system fonts for proper rendering), English surah names, IPA transliteration, romanization, and English translation as a single PDF file (6.8 MB) from the [unified translation directory](translations/unified/)
- **Unicode Arabic Text**: The Qur'an is displayed using Unicode characters for proper Arabic rendering
- **IPA Transliteration**: Each verse includes a mechanical letter-by-letter transliteration into International Phonetic Alphabet
- **Multiple English Translations**: Four complete English translations included:
  - **Pickthall** (1938) - The Meaning of the Glorious Qur'ân by M.M. Pickthall
  - **Yusuf Ali** - The Holy Qur'ân: Text, Translation and Commentary
  - **Rodwell** (1876) - The Koran translated by J.M. Rodwell
  - **Palmer** (1880) - The Qur'ân from Sacred Books of the East by E.H. Palmer
- **Simple Navigation**: Navigate between surahs using Previous/Next links and the main index
- **Clean Layout**: Minimal design focused on the content without external advertisements or tracking

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
