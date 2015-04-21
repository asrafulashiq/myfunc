"""PyAudio example: Record a few seconds of audio and save to a WAVE file."""

import pyaudio
import wave
import sys
from scipy.io.wavfile import read

def record(
	file="my.wav",
	CHUNK = 1024,
	FORMAT = pyaudio.paInt16,
	CHANNELS = 2,
	RATE = 44100,
	RECORD_SECONDS = 5):

	p = pyaudio.PyAudio()

	stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

	print("* recording")

	frames = []

	for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
	    data = stream.read(CHUNK)
	    frames.append(data)

	print("* done recording")

	stream.stop_stream()
	stream.close()
	p.terminate()


	if len(file)<=1:
		file="tmp.wav"
	WAVE_OUTPUT_FILENAME = file
	wf = wave.open(WAVE_OUTPUT_FILENAME, 'w')
	wf.setnchannels(CHANNELS)
	wf.setsampwidth(p.get_sample_size(FORMAT))
	wf.setframerate(RATE)
	wf.writeframes(b''.join(frames))
	wf.close()

	adata = read(file)
	return adata[1]
