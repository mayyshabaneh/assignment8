class BubbleSort:
    def __init__(self) -> None:
        pass

    def sort(self, arr):
        for i in range(len(arr)):
             # Last i elements are already sorted
            for j in range(0, len(arr)-i-1):
                # Swap this element with next who greater than
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr

