"""
this program reads a file with both single words and two-word combinations and their respective payloads into a dictionary
it then checks of each of these two words is present in an incoming sentence
if they are both present, the payload message is activated
TTD: we can/may extend quarks.txt file to handling three words
"""

#input = "i am looking for judy"#
#input = "bye for now"
#input = "i am looking for her, bye for now"
#input = "i am interested in product"
input = input()
a = {}
with open("quarks.txt") as f:
    for line in f:
       (k, v) = line.split("|")
       strippedv = v.replace("\n", "") #remove the newline character
       a[str(k)] = strippedv
print(a)

quarkset = []
for key in a.keys(): #cycle through all entries of the quarks.txt file
    word = key.split()
    lenw = len(word)
    count = 0
    if (word[0] in input):
        count += 1
        #print (" found a part of: " + key)
        if (lenw > 1):
            if (word[1] in input):
                count += 1
                #print (" found a part of: " + key)
                #print("count = " + str(count))
    if (count == lenw):
        print ("all words found for: " + key)
        print ("payload = " + a[key])
        quarkset.append(a[key])

print(quarkset)

print("------------output----------------")
"""
this part of the program
does more or less same as the first part
only now the input is the 'quarkset'
and the lookup list is replaced with 'summary.txt'
"""
b = {}
with open("summary.txt") as f:
    for line in f:
       (k, v) = line.split("|")
       strippedv = v.replace("\n", "") #remove the newline character
       b[str(k)] = strippedv
print(b)

output = []
for key in b.keys(): #cycle through all entries of summary.txt file
    if (key in quarkset):
        print ("match found for: " + key)
        print ("payload = " + b[key])
        output.append(b[key])

print(output)