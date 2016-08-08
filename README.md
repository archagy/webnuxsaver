# Webnuxsaver
Screensaver for linux with web-kit that can loop of multiple videos in mp4 and webm format.

# Preview
![screenshot from 2016-02-08 09 35 42](https://cloud.githubusercontent.com/assets/4847289/12890026/5ebe4064-ce47-11e5-9367-c97e9b0b9e7b.png)



# Installation

Install xscreensaver
> sudo apt-get install xscreensaver

and install webscreensaver.

> [instructions here](https://github.com/lmartinking/webscreensaver)

clone webnuxsaver project wherever you want and add mp4/webm format in folder videos.
run getArrayVideos.py inside of the videos folder to get all the array of videos.

> cd videos 
> python getArrayVideos.py

Example output:
> ['nameofvideo.mp4','nameofvideo2.webm'.....]

Copy the output and add in index.html  the array of videos in *videosStorage* variable.

Open index.html in browser to view everything is working fine and copy de path.

Example path in browser:
> file:///usr/lib/xscreensaver/webnuxsaver/index.html

Then need to open xscreenserver to generate a ~/.xscreensaver file.
Close xscreensaver and open ~/.xscreensaver file
then edit `~/.xscreensaver`:

    programs:
                  webscreensaver                  \n\

Open xscreensaver and search for webscreensaver then click in settings then advanced>>

in command line add:
> webscreensaver -url "file:///usr/lib/xscreensaver/webnuxsaver/index.html"

Note: is the url of local file of the index.html. Open your browser to get the path.

Extra note: Try to use simple name of the videos without special characters.


Finally to start with xscreensaver as default.
Follow the next steps:


    1) xscreensaver needs to be launched at startup via "Startup Applications" (hit Super and type "Startup"). Add a new entry to launch the xscreensaver daemon on startup as xscreensaver -no-splash.

    2)You need to bring up the xscreensaver config app. Hit Super and type screensaver. Set the "Blank after x minutes" to your desired amount (e.g. 5 minutes). Remember this value for later. Ensure "Lock screen after" is UNCHECKED.

    3)Finally, go to System Settings / Brightness & Lock. Set "Turn screen off when inactive for x minutes" to the same value as you set xscreensavers "Blank after x minutes" setting (e.g. 5 minutes). Then still under Brightness & Lock, set "Lock screen after:" to "Screen turns off".

Or in shortcuts keyboard add the next command:

> xscreensaver-command -lock 

with the shortcut you prefer. Ex. Ctrl+alt+l

more info: http://askubuntu.com/questions/491516/how-do-i-configure-xscreensaver-to-use-the-gnome-lockscreen-on-ubuntu-14-04
