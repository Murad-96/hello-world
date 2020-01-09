'''
Author: Murad Magdiyev
Date: 11/26/2019
exercise 5.2.1
'''

from Utils.timer import Timer
from time import sleep

@Timer
def myFunc(arg1, arg2):
    sleep(5)
    return arg1 * arg2

def main():

    # test Timer decorator
    myFunc(1, 3)

    # IMO decorators are more useful when applied to class internal functions
    # because we wouldn't have to type 'with ___ as __:' each time we want to measure time for example




if __name__ == '__main__':
    main()
