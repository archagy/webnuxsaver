import glob
string = glob.glob("*.webm")
string += glob.glob("*.mp4")
print string
