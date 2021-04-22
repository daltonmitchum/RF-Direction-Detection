from tkinter import Tk, Canvas, Frame, BOTH
import math
from directionCalculation import main

class Example(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.master.title("Direction Calculator")
        self.pack(fill=BOTH, expand=1)
        with open("printDOA.txt") as f1:
            directionOfArrival = f1.read()
            angle = float(directionOfArrival)
            x = 900
            y = 900
            rB = 0.35 * y
            rL = 0.02 * y
            cxB = x * 0.5
            cyB = y * 0.5
            cxL = cxB + (rB * (math.cos(math.radians(angle))))
            cyL = cyB + (rB * (math.sin(math.radians(angle))))

            canvas = Canvas(self)
            canvas.configure(bg='black')
            oval_big = canvas.create_oval(cxB - rB, cyB - rB, cxB + rB, cyB + rB, outline="#cc0000", fill="#ffffff",
                                          width=y * .01)
            oval_small = canvas.create_oval(cxL - rL, cyL - rL, cxL + rL, cyL + rL, outline="#cc0000", fill="#ffffff",
                                            width=y * .005)
            canvas.move(oval_big, 200, -100)
            canvas.move(oval_small, 200, -100)
            angleString = ("{} Degrees".format(angle))
            text = canvas.create_text(cxB, cyB, fill="#000000", font=200, text=angleString)
            canvas.move(text, 200, -100)
            canvas.pack(fill=BOTH, expand=1)


def main_2():
    root = Tk()
    ex = Example()
    root.geometry("900x900+300+300")
    root.mainloop()


if __name__ == '__main__':
    main()
    main_2()
