import qrcode,os
os.chdir("C:\\Users\\asus\\Desktop\\")
image=qrcode.make("https://github.com/ataberkkoroglu")
image.save('Qrcode.png')

