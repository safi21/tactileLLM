# without extended wires
# This only produces sensor arrays. No interconnects of wires are not added.
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
        height = height / 2
        width = width / 2
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
    for i in range(horizontal_lines):
        canvas.append(draw.Lines(x1, t2, x2, t2, stroke = 'black'))
        t2 += ((height)/(horizontal_lines + 1))
    temp = x2 - x1
    for j in range(vertical_lines):
        canvas.append(draw.Lines(x1, y1, x1, y2, stroke = 'black'))
        x1 += temp / (vertical_lines - 1)

if __name__ == '__main__':
    base = draw.Drawing(400, 400, origin= (0, 0))
    position = ['top left', 'top right', 'bottom left', 'bottom right']
    array_list = [(6, 6), (6, 4), (4, 4), (4, 5)]
    for (i, j) in zip(array_list, position):
        x, y = i
        sensor_array(base, x, y, j)
    base.save_svg('sensor_array.svg')
    print("Sensor array design generated.")