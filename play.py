
import pyaudio
import wave
import sys

def play(file,chunk=1024):
	"""	
		play an audio file from a file
		input argumets:
			chunk : default 1024
			file : audio file name to be played, like .wav
	"""

	wf = wave.open(file, 'rb')
	p = pyaudio.PyAudio()
	stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True)
	data = wf.readframes(chunk)
	while data != '':
		stream.write(data)
		data = wf.readframes(chunk)
	stream.stop_stream()
	stream.close()
	p.terminate()
