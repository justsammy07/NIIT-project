import os.path
import cv2

def blur():
    while True:
        pic = input("""
    |-------------------------|
    |Enter the image directory|
    |---Type "exit" to stop---|
    |-------------------------|""")
        if pic.lower() == "exit":
            print("""
                   |-------------------|
                   | Action Forfeited  |
                   |-------------------|""")
            break
        dir_test = os.path.exists(pic)
        if dir_test is True:
            img = cv2.imread(pic)
            blur_img = cv2.GaussianBlur(img,(5,55),)
            status = cv2.imwrite(pic, resized_img)
            print(f"""
                    |-----------------------|
                    | Image saved: {status} |||
                    |-----------------------|""")
            cv2.imshow('Original Image', img)
            cv2.imshow('Blur Image', blur_img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        if dir_test is False:
            print("""
                   |-------------------|
                   | Invalid Directory |
                   |-------------------|""")
