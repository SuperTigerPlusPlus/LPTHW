tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

# Mhhh, I there is no difference between double quotes and single quotes
# Source: http://stackoverflow.com/questions/5087425/python-difference-between-using-and
fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

while True:
	for i in ["/","-","|","\\","|"]:
		#The comma is special syntax for the print function.
		#It disables the "invisible" \n at the end of every print 
		print "%s\r" %i,
