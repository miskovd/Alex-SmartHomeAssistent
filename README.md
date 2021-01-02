# Alex-SmartHomeAssistent
Alex :robot: - Smart Home Virtual Assistant powered by Raspberry Pi 4. 
This is the simplest project that demonstrate voice controlled assistent. He can answer some questions, play(local music or video), search youtube video and **light up electric appliance**.

[Video Demo](https://youtu.be/Glquotd4dMo)

Current features:
Can understand commands:
* Hello Alex
* Alex, my name is [Your name]
* Alex, what time is it?
* Alex, turn on the music.
* Alex, relax.
* Alex, find video [YouTube video name]
* Alex, Light up Christmas Tree.

Last command can turn on any electrical appliance using RPi.GPIO library and Relay switch.

Used Hardware:
* Raspbbery Pi 4 8Gb (Ubuntu 20.04/Python v3.8)
* 5v Relay Switch (DC AC 220v)
* Led(To indicate when Alex listen you)
* Microphone
