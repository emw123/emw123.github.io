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
    draw_scene(canvas, 0, 0, width-1, height-1)

    root.mainloop()


def draw_scene(canvas, scene_left, scene_top, scene_right, scene_bottom):
    draw_sky(canvas)
    draw_sun(canvas)
    draw_grass(canvas)
    draw_tree(canvas)
    draw_clouds(canvas)
    draw_well(canvas)
    draw_bricks(canvas)
    #draw_grid(canvas, scene_left, scene_top, scene_right, scene_bottom, 20)
    
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
   

# Define more functions here, like draw_sky, draw_ground,
# draw_cloud, draw_tree, draw_kite, draw_snowflake, etc.
def draw_sky(canvas):
    canvas.create_rectangle(0, 0, 799, 300, outline = '#87CEEB', fill='#87CEEB')

def draw_grass(canvas):
    canvas.create_rectangle(0, 499, 799, 299, outline = '#567d46',fill='#567d46')

def draw_tree(canvas):
    canvas.create_rectangle(400, 499, 500, 300, outline= '#964B00',fill='#964B00')
    canvas.create_oval(350, 320, 550, 100, outline = '#90ee90', fill='#90ee90')
    canvas.create_oval(340, 315, 400, 260, outline = '#90ee90', fill='#90ee90')
    canvas.create_oval(325, 210, 400, 270, outline = '#90ee90', fill='#90ee90')
    canvas.create_oval(320, 160, 400, 215, outline = '#90ee90', fill='#90ee90')
    canvas.create_oval(330, 115, 400, 165, outline = '#90ee90', fill='#90ee90')
    canvas.create_oval(350, 80, 420, 130, outline = '#90ee90', fill='#90ee90')
    canvas.create_oval(390, 70, 475, 215, outline = '#90ee90', fill='#90ee90')
    canvas.create_oval(490, 80, 545, 150, outline = '#90ee90', fill='#90ee90')
    canvas.create_oval(450, 70, 510, 150, outline = '#90ee90', fill='#90ee90')
    canvas.create_oval(570, 110, 520, 160, outline = '#90ee90', fill='#90ee90')
    canvas.create_oval(580, 150, 520, 200, outline = '#90ee90',fill='#90ee90')
    canvas.create_oval(575, 190, 520, 240, outline = '#90ee90', fill='#90ee90')
    canvas.create_oval(575, 230, 520, 280, outline = '#90ee90',fill='#90ee90')
    canvas.create_oval(570, 265, 510, 310, outline ='#90ee90',fill='#90ee90')
    canvas.create_oval(555, 290, 480, 340, outline = '#90ee90',fill='#90ee90')
    canvas.create_oval(520, 290, 460, 350, outline = '#90ee90',fill='#90ee90')
    canvas.create_oval(490, 290, 420, 350, outline = '#90ee90',fill='#90ee90')
    canvas.create_oval(430, 290, 370, 340, outline = '#90ee90',fill='#90ee90')
    canvas.create_oval(430,250,460,220,outline = '#FF0000',fill='#FF0000')
    canvas.create_oval(390,190,410,170,outline = '#FF0000',fill="#FF0000")
    canvas.create_oval(520,220,540,200,outline = '#FF0000',fill='#FF0000')

def draw_clouds(canvas):
    #first cloud
    canvas.create_oval(10, 120, 250, 20, outline = '#FFFFFF', fill='#FFFFFF')
    canvas.create_oval(10,100,40,60,outline = '#FFFFFF', fill ='#FFFFFF')
    canvas.create_oval(35,115,70,80, outline = '#FFFFFF', fill ='#FFFFFF')
    canvas.create_oval(60,120,84,80,outline = '#FFFFFF', fill ='#FFFFFF')
    canvas.create_oval(80,130,120,80,outline = '#FFFFFF', fill ='#FFFFFF')
    canvas.create_oval(117,129,160,80,outline = '#FFFFFF', fill ='#FFFFFF')
    canvas.create_oval(155,125,180,80,outline ='#FFFFFF', fill ='#FFFFFF')
    canvas.create_oval(176,128,210,80,outline ='#FFFFFF', fill ='#FFFFFF')
    canvas.create_oval(208,120,240,100,outline ='#FFFFFF', fill ='#FFFFFF')
    canvas.create_oval(220,100,250,80,outline ='#FFFFFF', fill ='#FFFFFF')
    canvas.create_oval(240,80,255,60,outline ='#FFFFFF', fill ='#FFFFFF')
    canvas.create_oval(230,60,250,40,outline ='#FFFFFF', fill ='#FFFFFF')
    canvas.create_oval(200,45,240,20,outline ='#FFFFFF', fill ='#FFFFFF')
    canvas.create_oval(160,40,202,15,outline ='#FFFFFF', fill ='#FFFFFF')
    canvas.create_oval(120,40,162,12,outline ='#FFFFFF', fill ='#FFFFFF')
    canvas.create_oval(100,40,122,10,outline ='#FFFFFF', fill ='#FFFFFF')
    canvas.create_oval(60,40,102,15,outline ='#FFFFFF', fill ='#FFFFFF')
    canvas.create_oval(30,40,62,20,outline ='#FFFFFF', fill ='#FFFFFF')
    canvas.create_oval(15,60,38,30,outline ='#FFFFFF', fill ='#FFFFFF')
    canvas.create_oval(5,65,25,40,outline ='#FFFFFF', fill ='#FFFFFF')

    #second cloud
    canvas.create_oval(540, 100, 650, 40, outline ='#FFFFFF', fill='#FFFFFF')
    canvas.create_oval(543,100,570,80,outline ='#FFFFFF', fill='#FFFFFF')
    canvas.create_oval(565,110,590,80,outline ='#FFFFFF', fill='#FFFFFF')
    canvas.create_oval(587,115,605,80,outline ='#FFFFFF', fill='#FFFFFF')
    canvas.create_oval(602,112,630,80,outline ='#FFFFFF', fill='#FFFFFF')
    canvas.create_oval(627,110,644,80,outline ='#FFFFFF', fill='#FFFFFF')
    canvas.create_oval(640,100,665,80,outline ='#FFFFFF', fill='#FFFFFF')
    canvas.create_oval(640,82,670,60,outline ='#FFFFFF', fill='#FFFFFF')
    canvas.create_oval(630,62,660,40,outline ='#FFFFFF', fill='#FFFFFF')
    canvas.create_oval(620,35,632,60,outline ='#FFFFFF', fill='#FFFFFF')
    canvas.create_oval(590,30,623,45,outline ='#FFFFFF', fill='#FFFFFF')
    canvas.create_oval(560,35,592,45,outline ='#FFFFFF', fill='#FFFFFF')
    canvas.create_oval(540,40,570,60,outline ='#FFFFFF', fill='#FFFFFF')
    canvas.create_oval(525,55,550,85,outline ='#FFFFFF', fill='#FFFFFF')

def draw_sun(canvas):
    canvas.create_oval(690, 130, 880, -30, outline = '#f9d71c',fill = '#f9d71c')

def draw_bricks(canvas):
    x, y, loop_count, row_count = [40, 80], [460, 480], 0, 0
    for i in range(21) :
        canvas.create_rectangle(x[0], y[0], x[1], y[1],outline = '#808080', fill='#666666')
        if loop_count % 3 == 2 and loop_count > 0: # start new row 
            row_count += 1
            x = [i-80 for i in x]
            y = [i-20 for i in y]
        else: # increment x for a brick to the right in row
            x = [i+40 for i in x]
        loop_count += 1 # increment total brick count

def draw_well(canvas):
    draw_bricks(canvas)
    canvas.create_rectangle(40,240,60,340,outline = '#4E3524',fill='#4E3524')
    canvas.create_rectangle(140,240,160,340,outline = '#4E3524',fill='#4E3524')
    canvas.create_rectangle(40,240,160,220,outline = '#4E3524',fill='#4E3524')
    canvas.create_rectangle(60,260,140,250,outline = '#C0C0C0', fill='#C0C0C0')
    canvas.create_rectangle(160,260,200,250,outline = '#C0C0C0',fill='#C0C0C0')
    canvas.create_rectangle(190,300,200,260,outline = '#C0C0C0',fill='#C0C0C0')
    canvas.create_rectangle(95,340,105,250,outline = '#C4A484',fill='#C4A484')

    
# Call the main function so that
# this program will start executing.
main()