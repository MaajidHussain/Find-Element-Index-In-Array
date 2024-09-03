import numpy as np
myArray=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])

def findElement(Array,targetElement):
    for index in range(len(myArray)):
        if Array[index]==targetElement:
            print(f"Index of given Element is {index}.")
            return
    if targetElement not in myArray:
            print(f"Element {targetElement},not found in given array.")
findElement(myArray,7)
findElement(myArray,31)