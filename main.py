from Project1 import *

def AddValues(list, fp):
    for num in fp:
        list.append( int(num))

if __name__ == '__main__':
    fp = open(input("Please Enter File Name: "), "r")
    list = LinkedList()

    AddValues(list, fp)




    list.head = MergeSort(list.head)
    print(list)
    fp.close()