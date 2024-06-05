import base64



with open("base64/img.jpg", "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read())
    pre = 'data:image/jpeg;base64,'
    # print(pre+encoded_string.decode('utf-8'))
    res = pre+encoded_string.decode('utf-8')


