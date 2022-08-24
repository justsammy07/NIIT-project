# Tunde = 2
# Cindy = 1
# Samuel = 3
# Richard = 4
# print(Tunde + Cindy + Samuel + Richard)
# print(Richard - Tunde)
# print(10 ** 2)
# print(Samuel - Cindy)

# number1 = int(input("enter number:"))
# number2 = float(input("enter number:"))
# print(number1 + number2)


# register_name = ["kilani Fathia", "Nwachukwu Samuel", "Ngaikedi Freedom", "Olatunji Olanike", "Onyeka Ifeanyichukwu", "Samuel abiodun",
# "Ezennubia Chidera", "Shaibu Gana", "Salvador Mazeed"]
# student_name = input("Enter your name:")
# attendance_number = input("Enter number of classes attended:")
# if student_name not in register_name:
#     print("You're not in this class")
# elif student_name in register_name:
#     attendance = [student_name + ";" + attendance_number]
#     print(attendance)
#
# add = input("Would you like to add another name :")
# if add == "yes":
#     student_name2 = input("Enter your name:")
# register_name.append(student_name2)
# print(register_name)

# cab=5
# while cab>0:
#     print(cab)
#     cab=cab-1
#     print("tired of everything")
# counter=0
# while counter<5:
#     print("meow")
#     counter+=1
# from pathlib import Path
# filepath = "C:\\Users\\udanb\\Documents\\game.txt"
# filepath2 = "C:\\Users\\udanb\\Pictures\\Screenshots\\ame.png"
# f = open(filepath2, "rb")
# s = f.read()
# print(s)
# f.close()

# import cv2
# # img = cv2.imread("C:\\Users\\udanb\\Pictures\\Screenshots\\ame.png")
# # print("image Dimensions:", img.shape)
# src = cv2.imread("C:\\Users\\udanb\\Pictures\\Screenshots\\ame.png", cv2.IMREAD_UNCHANGED)
# scale_percent = 66
# width = int(src.shape[1] * scale_percent / 100)
# height = int(src.shape[0] * scale_percent / 100)
# dsize = (width, height)
# output = cv2.resize(src, dsize)
# cv2.imwrite("C:\\Users\\udanb\\Pictures\\Screenshots\\ame.png", output)
# new_height = int(input("Enter new height: "))
# new_width = int(input("Enter new width: "))
# dim = (src.shape[1], new_width, new_height)
# output = cv2.resize(src, dim, interpolation = cv2.INTER_AREA)
# cv2.imwrite("C:\\Users\\udanb\\Pictures\\Screenshots\\ame.png", output)


# Importing cv2
# import cv2
# # Path
# path = 'C:\\Users\\udanb\\Pictures\\Screenshots\\ame.png'
#
# # Reading an image in default mode
# image = cv2.imread(path)
#
# print('Original Dimensions : ', image.shape)
#
# scale_percent = 500  # percent of original size
# width = int(image.shape[1] * scale_percent / 100)
# height = int(image.shape[0] * scale_percent / 100)
# dim = (width, height)
# # resize image
# resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
#
# print('Resized Dimensions : ', resized.shape)
#
# cv2.imshow("Resized image", resized)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

import cv2
img = cv2.imread("C:\\Users\\udanb\\Pictures\\iphone\\101APPLE\\bart.jpg")
h, w = img.shape[:2]
new_h, new_w = int(1000 / 2), int(1000 / 2)
resizeImg = cv2.resize(img, (new_w, new_h))
cv2.imshow('Original', img)
cv2.imshow('Resizing', resizeImg)
cv2.waitKey(0)
cv2.destroyAllWindows()






