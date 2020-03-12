import math
import copy
import cv2
import numpy as np
hei = img.shape[0];
wid = img.shape[1];
img = cv2.imread('U:\.UNIVERSITY\Semester 5\DIP\Assignments\DIP_A2_Fall2019\White-Bars.png');
choice = int(input("Input 1 for application of 3*3 filter or Input 2 for application of 5*5 filter"))
result = copy.deepcopy(img)
if choice == 1:
        for i in np.arange(1 , hei-1):
                for j in np.arange(1, wid-1):
                        maximum = 0
                        minimum = 255
                        median = []
                        for x in np.arange(-1,2):
                                for y in np.arange(-1,2):
                                        grey_level = result.item(i + x,j + y)
                                        print(grey_level)
                                        if grey_level > maximum:
                                            maximum = grey_level
                                        if grey_level < minimum:
                                            minimum = grey_level
                                        median.append(grey_level)
                        median.sort()
                        median = median[4]
                        A1 = median - minimum
                        A2 = median - maximum
                        print(median , maximum , minimum)
                        if(A1 > 0 and  A2 < 0):
                            center = result.item(i,j)
                            B1 = center - minimum
                            B2 = center - maximum
                            if(B1 > 0 and B2 < 0):
                                result.itemset((i,j) , center)
                            else:
                                result.itemset((i,j) , median)
                        else:
                            result.itemset((i,j) , median)
elif choice == 2:

        for i in np.arange(2, hei - 2):
                for j in np.arange(2, wid - 2):
                        maximum = 0
                        minimum = 255
                        median = []
                        for x in np.arange(-2, 3):
                                for y in np.arange(-2, 3):
                                    grey_level = result.item(i + x, j + y)
                                    print(grey_level)
                                    if grey_level > maximum:
                                        maximum = grey_level
                                    if grey_level < minimum:
                                        minimum = grey_level
                                    median.append(grey_level)
                        median.sort()
                        median = median[12]
                        A1 = median - minimum
                        A2 = median - maximum
                        print(median , maximum , minimum)
                        if (A1 > 0 and A2 < 0):
                                center = img.item(i, j)
                                B1 = center - minimum
                                B2 = center - maximum
                                if (B1 > 0 and B2 < 0):
                                    result.itemset((i, j), center)
                                else:
                                    result.itemset((i, j), median)
                        else:
                            result.itemset((i,j) , median)
cv2.imwrite('Adaptive Median Filtered img', result)
cv2.imshow('Image',result)
cv2.waitKey(0)
cv2.destroyAllWindows()







