import pyqrcode
from PIL import Image

def generate_qr_code(link, filename, scale):
    qr_code = pyqrcode.create(link)
    qr_code.png(filename, scale=scale)
    return Image.open(filename)

link = input("Enter the link to generate QR code: ")
filename = "QRCode.png"
scale = 5

try:
    qr_code_image = generate_qr_code(link, filename, scale)
    print(f"QR code saved as {filename}")
except Exception as e:
    print(f"Error generating QR code: {e}")
