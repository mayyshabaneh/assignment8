import random
from mergesort import MergeSort
from bubblesort import BubbleSort
mergsort = MergeSort()
bubbleSort = BubbleSort()
#test with random size and random int elements
list1 = random.sample(range(1,100),20)
print("unsorted array : ",list1)
print("Merge Sorted array : ",mergsort.divide(list1))
print("Bubble Sorted array : ",bubbleSort.sort(list1))

#test with random size and random float elements
print('\n')
list2 = [random.uniform(1.0,100.0) for _ in range(5)]
print("unsorted array : ",list2)
print("Merge Sorted array : ",mergsort.divide(list2))
print("Bubble Sorted array : ",bubbleSort.sort(list2))


#test with random size and random int elements
print('\n')
list3 = random.sample(range(1,100),10)
print("unsorted array : ",list3)
print("Merge Sorted array : ",mergsort.divide(list3))
print("Bubble Sorted array : ",bubbleSort.sort(list3))

#test with one element
print("\n")
list4 = [1]
print("unsorted array : ",list4)
print("Merge Sorted array : ",mergsort.divide(list4))
print("Bubble Sorted array : ",bubbleSort.sort(list4))

#test with empty list
print("\n")
Empty_list = []
print("unsorted array : ",Empty_list)
print("Merge Sorted array : ",mergsort.divide(Empty_list))
print("Bubble Sorted array : ",bubbleSort.sort(Empty_list))

#test with single element
print("\n")
Single_element=[1]
print("unsorted array : ",Single_element)
print("Merge Sorted array : ",mergsort.divide(Single_element))
print("Bubble Sorted array : ",bubbleSort.sort(Single_element))

#test with random size and random int elements
print("\n")
Unsorted_list=[3, 1, 2]
print("unsorted array : ",Unsorted_list)
print("Merge Sorted array : ",mergsort.divide(Unsorted_list))
print("Bubble Sorted array : ",bubbleSort.sort(Unsorted_list))

#test with sorted array
print("\n")
Already_sorted_list=[1, 2, 3]
print("unsorted array : ",Already_sorted_list)
print("Merge Sorted array : ",mergsort.divide(Already_sorted_list))
print("Bubble Sorted array : ",bubbleSort.sort(Already_sorted_list))

#test with same elements
print("\n")
All_elements_the_same=[4, 4, 4, 4]
print("unsorted array : ",All_elements_the_same)
print("Merge Sorted array : ",mergsort.divide(All_elements_the_same))
print("Bubble Sorted array : ",bubbleSort.sort(All_elements_the_same))

#test with duplicates
print("\n")
List_with_duplicates=[5, 1, 3, 3, 2, 2, 4, 4]
print("unsorted array : ",List_with_duplicates)
print("Merge Sorted array : ",mergsort.divide(List_with_duplicates))
print("Bubble Sorted array : ",bubbleSort.sort(List_with_duplicates))
