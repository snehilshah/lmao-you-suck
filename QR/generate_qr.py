import qrcode
img = qrcode.make('linkdin.com/in/your-profile')
type(img)  # qrcode.image.pil.PilImage
img.save("./QR/qr.png")
