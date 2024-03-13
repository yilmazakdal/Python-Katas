def find_partner(students,directions):
    right = 0
    left = 0
    up = 0
    down = 0
    result_list = []
    for direction in directions:
        if direction == 'right':
            right += 1
        elif direction == 'left':
            left += 1
        elif direction == 'up':
            up += 1
        elif direction == 'down':
            down += 1
    position = right - left
    row = down - up
    if row >0 :
        if position < 6 and position > -6 :
            result_list.append(students[row][position])
            return result_list
        else:
            result_list.append(students[row][position%6])
            return result_list
    else:
        if position < 6 and position > -6 :
            result_list.append(students[0][position])
            return result_list
        else:
            result_list.append(students[0][position%6])
            return result_list
        



    
