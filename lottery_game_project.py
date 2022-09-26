import random

numbers_in_combination = 0
total_numbers = 0
counter_met = 0
profit = 0
win_combination_set = set()
player_numbers_list_str = []
player_numbers_list_int = []
type_of_game = input('Enter your prefer type of game [5/35], [6/42] or [6/49]: ')


while True:
    try:
        player_bet = float(input('Enter your bet (in BGN): '))
        break
    except:
        print("Bet must be a above 1.00 BGN!")

if type_of_game == "5/35":
    numbers_in_combination = 5
    total_numbers = 35
elif type_of_game == "6/42":
    numbers_in_combination = 6
    total_numbers = 42
if type_of_game == "6/49":
    numbers_in_combination = 6
    total_numbers = 49

while len(win_combination_set) < numbers_in_combination:
    win_combination_set.add(random.randint(1, total_numbers))

while len(player_numbers_list_str) < numbers_in_combination:
    try:
        player_numbers = input(f'Enter your combination of {numbers_in_combination} numbers '
                               f'with "," between them /in diapason between 1 and {total_numbers}/:')
        player_numbers_list_str = player_numbers.split(",")
        break
    except:
        print(f"Numbers must be {numbers_in_combination}!")

for every_number in range(len(player_numbers_list_str)):
    player_numbers_list_int.append(int(player_numbers_list_str[every_number]))

win_combination_list = list(win_combination_set)
win_combination_list.sort()
player_numbers_list_int.sort()

for every_number in range(numbers_in_combination):
    if player_numbers_list_int[every_number] in win_combination_list:
        counter_met += 1

if counter_met == 0:
    print('Sorry, you don\'t have any matches and you lost your bet!')
elif counter_met == 1:
    print(f'Sorry, you have only {counter_met} match and you lost your bet!')
elif counter_met < 3:
    print(f'Sorry, you have only {counter_met} matches and you lost your bet!')
elif counter_met >= 3:
    print(f'Congratulations! You have {counter_met} match numbers!')
    profit = player_bet ** (counter_met + total_numbers / counter_met)
    print(f'You win {profit:.2f}!')
if counter_met < 6:
    print(f'Win combination is {win_combination_list} '
      f'and your combination is {player_numbers_list_int}')
else:
    print(f'Your lucky combination is {win_combination_list}')