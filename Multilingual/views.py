from django.shortcuts import render
from .forms import TextForm
from langdetect import detect
from deep_translator import GoogleTranslator
from textblob import TextBlob
import matplotlib.pyplot as plt
import io
import base64

LANGUAGE_MAP = {
    'en': 'English', 'fr': 'French', 'es': 'Spanish', 'de': 'German',
    'hi': 'Hindi', 'te': 'Telugu', 'ta': 'Tamil', 'zh-cn': 'Chinese'
}

def detect_language(text):
    try:
        return detect(text)
    except Exception:
        return "unknown"

def translate_text(text, src_lang):
    try:
        return GoogleTranslator(source=src_lang, target='en').translate(text)
    except:
        return text

def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0:
        return "Positive", polarity
    elif polarity < 0:
        return "Negative", polarity
    else:
        return "Neutral", polarity

def generate_chart_base64(sentiment):
    labels = ['Positive', 'Negative', 'Neutral']
    values = [1 if sentiment == label else 0 for label in labels]

    fig, ax = plt.subplots()
    ax.bar(labels, values, color=['green', 'red', 'gray'])
    ax.set_title("Sentiment Analysis")

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    plt.close(fig)
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    encoded = base64.b64encode(image_png).decode('utf-8')
    return encoded

def index(request):
    form = TextForm()
    return render(request, 'translator/index.html', {'form': form})

def process_text(request):
    if request.method == 'POST':
        form = TextForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['input_text']
            lang_code = detect_language(text)
            translated = translate_text(text, lang_code)
            sentiment, polarity = analyze_sentiment(translated)
            chart_base64 = generate_chart_base64(sentiment)

            return render(request, 'translator/result.html', {
                'original_text': text,
                'translated_text': translated,
                'language': LANGUAGE_MAP.get(lang_code, lang_code),
                'sentiment': sentiment,
                'polarity': polarity,
                'chart_base64': chart_base64
            })

    return render(request, 'translator/index.html', {'form': TextForm()})
