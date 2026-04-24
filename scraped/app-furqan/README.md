# app-furqan / quran-app-data

SQLite databases containing Shia tafsir (Quranic exegesis) editions in
Arabic, Farsi, English, and Urdu.

## Source

- **Repository:** https://github.com/app-furqan/quran-app-data
- **License:** CC BY-ND 4.0 (Attribution, NoDerivatives)
- **Original use:** Data for the "Quran - Furqan" mobile application

## What's committed vs extracted

Only the `.tar.xz` archives (~40 MB total) are committed to this repo.
The extracted `.db` SQLite databases (~253 MB) are **gitignored** and must
be extracted before running the tafsir converter.

## First-time setup — extract archives

```bash
cd ThaqalaynDataSources/scraped/app-furqan
for f in *.tar.xz; do tar xf "$f"; done
```

This creates the `.db` files (plus `database/tafsir_almizan_fa.db`) that
`app/tafsir_converter.py` in ThaqalaynDataGenerator consumes.

## Re-download from source (if archives are missing)

```bash
cd ThaqalaynDataSources/scraped/app-furqan
for f in \
  tafsir_almizan_ar.db.tar.xz \
  tafsir_almizan_en.db.tar.xz \
  tafsir_almizan_fa.db.tar.xz \
  tafsir_nemouneh_fa_en_ur.tar.xz \
  tafsir-noor.tar.xz \
  tafsir_safi_ar_en_ur.db.tar.xz ; do
    curl -L -O "https://github.com/app-furqan/quran-app-data/raw/main/data/$f"
done
```

## Files

| Archive | Extracts to | Contents |
|---------|-------------|----------|
| `tafsir_almizan_ar.db.tar.xz` | `tafsir_almizan_ar.db` | Al-Mizan (Arabic original) |
| `tafsir_almizan_en.db.tar.xz` | `tafsir_almizan_en.db` | Al-Mizan (English translation) |
| `tafsir_almizan_fa.db.tar.xz` | `database/tafsir_almizan_fa.db` | Al-Mizan (Farsi translation) |
| `tafsir_nemouneh_fa_en_ur.tar.xz` | `tafsir_namouneh.db` | Tafsir Nemooneh (Farsi, English, Urdu) |
| `tafsir-noor.tar.xz` | `tafsir-noor.db` | Tafsir Noor (Farsi, English, Urdu) |
| `tafsir_safi_ar_en_ur.db.tar.xz` | `tafsir_safi_ar.db` | Tafsir as-Safi (Arabic, English, Urdu) |

## Schema

Each database has three key tables:

- `ayah_mapping (id, surah_number, ayah_number, content_id)`:
  maps each ayah to a `content_id`
- `content (content_id, content [, content_en, content_ur])`:
  stores the commentary text (Markdown with `~~~arabic` / `~~~english` code blocks);
  multi-language DBs have `content_en` and `content_ur` columns too
- `muqadimah`: introductory preface (not consumed by our converter)

Multiple ayahs often share the same `content_id` (e.g., al-Mizan discusses
verse groups together). Our converter preserves this via block-reference
format in the output JSON.

## Consumed by

- `app/tafsir_converter.py` in ThaqalaynDataGenerator
- Output goes to ThaqalaynTafsirData (deployed at
  https://thaqalayntafsir.netlify.app)
