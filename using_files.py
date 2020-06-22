my_file = open('xmen.txt', 'w+') # All files open, needs to start with open.
# The file doesn't need to exist, and can be created in VIM.
my_file.write('Beast\n') # The \n is for new line
my_file.write('Phoenix\n')
my_file.writelines([ # Can create multiple lines.
    'Cyclops\n',
    'Bishop\n',
    'Nightcrawler\n'
])

my_file.close() # Need close so the file doesn't continue going.

my_file = open('xmen.txt', 'r') # r allows it to be read in all content in a signal variable
with my_file:  #A with statement takes an object that has a close method and will call that method after the block has run.
    print(my_file.read())