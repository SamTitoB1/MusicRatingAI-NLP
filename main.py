# main.py

from lyrics_api import get_lyrics, analyze_lyrics_with_bert
from audio_analysis import analyze_audio, analyze_audio_for_key_and_mode
from radiohost import generate_radio_intro

def sentiment_rating(sentiment_label):
    if (sentiment_label in ["positive", "very positive"]):
        sentiment = 1
    elif (sentiment_label in ["negative", "very negative"]):
        sentiment = -1
    elif (sentiment_label in ["neutral"]):
        sentiment = 0
    return sentiment

def tempo_rating(tempo_bpm):
    if (tempo_bpm > 100):
        tempo = 1
    elif (tempo_bpm < 100):
        tempo = -1
    elif (tempo_bpm == 100):
        tempo = 0
    return tempo

def key_rating(key):
    if (key[1] == "Major"):
        key = 1
    elif (key[1] == "Minor"):
        key = -1
    return key
def main():
    artist = "Jack Johnson"
    title = "Upside Down"
    print(f"Provided song: {artist} - {title}...")
    #audio_path = "C:/Users/San/Downloads/Eminem - Lose Yourself - EminemMusic.mp3"
    #audio_path = "C:/Users/San/Downloads/Phil Collins - In the Air Tonight - Rewind Music.mp3"
    #audio_path = "C:/Users/San/Downloads/Promises, Promises - Naked Eyes.mp3"
    #audio_path = "C:/Users/San/Downloads/Philip Bailey, Phil Collins - Easy Lover (Audio) - EarthWindandFireVEVO.mp3"
    #audio_path = "C:/Users/San/Downloads/Duran Duran - Come Undone - DuranDuranMusic1.mp3"
    #audio_path = "C:/Users/San/Downloads/Daft Punk - Get Lucky (Official Audio) ft. Pharrell Williams, Nile Rodgers - DaftPunkVEVO.mp3"
    audio_path = "C:/Users/San/Downloads/Jack Johnson - Upside Down - MusicShop94.mp3"
   # "C:\Users\San\Downloads\"
    # Fetch lyrics
    lyrics = get_lyrics(artist, title)
    if not lyrics:
        print("\nLyrics not found. Please check the artist/title.")
        return

    print("\nLyrics fetched successfully!")
    print("\nAnalyzing lyrics sentiment with BERT...")

    sentiment_label, sentiment_score = analyze_lyrics_with_bert(lyrics)
    print(f"\nLyrics Sentiment: {sentiment_label} (Confidence: {sentiment_score:.2f})")

    # Analyze audio
    tempo_bpm = float(analyze_audio(audio_path))
    print(f"Detected Tempo (BPM): {tempo_bpm:.2f}")

    # Simple mood conclusion
    print("\n🎵 Mood Analysis Result:")
    if (sentiment_label in ["positive", "very positive"]) and tempo_bpm > 100:
        print("-> This is a Happy / Party Song!")
    elif (sentiment_label in ["negative", "very negative"]) and tempo_bpm < 100:
        print("-> This is a Sad / Chill Song.")
    else:
        print("-> This is a Mixed Mood Song.")


    # Privide chroma Key best fit
    key = analyze_audio_for_key_and_mode(audio_path)
    #print(key)
    
    # PRINT ALL THE RESULTS
    sRate = int(sentiment_rating(sentiment_label))
    tRate = int(tempo_rating(tempo_bpm))
    kRate = int(key_rating(key))
    print(sRate)
    print(tRate)
    print(kRate)

    rating = (kRate*2)+(tRate*1)+(sRate*-2)
    if rating >= 3:
        print("HYPE")
    elif rating == 2:
        print("Kinda Hype + bit chill")
    elif rating == 1:
        print("Kinda Chill + bit hype")
    elif rating <= 0:
        print("c h i l l")
    print(f"Rating: {rating}")
    # The final rating is a combination of the sentiment, tempo, and key ratings.


    #Rating function.
    
    print("\nGenerating radio intro...")
    radio_intro = generate_radio_intro(artist, title, lyrics, sentiment_label, tempo_bpm, key)

if __name__ == "__main__":
    main()


