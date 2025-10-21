import sounddevice as sd
import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import write
from scipy.fft import fft, fftfreq
from scipy import signal
import os
import random

# Configuration parameters
SAMPLE_RATE = 44100  # Hz (CD quality)
DURATION = 5  # seconds
CHANNELS = 1  # Mono audio

def record_audio(duration=DURATION, sample_rate=SAMPLE_RATE):
    """
    Record audio from the default microphone.
    
    Args:
        duration: Recording duration in seconds
        sample_rate: Sampling rate in Hz
    
    Returns:
        audio_data: Recorded audio as numpy array
    """
    print(f"Recording for {duration} seconds...")
    print("Speak now!")
    
    # Record audio
    audio_data = sd.rec(int(duration * sample_rate), 
                        samplerate=sample_rate, 
                        channels=CHANNELS, 
                        dtype='float64')
    sd.wait()  # Wait until recording is finished
    
    print("Recording finished!")
    return audio_data.flatten()

def plot_waveform(audio_data, sample_rate=SAMPLE_RATE, save_path=None):
    """
    Plot the time-domain waveform of audio data.
    
    Args:
        audio_data: Audio signal as numpy array
        sample_rate: Sampling rate in Hz
        save_path: Optional path to save the plot
    """
    # Create time axis
    time = np.linspace(0, len(audio_data) / sample_rate, num=len(audio_data))
    
    # Create figure and plot
    plt.figure(figsize=(12, 6))
    plt.plot(time, audio_data, linewidth=0.5, color='blue')
    plt.xlabel('Time (seconds)', fontsize=12)
    plt.ylabel('Amplitude', fontsize=12)
    plt.title('Speech Signal Waveform (Time Domain)', fontsize=14, fontweight='bold')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"Plot saved to {save_path}")
    
    plt.show()

def save_audio(audio_data, filename, sample_rate=SAMPLE_RATE):
    """
    Save audio data to a WAV file.
    
    Args:
        audio_data: Audio signal as numpy array
        filename: Output filename with path
        sample_rate: Sampling rate in Hz
    """
    # Normalize and convert to 16-bit PCM
    audio_normalized = np.int16(audio_data * 32767)
    write(filename, sample_rate, audio_normalized)
    print(f"Audio saved to {filename}")

def plot_frequency_spectrum(audio_data, sample_rate=SAMPLE_RATE, save_path=None):
    """
    Perform FFT and plot the frequency spectrum.
    
    Args:
        audio_data: Audio signal as numpy array
        sample_rate: Sampling rate in Hz
        save_path: Optional path to save the plot
    """
    # Perform FFT
    n = len(audio_data)
    fft_values = fft(audio_data)
    fft_magnitude = np.abs(fft_values)
    frequencies = fftfreq(n, 1/sample_rate)
    
    # Only plot positive frequencies
    positive_freq_idx = frequencies > 0
    frequencies = frequencies[positive_freq_idx]
    fft_magnitude = fft_magnitude[positive_freq_idx]
    
    # Create plot
    plt.figure(figsize=(12, 6))
    plt.plot(frequencies, fft_magnitude, linewidth=0.5, color='green')
    plt.xlabel('Frequency (Hz)', fontsize=12)
    plt.ylabel('Magnitude', fontsize=12)
    plt.title('Frequency Spectrum (FFT)', fontsize=14, fontweight='bold')
    plt.grid(True, alpha=0.3)
    plt.xlim(0, sample_rate/2)  # Nyquist frequency
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"Frequency spectrum saved to {save_path}")
    
    plt.show()

def plot_spectrogram(audio_data, sample_rate=SAMPLE_RATE, save_path=None):
    """
    Generate and plot spectrogram of the audio signal.
    
    Args:
        audio_data: Audio signal as numpy array
        sample_rate: Sampling rate in Hz
        save_path: Optional path to save the plot
    """
    # Compute spectrogram
    frequencies, times, spectrogram = signal.spectrogram(
        audio_data, 
        sample_rate,
        window='hann',
        nperseg=1024,
        noverlap=512
    )
    
    # Create plot
    plt.figure(figsize=(12, 6))
    plt.pcolormesh(times, frequencies, 10 * np.log10(spectrogram + 1e-10), 
                   shading='gouraud', cmap='viridis')
    plt.ylabel('Frequency (Hz)', fontsize=12)
    plt.xlabel('Time (seconds)', fontsize=12)
    plt.title('Spectrogram', fontsize=14, fontweight='bold')
    plt.colorbar(label='Power (dB)')
    plt.ylim(0, 8000)  # Focus on speech frequencies
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"Spectrogram saved to {save_path}")
    
    plt.show()

def export_all_plots(audio_data, sample_rate=SAMPLE_RATE, output_dir='output'):
    """
    Generate and export all plots as PNG files with random numbers.
    
    Args:
        audio_data: Audio signal as numpy array
        sample_rate: Sampling rate in Hz
        output_dir: Directory to save plots (default: 'output')
    
    Returns:
        random_id: The random number used for file naming
    """
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Created output directory: {output_dir}")
    
    # Generate random ID for files
    random_id = random.randint(10000, 99999)
    print(f"\nSession ID: {random_id}")
    
    # Define file paths
    audio_path = os.path.join(output_dir, f'recorded_speech_{random_id}.wav')
    waveform_path = os.path.join(output_dir, f'waveform_{random_id}.png')
    spectrum_path = os.path.join(output_dir, f'frequency_spectrum_{random_id}.png')
    spectrogram_path = os.path.join(output_dir, f'spectrogram_{random_id}.png')
    
    # Save audio file
    save_audio(audio_data, audio_path, sample_rate)
    
    # Generate and save all plots
    print("\nExporting all plots...")
    plot_waveform(audio_data, sample_rate, save_path=waveform_path)
    plot_frequency_spectrum(audio_data, sample_rate, save_path=spectrum_path)
    plot_spectrogram(audio_data, sample_rate, save_path=spectrogram_path)
    
    print(f"\n[SUCCESS] All files exported to '{output_dir}/' directory with ID: {random_id}")
    return random_id




# Main execution
if __name__ == "__main__":
    print("=" * 50)
    print("Speech Signal Capture and Visualization")
    print("=" * 50)
    
    # Record audio
    audio = record_audio(duration=DURATION, sample_rate=SAMPLE_RATE)
    
    # Display basic statistics
    print(f"\nAudio Statistics:")
    print(f"Duration: {DURATION} seconds")
    print(f"Sample Rate: {SAMPLE_RATE} Hz")
    print(f"Number of samples: {len(audio)}")
    print(f"Max amplitude: {np.max(np.abs(audio)):.4f}")
    print(f"Mean amplitude: {np.mean(np.abs(audio)):.4f}")
    
    # Export all files (audio + plots) with random ID
    export_all_plots(audio, SAMPLE_RATE, output_dir='output')