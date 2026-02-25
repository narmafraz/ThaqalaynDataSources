# ThaqalaynDataSources

Source data repository for the Thaqalayn project. Contains scraped source data, AI pipeline configuration, and AI-generated content that feeds into ThaqalaynDataGenerator.

## Directory Structure

```
ThaqalaynDataSources/
  scraped/                   # Scraped source data (HTML, XML, JSON)
    tanzil_net/             # Quran text + 27 translations (XML/TXT)
    hubeali_com/            # Al-Kafi Vols 1-8, Basair al-Darajaat (HTML)
    thaqalayn_api/          # 25 book folders from ThaqalaynAPI (JSON)
    thaqalayn_net/          # 2020 site mirror (HTML) — used for Sarwar translation
    corrections/            # Manual JSON fixes for parser edge cases
    alhassanain_org/        # Usul al-Kafi Vols 1-3 (HTML) — future cross-validation
  ai-pipeline-data/         # AI pipeline configuration files
    glossary.json           # Islamic term glossary for AI prompts
    few_shot_examples.json  # Few-shot examples for AI content generation
    sample_verses.json      # 20 sample verse paths for testing
  ai-content/               # AI-generated content
    samples/                # Sample AI responses (manual + batch)
      requests/             # JSONL request files for Anthropic Batch API
      responses/            # Validated AI response JSON files
```

## Data Flow

```
ThaqalaynDataSources  -->  ThaqalaynDataGenerator  -->  ThaqalaynData  -->  Thaqalayn (Angular UI)
     (this repo)              (Python parsers)          (JSON API)         (web app)
```

## Usage

ThaqalaynDataGenerator reads from this repo via the `SOURCE_DATA_DIR` environment variable:

```bash
export SOURCE_DATA_DIR="../ThaqalaynDataSources/"
```

Or use the default (which assumes the standard sibling directory layout).

## Scraped Data Sources

| Directory | Source | Contents |
|-----------|--------|----------|
| `tanzil_net/` | tanzil.net | Quran text + 27 translations (XML/TXT) |
| `hubeali_com/` | hubeali.com | Al-Kafi Vols 1-8 HTML, Basair al-Darajaat, Book of Sulaym |
| `thaqalayn_api/` | thaqalayn-api.net | 25 book folders, each with `hadiths.json` |
| `thaqalayn_net/` | thaqalayn.net (2020 mirror) | 23 books as HTML pages |
| `corrections/` | Manual | JSON fixes for parser edge cases |
| `alhassanain_org/` | alhassanain.org | Usul al-Kafi Vols 1-3 (HTML) |

## Re-scraping Data

Data can be re-scraped using the scraper scripts in `ThaqalaynDataGenerator/app/scrapers/`. Set `SOURCE_DATA_DIR` to point scrapers' output here.
