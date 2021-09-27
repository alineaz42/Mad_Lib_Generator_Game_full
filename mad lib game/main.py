from tkinter import*
from stories import madlib1, madlib2, madlib3
root = Tk()
root.title("Mad Lib Generator Game")
root.geometry("600x500")
# labels###############################################################################
Label(root, text="Mad Libs Generator\n Have fun!", font="arial 20 bold").pack()
Label(root, text="Click Any One:", font="arial 15 bold").place(x=40, y=80)

# buttons ######################################
Button(root, text='The Photographer', font='arial 15',
       command=madlib1, bg='ghost white').place(x=60, y=120)
Button(root, text='apple and apple', font='arial 15',
       command=madlib3, bg='ghost white').place(x=70, y=180)
Button(root, text='The Butterfly', font='arial 15',
       command=madlib2, bg='ghost white').place(x=80, y=240)

# main loop #################################################
root.mainloop()
