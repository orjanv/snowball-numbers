#!/usr/bin/env python
import sys, os, re, subprocess
from num2words import num2words
import time

def EmailNotify(SUBJECT, TEXT, TO):
    """Sends the email
    """
    cmd = ('echo "%s" | mailx -s "%s" "%s"' % (TEXT, SUBJECT, TO))
    subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True).communicate()[0]

def letters(letter):
    """Validate and remove non-alphabetical letters
    """
    valid = []
    for character in letter:
        if character.isalpha():
            valid.append(character)
    return ''.join(valid)

def get_num_list(number):
    """Converts the integer to text, removes whitespace and unwanted
    characters and symbols and return sorted list of letter occurrences
    """
    num = num2words(number)
    # remove "and" occurences
    line = re.sub(' and', '', num)
    # Take away non-letter characters
    num = letters(line)
    # Find unique alphabetic chars
    num_chars = ''.join(set(num))
    # Add unique letters as keys and occurrences as values in a dict
    num_dict = {}
    for c in num_chars:
        num_dict[c] = num.count(c)
    # Create a list based on the values for increment check
    oc_list = []
    for w in num_dict:
        oc_list.append(num_dict[w])
    oc_list.sort()
    return oc_list

def main():
    num = int(sys.argv[1])
    to = sys.argv[2]
    start_time = time.time()
    while 1:
        num_list = get_num_list(num)
        # Notify every 100 run
        if num % 10000 == 0:
            print num, num_list, ("--- %s seconds ---" % (time.time() - start_time))
            start_time = time.time()
        if num % 100000000 == 0:
            subject = 'Snowball alert: reached number:' + str(num)
            EmailNotify(subject, str(num), to)

        # TEST 1 - Test if the last value of the list is the same as the length 
        # of the list. If not, try next number
        if num_list[-1] != len(num_list):
            num += 1
        else:
            # TEST 2 - Compare the partial sum: n*(n+1))/2 based on list 
            # length with the sum of all items in the list
            n = (len(num_list) * (len(num_list) + 1)) / 2
            x = sum(num_list)
            if n != x:
                num += 1
            else:
                # TEST 3 - check list items are incremented by exactly 1
                list_match = False
                for i in range(len(num_list)):
                    if [(num_list[i] + 1, num_list[i]) == 1]:
                        list_match = True
                    else:
                        list_match = False
                if list_match == True:
                    result = "I have found a snowball number: " + str(num)
                    f = open('snowball_numbers.txt', 'a')
                    f.write(str(result) + '\n')
                    f.close()
                    print result
                    subject = 'Snowballnumber found!'
                    EmailNotify(subject, result, to)
                    exit(0)
                else:
                    num += 1

if __name__ == '__main__':
    main()
