# with extended wires
import drawsvg as draw

def sensor_array(canvas, horizontal_lines, vertical_lines, position):
    height = canvas.height
    width = canvas.width
    if position == 'top left':
        width = width / 2
        height = height / 2 
    elif position == 'center':
        width = width
        height = height
    if position == 'top right':
        width = width / 2
        height = height / 2
        x1, y1 = (width + (width / (horizontal_lines + 1))), ((height / (horizontal_lines+1)))
        x2, y2 = width + (width - (width / (horizontal_lines + 1))), (height - (height / (horizontal_lines + 1)))
    elif position == 'bottom left':
        width = width / 2
        height = height / 2
        x1, y1 = (width / (horizontal_lines + 1)), (height + (height / (horizontal_lines+1)))
        x2, y2 = (width - (width / (horizontal_lines + 1))), (height + (height - (height / (horizontal_lines + 1))))
    elif position == 'left':
        width = width / 2
        x1, y1 = (width / (horizontal_lines + 1)), (height / (horizontal_lines+1))
        x2, y2 = (width - (width / (horizontal_lines + 1))), (height - (height / (horizontal_lines + 1)))
    elif position == 'right':
        width = width / 2
        x1, y1 = width + (width / (horizontal_lines + 1)), (height / (horizontal_lines+1))
        x2, y2 = width + (width - (width / (horizontal_lines + 1))), (height - (height / (horizontal_lines + 1)))
    elif position == 'top':
        height = height / 2
        x1, y1 = (width / (horizontal_lines + 1)), (height / (horizontal_lines+1))
        x2, y2 = (width - (width / (horizontal_lines + 1))), (height - (height / (horizontal_lines + 1)))
    elif position == 'bottom':
        height = height / 2
        x1, y1 = (width / (horizontal_lines + 1)), (height + (height / (horizontal_lines+1)))
        x2, y2 = (width - (width / (horizontal_lines + 1))), (height + (height - (height / (horizontal_lines + 1))))
    elif position == 'bottom right':
        height = height / 2
        width = width / 2
        x1, y1 = width + (width / (horizontal_lines + 1)), height + (height / (horizontal_lines+1))
        x2, y2 = width + (width - (width / (horizontal_lines + 1))), height + (height - (height / (horizontal_lines + 1)))
    else:
        x1, y1 = (width / (horizontal_lines + 1)), (height / (horizontal_lines+1))
        x2, y2 = (width - (width / (horizontal_lines + 1))), (height - (height / (horizontal_lines + 1)))
    t1, t2 = x1, y1
    m = abs(x1-x2) * 0.08
    for i in range(horizontal_lines):
        canvas.append(draw.Lines(x1 - m, t2, x2 + m, t2, stroke = 'black'))
        t2 += ((height)/(horizontal_lines + 1))
    temp = x2 - x1
    for j in range(vertical_lines):
        canvas.append(draw.Lines(x1, y1 - m, x1, y2 + m, stroke = 'black'))
        x1 += temp / (vertical_lines - 1)

if __name__ == "__main__":
    base = draw.Drawing(400, 400, origin= (0, 0))
    l = ['top left', 'bottom left', 'top right', 'bottom right']
    array_list = [(4, 4), (5, 5), (3, 6), (2, 2)]
    for (i, j) in zip(array_list, l):
        x, y = i
        sensor_array(base, x, y, j)
    base.save_svg('sensor_array_extended.svg')
    print("Sensor arrays generated.")