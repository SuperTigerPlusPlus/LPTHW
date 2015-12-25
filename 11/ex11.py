print "How old are your?",
# According to http://learnpythonthehardway.org/book/ex11.html
# raw_input() is preffered to input(), since its more secure
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weight?",
weight = raw_input()

print "So, you are %r old, %r tall and %r heavy." % (
age, height, weight)