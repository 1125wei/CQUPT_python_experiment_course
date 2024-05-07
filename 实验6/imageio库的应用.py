import imageio, os, numpy
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from PIL import Image

picture_jpg = imageio.imread(os.getcwd() + "\\图片.jpg")
print("图片数据类型：", picture_jpg.dtype)
img_shape = picture_jpg.shape
print("(图片大小，通道数)：", img_shape)
modified_color = (picture_jpg.astype(np.float32) * [1, 0.5, 0.5]).clip(0, 255).astype(np.uint8)
imageio.imwrite("图片修改颜色.jpg", modified_color)
imageio.imwrite("修改图片大小.jpg", numpy.array(Image.fromarray(picture_jpg).resize((120, 70))))
imageio.imwrite("图片裁剪.jpg", picture_jpg[50:130, 100:240])
"""——————————————————————————绘制图片——————————————————————————————"""
plt.figure()
plt.subplot(2, 2, 1)
picture_jpg1 = mpimg.imread(os.getcwd() + "\\图片.jpg")
plt.imshow(picture_jpg1)
plt.axis("off")
plt.subplot(2, 2, 2)
picture_jpg2 = mpimg.imread("图片修改颜色.jpg")
plt.imshow(picture_jpg2)
plt.axis('off')
plt.subplot(2, 2, 3)
picture_jpg3 = mpimg.imread("修改图片大小.jpg")
plt.imshow(picture_jpg3)
plt.axis('off')
plt.subplot(2, 2, 4)
picture_jpg4 = mpimg.imread("图片裁剪.jpg")
plt.imshow(picture_jpg4)
plt.axis('off')
plt.show()
