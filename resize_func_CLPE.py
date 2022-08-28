import os.path
import cv2

def resize_small():
    scale_percent = 40
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
            h, w = img.shape[:2]
            new_w, new_h = int(img.shape[1] * scale_percent / 100), int(img.shape[0] * scale_percent / 100)
            resized_img = cv2.resize(img, (new_w, new_h))
            status = cv2.imwrite(pic, resized_img)
            print(f"""
                    |-----------------------|
                    | Image saved: {status} |||
                    |-----------------------|""")
            cv2.imshow("Original", img)
            cv2.imshow("Resizing", resized_img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        if dir_test is False:
                print("""
                |-------------------|
                | Invalid Directory |
                |-------------------|""")


def resize_medium():
    scale_percent = 65
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
            h, w = img.shape[:2]
            new_w, new_h = int(img.shape[1] * scale_percent / 100), int(img.shape[0] * scale_percent / 100)
            resized_img = cv2.resize(img, (new_w, new_h))
            status = cv2.imwrite(pic, resized_img)
            print(f"""
                    |-----------------------|
                    | Image saved: {status} |||
                    |-----------------------|""")
            cv2.imshow("Original", img)
            cv2.imshow("Resizing", resized_img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        if dir_test is False:
                print("""
                |-------------------|
                | Invalid Directory |
                |-------------------|""")


def resize_large():
    scale_percent = 80
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
            h, w = img.shape[:2]
            new_w, new_h = int(img.shape[1] * scale_percent / 100), int(img.shape[0] * scale_percent / 100)
            resized_img = cv2.resize(img, (new_w, new_h))
            status = cv2.imwrite(pic, resized_img)
            print(f"""
                    |-----------------------|
                    | Image saved: {status} |||
                    |-----------------------|""")
            cv2.imshow("Original", img)
            cv2.imshow("Resizing", resized_img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        if dir_test is False:
                print("""
                |-------------------|
                | Invalid Directory |
                |-------------------|""")
