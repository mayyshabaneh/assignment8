import random
class MergeSort:
    def __init__(self) -> None:
        pass

    def divide(self, arr):
        if len(arr) <= 1:
            return arr
        #chick the mid point of array
        mid = len(arr) // 2

        #define the halfs of array right half as arr1 and left half as a arr2 the recursively the divide function
        arr1 = self.divide(arr[:mid])
        arr2 = self.divide(arr[mid:])
        
        return self.merge(arr1, arr2)

    def merge(self, arr1, arr2):
        arr = []
        i = 0
        j = 0
        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                arr.append(arr1[i])
                i += 1
            else:
                arr.append(arr2[j])
                j += 1
        
        # Append remaining elements of arr1 and arr2 (if any)
        arr.extend(arr1[i:])
        arr.extend(arr2[j:])
        return arr