# Unicode Qur'an

This is an independent website presenting the complete Holy Qur'an in Unicode Arabic with both IPA (International Phonetic Alphabet) and DIN31635 transliteration systems.

## Contents

- **index.html** - Main index page with links to all 114 surahs and English translations
- **001.html - 114.html** - Individual surahs (chapters) of the Qur'an with Arabic Unicode, IPA transliteration, and DIN31635 transliteration
- **xlit.html** - Transliteration table explaining both the IPA and DIN31635 systems used
- **arabic.jpg** - Arabic calligraphy image
- **css/marg.css** - Stylesheet for the website
- **fonts/** - Directory containing Amiri font files for beautiful Arabic typography
- **translations/** - English translations of the Qur'an:
  - **pickthall/** - Pickthall translation (1938)
  - **yusuf-ali/** - Yusuf Ali translation with commentary
  - **rodwell/** - Rodwell translation (1876)
  - **palmer/** - Palmer translation (1880, Sacred Books of the East)

## Features

- **Amiri Font**: Uses the beautiful Amiri typeface, a classical Arabic font in Naskh style specifically designed for Quranic text
- **Unicode Arabic Text**: The Qur'an is displayed using Unicode characters for proper Arabic rendering
- **Dual Transliteration System**: Each verse includes two transliteration systems:
  - **IPA Transliteration**: Mechanical letter-by-letter conversion into International Phonetic Alphabet for linguistic study
  - **DIN31635 Transliteration**: Phonetic transliteration following the German DIN 31635:1982 standard, showing only recited sounds for easier pronunciation learning
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

This website provides two different transliteration systems:

1. **IPA (International Phonetic Alphabet)**: A mechanical conversion of Arabic text, letter by letter, into equivalent IPA characters. This is NOT a pronunciation guide but rather a linguistic tool for precise character mapping.

2. **DIN31635**: A phonetic transliteration following the German standard DIN 31635:1982. This system shows only the sounds that are actually recited/pronounced during Quranic recitation, making it more practical and easier to read for those learning proper Arabic pronunciation.

The Arabic text should always be treated as primary, with both transliterations serving as study aids.

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
