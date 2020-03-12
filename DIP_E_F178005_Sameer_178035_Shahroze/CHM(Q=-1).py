import math
import copy
import cv2
import numpy as np
img = cv2.imread('U:\.UNIVERSITY\Semester 5\DIP\Assignments\DIP_A2_Fall2019\White-Bars.png');
option = int(input("Input 1 for application of 3*3 filter or Input 2 for application of 5*5 filter"))
add_1 = 0
add_2 = 0
Q = -1
hei = img.shape[0]
wid = img.shape[1]
resultant = copy.deepcopy(img)
if option == 1:
        for i in np.arange(1 , hei-1):
                for j in np.arange(1, wid-1):
                        add_1 = 0
                        add_2 = 0
                        for x in np.arange(-1,2):
                                for y in np.arange(-1,2):
                                    grey_levle = resultant.item(i + x, j + y)
                                    add_1 += int(np.float_power(grey_level, Q + 1))
                                    add_2 += round((np.float_power(grey_level, Q)), 2)
                        if add_2 == 0:
                            output = int(add_1 / 0.1)
                            resultant.itemset((i, j), output)
                        else:
                            output = int(add_1 / add_2)
                            resultant.itemset((i, j), output)
elif option == 2:
        for i in np.arange(2, hei - 2):
                for j in np.arange(2, wid - 2):
                        add_1 = 0
                        add_2 = 0
                        for x in np.arange(-2, 3):
                                for y in np.arange(-2, 3):
                                    grey_level = resultant.item(i + x, j + y)
                                    add_1 += int(np.float_power(grey_level,Q+1))
                                    add_2 += round((np.float_power(grey_level,Q)),2)
                        if add_2 == 0:
                            output = int(add_1 / 0.1)
                            resultant.itemset((i, j), output)
                        else:
                            output = int(add_1 / add_2)
                            resultant.itemset((i, j), output)
cv2.imwrite('Contra Harmonic Filtered Image', resultant)
cv2.imshow('Image',resultant)
cv2.waitKey(0)
cv2.destroyAllWindows()







