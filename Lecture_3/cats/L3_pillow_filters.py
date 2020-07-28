from PIL import Image, ImageFilter

im = Image.open("cat.jpg")
im2 = im.filter(ImageFilter.GaussianBlur)  # 高斯模糊
im3 = im.filter(ImageFilter.BLUR)  # 普通模糊
im4 = im.filter(ImageFilter.EDGE_ENHANCE)  # 边缘增强
im5 = im.filter(ImageFilter.FIND_EDGES)  # 找到边缘
im6 = im.filter(ImageFilter.EMBOSS)  # 浮雕
im7 = im.filter(ImageFilter.CONTOUR)  # 轮廓
im8 = im.filter(ImageFilter.SHARPEN)  # 锐化
im9 = im.filter(ImageFilter.SMOOTH)  # 平滑
im10 = im.filter(ImageFilter.DETAIL)  # 细节

im2.save("./cats/cat_高斯模糊.jpg")
im3.save("./cats/cat_普通模糊.jpg")
im4.save("./cats/cat_边缘增强.jpg")
im5.save("./cats/cat_找到边缘.jpg")
im6.save("./cats/cat_浮雕.jpg")
im7.save("./cats/cat_轮廓.jpg")
im8.save("./cats/cat_锐化.jpg")
im9.save("./cats/cat_平滑.jpg")
im10.save("./cats/cat_细节.jpg")

