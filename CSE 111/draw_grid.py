import tkinter as tk


def main():
    # The width and height of the scene window.
    width = 800
    height = 500

    # Create the Tk root object.
    root = tk.Tk()
    root.geometry(f"{width}x{height}")

    # Create a Frame object.
    frame = tk.Frame(root)
    frame.master.title("Scene")
    frame.pack(fill=tk.BOTH, expand=1)

    # Create a canvas object that will draw into the frame.
    canvas = tk.Canvas(frame)
    canvas.pack(fill=tk.BOTH, expand=1)

    # Call the draw_scene function.
    draw_scene(canvas, 0, 0, 799, 599)

    root.mainloop()


def draw_scene(canvas, scene_left, scene_top, scene_right, scene_bottom):
    canvas.create_oval(150, 150, 250, 250, fill="#ff0000")
    draw_grid(canvas, scene_left, scene_top, scene_right, scene_bottom, 100)

def draw_grid(canvas,left, top, right, bottem, grid_spacing):
    
    text_horizontal_margin = 20
    text_vertical_margin = 10
    
    #Draw horizontal lines
    for i in range(top, bottem, grid_spacing):
        canvas.create_line(left, i ,right, i)
        canvas.create_text(left + text_horizontal_margin, i + text_vertical_margin, text = f'{i}')

    #draw vertical lines
    for i in range(left, right, grid_spacing):
        canvas.create_line(i, top, i, bottem)
        canvas.create_text(i, top + text_vertical_margin, text = f'{i}')

main()