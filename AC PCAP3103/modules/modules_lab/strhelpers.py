# import random imports the random module, 
# which contains a variety of things to do with random number generation. 
# Among these is the random() function, 
# which generates random numbers between 0 and 


from random import shuffle l_shuffle # l is used as a list

def reverse(str_value):
    return str_value[::-1]

def str_shuffle(str_value):
    str_list = list(str_value)
    l_shuffle(str_list)
    return "".join(str_list)