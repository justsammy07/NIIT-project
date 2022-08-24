
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






