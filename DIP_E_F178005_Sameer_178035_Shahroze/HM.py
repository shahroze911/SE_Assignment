import math
import copy
import cv2
import numpy as np
hei = img.shape[0]
wid = img.shape[1]
img = cv2.imread('U:\.UNIVERSITY\Semester 5\DIP\Assignments\DIP_A2_Fall2019\White-Bars.png');
option = int(input("Press 1 to apply 3*3 or Press 2 to apply 5*5 filter"))

result = copy.deepcopy(img)
if option == 1:

        for i in np.arange(1 , hei-1):
                for j in np.arange(1, wid-1):
                        sum = 0
                        for x in np.arange(-1,2):
                                for y in np.arange(-1,2):
                                        grey_level = result.item(i + x,j + y)
                                        if grey_level != 0:
                                                sum += 1 / grey_level
                        if(sum != 0):
                                res = int(9 / sum)
                                result.itemset( (i , j ), res)
                        else:
                                result.itemset( (i , j ), 0)
elif option == 2:
        factor = 1
        for i in np.arange(2, hei - 2):
                for j in np.arange(2, wid - 2):
                        for x in np.arange(-2, 3):
                                for y in np.arange(-2, 3):
                                        grey_level = result.item(i + x, j + y)
                                        if grey_level == 0:
                                                sum += 1 / 0.1
                                        else:
                                                sum += 1 / grey_level
                        res = int(25 / sum)
                        result.itemset((i, j), res)
                        sum = 0
cv2.imwrite('Harmonic Filtered img', result)
cv2.imshow('img',result)
cv2.waitKey(0)
cv2.destroyAllWindows()






