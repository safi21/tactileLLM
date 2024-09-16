# This code connects sensor arrays for two combinations. They are: {top left, bottom right} and {top right, bottom left}
import drawsvg as draw

def sensor_array(canvas, horizontal_lines, vertical_lines, position):
    lst = []
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
        if position == 'bottom right':
            s = [x1, t2]
            lst.append(s)
        if position == 'bottom left':
            b = [x2, t2]
            lst.append(b)
        t2 += ((height)/(horizontal_lines + 1))
    temp = x2 - x1
    for j in range(vertical_lines):
        canvas.append(draw.Lines(x1, y1, x1, y2, stroke = 'black'))
        if position == 'top left':
            points = [x1, y2]
            lst.append(points)
        if position == 'top right':
            points = [x1, y2]
            lst.append(points)
        x1 += temp / (vertical_lines - 1)
    return lst
if __name__ == '__main__':
    base = draw.Drawing(400, 400, origin= (0, 0))
    d = []
    l = ['bottom right', 'top left']
    l.sort() # bottom one first and top one second
    w = [-1, -1]
    array_list = [(4, 4), (6, 6)]
    for (i, j) in zip(array_list, l):
        x, y = i
        if j == 'top right':
            w[0] = y
        if j == 'bottom left':
            w[1] = x
        abc = sensor_array(base, x, y, j)
        d.append(abc)
    nl = []
    for i in d:
        for j in i:
            nl.append(j)
    #print(nl)

    if 'top left' in l and 'bottom right' in l and len(l) == 2:
        print("Connector added")
        for i in range(int(len(nl)/2)):
            a, b = nl[i]
            c, d = nl[len(nl)-1-i]
            base.append(draw.Lines(a, b, c, b, c, d, stroke = 'black', fill = 'none'))
    elif 'top right' in l and 'bottom left' in l and len(l) == 2:
        print("True")
        cd = 0
        for i in range(int(len(nl)-1), -1, -1):
            a, b = nl[i]
            c, d = nl[i-w[0]]
            base.append(draw.Lines(a, b, a, d, c, d, stroke = 'black', fill = 'none'))
            cd += 1
            if cd == min(w):
                break
    base.save_svg('arrayWithConnector.svg')
    print('Array with connector design generated.')