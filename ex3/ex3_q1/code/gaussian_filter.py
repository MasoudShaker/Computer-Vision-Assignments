import cv2 as cv
from matplotlib import pyplot as plt


img_path = './Original/Fig0333(a)(test_pattern_blurring_orig).tif'

original_img = cv.imread(img_path)

blurred_img = cv.GaussianBlur(original_img,(3,3),0)
blurred_img_again = cv.GaussianBlur(blurred_img,(3,3),0)
blurred_img_again = cv.GaussianBlur(blurred_img_again,(3,3),0)
blurred_img_again = cv.GaussianBlur(blurred_img_again,(3,3),0)
blurred_img_again = cv.GaussianBlur(blurred_img_again,(3,3),0)
blurred_img_again = cv.GaussianBlur(blurred_img_again,(3,3),0)
blurred_img_again = cv.GaussianBlur(blurred_img_again,(3,3),0)
blurred_img_again = cv.GaussianBlur(blurred_img_again,(3,3),0)
blurred_img_again = cv.GaussianBlur(blurred_img_again,(3,3),0)
blurred_img_again = cv.GaussianBlur(blurred_img_again,(3,3),0)
blurred_img_again = cv.GaussianBlur(blurred_img_again,(3,3),0)
blurred_img_again = cv.GaussianBlur(blurred_img_again,(3,3),0)
blurred_img_again = cv.GaussianBlur(blurred_img_again,(3,3),0)

plt.subplot(121),plt.imshow(original_img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blurred_img_again),plt.title('3*3 multiple times Blurred')
plt.xticks([]), plt.yticks([])

plt.show()