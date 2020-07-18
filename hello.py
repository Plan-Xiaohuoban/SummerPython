

import os
import easygui

file = easygui.fileopenbox()
with open(file, "r",encoding="utf-8") as f:
    print(f.read())

print("Hello~"*3)