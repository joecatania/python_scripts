
# word count
#
#


f1 = open('data/group.txt', 'r')

l1 = []
x = 0

for line in f1:
    l1 = line.split()

    x = len(l1) + x


print 'word count', x

f1.close

