# Use the file name mbox-short.txt as the file name to print average of "0.8475" found in each line
fname = input("Enter file name: ")
fh = open(fname)
count = 0
add = 0
for line in fh:
    line = line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count = count + 1
    Num = line.find('0')
    num = Num + 6
    num = float(line[Num : num])
    add = num + add
print("Average spam confidence:", add/count)