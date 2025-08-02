from langdetect import detect, detect_langs
from deep_translator import GoogleTranslator
from textblob import TextBlob
import matplotlib.pyplot as plt


def detect_language(text):
    language = detect(text)
    print(" Detected Language Code:", language)
    print(" Language Probabilities:", detect_langs(text))
    return language

def translate_text(text, source_lang, target_lang):
    translated = GoogleTranslator(source=source_lang, target=target_lang).translate(text)
    print(" Translated Text:", translated)
    return translated
def analyze(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"
def visualize(sentiment):
    lbl = ['Positive','Negative','Neutral']
    val = [1 if sentiment.lower() == label.lower() else 0 for label in lbl]
    plt.figure(figsize=(6,4))
    bars = plt.bar(lbl,val,color = ['red','blue','green'])
    plt.title("Analyzed result")
    plt.ylabel("Analyzed score")
    for i in bars:
        h = i.get_height()
        plt.text(i.get_x()+i.get_width()/2.0,h,str(h),ha = 'center',va = 'bottom')
    plt.ylim(0,1.2)
    plt.show()
    

# ----------- Run the Program -----------
text = input(" Enter text in any language: ")
source_lang = detect_language(text)

target_lang = input(" Enter target language code (e.g., en, te, hi, ta): ")
translate_text(text, source_lang, target_lang)
sentiment = analyze(text)
print("Sentiment of the text:", sentiment)
visualize(sentiment)

