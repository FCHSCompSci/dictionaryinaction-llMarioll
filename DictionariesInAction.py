""" Mario Lopez, 09/24/2018, DictionariesInAction(Project 2) """
print("Please Input Your Fantasy Soccer Team Using A 4-4-2 Formation")
soccer_team = {
    'fs_1': "",
    'fs_2': "",
    'mid_1': "",
    'mid_2': "",
    'mid_3': "",
    'mid_4': "",
    'def_1': "",
    'def_2': "",
    'def_3': "",
    'def_4': "",
    'gk_1': "",
    }

def substitutions(position):
    x = input(" Who would you like to substitute? ")
    soccer_team[position] = x

def print_team():
    for k,v in soccer_team.items():
        print(k,v)

def update_team():
    pos = input("What position would you like to substitute?")
    substitutions(pos)
    print_team()

for position,player in soccer_team.items():
        print(position,player)
        playerInput = input()
        soccer_team[position] = playerInput

while True: 
    i = input(" Would You Like To Keep This As Your Permanent Team? [y] or [n]")
    if i == "y" or i == "Y":
        print(soccer_team)
        break
    else:
        update_team()
     
    
