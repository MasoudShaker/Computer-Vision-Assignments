import cv2
import matplotlib.pyplot as plt


img_address = '../original image/AmirMasoud3.jpg'
img = cv2.imread(img_address)

# convert BGR to RGB
RGB_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# convert to grey image
grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# invert image
invert_img = cv2.bitwise_not(grey_img)

# blur image
blur_img=cv2.GaussianBlur(invert_img, (111,111),0)

# invert blurred image
invblur_img=cv2.bitwise_not(blur_img)

# sketch
sketch_img=cv2.divide(grey_img,invblur_img, scale=256.0)

cv2.imwrite('sketch.png', sketch_img)

plt.figure(figsize=(14,8))
plt.subplot(1,2,1)
plt.title('Original image', size=18)
plt.imshow(RGB_img)
plt.axis('off')
plt.subplot(1,2,2)
plt.title('Sketch', size=18)
rgb_sketch=cv2.cvtColor(sketch_img, cv2.COLOR_BGR2RGB)
plt.imshow(rgb_sketch)
plt.axis('off')
plt.show()