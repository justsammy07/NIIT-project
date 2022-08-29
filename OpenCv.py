import cv2

img = cv2.imread('lena.jpg', 1)

print(img)
cv2.imshow('photos', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#imwrite used to write an image in the form of a file
cv2.write('leso_copy.pg',img)



