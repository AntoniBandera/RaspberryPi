high = 15
czcionka = "PixelOperator.ttf"


import time

import Adafruit_Nokia_LCD as LCD
import Adafruit_GPIO.SPI as SPI

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


# Raspberry Pi hardware SPI config:
DC = 23
RST = 24
SPI_PORT = 0
SPI_DEVICE = 0

# Raspberry Pi software SPI config:
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

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
image = Image.new('1', (LCD.LCDWIDTH, LCD.LCDHEIGHT))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a white filled box to clear the image.
draw.rectangle((0,0,LCD.LCDWIDTH,LCD.LCDHEIGHT), outline=255, fill=255)

# Load default font.
#font = ImageFont.load_default()

# Alternatively load a TTF font.
# Some nice fonts to try: http://www.dafont.com/bitmap.php
#font = ImageFont.truetype('Minecraftia.ttf', 8)
font = ImageFont.truetype(czcionka, high)

# Write some text.
#s = raw_input()

s = "----"

#draw.text((1,10), 'Hello World!', font=font)
#draw.text((1,20), 'Hello World!', font=font)
#draw.text((1,30), 'Hello World!', font=font)
#draw.text((1,40), 'Hello World!', font=font)


# Display image.
disp.image(image)
disp.display()


draw.text((1,1),  'Teraz gramy' , font=font)
draw.text((1,20), s, font=font)
disp.image(image)
disp.display()

f = "ls"


import os
import subprocess as sub
import signal

temp_cpu = os.popen(f).readline()

os.chdir("fm")
pwd_pwd = os.popen("pwd").readline()
print pwd_pwd

#sub.call("sudo ./fm_transmitter -f 100.0 o.wav",stdout=sub.PIPE)
#pro = sub.Popen(["sudo ./fm_transmitter -f 100.0","o.wav "], stdout=sub.PIPE)
process = sub.Popen("sudo ./fm_transmitter -f 100.0 o.wav", shell=True)

#sub.Popen("TASKKill /F /PID {pid} /T".format(pid=process.pd))

print temp_cpu



disp.clear()
disp.display()
image = Image.new('1', (LCD.LCDWIDTH, LCD.LCDHEIGHT))
draw = ImageDraw.Draw(image)
draw.text((1,1),  'Teraz gramy' , font=font)

F = "100.0"

print 'Press Ctrl-C to quit.'
while True:
	przerwa = raw_input()
	

	if przerwa == "f" :
#		"Podaj czestotliwosc"
		print "Podaj czestotliowsc"
		numer_pid = process.pid +5
		F = raw_input()
		os.kill(numer_pid, signal.SIGINT)
		thread = "sudo ./fm_transmitter -f " + F + " o.wav"
		process = sub.Popen( thread, shell=True)
		print thread
		
	if przerwa == "n" :
#		"Podaj nazwe utworu"
		print "Podaj nazwe utowru"
		numer_pid = process.pid +5
		name = raw_input()
		print name
		os.kill(numer_pid, signal.SIGINT)
		thread = "sudo ./fm_transmitter -f " + F + " " + name
		process = sub.Popen( thread, shell=True)
		print thread

#		process.terminate()
	draw.rectangle((0,0,LCD.LCDWIDTH,50), outline=255, fill=255)
	disp.clear()
	disp.image(image)
	disp.display()
#		draw.text((1,20), d, font=font)
	disp.image(image)
	disp.display()
	time.sleep(0.2)


