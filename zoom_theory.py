
import cv2 as cv
import numpy as np

im = cv.imread('Navi.jpg')

cv.namedWindow('original', cv.WINDOW_AUTOSIZE)
cv.imshow('original', im)
# cv.waitKey(0)



scale = 0.5
rows = int(scale*im.shape[0])
cols = int(scale*im.shape[1])
# print(rows, cols)

zoomed = np.zeros((rows, cols), dtype=im.dtype)

# for i in range(0, rows-1):
# 	for j in range(0, cols-1):
# 		# print(zoomed[i, j])
# 		zoomed[i,j] = im[int(i/scale), int(j/scale)]
		# print(im[int(i/scale), int(j/scale)])


cv.namedWindow('zoomed', cv.WINDOW_AUTOSIZE)
cv.imshow('zoomed', zoomed)
cv.waitKey(0)

cv.destroyAllWindows()