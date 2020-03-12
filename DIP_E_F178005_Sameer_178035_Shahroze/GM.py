import math
import copy
import cv2
import numpy as np
img= cv2.imread('U:\.UNIVERSITY\Semester 5\DIP\Assignments\DIP_A2_Fall2019\White-Bars.png');
wid = img.shape[1]
hei = img.shape[0]
options = int(input("Input 1 for application of 3*3 filter or Input 2 for application of 5*5 filter"))
output = copy.deepcopy(img)
if options == 1:
        factor = 1
        for i in np.arange(1 , hei-1):
                for j in np.arange(1, wid-1):
                        for x in np.arange(-1,2):
                                for y in np.arange(-1,2):
                                        grey_level = output.item(i + x,j + y)
                                        print(grey_level)
                                        if grey_level != 0:
                                                factor *= grey_level
                        res = int(pow(factor,(1 / 9)))
                        output.itemset((i , j ), res)
                        factor = 1
elif options == 2:
        factor = 1
        for i in np.arange(2, hei - 2):
                for j in np.arange(2, wid - 2):
                        for x in np.arange(-2, 3):
                                for y in np.arange(-2, 3):
                                        grey_level = output.item(i + x, j + y)
                                        if grey_level != 0:
                                                factor *= grey_level
                        res = int(pow(factor, (1 / 25)))
                        output.itemset((i, j), res)
                        factor = 1
cv2.imwrite('Geometric Filtered Image', output)
cv2.imshow('Image',output)
cv2.waitKey(0);
cv2.destroyAllWindows()







