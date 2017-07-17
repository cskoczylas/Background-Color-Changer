# Background Color Changer

1)	Install Python 3.6+ and Pillow  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pip install Pillow  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;or get from PIL's git page - https://github.com/python-pillow/Pillow

2)	Place the transparent image in the Images Folder  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;transparent image should be the size of you screen  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name the image transparent.png

3)	Run setup.py  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;change values in setup.py to your discretion

4)	Open up task scheduler and schedule a new task  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Under "Actions" tab, hit New  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The Action will be Start a program  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Hit browse and search from wscript.exe - this is usually under C:\Windows\System32\wscript.exe  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Under arguments, add the absolute path of invisible.vbs and background.bat - quote are necessary  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;For me, this looks like  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"C:\Background Color Changer\invisible.vbs" "C:\Background Color Changer\background.bat"  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Now you can set your trigger - I do it when I log on  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Save the new task when you're done

5)	Go to Personalization, and change the desktop background  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Select both "background1.png" and "background2.png" and set windows to change picture every 10 seconds

6)	You're done  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hoorah