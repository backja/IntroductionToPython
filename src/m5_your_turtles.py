"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Jacob Back.
"""
########################################################################
# Done: 1.
# On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# TODO: 2.
#
#  You should have RUN the PREVIOUS module and READ its code.
#  (Do so now if you have not already done so.)
#
#  Below this comment, add ANY CODE THAT YOUR WANT, as long as:
#    1. You construct at least 2 rg.SimpleTurtle objects.
#    2. Each rg.SimpleTurtle object draws something
#         (by moving, using its rg.Pen).  ANYTHING is fine!
#    3. Each rg.SimpleTurtle moves inside a LOOP.
#
#  Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#  If you make syntax (notational) errors, no worries -- get help
#  fixing them at either this session OR at the NEXT session.
#
#  Don't forget to COMMIT your work by using  VCS ~ Commit and Push.
########################################################################
import rosegraphics as rg
window= rg.TurtleWindow()
window.delay(20)
jacob=rg.SimpleTurtle("turtle")
jacob.pen=rg.Pen("green",12)
jacob.speed=5
craig=rg.SimpleTurtle()
craig.pen=rg.Pen("red",12)
craig.speed=5

for x in range(15):
    jacob.forward(100)
    craig.backward(100)
    jacob.left(90)
    craig.left(90)
    jacob.forward(100)
    craig.forward(100)
    jacob.left(90)
    craig.right(90)
    jacob.forward(100)
    craig.forward(100)
    jacob.left(90)
    craig.right(90)
    jacob.forward(90)
    craig.forward(90)


window.close_on_mouse_click()
