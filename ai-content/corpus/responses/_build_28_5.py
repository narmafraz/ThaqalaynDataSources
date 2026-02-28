#!/usr/bin/env python3
"""Build complete AI content for al-amali-saduq:28:5"""
import json, sys, os
sys.stdout.reconfigure(encoding='utf-8')

# Word analysis for the complete hadith - 361 words
# Chunk plan:
# Chunk 0 (isnad): words 0-18 (حَدَّثَنَا...قَالَ)
# Chunk 1 (body): words 19-95 (دَخَلْتُ...السَّلَامُ) - Zakariyya section
# Chunk 2 (body): words 96-144 (ثُمَّ...أَبَدًا) - Muharram sanctity / Karbala crimes
# Chunk 3 (body): words 145-212 (يَا...الْحُسَيْنِ) - Weep for Husayn / angels
# Chunk 4 (body): words 213-237 (يَا...أَحْمَرَ) - sky rained blood
# Chunk 5 (body): words 238-265 (يَا...كَثِيرًا) - weeping forgives sins
# Chunk 6 (body): words 266-282 (يَا...السَّلَامُ) - visit Husayn = no sin
# Chunk 7 (body): words 283-302 (يَا...الْحُسَيْنِ) - curse killers of Husayn
# Chunk 8 (body): words 303-331 (يَا...عَظِيمًا) - wish to be martyred with Husayn
# Chunk 9 (closing): words 332-360 (يَا...الْقِيَامَةِ) - wilaya conclusion

word_analysis = [
    # Chunk 0: Isnad (words 0-18)
    {"word": "حَدَّثَنَا", "translation": {"en": "narrated to us", "ur": "ہم سے بیان کیا", "tr": "bize rivayet etti", "fa": "برای ما نقل کرد", "id": "menceritakan kepada kami", "bn": "আমাদের বর্ণনা করেছেন", "es": "nos narró", "fr": "nous a rapporté", "de": "überlieferte uns", "ru": "рассказал нам", "zh": "向我们传述了"}, "pos": "V"},
    {"word": "مُحَمَّدُ", "translation": {"en": "Muhammad", "ur": "محمد", "tr": "Muhammed", "fa": "محمد", "id": "Muhammad", "bn": "মুহাম্মাদ", "es": "Muhammad", "fr": "Muhammad", "de": "Muhammad", "ru": "Мухаммад", "zh": "穆罕默德"}, "pos": "N"},
    {"word": "بْنُ", "translation": {"en": "son of", "ur": "بن", "tr": "bin", "fa": "بن", "id": "bin", "bn": "ইবনে", "es": "hijo de", "fr": "fils de", "de": "Sohn von", "ru": "ибн", "zh": "之子"}, "pos": "N"},
    {"word": "عَلِيٍّ", "translation": {"en": "Ali", "ur": "علی", "tr": "Ali", "fa": "علی", "id": "Ali", "bn": "আলী", "es": "Ali", "fr": "Ali", "de": "Ali", "ru": "Али", "zh": "阿里"}, "pos": "N"},
    {"word": "مَاجِيلُوَيْهِ", "translation": {"en": "Majiluwayh", "ur": "ماجیلویہ", "tr": "Mâcîluveyh", "fa": "ماجیلویه", "id": "Majiluwayh", "bn": "মাজিলুওয়াইহ", "es": "Majiluwayh", "fr": "Mâjîluwayh", "de": "Majiluwayh", "ru": "Маджилувайх", "zh": "马吉卢韦赫"}, "pos": "N"},
    {"word": "رَحِمَهُ", "translation": {"en": "may He have mercy on him", "ur": "اللہ اس پر رحم کرے", "tr": "Allah rahmet eylesin", "fa": "رحمت خدا بر او", "id": "semoga Allah merahmatinya", "bn": "আল্লাহ তাঁর উপর রহম করুন", "es": "que Dios tenga misericordia de él", "fr": "qu'Allah lui fasse miséricorde", "de": "möge Gott sich seiner erbarmen", "ru": "да помилует его", "zh": "愿真主怜悯他"}, "pos": "V"},
    {"word": "اللَّهُ", "translation": {"en": "God", "ur": "اللہ", "tr": "Allah", "fa": "خدا", "id": "Allah", "bn": "আল্লাহ", "es": "Dios", "fr": "Dieu", "de": "Gott", "ru": "Аллах", "zh": "真主"}, "pos": "N"},
    {"word": "قَالَ", "translation": {"en": "he said", "ur": "کہا", "tr": "dedi", "fa": "گفت", "id": "berkata", "bn": "বললেন", "es": "dijo", "fr": "a dit", "de": "sagte", "ru": "сказал", "zh": "他说"}, "pos": "V"},
    {"word": "حَدَّثَنَا", "translation": {"en": "narrated to us", "ur": "ہم سے بیان کیا", "tr": "bize rivayet etti", "fa": "برای ما نقل کرد", "id": "menceritakan kepada kami", "bn": "আমাদের বর্ণনা করেছেন", "es": "nos narró", "fr": "nous a rapporté", "de": "überlieferte uns", "ru": "рассказал нам", "zh": "向我们传述了"}, "pos": "V"},
    {"word": "عَلِيُّ", "translation": {"en": "Ali", "ur": "علی", "tr": "Ali", "fa": "علی", "id": "Ali", "bn": "আলী", "es": "Ali", "fr": "Ali", "de": "Ali", "ru": "Али", "zh": "阿里"}, "pos": "N"},
    {"word": "بْنُ", "translation": {"en": "son of", "ur": "بن", "tr": "bin", "fa": "بن", "id": "bin", "bn": "ইবনে", "es": "hijo de", "fr": "fils de", "de": "Sohn von", "ru": "ибн", "zh": "之子"}, "pos": "N"},
    {"word": "إِبْرَاهِيمَ", "translation": {"en": "Ibrahim", "ur": "ابراہیم", "tr": "İbrahim", "fa": "ابراهیم", "id": "Ibrahim", "bn": "ইব্রাহীম", "es": "Ibrahim", "fr": "Ibrahim", "de": "Ibrahim", "ru": "Ибрахим", "zh": "伊卜拉欣"}, "pos": "N"},
    {"word": "عَنْ", "translation": {"en": "from", "ur": "سے", "tr": "-den", "fa": "از", "id": "dari", "bn": "থেকে", "es": "de", "fr": "de", "de": "von", "ru": "от", "zh": "从"}, "pos": "PREP"},
    {"word": "أَبِيهِ", "translation": {"en": "his father", "ur": "اپنے والد", "tr": "babası", "fa": "پدرش", "id": "ayahnya", "bn": "তাঁর পিতা", "es": "su padre", "fr": "son père", "de": "sein Vater", "ru": "его отец", "zh": "他的父亲"}, "pos": "N"},
    {"word": "عَنِ", "translation": {"en": "from", "ur": "سے", "tr": "-den", "fa": "از", "id": "dari", "bn": "থেকে", "es": "de", "fr": "de", "de": "von", "ru": "от", "zh": "从"}, "pos": "PREP"},
    {"word": "الرَّيَّانِ", "translation": {"en": "al-Rayyan", "ur": "ریان", "tr": "Reyyan", "fa": "ریان", "id": "al-Rayyan", "bn": "আল-রায়্যান", "es": "al-Rayyan", "fr": "al-Rayyan", "de": "al-Rayyan", "ru": "ар-Раййан", "zh": "赖扬"}, "pos": "N"},
    {"word": "بْنِ", "translation": {"en": "son of", "ur": "بن", "tr": "bin", "fa": "بن", "id": "bin", "bn": "ইবনে", "es": "hijo de", "fr": "fils de", "de": "Sohn von", "ru": "ибн", "zh": "之子"}, "pos": "N"},
    {"word": "شَبِيبٍ", "translation": {"en": "Shabib", "ur": "شبیب", "tr": "Şebib", "fa": "شبیب", "id": "Shabib", "bn": "শাবীব", "es": "Shabib", "fr": "Shabib", "de": "Shabib", "ru": "Шабиб", "zh": "沙比卜"}, "pos": "N"},
    {"word": "قَالَ", "translation": {"en": "he said", "ur": "کہا", "tr": "dedi", "fa": "گفت", "id": "berkata", "bn": "বললেন", "es": "dijo", "fr": "a dit", "de": "sagte", "ru": "сказал", "zh": "他说"}, "pos": "V"},

    # Chunk 1: Zakariyya section (words 19-95)
    {"word": "دَخَلْتُ", "translation": {"en": "I entered", "ur": "میں داخل ہوا", "tr": "girdim", "fa": "داخل شدم", "id": "saya masuk", "bn": "আমি প্রবেশ করলাম", "es": "entré", "fr": "je suis entré", "de": "ich trat ein", "ru": "я вошёл", "zh": "我进入了"}, "pos": "V"},
    {"word": "عَلَى", "translation": {"en": "upon/to", "ur": "کے پاس", "tr": "yanına", "fa": "نزد", "id": "kepada", "bn": "কাছে", "es": "ante", "fr": "auprès de", "de": "zu", "ru": "к", "zh": "到"}, "pos": "PREP"},
    {"word": "الرِّضَا", "translation": {"en": "al-Rida", "ur": "الرضا", "tr": "Rıza", "fa": "الرضا", "id": "al-Rida", "bn": "আল-রিদা", "es": "al-Rida", "fr": "al-Ridâ", "de": "al-Rida", "ru": "ар-Рида", "zh": "里达"}, "pos": "N"},
    {"word": "عَلَيْهِ", "translation": {"en": "upon him", "ur": "علیہ", "tr": "ona", "fa": "بر او", "id": "atasnya", "bn": "তাঁর উপর", "es": "sobre él", "fr": "sur lui", "de": "auf ihm", "ru": "на нём", "zh": "在他之上"}, "pos": "PREP"},
    {"word": "السَّلَامُ", "translation": {"en": "peace", "ur": "السلام", "tr": "selam", "fa": "سلام", "id": "salam", "bn": "শান্তি", "es": "paz", "fr": "paix", "de": "Friede", "ru": "мир", "zh": "平安"}, "pos": "N"},
    {"word": "فِي", "translation": {"en": "on", "ur": "میں", "tr": "-de", "fa": "در", "id": "pada", "bn": "তে", "es": "en", "fr": "le", "de": "am", "ru": "в", "zh": "在"}, "pos": "PREP"},
    {"word": "أَوَّلِ", "translation": {"en": "first", "ur": "پہلے", "tr": "ilk", "fa": "اول", "id": "pertama", "bn": "প্রথম", "es": "primer", "fr": "premier", "de": "ersten", "ru": "первый", "zh": "第一"}, "pos": "N"},
    {"word": "يَوْمٍ", "translation": {"en": "day", "ur": "دن", "tr": "gün", "fa": "روز", "id": "hari", "bn": "দিন", "es": "día", "fr": "jour", "de": "Tag", "ru": "день", "zh": "天"}, "pos": "N"},
    {"word": "مِنَ", "translation": {"en": "of", "ur": "کے", "tr": "-nın", "fa": "از", "id": "dari", "bn": "এর", "es": "de", "fr": "de", "de": "von", "ru": "из", "zh": "的"}, "pos": "PREP"},
    {"word": "الْمُحَرَّمِ", "translation": {"en": "Muharram", "ur": "محرم", "tr": "Muharrem", "fa": "محرم", "id": "Muharram", "bn": "মুহাররম", "es": "Muharram", "fr": "Muharram", "de": "Muharram", "ru": "Мухаррам", "zh": "穆哈拉姆月"}, "pos": "N"},
    {"word": "فَقَالَ", "translation": {"en": "so he said", "ur": "تو فرمایا", "tr": "buyurdu", "fa": "پس فرمود", "id": "maka beliau bersabda", "bn": "তখন তিনি বললেন", "es": "entonces dijo", "fr": "alors il dit", "de": "dann sagte er", "ru": "тогда он сказал", "zh": "于是他说"}, "pos": "V"},
    {"word": "لِي", "translation": {"en": "to me", "ur": "مجھ سے", "tr": "bana", "fa": "به من", "id": "kepadaku", "bn": "আমাকে", "es": "a mí", "fr": "à moi", "de": "zu mir", "ru": "мне", "zh": "对我"}, "pos": "PREP"},
    {"word": "يَا", "translation": {"en": "O", "ur": "اے", "tr": "ey", "fa": "ای", "id": "wahai", "bn": "হে", "es": "oh", "fr": "ô", "de": "o", "ru": "о", "zh": "哦"}, "pos": "INTJ"},
    {"word": "بْنَ", "translation": {"en": "son of", "ur": "بن", "tr": "bin", "fa": "بن", "id": "bin", "bn": "ইবনে", "es": "hijo de", "fr": "fils de", "de": "Sohn von", "ru": "ибн", "zh": "之子"}, "pos": "N"},
    {"word": "شَبِيبٍ", "translation": {"en": "Shabib", "ur": "شبیب", "tr": "Şebib", "fa": "شبیب", "id": "Shabib", "bn": "শাবীব", "es": "Shabib", "fr": "Shabib", "de": "Shabib", "ru": "Шабиб", "zh": "沙比卜"}, "pos": "N"},
    {"word": "أَصَائِمٌ", "translation": {"en": "are you fasting?", "ur": "کیا روزے سے ہو؟", "tr": "oruçlu musun?", "fa": "آیا روزه‌دار هستی؟", "id": "apakah kamu berpuasa?", "bn": "তুমি কি রোযা রেখেছ?", "es": "¿estás ayunando?", "fr": "es-tu en jeûne ?", "de": "fastest du?", "ru": "ты постишься?", "zh": "你在封斋吗？"}, "pos": "N"},
    {"word": "أَنْتَ", "translation": {"en": "you", "ur": "تم", "tr": "sen", "fa": "تو", "id": "kamu", "bn": "তুমি", "es": "tú", "fr": "tu", "de": "du", "ru": "ты", "zh": "你"}, "pos": "PRON"},
    {"word": "فَقُلْتُ", "translation": {"en": "so I said", "ur": "تو میں نے کہا", "tr": "dedim", "fa": "پس گفتم", "id": "maka saya berkata", "bn": "তখন আমি বললাম", "es": "entonces dije", "fr": "alors je dis", "de": "dann sagte ich", "ru": "тогда я сказал", "zh": "于是我说"}, "pos": "V"},
    {"word": "لَا", "translation": {"en": "no", "ur": "نہیں", "tr": "hayır", "fa": "نه", "id": "tidak", "bn": "না", "es": "no", "fr": "non", "de": "nein", "ru": "нет", "zh": "不"}, "pos": "NEG"},
    {"word": "فَقَالَ", "translation": {"en": "so he said", "ur": "تو فرمایا", "tr": "buyurdu", "fa": "پس فرمود", "id": "maka beliau bersabda", "bn": "তখন তিনি বললেন", "es": "entonces dijo", "fr": "alors il dit", "de": "dann sagte er", "ru": "тогда он сказал", "zh": "于是他说"}, "pos": "V"},
    {"word": "إِنَّ", "translation": {"en": "indeed", "ur": "بے شک", "tr": "muhakkak ki", "fa": "به درستی", "id": "sesungguhnya", "bn": "নিশ্চয়", "es": "ciertamente", "fr": "certes", "de": "wahrlich", "ru": "поистине", "zh": "确实"}, "pos": "PART"},
    {"word": "هَذَا", "translation": {"en": "this", "ur": "یہ", "tr": "bu", "fa": "این", "id": "ini", "bn": "এই", "es": "este", "fr": "ce", "de": "dieser", "ru": "этот", "zh": "这"}, "pos": "DEM"},
    {"word": "الْيَوْمَ", "translation": {"en": "the day", "ur": "دن", "tr": "gün", "fa": "روز", "id": "hari", "bn": "দিন", "es": "el día", "fr": "le jour", "de": "der Tag", "ru": "день", "zh": "日"}, "pos": "N"},
    {"word": "هُوَ", "translation": {"en": "it is", "ur": "وہ ہے", "tr": "odur", "fa": "آن است", "id": "adalah", "bn": "সেটি", "es": "es", "fr": "est", "de": "ist", "ru": "это", "zh": "是"}, "pos": "PRON"},
    {"word": "الْيَوْمُ", "translation": {"en": "the day", "ur": "دن", "tr": "gün", "fa": "روز", "id": "hari", "bn": "দিন", "es": "el día", "fr": "le jour", "de": "der Tag", "ru": "день", "zh": "日"}, "pos": "N"},
    {"word": "الَّذِي", "translation": {"en": "in which", "ur": "جس میں", "tr": "ki", "fa": "که", "id": "yang", "bn": "যেদিন", "es": "en el que", "fr": "dans lequel", "de": "an dem", "ru": "в который", "zh": "在那天"}, "pos": "REL"},
    {"word": "دَعَا", "translation": {"en": "called upon", "ur": "دعا کی", "tr": "dua etti", "fa": "دعا کرد", "id": "berdoa", "bn": "প্রার্থনা করেছিলেন", "es": "invocó", "fr": "invoqua", "de": "anrief", "ru": "призвал", "zh": "祈祷了"}, "pos": "V"},
    {"word": "فِيهِ", "translation": {"en": "in it", "ur": "اس میں", "tr": "onda", "fa": "در آن", "id": "di dalamnya", "bn": "এতে", "es": "en él", "fr": "en lui", "de": "darin", "ru": "в нём", "zh": "在其中"}, "pos": "PREP"},
    {"word": "زَكَرِيَّا", "translation": {"en": "Zakariyya", "ur": "زکریا", "tr": "Zekeriya", "fa": "زکریا", "id": "Zakariyya", "bn": "যাকারিয়া", "es": "Zacarías", "fr": "Zacharie", "de": "Zakariyya", "ru": "Закария", "zh": "宰凯里雅"}, "pos": "N"},
    {"word": "عَلَيْهِ", "translation": {"en": "upon him", "ur": "علیہ", "tr": "ona", "fa": "بر او", "id": "atasnya", "bn": "তাঁর উপর", "es": "sobre él", "fr": "sur lui", "de": "auf ihm", "ru": "на нём", "zh": "在他之上"}, "pos": "PREP"},
    {"word": "السَّلَامُ", "translation": {"en": "peace", "ur": "السلام", "tr": "selam", "fa": "سلام", "id": "salam", "bn": "শান্তি", "es": "paz", "fr": "paix", "de": "Friede", "ru": "мир", "zh": "平安"}, "pos": "N"},
    {"word": "رَبَّهُ", "translation": {"en": "his Lord", "ur": "اپنے رب سے", "tr": "Rabbine", "fa": "پروردگارش را", "id": "Tuhannya", "bn": "তাঁর রবকে", "es": "a su Señor", "fr": "son Seigneur", "de": "seinen Herrn", "ru": "своего Господа", "zh": "他的养主"}, "pos": "N"},
    {"word": "عَزَّ", "translation": {"en": "Mighty", "ur": "عزت والا", "tr": "aziz", "fa": "عزیز", "id": "Yang Maha Mulia", "bn": "মহামহিম", "es": "Poderoso", "fr": "Puissant", "de": "Erhaben", "ru": "Всемогущий", "zh": "至尊"}, "pos": "V"},
    {"word": "وَجَلَّ", "translation": {"en": "and Majestic", "ur": "اور جلال والا", "tr": "ve celil", "fa": "و جلیل", "id": "dan Maha Agung", "bn": "ও মহিমান্বিত", "es": "y Majestuoso", "fr": "et Majestueux", "de": "und Majestätisch", "ru": "и Величественный", "zh": "至伟"}, "pos": "V"},
    {"word": "فَقَالَ", "translation": {"en": "and he said", "ur": "تو کہا", "tr": "dedi", "fa": "پس گفت", "id": "lalu berkata", "bn": "তখন বললেন", "es": "y dijo", "fr": "et il dit", "de": "und er sagte", "ru": "и сказал", "zh": "于是说"}, "pos": "V"},
    {"word": "رَبِّ", "translation": {"en": "My Lord", "ur": "اے میرے رب", "tr": "Rabbim", "fa": "پروردگارا", "id": "Ya Tuhanku", "bn": "হে আমার রব", "es": "Señor mío", "fr": "Mon Seigneur", "de": "Mein Herr", "ru": "Господи", "zh": "我的养主啊"}, "pos": "N"},
    {"word": "هَبْ", "translation": {"en": "grant", "ur": "عطا فرما", "tr": "bağışla", "fa": "عطا کن", "id": "karuniakanlah", "bn": "দান করুন", "es": "concédeme", "fr": "accorde-moi", "de": "schenke mir", "ru": "даруй", "zh": "赐予"}, "pos": "V"},
    {"word": "لِي", "translation": {"en": "to me", "ur": "مجھے", "tr": "bana", "fa": "به من", "id": "kepadaku", "bn": "আমাকে", "es": "a mí", "fr": "à moi", "de": "mir", "ru": "мне", "zh": "给我"}, "pos": "PREP"},
    {"word": "مِنْ", "translation": {"en": "from", "ur": "سے", "tr": "-den", "fa": "از", "id": "dari", "bn": "থেকে", "es": "de", "fr": "de", "de": "von", "ru": "от", "zh": "从"}, "pos": "PREP"},
    {"word": "لَدُنْكَ", "translation": {"en": "You (Your presence)", "ur": "اپنے پاس سے", "tr": "katından", "fa": "نزد تو", "id": "sisi-Mu", "bn": "তোমার কাছ থেকে", "es": "de Tu parte", "fr": "de Ta part", "de": "von Dir", "ru": "от Себя", "zh": "从你那里"}, "pos": "N"},
    {"word": "ذُرِّيَّةً", "translation": {"en": "offspring", "ur": "اولاد", "tr": "nesil", "fa": "فرزند", "id": "keturunan", "bn": "সন্তান", "es": "descendencia", "fr": "progéniture", "de": "Nachkommen", "ru": "потомство", "zh": "后裔"}, "pos": "N"},
    {"word": "طَيِّبَةً", "translation": {"en": "good/pure", "ur": "پاکیزہ", "tr": "temiz/iyi", "fa": "پاکیزه", "id": "yang baik", "bn": "পবিত্র", "es": "buena", "fr": "bonne", "de": "gute", "ru": "благую", "zh": "善良的"}, "pos": "ADJ"},
    {"word": "إِنَّكَ", "translation": {"en": "surely You are", "ur": "بے شک تو", "tr": "muhakkak Sen", "fa": "به درستی تو", "id": "sesungguhnya Engkau", "bn": "নিশ্চয়ই তুমি", "es": "ciertamente Tú eres", "fr": "certes Tu es", "de": "wahrlich Du bist", "ru": "поистине Ты", "zh": "你确是"}, "pos": "PART"},
    {"word": "سَمِيعُ", "translation": {"en": "the Hearer of", "ur": "سننے والا", "tr": "işiten", "fa": "شنوای", "id": "Yang Maha Mendengar", "bn": "শ্রবণকারী", "es": "el que escucha", "fr": "Celui qui entend", "de": "der Erhörer", "ru": "Слышащий", "zh": "倾听者"}, "pos": "ADJ"},
    {"word": "الدُّعَاءِ", "translation": {"en": "prayers", "ur": "دعاؤں کا", "tr": "duaları", "fa": "دعا", "id": "doa", "bn": "প্রার্থনা", "es": "las súplicas", "fr": "les prières", "de": "Gebete", "ru": "молитв", "zh": "祈祷"}, "pos": "N"},
    {"word": "فَاسْتَجَابَ", "translation": {"en": "so He answered", "ur": "تو قبول کیا", "tr": "icabet etti", "fa": "پس اجابت کرد", "id": "maka Allah mengabulkan", "bn": "তখন তিনি কবুল করলেন", "es": "entonces respondió", "fr": "alors Il exauça", "de": "da erhörte Er", "ru": "и Он ответил", "zh": "于是应答了"}, "pos": "V"},
    {"word": "لَهُ", "translation": {"en": "him", "ur": "اسے", "tr": "ona", "fa": "او را", "id": "kepadanya", "bn": "তাঁকে", "es": "a él", "fr": "à lui", "de": "ihm", "ru": "ему", "zh": "他"}, "pos": "PREP"},
    {"word": "وَأَمَرَ", "translation": {"en": "and ordered", "ur": "اور حکم دیا", "tr": "ve emretti", "fa": "و فرمان داد", "id": "dan memerintahkan", "bn": "এবং আদেশ দিলেন", "es": "y ordenó", "fr": "et ordonna", "de": "und befahl", "ru": "и повелел", "zh": "并命令"}, "pos": "V"},
    {"word": "الْمَلَائِكَةَ", "translation": {"en": "the angels", "ur": "فرشتوں کو", "tr": "meleklere", "fa": "فرشتگان را", "id": "para malaikat", "bn": "ফেরেশতাদের", "es": "a los ángeles", "fr": "les anges", "de": "den Engeln", "ru": "ангелов", "zh": "天使们"}, "pos": "N"},
    {"word": "فَنَادَتْ", "translation": {"en": "and they called out to", "ur": "تو پکارا", "tr": "seslendi", "fa": "پس ندا دادند", "id": "lalu mereka menyeru", "bn": "তখন তারা ডাকলেন", "es": "y llamaron a", "fr": "et ils appelèrent", "de": "und sie riefen", "ru": "и воззвали к", "zh": "于是呼唤了"}, "pos": "V"},
    {"word": "زَكَرِيَّا", "translation": {"en": "Zakariyya", "ur": "زکریا", "tr": "Zekeriya", "fa": "زکریا", "id": "Zakariyya", "bn": "যাকারিয়া", "es": "Zacarías", "fr": "Zacharie", "de": "Zakariyya", "ru": "Закарию", "zh": "宰凯里雅"}, "pos": "N"},
    {"word": "وَهُوَ", "translation": {"en": "while he was", "ur": "اور وہ", "tr": "o ise", "fa": "و او", "id": "sedangkan dia", "bn": "এবং তিনি", "es": "mientras él", "fr": "tandis qu'il", "de": "während er", "ru": "а он", "zh": "而他"}, "pos": "PRON"},
    {"word": "قَائِمٌ", "translation": {"en": "standing", "ur": "کھڑا", "tr": "ayakta", "fa": "ایستاده", "id": "berdiri", "bn": "দাঁড়িয়ে", "es": "de pie", "fr": "debout", "de": "stehend", "ru": "стоящий", "zh": "站立着"}, "pos": "N"},
    {"word": "يُصَلِّي", "translation": {"en": "praying", "ur": "نماز پڑھ رہا تھا", "tr": "namaz kılarken", "fa": "نماز می‌خواند", "id": "sedang salat", "bn": "নামায পড়ছিলেন", "es": "rezando", "fr": "priant", "de": "betend", "ru": "молящийся", "zh": "礼拜中"}, "pos": "V"},
    {"word": "فِي", "translation": {"en": "in", "ur": "میں", "tr": "-de", "fa": "در", "id": "di", "bn": "এ", "es": "en", "fr": "dans", "de": "in", "ru": "в", "zh": "在"}, "pos": "PREP"},
    {"word": "الْمِحْرَابِ", "translation": {"en": "the prayer-niche", "ur": "محراب", "tr": "mihrâb", "fa": "محراب", "id": "mihrab", "bn": "মিহরাব", "es": "el nicho de oración", "fr": "le mihrâb", "de": "die Gebetsnische", "ru": "михраб", "zh": "壁龛中"}, "pos": "N"},
    {"word": "أَنَّ", "translation": {"en": "that", "ur": "کہ", "tr": "ki", "fa": "که", "id": "bahwa", "bn": "যে", "es": "que", "fr": "que", "de": "dass", "ru": "что", "zh": "即"}, "pos": "PART"},
    {"word": "اللَّهَ", "translation": {"en": "God", "ur": "اللہ", "tr": "Allah", "fa": "خدا", "id": "Allah", "bn": "আল্লাহ", "es": "Dios", "fr": "Dieu", "de": "Gott", "ru": "Аллах", "zh": "真主"}, "pos": "N"},
    {"word": "يُبَشِّرُكَ", "translation": {"en": "gives you glad-tidings", "ur": "تجھے بشارت دیتا ہے", "tr": "seni müjdeliyor", "fa": "تو را بشارت می‌دهد", "id": "memberimu kabar gembira", "bn": "তোমাকে সুসংবাদ দিচ্ছেন", "es": "te da la buena nueva", "fr": "t'annonce la bonne nouvelle", "de": "verkündet dir frohe Botschaft", "ru": "радует тебя вестью", "zh": "向你报喜"}, "pos": "V"},
    {"word": "بِيَحْيَى", "translation": {"en": "of Yahya", "ur": "یحیی کی", "tr": "Yahya ile", "fa": "به یحیی", "id": "tentang Yahya", "bn": "ইয়াহইয়ার", "es": "de Yahya", "fr": "de Yahyâ", "de": "von Yahya", "ru": "о Яхье", "zh": "关于叶哈雅"}, "pos": "N"},
    {"word": "فَمَنْ", "translation": {"en": "so whoever", "ur": "پس جو", "tr": "kim ki", "fa": "پس هر کس", "id": "maka barangsiapa", "bn": "সুতরাং যে", "es": "pues quien", "fr": "quiconque", "de": "wer also", "ru": "и кто", "zh": "凡是"}, "pos": "PRON"},
    {"word": "صَامَ", "translation": {"en": "fasts", "ur": "روزہ رکھے", "tr": "oruç tutarsa", "fa": "روزه بگیرد", "id": "berpuasa", "bn": "রোযা রাখে", "es": "ayune", "fr": "jeûne", "de": "fastet", "ru": "постится", "zh": "封斋"}, "pos": "V"},
    {"word": "هَذَا", "translation": {"en": "this", "ur": "اس", "tr": "bu", "fa": "این", "id": "ini", "bn": "এই", "es": "este", "fr": "ce", "de": "diesen", "ru": "этот", "zh": "这"}, "pos": "DEM"},
    {"word": "الْيَوْمَ", "translation": {"en": "day", "ur": "دن", "tr": "gün", "fa": "روز", "id": "hari", "bn": "দিন", "es": "día", "fr": "jour", "de": "Tag", "ru": "день", "zh": "日"}, "pos": "N"},
    {"word": "ثُمَّ", "translation": {"en": "then", "ur": "پھر", "tr": "sonra", "fa": "سپس", "id": "kemudian", "bn": "তারপর", "es": "luego", "fr": "puis", "de": "dann", "ru": "затем", "zh": "然后"}, "pos": "CONJ"},
    {"word": "دَعَا", "translation": {"en": "calls upon", "ur": "دعا کرے", "tr": "dua ederse", "fa": "دعا کند", "id": "berdoa kepada", "bn": "প্রার্থনা করে", "es": "invoque a", "fr": "invoque", "de": "anruft", "ru": "призовёт", "zh": "祈祷"}, "pos": "V"},
    {"word": "اللَّهَ", "translation": {"en": "God", "ur": "اللہ", "tr": "Allah", "fa": "خدا", "id": "Allah", "bn": "আল্লাহকে", "es": "a Dios", "fr": "Dieu", "de": "Gott", "ru": "Аллаха", "zh": "真主"}, "pos": "N"},
    {"word": "عَزَّ", "translation": {"en": "Mighty", "ur": "عزت والا", "tr": "aziz", "fa": "عزیز", "id": "Yang Maha Mulia", "bn": "মহামহিম", "es": "Poderoso", "fr": "Puissant", "de": "Erhaben", "ru": "Всемогущий", "zh": "至尊"}, "pos": "V"},
    {"word": "وَجَلَّ", "translation": {"en": "and Majestic", "ur": "اور جلال والا", "tr": "ve celil", "fa": "و جلیل", "id": "dan Maha Agung", "bn": "ও মহিমান্বিত", "es": "y Majestuoso", "fr": "et Majestueux", "de": "und Majestätisch", "ru": "и Величественный", "zh": "至伟"}, "pos": "V"},
    {"word": "اسْتَجَابَ", "translation": {"en": "will respond to", "ur": "قبول کرے گا", "tr": "icabet eder", "fa": "اجابت می‌کند", "id": "Allah akan mengabulkan", "bn": "কবুল করবেন", "es": "responderá", "fr": "exaucera", "de": "wird erhören", "ru": "ответит", "zh": "将应答"}, "pos": "V"},
    {"word": "اللَّهُ", "translation": {"en": "God", "ur": "اللہ", "tr": "Allah", "fa": "خدا", "id": "Allah", "bn": "আল্লাহ", "es": "Dios", "fr": "Dieu", "de": "Gott", "ru": "Аллах", "zh": "真主"}, "pos": "N"},
    {"word": "لَهُ", "translation": {"en": "him", "ur": "اسے", "tr": "ona", "fa": "او را", "id": "kepadanya", "bn": "তাকে", "es": "a él", "fr": "à lui", "de": "ihm", "ru": "ему", "zh": "他"}, "pos": "PREP"},
    {"word": "كَمَا", "translation": {"en": "just as", "ur": "جیسے", "tr": "nasıl ki", "fa": "همانطور که", "id": "sebagaimana", "bn": "যেমন", "es": "como", "fr": "comme", "de": "wie", "ru": "как", "zh": "正如"}, "pos": "CONJ"},
    {"word": "اسْتَجَابَ", "translation": {"en": "He responded to", "ur": "قبول کیا", "tr": "icabet ettiği gibi", "fa": "اجابت کرد", "id": "Dia mengabulkan", "bn": "কবুল করেছিলেন", "es": "respondió a", "fr": "Il exauça", "de": "Er erhörte", "ru": "Он ответил", "zh": "应答了"}, "pos": "V"},
    {"word": "لِزَكَرِيَّا", "translation": {"en": "Zakariyya", "ur": "زکریا کی", "tr": "Zekeriya'ya", "fa": "زکریا را", "id": "Zakariyya", "bn": "যাকারিয়ার", "es": "a Zacarías", "fr": "Zacharie", "de": "Zakariyya", "ru": "Закарию", "zh": "宰凯里雅"}, "pos": "N"},
    {"word": "عَلَيْهِ", "translation": {"en": "upon him", "ur": "علیہ", "tr": "ona", "fa": "بر او", "id": "atasnya", "bn": "তাঁর উপর", "es": "sobre él", "fr": "sur lui", "de": "auf ihm", "ru": "на нём", "zh": "在他之上"}, "pos": "PREP"},
    {"word": "السَّلَامُ", "translation": {"en": "peace", "ur": "السلام", "tr": "selam", "fa": "سلام", "id": "salam", "bn": "শান্তি", "es": "paz", "fr": "paix", "de": "Friede", "ru": "мир", "zh": "平安"}, "pos": "N"},
]

# Save part 1
import os
outpath = os.path.join(os.path.dirname(os.path.abspath(__file__)), '_wa_28_5_part1.json')
with open(outpath, 'w', encoding='utf-8') as f:
    json.dump(word_analysis, f, ensure_ascii=False, indent=2)
print(f'Part 1 saved: {len(word_analysis)} words (indices 0-95)')
