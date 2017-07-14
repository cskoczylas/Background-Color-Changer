# Background Color Changer

1)	Install Python 3.6+ and Pillow
		pip install Pillow
		or get from PIL's git page - https://github.com/python-pillow/Pillow

2)	Place the transparent image in the Images Folder
		transparent image should be the size of you screen
		name the image transparent.png

3)	Run setup.py
		change values in setup.py to your discretion

4)	Open up task scheduler and schedule a new task
		Under "Actions" tab, hit New
			The Action will be Start a program
			Hit browse and search from wscript.exe - this is usually under C:\Windows\System32\wscript.exe
			Under arguments, add the absolute path of invisible.vbs and background.bat - quote are necessary
				For me, this looks like 
					"C:\Background Color Changer\invisible.vbs" "C:\Background Color Changer\background.bat"
		Now you can set your trigger - I do it when I log on
		Save the new task when you're done

5)	Go to Personalization, and change the desktop background
		Select both "background1.png" and "background2.png" and set windows to change picture every 10 seconds

6)	You're done
		hoorah