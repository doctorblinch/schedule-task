import random
import os


def configure_height4graph_from_condition(condition):
    min_val = min([i[0] for i in condition])
    max_val = max([i[1] for i in condition])

    height_lines = [[0] * (max_val + 1) for i in range(len(condition))]

    new_condition = []
    for section in condition:
        layer = layer_that_can_be_added(height_lines, section)
        new_condition.append((section[0], section[1], layer))

    return new_condition


def layer_that_can_be_added(height_lines, value):
    start, finish = value
    if start != 0:
        start -= 1
    can_be_added = False
    layer = 0
    while not can_be_added:
        for i in height_lines[layer][start:finish + 1]:
            if i == 1:
                layer += 1
                can_be_added = False
                break
            else:
                can_be_added = True

    else:
        for i in range(start, finish + 1):
            height_lines[layer][i] = 1

    return layer


def create_file_with_condition(condition):
    names = {name for root, dirs, files in os.walk('data/input_files') for name in files}
    available_name_found = False
    skeleton = 'condition_{}.csv'
    i = 1
    while not available_name_found:
        if skeleton.format(i) not in names:
            available_name_found = True
            with open('data/input_files/' + skeleton.format(i), 'w') as f:
                for i in condition:
                    f.write('{},{},{}\n'.format(i[0], i[1], i[2]))
        else:
            i += 1


def markdown2string(file_path):
    with open(file_path, 'r') as f:
        string = f.read()

    return string


def parse_condition_csv(path):
    schedules = []
    try:
        with open(path, 'r') as f:
            lines = f.readlines()
            for line in lines:
                schedules.append(
                    tuple(map(int, line.strip().split(',')))
                )
    except:
        return 'Wrong file format!'

    return schedules


def generate_random_condition(quantity, work_end, min_fine, max_fine, min_execution_time, max_execution_time):
    condition = []
    # кінцевий срок сдачі, штраф, час виконання
    for _ in range(quantity):
        a = random.randint(1, work_end)
        b = random.randint(min_fine, max_fine)
        c = random.randint(min_execution_time, max_execution_time)
        condition.append((a, b, c))

    return condition
