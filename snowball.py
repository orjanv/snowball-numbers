#!/usr/bin/env python
from num2words import num2words
from subprocess import call
import sys, itertools, os

EMAIL_ADDRESS = 'user@host.com'

def letters(input):
    '''Validate and remoce non-alphabetical letters
    '''
    valids = []
    for character in input:
        if character.isalpha():
            valids.append(character)
    return ''.join(valids)

def get_num_list(number):
    '''Return sorted list of letter occurences
    '''
    num = num2words(number)
    # Take away non-letter characters
    num = letters(num)
    # Find unique alphabetic chars
    num_chars = ''.join(set(num))
    # Add unique letters as keys and occurences as values in a dict
    num_dict = {}
    for c in num_chars:
        #print c, ': ', num.count(c)
        num_dict[c] = num.count(c)

    # Sort the dict values
    oc_list = []
    for w in sorted(num_dict, key=num_dict.get):
        #print w, num_dict[w]
        # create a list based on the values for increment check
        oc_list.append(num_dict[w])
	
    return oc_list

def main():
    num = int(sys.argv[1])
    while (1):
        num_list = get_num_list(num)

        # Notify every 100 run
        if (num % 1000000 == 0):
            print num, num_list

        # TEST 1 - Test if the last value of the list is the same as the length 
        # of the list. If not, try next number
        if (num_list[-1] != len(num_list)):
            num = num + 1
        else:
            # If the last value in the list equal the length of the list, 
            # proceed to test two:
            # TEST 2 - Compare the partial sum - n*(n+1))/2 - based on list 
            # length with the sum of all items in the list
            n = (len(num_list) * len(num_list) + 1) / 2
            x = sum(num_list)

            if (n != x):
                # If the sums didn't match, try next number
                num = num + 1
            else:
                # If the sums matched, proceed to check three.
                # TEST 3 - check list items are incremented by exactly 1
                for i in range(len(num_list)-1):
                    if ([num_list[i+1] - num_list[i]] != 1):
                        break
                    else:
                        x = i
                if (x == len(num_list)-1):
                    result = "You have found a snowball number: ", num, num_list, '\n'
                    file = open('snowball_numbers.txt','aU+')
                    file.write(str(result))
                    file.close()
                    print result
                    FNULL = open(os.devnull, 'w')
                    subprocess.call(['mailx', '-t', result, EMAIL_ADDRESS], stdout=FNULL, stderr=subprocess.STDOUT)
                    exit(0)
                else:
                    num = num + 1

if __name__ == '__main__':
    main()
