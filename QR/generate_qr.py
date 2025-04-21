import qrcode
img = qrcode.make('lmao')
type(img)  # qrcode.image.pil.PilImage
img.save("./QR/qr.png")
