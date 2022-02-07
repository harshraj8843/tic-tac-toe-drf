# for random number selection
import random

# for making combinations of a list
from itertools import combinations

# all numbers allowed for input
num_list = [1,2,3,4,5,6,7,8,9]

# wining list
win_list = [
    [1,2,3],
    [1,4,7],
    [1,5,9],
    [2,5,8],
    [3,5,7],
    [3,6,9],
    [4,5,6],
    [7,8,9]
]

# sublist function
def sub_list (list):
    temp_list = []
    for i in range(len(list)):
        for j in range(i, len(list)):
            if i == j:
                pass
            else:
                temp_list.append([list[i], list[j]])
    return(temp_list)

# user move analysis
def user_move_analysis(no_list, user_list):
    if len(user_list) == 2:
        for i in win_list:
            check = all(item in i for item in user_list)
            if check is True:
                if i in no_list:
                    pass
                else:
                    return i
    if len(user_list) > 2:
        user_move_list = sub_list(user_list)
        for i in user_move_list:
            for j in win_list:
                check = all(item in j for item in i)
                if check is True:
                    if j in no_list:
                        pass
                    else:
                        return j

# for user_input
def user_minus(user_list, fav_list):
    for i in fav_list:
        if i in user_list:
            pass
        else:
            return i

# computer self analysis list function
def self_analysis_list(user_list, com_list):
    if(len(com_list) == 1):
        for i in win_list:
            check = all(item in i for item in com_list)
            if check is True:
                flag = False
                for j in i:
                    if j in user_list:
                        flag = True
                        break
                if(flag == True):
                    pass
                else:
                    return i
    if len(com_list) > 1:
        com_move_list = sub_list(com_list)
        for i in com_move_list:
            for j in win_list:
                check = all(item in j for item in i)
                if check is True:
                    flag = False
                    for k in j:
                        if k in user_list:
                            flag = True
                            break
                    if(flag == True):
                        pass
                    else:
                        return j

def self_minus(com_list, fav_list):
    for i in fav_list:
        if i in com_list:
            pass
        else:
            return i

def minus(res_list):
    for i in num_list:
        if i in res_list:
            pass
        else:
            return i

def self_analysis(user_list, res_list, com_list):
    favourable_list = self_analysis_list(user_list, com_list)
    if favourable_list is None:
        fav_input = minus(res_list)
        com_list.append(fav_input)
        res_list.append(fav_input)
        return fav_input
    else:
        fav_input = self_minus(com_list, favourable_list)
        com_list.append(fav_input)
        res_list.append(fav_input)
        return fav_input

# computer first time input function
def computer_first_input(user_list, res_list, com_list):
    if(len(user_list) == 1):
        # most probable numbers to start to win
        fav = [1,2,3,4,7]
        try:
            # if user has given any input from fav list
            fav.remove(user_list[0])
        except:
            pass
        temp = random.choice(fav)
        com_list.append(temp)
        res_list.append(temp)
        return temp
    else:
        # most probable numbers to start to win
        temp = random.choice([1,2,3,4,7])
        com_list.append(temp)
        res_list.append(temp)
        return temp

# computer input function
def computer_input(no_list, res_list, user_list, com_list):
    if(len(user_list) > 1):
        # user move analysis
        favourable_list = user_move_analysis(no_list, user_list)
        if favourable_list is None:
            # self move analysis
            return self_analysis(user_list, res_list, com_list)
        else:
            fav_input = user_minus(user_list, favourable_list)
            if fav_input in res_list:
                # self move analysis
                return self_analysis(user_list, res_list, com_list)
            else:
                com_list.append(fav_input)
                res_list.append(fav_input)
                no_list.append(favourable_list)
                return fav_input
    else:
        # self move analysis
        return self_analysis(user_list, res_list, com_list)

# check if computer won
def match_computer(com_list):
    comb = list(combinations(com_list,3))
    arr = []
    for ii in comb:
        arr.append(list(ii))
    for i in win_list:
        for j in arr:
            check = all(item in i for item in j)
            if check is True:
                return True
            else:
                pass

# check if user won
def match_user(user_list):
    comb = list(combinations(user_list,3))
    arr = []
    for ii in comb:
        arr.append(list(ii))
    for i in win_list:
        for j in arr:
            check = all(item in i for item in j)
            if check is True:
                return True
            else:
                pass

# our main function
def main(no_list, res_list, user_list, com_list):

    # computer first input
    if(com_list == []):
        move = computer_first_input(user_list, res_list, com_list)
        output = {
            'user_win': False,
            'com_win': False,
            'move': move,
            'no_list': no_list,
            'res_list': res_list,
            'user_list': user_list,
            'com_list': com_list
        }
        return output
    else:
        # computer input
        move = computer_input(no_list, res_list, user_list, com_list)

        # check if user won
        user_win = False
        user_done = match_user(user_list)
        if user_done == True:
            user_win = True
        
        # check if computer won
        com_done = match_computer(com_list)
        com_win = False
        if com_done == True:
            com_win = True
        
        # if none of them won
        if(user_win != True and com_win != True):
            output = {
                'user_win': user_win,
                'com_win': com_win,
                'move': move,
                'no_list': no_list,
                'res_list': res_list,
                'user_list': user_list,
                'com_list': com_list
            }
        else:
            # if user won, there id no need to return lists
            if(user_win == True):
                output = {
                    'user_win': user_win,
                    'com_win': com_win
                }
            else:
                # if computer won
                output = {
                    'user_win': user_win,
                    'com_win': com_win,
                    'move': move,
                    'no_list': no_list,
                    'res_list': res_list,
                    'user_list': user_list,
                    'com_list': com_list
                }
        return output

## End here, byeeeeeeeeeeeeeeeee......
