from Project1_Solution import *
import sys
def AddValues(list, fp):
    for num in fp:
        list.append( float(num))

sys.setrecursionlimit(90000)
if __name__ == '__main__':
    fp = open(input("Please Enter File Name: "), "r")
    list_ = LinkedList()

    AddValues(list_, fp)
    list_.head = MergeSort(list_.head)
    print(list_)
    fp.close()