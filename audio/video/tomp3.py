import soundfile as sf
import librosa

# wav, sr = sf.read('./sourceaespa.mp4')
wav, sr = librosa.load('./sourceaespa.mp4')
sf.write('./sourceaespa.wav', wav, samplerate=sr)