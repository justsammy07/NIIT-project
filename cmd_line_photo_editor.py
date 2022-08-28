from resize_func_CLPE import *
from blur_func_CLPE import *
from gray_scale_CLPE import *
import cv2
import os.path

print("""
|----------------------------|
|       Welcome to the       |
|  Command Line Photo Editor |
|----------------------------|""")
while True:
    chose = input("""
    |-------------------|
    |What would you like|
    |To do:             |
    |--{resize}         |
    |--{blur} or        |
    |--{gray}           |
    |To shut down the   |
    |The program:       |
    |--{exit}           |
    |-------------------|""")
    if chose.lower() == "exit":
        print("Program Shut Down")
        break
    elif chose.lower() == "resize":
        while True:
            resize_chose = input("""
        |-----------------|
        |Would you like to|
        |resize to:       |
        |--{small}        |
        |--{medium}       |
        |--{large}        |
        |To forfeit action|
        |--{exit}         |
        |-----------------|""")
            if resize_chose == "exit":
                print("""
                |-------------------|
                | Action Forfeited  |
                |-------------------|""")
                break
            elif resize_chose.lower() == "small":
                resize_small()
            elif resize_chose.lower() == "medium":
                resize_medium()
            elif resize_chose.lower() == "large":
                resize_large()
            else:
                print("""
                |---------------|
                | Invalid Entry |
                |---------------|""")
    elif chose.lower() == "blur":
        blur()
    elif chose.lower() == "gray":
        gray_scale(
