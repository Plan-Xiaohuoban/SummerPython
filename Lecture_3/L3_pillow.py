from PIL import Image

im = Image.open("cat.jpg")

box = (0, 0, 300, 375)


region = im.crop(box)  # 裁剪

region.save("cat_croped.jpg")

print(im.size)
# 改变尺寸
im = im.resize((800, 375))
im.save("cat_resized.jpg")

print(im.size)
print(region)
