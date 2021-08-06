import tkinter as tk
WIDTH = 500
HEIGHT = 800



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

	root.mainloop()
