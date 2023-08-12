# A python program which read file mbox-short.txt and print hour and its count
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
count = dict()
for line in handle:
    line = line.rstrip()
    if not line.startswith('From '): continue
    word = line.split()
    new_word = word[5]
    n_w = new_word[0:2]
    count[n_w] = count.get(n_w, 0) + 1
   
a_list = list()
for value, count in count.items():
    a_list.append((value,count))
 
a_list.sort()

for value, key in a_list:
    print(value, key)
