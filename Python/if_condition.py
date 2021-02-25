# the if keyword;
# one or more white spaces;
# an expression (a question or an answer) whose value will be interpreted solely in terms of True (when its value is non-zero) 
#   and False (when it is equal to zero);
#a colon followed by a newline;
# an indented instruction or set of instructions (at least one instruction is absolutely required); 
# the indentation may be achieved in two ways - by inserting a particular number of spaces 
# (the recommendation is to use four spaces of indentation), or by using the tab character; note: if ther
# e is more than one instruction in the indented part, the indentation should be the same in all lines; 
# even though it may look the same if you use tabs mixed with spaces, it's 
# important to make all indentations exactly the same - Python 3 does not allow mixing spaces and tabs for indentation.

if sheep_counter >= 120:
    make_a_bed()
    take_a_shower()
    sleep_and_dream()
feed_the_sheepdogs()

# Feeding the sheepdogs, however, is always done (i.e., the feed_the_sheepdogs() 
# function is not indented and does not belong to the if block, which means it is always executed.)
