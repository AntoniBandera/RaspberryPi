import math
import time

import Adafruit_Nokia_LCD as LCD
import Adafruit_GPIO.SPI as SPI

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


# Raspberry Pi hardware SPI config:
DC = 23
RST = 24
SPI_PORT = 0
SPI_DEVICE = 0

SCLK = 4
DIN = 17
DC = 23
RST = 24
CS = 8

# Hardware SPI usage:
disp = LCD.PCD8544(DC, RST, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=4000000))

# Initialize library.
disp.begin(contrast=60)

# Clear display.
disp.clear()
disp.display()

# Create image buffer.
# Make sure to create image with mode '1' for 1-bit color.
image = Image.new('1', (LCD.LCDWIDTH, LCD.LCDHEIGHT))

# Load default font.
#font = ImageFont.load_default()
font1 = ImageFont.truetype('PixelOperatorMono-Bold.ttf', 10)
font2 = ImageFont.truetype('PixelOperatorMono-Bold.ttf', 20)

# Alternatively load a TTF font.
# Some nice fonts to try: http://www.dafont.com/bitmap.php
font = ImageFont.truetype('PixelOperatorMono-Bold.ttf', 15)

# Create drawing object.
draw = ImageDraw.Draw(image)

# Define text and get total width.
text = 'Alchemik-Spotkanie w kraczmie'
maxwidth, height = draw.textsize(text, font=font)

# Set starting position.
startpos = 13
pos = startpos


#read names of songs
#wc play_lista | cut -c 3-5   #how many lince has play lista

from os import popen

how_many_songs = int(popen("wc play_list | cut -c 3-5").read())  #check how many song is n play list
list = [popen("sed -n 1p play_list").read()] #takes 1'th name of song

counter = 1
while (counter <= how_many_songs):
	counter += 1
	list.append(popen("sed -n "+str(counter)+"p play_list").read())

# Animate text moving in sine wave.
print 'Press Ctrl-C to quit.'
which_song_is_playing = 0 
previous_song = 0
FM = 106.5
pr_FM = 106.5


import subprocess as sub
import signal
import os

print list[which_song_is_playing]

os.chdir("/home/pi/fm")
f="sudo ./fm_transmitter -f " + str(FM) + " " + list[which_song_is_playing]
process = sub.Popen( f, shell=True)
number_pid = process.pid + 5
#os.kill(number_pid, signal.SIGINT)
print f

while True:
	draw.rectangle((0,0,83,47), outline=255, fill=255)
	# Enumerate characters and draw them offset vertically based on a sine wave.
	song_1 = which_song_is_playing - 1
	if song_1 < 0 :
		song_1 = how_many_songs - 1
	song_2 = song_1 - 1
	if song_2 < 0 :
		song_2 = how_many_songs - 1
	song_3 = song_2 - 1
	if song_3 < 0 :
		song_3 = how_many_songs - 1
	song_plus1 = which_song_is_playing + 1
	if song_plus1 > (how_many_songs - 1) :
		song_plus1 = 0

	draw.text((0, 0), list[song_3] , font=font1, fill=0)
	draw.text((0, 8), list[song_2] , font=font1, fill=0)
	draw.text((0, 16), list[song_1] , font=font1, fill=0)

	draw.text((0, 24), list[which_song_is_playing] , font=font, fill=0)


	draw.text((0, 37), list[song_plus1] , font=font1, fill=0)

	if (previous_song != which_song_is_playing) or (pr_FM != FM) :
		print FM
		os.chdir("/home/pi/fm")
		os.kill(number_pid, signal.SIGINT)
		time.sleep(0.5)
		f="sudo ./fm_transmitter -f " + str(FM) + " " + list[which_song_is_playing]
		process = sub.Popen( f, shell=True)
		number_pid = process.pid + 5
		previous_song = which_song_is_playing
		pr_FM = FM
	# Draw the image buffer.
	disp.image(image)
	disp.display()
	# Move position for next frame.
	pos -= 5
	# Start over if text has scrolled completely off left side of screen.
	if pos < -maxwidth:
		pos = startpos
	# Pause briefly before drawing next frame.
#	time.sleep(0.5)
	s = raw_input()

	if s == "p":
		which_song_is_playing += 1
		if (which_song_is_playing + 1) > how_many_songs :
			which_song_is_playing = 0
	if s == "l" :
		which_song_is_playing -= 1
		if which_song_is_playing < 0 :
			which_song_is_playing = (how_many_songs - 1)
	if s == "f" :
		w = "q"
		while w != "r":
			draw.rectangle((0,0,83,47), outline=255, fill=255)
			draw.text((0, 20), "FM:"+str(FM) , font=font2, fill=0)
			disp.image(image)
			disp.display()
			w = raw_input()
			if w == "p" :
				FM += 0.1
			if w =="l" :
				FM -= 0.1

	
		


