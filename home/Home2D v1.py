from graphics import *

win = GraphWin("Home2D", 640, 360)

c1 = Circle(Point(568, 68), 32)
c1.setFill("#ffff00")
r1 = Rectangle(Point(247, 200), Point(421, 336))
r1.setFill("#804000")
r2 = Rectangle(Point(268, 218), Point(329, 249))
r2.setFill("#0080ff")
r3 = Rectangle(Point(359, 218), Point(402, 237))
r3.setFill("#0080ff")
r4 = Rectangle(Point(268, 268), Point(330, 316))
r4.setFill("#0080ff")
l1 = Line(Point(299, 268), Point(299, 316))
l2 = Line(Point(299, 281), Point(330, 281))
r5 = Rectangle(Point(365, 268), Point(397, 336))
r5.setFill("#ff8040")
c2 = Circle(Point(392, 303), 2)
c2.setFill("#008000")
p1 = Polygon(Point(213, 200), Point(331, 101), Point(454, 200))
p1.setFill("#008080")
p2 = Polygon(Point(247, 200), Point(331, 101), Point(420, 200))
c3 = Circle(Point(308, 173), 14)
c3.setFill("#00ffff")
c4 = Circle(Point(357, 173), 14)
c4.setFill("#00ffff")
l3 = Line(Point(294, 173), Point(322, 173))
l4 = Line(Point(357, 159), Point(357, 187))
l5 = Line(Point(308, 159), Point(308, 187))
l6 = Line(Point(343, 173), Point(371, 173))


c1.draw(win)
r1.draw(win)
r2.draw(win)
r3.draw(win)
r4.draw(win)
l1.draw(win)
l2.draw(win)
r5.draw(win)
c2.draw(win)
p1.draw(win)
p2.draw(win)
c3.draw(win)
c4.draw(win)
l3.draw(win)
l4.draw(win)
l5.draw(win)
l6.draw(win)

win.getMouse()
win.close()