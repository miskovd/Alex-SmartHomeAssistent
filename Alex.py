import speech_recognition as s_r
import pyttsx3
import pywhatkit
import datetime
import RPi.GPIO as GPIO
import time
import os
from playsound import playsound

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)#relay
GPIO.setup(11, GPIO.OUT)#led

GPIO.output(7, 0)
GPIO.output(11, 0)

engine = pyttsx3.init()
#voices = engine.getProperty('voices')
#engine.setProperty('voice', voices[1].id)

r = s_r.Recognizer()
#engine.say("Hello, my name is Alex!")
my_mic = s_r.Microphone(device_index=1) #my microphone-device index is 1,change it to the appropriate device id of your microphone

commant = True

def talk(text):
	print(text)
	engine.say(text)
	engine.runAndWait()

def take_command():
	commant = True
	try:
		with my_mic as source:
			print("Say some words...")
			GPIO.output(11, 1)
			audio = r.listen(source) #take voice input from the microphone
			command = r.recognize_google(audio) #to print voice into text
			command = command.lower()
			if 'alex' in command:
				GPIO.output(11, 0)
				command = command.replace('alex', '')
				
	except:
		pass
	return command

def light_up_the_tree():
	print('Light...')
	try:
		GPIO.output(7, GPIO.HIGH)
		#time.sleep(3)
		#GPIO.output(7, GPIO.LOW)
		#time.sleep(1)
		#GPIO.cleanup()
	except:
		GPIO.cleanup()	

def run_alex():
	global command
	command = take_command()
	print(command)
	if 'find video' in command:
		song = command.replace('find video', '')
		talk('Playing youtube video'+song)
		pywhatkit.playonyt(song)
	elif 'relax' in command:
		os.system('parole -F "relax-video.mp4"')
	elif 'music' in command:
		playsound("christmas-music.mp3")
	#elif 'music' in command:
	#	os.system('parole -F "christmas-music.mp4"')
	elif 'time' in command:
		time = datetime.datetime.now().strftime('%H:%M');
		talk("Time is "+time)
	elif 'hello' in command:
		talk('Hello, my friend.')
	elif 'my name is' in command:
		name = command.replace('my name is', '')
		talk("Hi "+name+", how are you?")
	elif 'light up' in command:
		light_up_the_tree()
	else:
		talk('Please, Tell me again')

try:
	while True:
		run_alex()
except:
	GPIO.cleanup()
