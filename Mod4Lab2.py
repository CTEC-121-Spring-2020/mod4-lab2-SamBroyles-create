"""
CTEC 121
Sam Broyles
Module 4 Lab 2
Mod4 Lab2 in class demo
"""

""" IPO template
Input(s): list/description
Process: description of what function does
Output: return value and description
"""
from graphics import *
def main():
    '''
    startValue = 1
    endValue = 10
    sum = 0
    if startValue % 2 ==1:
        startValue = startValue + 1
    for i in range(startValue, endValue, 2):
        sum = sum + i
    print(sum)
    '''

    win = GraphWin("demo", 800, 800)
    win.setCoords(-4.0, -4.0, 4.0, 4.0)
    p1 = Circle(Point(2, 3), .5)
    p1.setFill("red")
    p1.draw(win)
    p2 = Circle(Point(-3, 1), .5)
    p2.setFill("blue")
    p2.draw(win)
    p3 = Circle(Point(-1.5, -2.5), .5)
    p3.setFill("green")
    p3.draw(win)

    input()


main()    