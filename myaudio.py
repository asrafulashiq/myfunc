"""
	This package has some functions to record or play 
	audio file..
	For recording call record().
	For playing call play().

"""

import pyaudio
import wave
import sys
import recordaudio
import play

def record(*args,**kwargs):
	return recordaudio.record(*args,**kwargs)


def play(file,chunk=1024):
	"""	
		play an audio file from a file
		input argumets:
			chunk : default 1024
			file : audio file name to be played, like .wav
	"""
	play.play(file,chunk)



def main():
		record(file="my.wav")
		play("my.wav")
		pass
if __name__ == '__main__':
	main()
	