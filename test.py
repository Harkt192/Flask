from PIL import Image

img = Image.open("static/images/man5.png")
new_img = img.resize((740, 740))
new_img.save("static/images/man5.png")