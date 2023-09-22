from  cryptography.fernet import Fernet
import cv2
from PIL import Image
img=cv2.imread("C:/Users/Asus/Desktop/Ataberk.jpg")
img2=Image.open("C:/Users/Asus/Desktop/Ataberk.jpg")

key=Fernet.generate_key()

with open('C:/Users/Asus/Desktop/key.zikstht','wb') as file:
    file.write(key)

with open('C:/Users/Asus/Desktop/key.zikstht','rb') as file:
    key=file.read()

with open("C:/Users/Asus/Desktop/Ataberk.txt","wb") as file:
    file.write(img)

with open("C:/Users/Asus/Desktop/Ataberk.txt","rb") as file:
    data=file.read()

fernet=Fernet(key)
encrypted=fernet.encrypt(data)
with open("C:/Users/Asus/Desktop/zikskey.zzikstht","wb") as f:
    f.write(encrypted)