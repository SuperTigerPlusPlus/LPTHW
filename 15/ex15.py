from sys import argv

script, filename = argv

# Calls the function open a creates a file object
txt = open(filename)

print "Here's your file %r" % filename
# Calls the read() function of this file object
print txt.read()

txt.close()

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()

txt.close()