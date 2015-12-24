name = "SuperTigerPlusPlus"
age = 28
height = 189 # in [cm]
weight = 80 # in [kg], approx. 
eyes = "brown"
teeth = "white"
hair = "brown"

print "Let's talk about %s" % name
print "He's %d centimeters tall." % height
print "He's %d kilogramms heavy." % weight
print "Actually that's not too heavy (but it used to be less)"
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

print "If I add %d, %d, and %d I get %d " % (
age, height, weight, age + height + weight)