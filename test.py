from PIL import Image

img = Image.open("static/images/marsian.png")
new_img = img.resize((660, 680))
new_img.save("static/images/marsian.png")