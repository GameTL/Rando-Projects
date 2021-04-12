# work for both Mac, Windows, Linux
# use clear() for clearing terminal
import os
import platform
platform = platform.system()
if platform == 'Darwin':
    text = "clear"
elif platform == 'Windows':
    text = 'cls'


def clear():
    os.system(text)
