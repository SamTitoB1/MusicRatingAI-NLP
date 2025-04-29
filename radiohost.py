import ollama

def generate_radio_intro_ollama(artist, title, lyrics_excerpt, sentiment_label, bpm, key):
    prompt = f"""
You're a charismatic radio DJ. Give a short and engaging intro for the next track, based on its mood, sentiment, and lyrics.

Song: "{title}" by {artist}  
Tempo: {bpm} BPM  
Sentiment: {sentiment_label}   
Chorus: "{lyrics_excerpt}"
Tonality Mood: "{key[1]}" (based on the song's key)
Create a stylish radio host intro:
"""

    # Correct API call syntax
    response = ollama.chat(
        prompt,
        model="tinyllama",  # or another model available
        temperature=0.7,
        max_tokens=200
    )

    return response['text']  # or use 'content' based on the structure of the response you get
