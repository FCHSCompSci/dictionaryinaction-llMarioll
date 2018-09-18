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
for position,player in soccer_team.items():
    print(position,player)
    playerInput = input()
    soccer_team[position] = playerInput
    print(soccer_team)

