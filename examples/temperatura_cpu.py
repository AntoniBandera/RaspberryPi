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

f = "/opt/vc/bin/vcgencmd measure_temp"


import os
temp_cpu = os.popen(f).readline()



print temp_cpu

temp_cpu_poprzednia = os.popen(f).readline()


disp.clear()
disp.display()
image = Image.new('1', (LCD.LCDWIDTH, LCD.LCDHEIGHT))
draw = ImageDraw.Draw(image)
draw.text((1,1),  'Teraz gramy' , font=font)


print 'Press Ctrl-C to quit.'
while True:
	temp_cpu_obecna = os.popen(f).readline()

	if temp_cpu_poprzednia != temp_cpu_obecna :
		temp_cpu_poprzednia = temp_cpu_obecna
#		draw.text((1,20), "", font=font)
		draw.rectangle((0,0,LCD.LCDWIDTH,48), outline=255, fill=255)
		disp.clear()
		disp.image(image)
		disp.display()
		
	draw.text((1,20), temp_cpu_poprzednia, font=font)
	disp.image(image)
	disp.display()
	time.sleep(0.2)

