'''
pal_checker.py
checks if words are palindromes

Tested on python 2.7.5+
'''

def open_to_list(my_file):
    ''' Takes the name of the file as a string
        Returns a list of lowercase words with some punctuation removed
    '''
    return open(my_file).read().lower().translate(None, ';:,.?\"\'\(\)').split()
    
def check_pal(wrd):
    ''' Takes a string
        Checks whether the word is a palindrome 
        by recursively comparing the (i)th and (len-i)th letters
        Returns True or False
    '''
    if len(wrd) <= 1:
        return True
    else:
        for i in xrange(len(wrd)):
            if wrd[i] == wrd[-(i+1)]:
                return check_pal(wrd[1:-1])
            else:
                return False
  

def main():
    words = open_to_list('sys_dict.txt')
    #words = words[0:1000]
    
    pal_list = []
    for word in words:
        if check_pal(word):
            pal_list.append(word)

    print pal_list

main()
