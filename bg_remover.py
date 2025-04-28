from rembg import remove
from PIL import Image

def remove_background(input_img, output_img):
    try:
        img = Image.open(input_img)
        output = remove(img)
        output.save(output_img)
        print("Background removed successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

input_img = 'C:\\Users\\hp\\Documents\\img_3.jpg'
output_img = 'C:\\Users\\hp\\Documents\\outputimg.png'

remove_background(input_img, output_img)
