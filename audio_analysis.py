# audio_analysis.py

import librosa
import numpy as np

def analyze_audio(audio_file_path):
    y, sr = librosa.load(audio_file_path)
    tempo, _ = librosa.beat.beat_track(y=y, sr=sr)
    return tempo[0] if isinstance(tempo, np.ndarray) else tempo



# Function to get the key (tonic) and the mode (major/minor)
def get_key_and_mode(chroma_vector):
    # The chroma vector represents energy for each of the 12 pitch classes
    # Find the index of the maximum value in the chroma vector
    dominant_pitch_class_idx = np.argmax(chroma_vector)
    
    # Map index back to the corresponding note (0 = C, 1 = C#, 2 = D, ..., 11 = B)
    pitch_classes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    tonic = pitch_classes[dominant_pitch_class_idx]
    
    # Define the intervals for major and minor scales (relative to tonic)
    # Major scale intervals: [2, 4, 5, 7, 9, 11, 12]
    # Minor scale intervals: [2, 3, 5, 7, 8, 10, 12]
    
    # To determine major/minor, we'll look at the third interval
    # Major third is 4 semitones, minor third is 3 semitones
    
    # Look at the chroma vector to see if we have a major third or minor third
    major_third_idx = (dominant_pitch_class_idx + 4) % 12  # 4 semitones up from tonic
    minor_third_idx = (dominant_pitch_class_idx + 3) % 12  # 3 semitones up from tonic
    
    major_third_value = chroma_vector[major_third_idx]
    minor_third_value = chroma_vector[minor_third_idx]
    
    # If the major third has more energy, it's a major key, otherwise minor
    if major_third_value > minor_third_value:
        mode = "Major"
    else:
        mode = "Minor"
    
    return tonic, mode

# Example usage:
def analyze_audio_for_key_and_mode(audio_file_path):
    # Load the audio file
    y, sr = librosa.load(audio_file_path)
    
    # Extract chroma features
    chroma = librosa.feature.chroma_cqt(y=y, sr=sr)
    
    # Take the mean across time (for the whole track)
    chroma_mean = np.mean(chroma, axis=1)
    
    # Get the key and mode (major/minor)
    tonic, mode = get_key_and_mode(chroma_mean)
    
    print(f"The track is in the key of {tonic} and the mode is {mode}.")
    
    return tonic, mode

