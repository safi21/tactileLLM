# This only works for ['top left', 'top right'], ['bottom left', 'bottom right'], and ['left', 'right'] combination
import drawsvg as draw

def sensor_array(canvas, horizontal_lines, vertical_lines, position):
    d = {}
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
        d['horizontal_'+str(i)] = [x1, t2, x2, t2]
        t2 += ((height)/(horizontal_lines + 1))
    temp = x2 - x1
    for j in range(vertical_lines):
        canvas.append(draw.Lines(x1, y1, x1, y2, stroke = 'black'))
        d['vertical_'+str(j)] = [x1, y1, x1, y2]
        x1 += temp / (vertical_lines - 1)
    return d


if __name__ == "__main__":
    arr = []
    arr1 = []
    base = draw.Drawing(400, 400, origin= (0, 0))
    all_data = {}
    l = ['bottom right', 'bottom left']
    array_list = [(4, 4), (8, 4)]
    for (i, j) in zip(array_list, l):
        x, y = i
        all_data[j] = sensor_array(base, x, y, j)
    #base.save_svg('array.svg')
    for key, value in all_data.items():
        if 'left' in key:
        # if key == 'top left':
            for k, v in value.items():
                if 'h' in k:
                    # print(v)
                    x = (v[-2], v[-1])
                    arr.append(x)
        if 'right' in key:
        # if key == 'top right':
            for n, m in value.items():
                if 'h' in n:
                    arr1.append((m[0], m[1]))
    # counter = min(len(arr), len(arr1))
    # print(min(len(arr), len(arr1)))
    # h_dis = abs(arr[0][0] - arr1[0][0])
    # print(h_dis)
    for i, j in zip(arr, arr1):
        base.append(draw.Lines(i[0], i[1], j[0], j[1], stroke = 'black', fill = 'none'))
        # base.append(draw.Lines(i[0], i[1], (i[0] + h_dis - h_dis/counter), i[1], (i[0] + h_dis - h_dis/counter), j[1], j[0], j[1], stroke = 'black', fill = 'none'))
        # h_dis -= h_dis/4
                    
    base.save_svg("ArrayConnectorHorizontal.svg")
    print('Done.')