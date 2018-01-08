fp_in = open("leetcode.txt")
fp_out = open("leetcode_out.txt", "w")


line = fp_in.readline()[1:-2]
line = [int(i) for i in line.split(',')]
print(line)
for i in line:
    print(i, file = fp_out)
