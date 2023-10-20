from pydub import AudioSegment
from pydub.playback import play

# Carregar o arquivo MP3
audio = AudioSegment.from_file("music.mp3", format="mp3")

# Reproduzir a música
play(audio)
