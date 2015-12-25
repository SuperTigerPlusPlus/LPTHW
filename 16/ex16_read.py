from sys import argv

script, filename = argv

txt = open(filename)

print "Reading %s ..." % filename
print "Printing %s ..." % filename
print txt.read()

txt.close()