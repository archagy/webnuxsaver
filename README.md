# Webnuxsaver
Screensaver for linux with web-kit that can loop of multiple videos in mp4 and webm format.

# Preview
![screenshot from 2016-02-08 09 35 42](https://cloud.githubusercontent.com/assets/4847289/12890026/5ebe4064-ce47-11e5-9367-c97e9b0b9e7b.png)


#Installation
### LinuxMint
Access in 

> /usr/share/cinnamon-screensaver/screensavers/webkit@cinnamon.org/

and clone the project, you need use sudo or root.

in the folder videos add all the videos as you want. 
run getArrayVideos.py inside of the videos folder to get all the array of videos.

1)
> cd videos

2)
> python getArrayVideos.py

Copy the output and add in index.html  the array of videos in *videosStorage* variable.



**Important note: in metadata.json the uuid value  must be  equal to the name folder.**


### Ubuntu

Install xscreensaver
> sudo apt-get install xscreensaver

and install webscreensaver.

> [instructions](https://github.com/lmartinking/webscreensaver)

in the folder videos add all the videos as you want. 
run getArrayVideos.py inside of the videos folder to get all the array of videos.

1)
> cd videos 

2)
> python getArrayVideos.py

Copy the output and add in index.html  the array of videos in *videosStorage* variable.
