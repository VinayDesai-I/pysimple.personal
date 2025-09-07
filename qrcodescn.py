import cv2 as cv
from pyzbar.pyzbar import decode

img = cv.imread("qrtry2.png")
img2 = cv.imread("idcard.jpg")

qr_detect = cv.QRCodeDetector()
op, _, _ = qr_detect.detectAndDecode(img)
op2 = qr_detect.detectAndDecode(img2)

pop = decode(img)
pop2 = decode(img2)

print(op)
print(op2)

print(pop[0])
print(pop2[0])