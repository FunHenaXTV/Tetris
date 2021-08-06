import tkinter as tk
from random import randint
WIDTH = 500
HEIGHT = 800

class Figures():
	"""docstring for Figures"""
	def __init__(self, canvas):
		pass


class s_shape(Figures):
	def create_figure(self):
		start = randint(0, 9)
		self.canvas = canvas
		res = []
		res.append(self.canvas.create_rectangle(start*(WIDTH//10), 0, (start+1)*(WIDTH//10), WIDTH//10, fill='green'))
		res.append(self.canvas.create_rectangle(start*(WIDTH//10), WIDTH//10, (start+1)*(WIDTH//10), 2*WIDTH//10, fill='green'))
		res.append(self.canvas.create_rectangle((start+1)*(WIDTH//10), WIDTH//10, (start+2)*(WIDTH//10), 2*WIDTH//10, fill='green'))
		res.append(self.canvas.create_rectangle((start+1)*(WIDTH//10), 2*WIDTH//10, (start+2)*(WIDTH//10), 3*WIDTH//10, fill='green'))



def draw_grid(canvas):
	lines_vertical = []
	lines_horisontal = []
	for i in range(0, 10):
		lines_vertical.append(canvas.create_line(WIDTH//10*i, 0, WIDTH//10*i, HEIGHT))
	for i in range(0, HEIGHT//(WIDTH//10)):
		lines_horisontal.append(canvas.create_line(0, i*(WIDTH//10), WIDTH, i*(WIDTH//10)))

	return lines_vertical, lines_horisontal


if __name__ == "__main__":
	root = tk.Tk()
	root.title("Tetris")
	root.configure(bg='#fff')

	canvas = tk.Canvas(root, bg='#fff', width=WIDTH, height=HEIGHT)
	canvas.pack()

	lines_vertical, lines_horisontal = draw_grid(canvas)

	s = s_shape(canvas)
	s.create_figure()

	root.mainloop()
