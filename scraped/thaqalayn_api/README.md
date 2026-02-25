# ThaqalaynAPI Scraped Data

Raw hadith data scraped from the [ThaqalaynAPI](https://www.thaqalayn-api.net/) REST API,
which provides structured access to hadith collections from [thaqalayn.net](https://thaqalayn.net/).

Scraped: 2026-02-21

## Contents

25 book folders, each containing a `hadiths.json` file. Total: **18,945 hadiths**.

| Folder | Book | Author | Hadiths | Aspiration List |
|--------|------|--------|---------|-----------------|
| `man-la-yahduruhu-al-faqih-v1` | Man La Yahduruhu al-Faqih Vol 1 | al-Saduq | 1,569 | Yes (Four Books) |
| `man-la-yahduruhu-al-faqih-v2` | Man La Yahduruhu al-Faqih Vol 2 | al-Saduq | 1,696 | Yes (Four Books) |
| `man-la-yahduruhu-al-faqih-v3` | Man La Yahduruhu al-Faqih Vol 3 | al-Saduq | 1,758 | Yes (Four Books) |
| `man-la-yahduruhu-al-faqih-v4` | Man La Yahduruhu al-Faqih Vol 4 | al-Saduq | 964 | Yes (Four Books) |
| `man-la-yahduruhu-al-faqih-v5` | Man La Yahduruhu al-Faqih Vol 5 (Mashaykha) | al-Saduq | 395 | Yes (Four Books) |
| `nahj-al-balagha` | Nahj al-Balagha | al-Sharif al-Radi | 2,260 | Yes |
| `al-amali-mufid` | Al-Amali | al-Mufid | 387 | Yes |
| `al-amali-saduq` | Al-Amali | al-Saduq | 1,082 | Yes |
| `al-tawhid-saduq` | Al-Tawhid | al-Saduq | 575 | Yes |
| `uyun-akhbar-al-rida-v1` | Uyun Akhbar al-Rida Vol 1 | al-Saduq | 347 | Yes |
| `uyun-akhbar-al-rida-v2` | Uyun Akhbar al-Rida Vol 2 | al-Saduq | 607 | Yes |
| `kitab-al-mumin` | Kitab al-Mumin | al-Ahwazi | 201 | Yes |
| `kamil-al-ziyarat` | Kamil al-Ziyarat | al-Qummi | 750 | Yes |
| `kitab-al-ghayba-numani` | Kitab al-Ghayba | al-Numani | 468 | Yes |
| `kitab-al-ghayba-tusi` | Kitab al-Ghayba | al-Tusi | 774 | Yes |
| `al-khisal` | Al-Khisal | al-Saduq | 1,282 | Bonus |
| `maani-al-akhbar` | Maani al-Akhbar | al-Saduq | 829 | Bonus |
| `kamal-al-din` | Kamal al-Din wa Tamam al-Nima | al-Saduq | 659 | Bonus |
| `thawab-al-amal` | Thawab al-Amal wa Iqab al-Amal | al-Saduq | 1,106 | Bonus |
| `kitab-al-zuhd` | Kitab al-Zuhd | al-Ahwazi | 290 | Bonus |
| `mujam-al-ahadith-al-mutabara` | Mujam al-Ahadith al-Mutabara | al-Muhsini | 555 | Bonus |
| `kitab-al-duafa` | Kitab al-Duafa | al-Ghadairi | 226 | Bonus |
| `risalat-al-huquq` | Risalat al-Huquq | Imam Zayn al-Abidin | 49 | Bonus |
| `fadail-al-shia` | Fadail al-Shia | al-Saduq | 45 | Bonus |
| `sifat-al-shia` | Sifat al-Shia | al-Saduq | 71 | Bonus |

## JSON Schema

### File Wrapper

Each `hadiths.json` has this top-level structure:

```json
{
  "source": "thaqalayn-api.net",
  "source_url": "https://www.thaqalayn-api.net/api/v2/{book-slug}",
  "original_site": "thaqalayn.net",
  "book_slug": "Man-La-Yahduruh-al-Faqih-Volume-1-Saduq",
  "total_hadiths": 1569,
  "scraped_at": "2026-02-21T08:42:28Z",
  "hadiths": [ ... ]
}
```

### Hadith Object

Each entry in the `hadiths` array has these fields:

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| `id` | int | Sequential ID within this book (1-based) | `5` |
| `bookId` | string | API slug for the book | `"Man-La-Yahduruh-al-Faqih-Volume-1-Saduq"` |
| `book` | string | Display name of the book (Unicode) | `"Man Lā Yaḥḍuruh al-Faqīh"` |
| `category` | string | Section/part within the book | `"Content"` |
| `categoryId` | string | Numeric ID for the category | `"1"` |
| `chapter` | string | Chapter title (English) | `"Water; Its Purity and Impurity"` |
| `author` | string | Book author name | `"Shaykh Muḥammad b. ʿAlī al-Ṣaduq"` |
| `translator` | string | English translator name | `"Bab Ul Qaim Publications"` |
| `englishText` | string | Full English text (sanad + matn combined) | (long text) |
| `arabicText` | string | Full Arabic text (UTF-8) | (long Arabic text) |
| `frenchText` | string | French translation (usually empty) | `""` |
| `majlisiGrading` | string | Allama Majlisi's grading | `""` or Arabic grading text |
| `mohseniGrading` | string | Mohseni's grading | `""` or `"معتبر"` |
| `behbudiGrading` | string | Behbudi's grading | `""` or grading text |
| `URL` | string | Direct URL on thaqalayn.net | `"https://thaqalayn.net/hadith/34/1/2/3"` |
| `volume` | int | Volume number within the book | `1` |
| `chapterInCategoryId` | int | Chapter number within the category | `2` |
| `thaqalaynSanad` | string | Narrator chain (isnad) separated from matn | (narrator chain text) |
| `thaqalaynMatn` | string | Main hadith text (matn) without narrator chain | (hadith content text) |
| `gradingsFull` | array | Detailed gradings with structured data | See below |

### gradingsFull Array Entry

When populated, each entry in `gradingsFull` has:

```json
{
  "grade_en": null,
  "grade_ar": "معتبر",
  "reference_en": "Muʿjam al-Aḥādīth al-Muʿtabara",
  "author": {
    "name_en": "Shaykh Asif al-Mohseni",
    "name_ar": null,
    "link": null,
    "death_date": null
  }
}
```

### Key Notes for Parser Development

1. **Text encoding**: All text is UTF-8. Arabic text is NOT escaped (ensure_ascii=False).

2. **Narrator chain separation**: `thaqalaynSanad` and `thaqalaynMatn` split the narrator chain from the hadith body. These may be empty strings for non-hadith entries (prefaces, commentary).

3. **`englishText` = sanad + matn**: The full English text combines both. Use `thaqalaynSanad` and `thaqalaynMatn` when you need them separated.

4. **Chapter hierarchy**: The URL field encodes the thaqalayn.net book/volume/chapter structure: `/hadith/{bookId}/{volumeNumber}/{chapterNumber}/{hadithNumber}`. This can be parsed to reconstruct the chapter hierarchy.

5. **Category vs Chapter**: `category`/`categoryId` represents the book-level section (e.g., "Book of Intellect and Knowledge"), while `chapter` is the specific chapter within that section.

6. **Grading fields**: Most books have empty grading strings. Only some books (Mujam al-Ahadith, Al-Khisal, some Kafi volumes) have populated gradings. When present, they may be in Arabic.

7. **Multi-volume books**: Man La Yahduruhu al-Faqih (5 vols), Uyun Akhbar al-Rida (2 vols) are split into separate folders. The `book` display name is shared across volumes.

## Scraper Script

The scraper is at `app/scrapers/scrape_thaqalayn_api.py` (committed to git).

```bash
# Scrape all books:
cd ThaqalaynDataGenerator
source .venv/Scripts/activate
python app/scrapers/scrape_thaqalayn_api.py

# Scrape specific book:
python app/scrapers/scrape_thaqalayn_api.py Nahj-al-Balagha-Radi

# List available books:
python app/scrapers/scrape_thaqalayn_api.py --list
```

## Data Source

- **API**: https://www.thaqalayn-api.net/api/v2/
- **Original site**: https://thaqalayn.net/
- **API docs**: https://www.thaqalayn-api.net/api-docs/
- **API GitHub**: https://github.com/MohammedArab1/ThaqalaynAPI
