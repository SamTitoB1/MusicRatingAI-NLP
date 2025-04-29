# lyrics_api.py

import requests
import torch
from transformers import BertTokenizer, BertForSequenceClassification

def get_lyrics(artist, title):
    url = f"https://api.lyrics.ovh/v1/{artist}/{title}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data['lyrics']
    else:
        return None

def analyze_lyrics_with_bert(lyrics_text):
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
    model = BertForSequenceClassification.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')

    inputs = tokenizer(lyrics_text, return_tensors='pt', truncation=True, padding=True, max_length=512)

    with torch.no_grad():
        outputs = model(**inputs)

    sentiment_score = torch.nn.functional.softmax(outputs.logits, dim=-1)
    sentiment_label = sentiment_score.argmax().item()

    sentiment_labels = ['very negative', 'negative', 'neutral', 'positive', 'very positive']
    sentiment = sentiment_labels[sentiment_label]
    return sentiment, sentiment_score[0, sentiment_label].item()
