
# word count
#
#

import sys

def word_count(file_name):

    f1 = open(file_name, 'r')

    l1 = []
    word_num = 0
    line_num = 0

    for line in f1:

        if len(line.strip()) != 0:
            line_num = line_num + 1

        l1 = line.split()
        word_num = len(l1) + word_num

    f1.close()

    return word_num, line_num


def main():
    if len(sys.argv) < 2:
        print 'Usage: python word_count.py <file_name>'
        exit(1)
    else:
        file_name = sys.argv[1]

    word_num, line_num = word_count(file_name)

    print 'The words count: ', word_num
    print 'the lines count: ', line_num


if __name__ == '__main__':
    main()

