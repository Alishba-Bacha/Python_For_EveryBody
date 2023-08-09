#Read from any file here is "romeo.txt" sort all element after appending it to list

fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    words = line.rstrip().split()
    for element in words:
        if element in lst:
            continue
        else:
            lst.append(element)
lst.sort()
print(lst)