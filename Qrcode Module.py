import qrcode,os
os.chdir("C:\\Users\\asus\\Desktop\\")
qr = qrcode.QRCode(version = 1,
                   box_size = 50,
                   border = 3)
data="https://github.com/ataberkkoroglu"
qr.add_data(data)
qr.make(fit=True)
image=qr.make_image(fill_color="black",back_color="blue")
image.save('Qrcode.png')

