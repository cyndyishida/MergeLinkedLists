import Project2_Solution as answer
import MergeSort as student
import LinkedList as llist
## global variable for grade
TOTAL = 0


def AddValues(list, fp):
    '''
    :param list: linked list type
    :param fp: file pointer of values
    :return: length of linked list

    add the values from file to list
    '''

    for count, num in enumerate(fp):
        list.push_back( float(num))
    return count + 1


def check(s_list, a_list):
    '''
    :param s_list: student linked list result
    :param a_list: answer key linked list result
    :return: count of number right for student linked list
    '''
    right = 0
    # assumes students linked list is the same length as answers
    while s_list.head and a_list.head:
        if s_list.head.val == a_list.head.val:
            right +=1
        s_list.head = s_list.head.next
        a_list.head = a_list.head.next
    return right




def runTest(fp):
    '''
    :param fp: file pointer to read in values
    :return: number of right and the length of the linked list

    creates linked lists and runs merge sort, then checks for correct result
    '''
    s_list = llist.LinkedList()
    count = AddValues(s_list,fp)
    s_list.head = student.MergeSort(s_list.head)


    a_list = llist.LinkedList()
    fp.seek(0,0)
    AddValues(a_list,fp)
    a_list.head = answer.MergeSort(a_list.head)

    right = check(s_list, a_list)


   # right = 0

   # while s_list.head.next:
   #     if s_list.head <= s_list.head.next:
   #         right +=1
   #     s_list.head = s_list.head.next




    return right, count


'''
UNIT TESTS 
'''
def test1():
    fp = open("testcase01.txt", 'r')
    right, count = runTest(fp)
    fp.close()

    cur_total = round(right/count * 5, 2)
    global TOTAL
    TOTAL += cur_total
    return f"Testcase 01: {cur_total} / 5"

def test2():
    fp = open("testcase02.txt", 'r')
    right, count = runTest(fp)
    fp.close()

    cur_total = round(right/count * 5, 2)
    global TOTAL
    TOTAL += cur_total
    return f"Testcase 02: {cur_total} / 5"

def test3():
    fp = open("testcase03.txt", 'r')
    right, count = runTest(fp)
    fp.close()

    cur_total = round(right/count * 5, 2)
    global TOTAL
    TOTAL += cur_total
    return f"Testcase 03: {cur_total } / 5"

def test4():
    fp = open("testcase04.txt", 'r')
    right, count = runTest(fp)
    fp.close()

    cur_total = round(right/count * 5, 2)
    global TOTAL
    TOTAL += cur_total
    return f"Testcase 04: {cur_total} / 5"


def test5():
    fp = open("testcase05.txt", 'r')
    right, count = runTest(fp)
    fp.close()

    cur_total = round(right/count * 5, 2)
    global TOTAL
    TOTAL += cur_total
    return f"Testcase 05: {cur_total} / 5"


def test6():
    fp = open("testcase06.txt", 'r')
    right, count = runTest(fp)
    fp.close()

    cur_total = round(right/count * 9, 2)
    global TOTAL
    TOTAL += cur_total
    return f"Testcase 06: {cur_total} / 9"

def test7():
    fp = open("testcase07.txt", 'r')
    right, count = runTest(fp)
    fp.close()

    cur_total = round(right/count * 9, 2)
    global TOTAL
    TOTAL += cur_total
    return f"Testcase 07: {cur_total} / 9"

def test8():
    fp = open("testcase08.txt", 'r')
    right, count = runTest(fp)
    fp.close()

    cur_total = round(right/count * 9, 2)
    global TOTAL
    TOTAL += cur_total
    return f"Testcase 08: {cur_total} / 9"


def test9():
    fp = open("testcase09.txt", 'r')
    right, count = runTest(fp)
    fp.close()

    cur_total = round(right/count * 9, 2)
    global TOTAL
    TOTAL += cur_total
    return f"Testcase 09: {cur_total} / 9"

def test10():
    fp = open("testcase10.txt", 'r')
    right, count = runTest(fp)
    fp.close()

    cur_total = round(right/count * 9, 2)
    global TOTAL
    TOTAL += cur_total
    return f"Testcase 10: {cur_total} / 9"



def main():
    print(test1())
    print(test2())
    print(test3())
    print(test4())
    print(test5())
    print(test6())
    print(test7())
    print(test8())
    print(test9())
    print(test10())
    print ("\n\nTotal Score: ", TOTAL )


# i truly believe this testcase scheme would be much easier to make in C++ w/ template specialization
# look into this next semester
if __name__ == '__main__':
    main()