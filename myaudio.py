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
import playaudio

def record(*args,**kwargs):
	return recordaudio.record(*args,**kwargs)


def play(file,chunk=1024):
	
	playaudio.play(file,chunk)



def main():
		#record(file="my.wav")
		play("my.wav")
		
if __name__ == '__main__':
	main()
	