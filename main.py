from Project2_Solution import *
import sys


def AddValues(list, fp):
    '''
    :param list: linked list to add values to
    :param fp: file pointer to read from
    :return:  None
    '''
    for num in fp:
        list.push_back( float(num))

sys.setrecursionlimit(90000)



if __name__ == '__main__':
    fp = open(input("Please Enter File Name: "), "r")
    list_ = LinkedList()

    AddValues(list_, fp)
    list_.head = MergeSort(list_.head)
    print(list_)
    fp.close()