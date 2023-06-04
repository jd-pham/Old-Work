from tkinter import Canvas, Tk
master = Tk()

canvas = Canvas(master, width=1000, height=1000)

canvas.create_rectangle(0, 0, 50, 50, fill="red", outline = 'red')

canvas.create_rectangle(500, 500, 100, 100, fill='blue', outline='green')
canvas.pack()

shape2={'bounds': [1000, 1000, 600, 700, 800, 900], 'kind': 'tri', 'fill': True}

canvas.create_polygon(list(shape2.values())[0], fill='green', outline='white', dash=(4,2) )


master.mainloop() 

