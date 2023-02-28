import tempfile
import numpy as np
from spleeter.separator import Separator
from spleeter.audio.adapter import AudioAdapter

def separate_audio(audio_file):
    audio_loader = AudioAdapter.default()
    sample_rate = 44100
    with tempfile.NamedTemporaryFile(suffix='.wav', delete=False) as audio_temp_file:
        audio_temp_file.write(audio_file.read())
        waveform, _ = audio_loader.load(audio_temp_file.name, sample_rate=sample_rate)
    separator = Separator('spleeter:2stems')

    prediction = separator.separate(waveform)
    return prediction
