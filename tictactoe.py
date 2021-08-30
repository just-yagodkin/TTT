# write your code here
counter = 1
li = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]
string = ''.join(li)


def rotate(string_):  # clockwise
    string_fake = string_.copy()
    string_[2] = string_fake[0]
    string_[5] = string_fake[1]
    string_[8] = string_fake[2]
    string_[1] = string_fake[3]
    string_[7] = string_fake[5]
    string_[0] = string_fake[6]
    string_[3] = string_fake[7]
    string_[6] = string_fake[8]
    return string_


def print_field():  # prints field
    print("---------")
    print('|', end=' ')
    print(li[0], li[1], li[2], end=' ')
    print("|")
    print('|', end=' ')
    print(li[3], li[4], li[5], end=' ')
    print("|")
    print('|', end=' ')
    print(li[6], li[7], li[8], end=' ')
    print("|")
    print("---------")


def how_many(string_):  # function can help to avoid situation when
    num_of_o = 0        # number of Xs greater number of Os and vice versa
    num_of_x = 0
    while string_.find('O') != -1:
        num_of_o += 1
        string_ = string_.replace('O', "_", 1)
    while string_.find('X') != -1:
        num_of_x += 1
        string_ = string_.replace('X', "_", 1)
    nums = [num_of_o, num_of_x]
    return nums


def xor2(a, b):
    if bool(a) == bool(b):
        return False
    else:
        return a or b


def xor3(x, y, z):  # not correct in global opinion
    if x == y == z == 1:
        return False
    elif x == 1 and y == z == 0:
        return True
    elif y == 1 and x == z == 0:
        return True
    elif z == 1 and x == y == 0:
        return True
    else:
        return False


def streakx(string_):  # checks the winner X
    strict = string_.copy()
    a = (strict[0] == strict[1] == strict[2] == 'X')
    b = (strict[1] == strict[4] == strict[7] == 'X')
    c = (strict[0] == strict[4] == strict[8] == 'X')
    for i in range(4):
        if xor3(a, b, c):
            return 1
        else:
            rotate(strict)
            a = (strict[0] == strict[1] == strict[2] == 'X')
            b = (strict[1] == strict[4] == strict[7] == 'X')
            c = (strict[0] == strict[4] == strict[8] == 'X')
    return 0


def streako(string_):  # checks the winner O
    strict = string_.copy()
    a = (strict[0] == strict[1] == strict[2] == 'O')
    b = (strict[1] == strict[4] == strict[7] == 'O')
    c = (strict[0] == strict[4] == strict[8] == 'O')
    for j in range(4):
        if xor3(a, b, c):
            return 1
        else:
            rotate(strict)
            a = (strict[0] == strict[1] == strict[2] == 'O')
            b = (strict[1] == strict[4] == strict[7] == 'O')
            c = (strict[0] == strict[4] == strict[8] == 'O')
    return 0


def check_the_game_stats():
    global flag
    if abs(how_many(string)[1] - how_many(string)[0]) >= 2:
        print("Impossible")
    elif string.find('_') == -1:
        if streako(li) == streakx(li) == 0:
            print("Draw")
        # if streako(li) == streakx(li) == 1:
        #    print("Impossible")
        if streako(li) == 1 and streakx(li) == 0:
            print("O wins")
        if streakx(li) == 1 and streako(li) == 0:
            print("X wins")
        flag = 1
    else:
        if streako(li) == streakx(li) == 0:
            pass
        # if streako(li) == streakx(li) == 1:
        #    print("Impossible")
        if streako(li) == 1 and streakx(li) == 0:
            print("O wins")
            flag = 1
        if streakx(li) == 1 and streako(li) == 0:
            print("X wins")
            flag = 1


print_field()


flag = 0


def fill_the_cell(i):
    global counter
    global flag
    if li[i] == "_":
        if counter % 2 == 1:
            li[i] = "X"
        else:
            li[i] = "O"
        print_field()
        counter += 1
    elif counter < 10:
        print("This cell is occupied! Choose another one!")
    else:
        print("Draw")
        flag = 1




while flag == 0:
    coord1, coord2 = input('Enter the coordinates:').split()
    arr1 = list(coord1)
    arr2 = list(coord2)
    flag1 = 1
    flag2 = 1
    for k in range(len(coord1)):
        if 48 <= ord(arr1[k]) <= 57:
            pass
        else:
            flag1 = -1

    for l in range(len(coord2)):
        if 48 <= ord(arr2[l]) <= 57:
            pass
        else:
            flag2 = -1
    
    if flag1 == flag2 == 1:
        coord1 = int(coord1)
        coord2 = int(coord2)
        if (coord1 != 1 and coord1 != 2 and coord1 != 3) or (coord2 != 1 and coord2 != 2 and coord2 != 3):
            print("Coordinates should be from 1 to 3!")
        elif coord1 == 1:
            if coord2 == 1:
                fill_the_cell(0)
            elif coord2 == 2:
                fill_the_cell(1)
            else:
                fill_the_cell(2)
        elif coord1 == 2:
            if coord2 == 1:
                fill_the_cell(3)
            elif coord2 == 2:
                fill_the_cell(4)
            else:
                fill_the_cell(5)
        else:
            if coord2 == 1:
                fill_the_cell(6)
            elif coord2 == 2:
                fill_the_cell(7)
            else:
                fill_the_cell(8)
        check_the_game_stats()
    else:
        print("You should enter numbers!")
        coord1, coord2 = input('Enter the coordinates:').split()
