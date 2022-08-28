import cv2
import os.path

def gray_scale():
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
            gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            status = cv2.imwrite(pic, gray_img)
            print(f"""
                    |-----------------------|
                    | Image saved: {status} |||
                    |-----------------------|""")
            cv2.imshow("Original", img)
            cv2.imshow("Resizing", gray_img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        if dir_test is False:
            print("""
                |-------------------|
                | Invalid Directory |
                |-------------------|""")