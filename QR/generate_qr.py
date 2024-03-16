import qrcode
img = qrcode.make('https://www.youtube.com/watch?v=PKuJoiP5wf0')
type(img)  # qrcode.image.pil.PilImage
img.save("qr.png")
