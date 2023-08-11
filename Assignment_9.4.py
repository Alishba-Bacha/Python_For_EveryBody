#Using a mbox-short.txt file to read through file and figureout who has sent most emails
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

address = dict()

for line in handle:
    line = line.rstrip()
    if not line.startswith("From"):
        continue
    words = line.split()
    sender = words[1]
    address[sender] = address.get(sender, 0) + 1
            

bigcount = None

for a,b in address.items():
    if bigcount is None or b > bigcount:
        bigcount = b
        sender = a
print(sender, bigcount)


