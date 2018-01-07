import random

X = 1




def makeTest(start, end, _range):
    fp = open("testcase0{}.txt".format(X), 'w')
    for i in range(_range):
        print(str(random.randint(start, end)), file = fp)

    fp.close()


#makeTest(0, 10, 15) # all positive repeats
#X = 2
#makeTest(-25, -1, 10) # all negative
#X = 3
#makeTest(-10, 10, 10) # mixed values
#
#X = 4
#fp = open("testcase04.txt", "w") # positive floats
#for i in range(10):
#    print(str(random.random()), file = fp)
#
#fp.close()
#
#X = 5
#makeTest(0, 100, 500) # all positive repeats
#
#X = 6
#makeTest(-1000, -1, 200) # all negatives
#X = 7
#makeTest(-1000, 1000, 600) # mixed values

X = 8
fp = open("testcase08.txt", "w") # positive floats
for i in range(200):
    print(str(random.random()), file = fp)

fp.close()

X = 9
makeTest(-10000, -1, 800) # all negatives, ~800 values

X = 10
makeTest(-10000, 10000, 700) # mixed ints, ~700 values
