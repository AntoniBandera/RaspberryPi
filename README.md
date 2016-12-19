Basic image for raspberry pi 3 B
=============================================
This is basic image made for raspbery pi 3 B base on yocto project

***
More info about yocto project you can find on:

https://www.yoctoproject.org/

http://git.yoctoproject.org/cgit/cgit.cgi/meta-raspberrypi/about/
***

Getting Started
---------------
If you want use it in your own raspberry

1.  Merge files in to the one file

 	   `$ cat a b c > image`
	    
	Make it executable:
	
 	   `$ chmod +x iamge`

2.  Copy image to SD card

	   `$ dd if=~/ of= +x iamge`
	   
	Use `lsblk' to find path of sd card
