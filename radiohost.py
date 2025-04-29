import openai

def generate_radio_intro(artist, title, lyrics_excerpt, sentiment_label, bpm, key):
    prompt = f"""
You're a charismatic radio DJ. Give a short and engaging intro for the next track, based on its mood, sentiment, and lyrics.

Song: "{title}" by {artist}  
Tempo: {bpm} BPM  
Sentiment: {sentiment_label}   
Chorus: "{lyrics_excerpt}"
Tonality Mood:"{key[1]}"(based on the song's key)
Create a stylish radio host intro:
"""

    response = openai.ChatCompletion.create(
        model="gpt-4",  # or gpt-3.5-turbo
        messages=[{"role": "user", "content": prompt}],
        max_tokens=100,
        temperature=0.8
    )
    return response.choices[0].message["content"]
