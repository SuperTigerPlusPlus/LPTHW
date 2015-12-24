# A string is put inside another string
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
#Two strings are put into another string
y = "Those who know %s and those who %s." % (binary,do_not)

print x
print y

# A string is put into another string
print "I said : %r." % x
# A Sstring is put into another string
print "I also said '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

#A string is put into another string
print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

# Ummmh, I'm actually not sure, if e is put into w. I believe not. 
print w+e

#Total number of string that were put into other strings: 6 (excluding the w+e stuff)