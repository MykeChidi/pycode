import cv2
import os

def pencil_sketch(image_path, output_path):
    if not os.path.exists(image_path):
        print("Image not found. Please check the path.")
        return

    image = cv2.imread(image_path)

    if image is None:
        print("Failed to read the image.")
        return

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    inverted_gray_image = cv2.bitwise_not(gray_image)
    blurred_image = cv2.GaussianBlur(inverted_gray_image, (21, 21), 0)

    inverted_blurred_image = cv2.bitwise_not(blurred_image)
    pencil_sketch_image = cv2.divide(gray_image, inverted_blurred_image, scale= 250.0)

    if not cv2.imwrite(output_path, pencil_sketch_image):
        print("Failed to write the output image.")
        return
    try:
        cv2.imshow('Pencil Sketch', pencil_sketch_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    except Exception as e:
        print(e)
       
input_image_path = 'C:\\Users\\hp\\Documents\\IMG_4.jpg'
output_image_path = 'C:\\Users\\hp\\Documents\\sketch_8.jpg'
pencil_sketch(input_image_path, output_image_path)