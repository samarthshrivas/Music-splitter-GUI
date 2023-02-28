from io import BytesIO
from pydub import AudioSegment
import numpy as np
import base64

def load_audio(audio_file):
    audio = AudioSegment.from_file(audio_file.name)
    samples = np.array(audio.get_array_of_samples())
    samples = samples.reshape((audio.channels, -1), order='F')
    return samples
    
def create_audio_player(audio_data, component_key):
    """
    Create an HTML audio player using JavaScript and HTML5 Audio API.

    Parameters:
    audio_data (bytes): The audio data to be played.
    component_key (int): A unique key for the audio component.

    Returns:
    str: The HTML code for the audio player.
    """
    html_template = """
    <div id="audio-container-{component_key}">
        <audio id="audio-{component_key}">
            <source src="data:audio/wav;base64,{audio_data}" type="audio/wav" />
        </audio>
        <button onclick="playAudio()">Play</button>
    </div>
    <script>
        var audio{component_key} = new Audio();
        var source{component_key} = document.createElement("source");
        source{component_key}.type = "audio/wav";
        source{component_key}.src = "data:audio/wav;base64,{audio_data}";
        audio{component_key}.appendChild(source{component_key});

        function playAudio() {{
            var audioContainers = document.querySelectorAll('[id^="audio-container-"]');
            for (var i = 0; i < audioContainers.length; i++) {{
                var audio = audioContainers[i].querySelector("audio");
                if (audio.paused) {{
                    audio.play();
                }}
            }}
        }}
    </script>
    """

    html = html_template.format(component_key=component_key, audio_data=base64.b64encode(audio_data).decode())
    return html




def set_audio_volume(audio_player, volume):
    audio_player._player.volume = volume / 100
