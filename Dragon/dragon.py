import svgwrite

PICTURE_WIDTH = 3000
PICTURE_HEIGHT = 3000
START_POSITION_X = int(PICTURE_WIDTH / 2)
START_POSITION_Y = int(PICTURE_HEIGHT / 2)

DRAGON_SIZE = 7
UP_DIRECTION = 'u'
LEFT_DIRECTION = 'l'
RIGHT_DIRECTION = 'r'
DOWN_DIRECTION = 'd'
PATH_START = 'M'


def rotate_element(given_direction):
    if given_direction == UP_DIRECTION:
        direction = RIGHT_DIRECTION
    elif given_direction == LEFT_DIRECTION:
        direction = UP_DIRECTION
    elif given_direction == DOWN_DIRECTION:
        direction = LEFT_DIRECTION
    elif given_direction == RIGHT_DIRECTION:
        direction = DOWN_DIRECTION
    else:
        direction = ''
    return direction


def expand(list_to_expand):
    reversed_list = list(list_to_expand)
    reversed_list.reverse()
    for k in reversed_list:
        list_to_expand = list_to_expand + [rotate_element(k)]
    return list_to_expand


def create_list(size, dragon_list):
    for i in range(size):
        dragon_list = expand(dragon_list)
    return dragon_list


def next_line(direction):
    next_string = ''
    if direction == UP_DIRECTION:
        next_string = LEFT_DIRECTION + ' ' + str(0) + ',' + str(DRAGON_SIZE) + ' '
    if direction == LEFT_DIRECTION:
        next_string = LEFT_DIRECTION + ' ' + str(-DRAGON_SIZE) + ',' + str(0) + ' '
    if direction == RIGHT_DIRECTION:
        next_string = LEFT_DIRECTION + ' ' + str(DRAGON_SIZE) + ',' + str(0) + ' '
    if direction == DOWN_DIRECTION:
        next_string = LEFT_DIRECTION + ' ' + str(0) + ',' + str(-DRAGON_SIZE) + ' '
    return next_string


def create_curve(dragon_list):
    curve_string = PATH_START + ' ' + str(int(START_POSITION_X)) + ',' + str(int(START_POSITION_Y)) + ' '
    for k in dragon_list:
        curve_string = curve_string + next_line(k)
    return curve_string


def create_dragon_image(size):
    picture = svgwrite.Drawing(filename='dragon.svg')
    picture.viewbox(width=PICTURE_WIDTH, height=PICTURE_HEIGHT)
    dragon_list = create_list(size, [UP_DIRECTION])
    dragon_curve = create_curve(dragon_list)
    picture_path = picture.path(d=dragon_curve, fill='none', stroke='black', stroke_width=2)
    picture.add(picture_path)
    picture.save()


create_dragon_image(14)
