import numpy as np
import librosa
import soundfile as sf


def remove_noise(audio_file, output_file, noise_factor=0.02):
    # Load audio file
    signal, sr = librosa.load(audio_file, sr=None)
    
    # Calculate the mean and standard deviation of the signal
    mean = np.mean(signal)
    std_dev = np.std(signal)
    
    # Identify noise threshold
    noise_threshold = mean + (std_dev * noise_factor)
    
    # Remove noise from the signal
    filtered_signal = np.where(np.abs(signal) < noise_threshold, 0, signal)
    
    # Save the filtered audio
    sf.write(output_file, filtered_signal, sr)
    
    print(f'Noise removed. Filtered audio saved as: {output_file}')


# Example usage:
# remove_noise('input_audio.wav', 'output_audio.wav', noise_factor=0.02)
