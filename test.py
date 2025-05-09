from PIL import Image

img = Image.open("static/images/mars_carousel_2.png")
new_img = img.resize((1920, 1080))
new_img.save("static/images/mars_image_2.png")