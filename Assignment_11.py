import re
sum = 0
try:
    handle = open("regex_sum.txt")
except:
    print("File can not be opened")
for line in handle:
    line = line.rstrip()
    try:
        s = re.findall('[0-9]+', line)
        for any in s:
            x = int(any)
            sum = sum + x
    except:
        print("No")

print(sum)