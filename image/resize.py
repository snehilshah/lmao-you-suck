import cv2

img = cv2.imread("image/img.jpg")

print('Image Width is', img.shape[1])
print('Image Height is', img.shape[0])

img_75 = cv2.resize(img, None, fx=0.75, fy=0.75,
                    interpolation=cv2.INTER_LANCZOS4)

# save the image_75
cv2.imwrite('image/image_75.jpg', img_75)
