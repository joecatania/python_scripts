
# word count
#
#

import sys

def word_count(file_name):

    f1 = open(file_name, 'r')

    l1 = []
    word_count = 0
    line_count = 0

    for line in f1:
        line_count = line_count + 1
        l1 = line.split()
        word_count = len(l1) + word_count

    print 'The words count: ', word_count
    print 'the lines count: ', line_count

    return 0

    f1.close


def main():
    print 'command line args: ', sys.argv[1]

    result = word_count(sys.argv[1])


if __name__ == '__main__':
    main()

