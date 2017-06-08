
# word count
#
#

import sys

def word_count(file_name):
    f1 = open(file_name, 'r')

    l1 = []
    x = 0

    for line in f1:
        l1 = line.split()

        x = len(l1) + x

    return x

    f1.close


def main():
    print 'command line args: ', sys.argv[1]

    result = word_count(sys.argv[1])
    print 'word count: ', result


if __name__ == '__main__':
    main()

