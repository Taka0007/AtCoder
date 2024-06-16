# import
import sys
import time

# Set the time limit
start_time = time.time()
max_duration = 1.85

# Function to identify the locations of negative and positive values in the grid
def make_place_set(lis):
    negative_place = set()
    positive_place = set()
    for i in range(len(lis)):
        for j in range(len(lis[i])):
            if lis[i][j] < 0:
                negative_place.add((i, j))
            elif lis[i][j] > 30:
                positive_place.add((i, j))
    return negative_place, positive_place

# Function to generate a movement string based on coordinates
def generate_movement_string(x1, y1, x2, y2):
    movement = []
    if y2 < y1:
        movement += ['U'] * (y1 - y2)
    if y2 > y1:
        movement += ['D'] * (y2 - y1)
    if x2 < x1:
        movement += ['L'] * (x1 - x2)
    if x2 > x1:
        movement += ['R'] * (x2 - x1)
    return movement

# Input processing
N = int(input())
field = []
for _ in range(N):
    field.append(list(map(int, input().split())))

# Initial variable setup
load = 0
operations = []
ope_num = 0
negative, positive = make_place_set(field)
now_x, now_y = 0, 0
flag = True

# Main processing loop
while flag:
    if time.time() - start_time > max_duration:
        break
    now_score = field[now_x][now_y]
    if load > 60 and negative:
        next_pos = negative.pop()
        next_x, next_y = next_pos
        move_list = generate_movement_string(now_x, now_y, next_x, next_y)
        operations += move_list
        if load > 0:
            operations.append('-' + str(load))
        load = 0
        now_x, now_y = next_x, next_y
        ope_num += len(move_list) + 1
        if ope_num > 100000:
            flag = False
            break
    elif now_score > 10:
        operations.append('+' + str(now_score)) 
        load += now_score
        ope_num += 1
        if ope_num > 100000:
            flag = False
            break
    elif positive:
        next_pos = positive.pop()
        next_x, next_y = next_pos
        move_list = generate_movement_string(now_x, now_y, next_x, next_y)
        operations += move_list
        if load + now_score > 0:
            operations.append('+' + str(load + now_score))
        load += now_score
        now_x, now_y = next_x, next_y
        ope_num += len(move_list) + 1
        if ope_num > 100000:
            flag = False
            break

# Output the operations
for op in operations:
    print("".join(op))
