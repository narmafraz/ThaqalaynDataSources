# altafsir.com

Scraped tafsir (Quranic exegesis) text from altafsir.com, a digital tafsir
library maintained by the Royal Aal al-Bayt Institute for Islamic Thought.

## Source

- **URL:** https://www.altafsir.com
- **Publisher:** Royal Aal al-Bayt Institute for Islamic Thought (Jordan)
- **Terms:** Academic and non-commercial use
- **Language:** Arabic (original text)
- **Encoding:** Windows-1256 (must decode correctly when fetching)

## What's here

Each subdirectory is named by the numeric tafsir ID used on altafsir.com.
These are all **Shia tafsirs** (madhab ID 4 on the site):

| ID | Tafsir (EN) | Tafsir (AR) | Author | Death |
|----|-------------|-------------|--------|-------|
| 3 | Majma' al-Bayan | مجمع البيان | al-Tabarsi | 548 AH |
| 38 | Tafsir al-Qummi | تفسير القرآن | Ali ibn Ibrahim al-Qummi | 329 AH |
| 39 | Al-Tibyan | التبيان | Sheikh al-Tusi | 460 AH |
| 40 | Mulla Sadra | تفسير صدر المتألهين | Sadr al-Muta'allihin (Mulla Sadra) | 1059 AH |
| 42 | Bayan al-Saadah | بيان السعادة | Sultan Muhammad al-Junabadhi | 1327 AH |
| 110 | Al-Burhan | البرهان | Hashim al-Bahrani | 1107 AH |

Each `{id}/{surah}.json` file is plain pre-HTML Arabic text, one file per
surah, in a block-reference format (multiple ayahs often share the same
commentary block). See schema below.

## How to re-scrape

Scraping is driven by `app/scrapers/scrape_altafsir.py` in
ThaqalaynDataGenerator:

```bash
cd ThaqalaynDataGenerator
# List available Shia tafsirs
python app/scrapers/scrape_altafsir.py --list

# Scrape one tafsir (all 114 surahs)
python app/scrapers/scrape_altafsir.py --tafsir 38    # al-Qummi

# Scrape one surah of one tafsir (for testing)
python app/scrapers/scrape_altafsir.py --tafsir 56 --surah 1

# Scrape everything
python app/scrapers/scrape_altafsir.py
```

Rate-limited to 0.2 sec/request (~1 minute per surah average).
The scraper is resume-safe — re-running skips surahs already saved.

## URL patterns (for reference)

- Tafsir page: `https://www.altafsir.com/Tafasir.asp?tMadhNo=4&tTafsirNo={id}&tSoraNo={surah}&tAyahNo={ayah}&tDisplay=yes&Page={page}&Size=1&LanguageId=1`
- Long commentary spans multiple pages. `Page` parameter paginates (up to ~10
  pages per block for al-Mizan).
- Response HTML is in windows-1256; commentary lives inside
  `<Font class='TextResultArabic'><font color=black>…</font></Font>`.

## Schema

```json
{
  "tafsir_id": 38,
  "edition_id": "ar.qummi",
  "surah": 2,
  "blocks": [
    "Plain Arabic commentary text, paragraphs separated by \\n\\n …"
  ],
  "ayahs": [
    {"ayah": 1, "block": 0},
    {"ayah": 2, "block": 0},
    ...
  ]
}
```

Not every ayah has a matching block — sparse tafsirs (al-Qummi, Mulla Sadra)
only cover some ayahs, so the `ayahs` array may skip numbers.

## Consumed by

- `app/altafsir_converter.py` in ThaqalaynDataGenerator — converts plain text
  to HTML and writes block-ref format to ThaqalaynTafsirData
  (https://thaqalayntafsir.netlify.app)

## Tafsirs NOT scraped (intentionally)

Two additional Shia tafsirs are available on altafsir.com but are **not**
scraped here because ThaqalaynTafsirData already has better versions from
the app-furqan SQLite source:

- ID 41: Al-Safi (Fayz Kashani) — have app-furqan `ar.safi`
- ID 56: Al-Mizan (Tabatabai) — have app-furqan `ar.mizan`
