import math
import time as sleep
import status_script_1_stat as CalculateStat
import ev_script_2_stat as CalculateEv

base = [6]
ivv = [6]
evv = [0, 0, 0, 0, 0, 0, 0]
evs = 0

#universal variables
atk_nature = 1
def_nature = 1
spec_atk_nature = 1
spec_def_nature = 1
speed_nature = 1

#looping variable
stat = ["ss", "Hp", "Attack", "Defense", "Special Attack", "Special Defense", "Speed"]

print("Welcome to Pokemon Calculator!\n")
print("Press [1] for EV calculator or Press [2] Status calculator\n")
choice = int(input("What would you like to choose? "))

if choice == 1:
    base = [6]
    ivv = [6]
    evv = [0, 0, 0, 0, 0, 0, 0]
    evs = 0
    lvl = int(input("Input the level of your pokemon: "))
    if (lvl < 0 or lvl > 100):
        print("Level Can only reach max 100!")
        sleep(1)
        exit()

    print("Input Base Stats")
    for x in range(1, 7):
        base.append(int(input("Input your Pokemon's " + stat[x] + ": ")))

    print("Input IV's on each Stats")
    for y in range(1, 7):
        ivv.append(int(input("Input your Pokemon's " + stat[y] + " IV: ")))
        if (ivv[y] < 0 or ivv[y] > 31):
            print("You can only set IVs from 0 to 31!")
            sleep(2)
            print("System is Closing!")
            sleep(3)
            exit()
    else:
        print("Wrong Input!")
    print("\n[1]hardy   [2]lonely  [3]brave    [4]adamant  [5]naughty\n"
            "[6]bold    [7]docile  [8]relaxed  [9]impish   [10]lax\n"
            "[11]timid  [12]hasty  [13]serious [14]jolly   [15]naive\n"
            "[16]modest [17]mild   [18]quiet   [19]bashful [20]rash\n"
            "[21]calm   [22]gentle [23]sassy   [24]careful [25]quirky")

    nature_pick_1 = int(input("Pick Pokemon's Nature: "))
    if (nature_pick_1 == 1 or nature_pick_1 == 7 or nature_pick_1 == 13 or nature_pick_1 == 19 or nature_pick_1 == 25):
        atk_nature = 1
        def_nature = 1
        spec_atk_nature = 1
        spec_def_nature = 1
        speed_nature = 1
    if (nature_pick_1 == 2 or nature_pick_1 == 3 or nature_pick_1 == 4 or nature_pick_1 == 5):
        atk_nature = 1.1
    if (nature_pick_1 == 2):
        def_nature = 0.9
    elif (nature_pick_1 == 3):
        speed_nature = 0.9
    elif (nature_pick_1 == 4):
        spec_atk_nature = 0.9
    else:
        spec_def_nature = 0.9
    if (nature_pick_1 == 6 or nature_pick_1 == 8 or nature_pick_1 == 9 or nature_pick_1 == 10):
        def_nature = 1.1
    if (nature_pick_1 == 6):
        atk_nature = 0.9
    elif (nature_pick_1 == 8):
        speed_nature = 0.9
    elif (nature_pick_1 == 9):
        spec_atk_nature = 0.9
    else:
        spec_def_nature = 0.9
    if (nature_pick_1 == 11 or nature_pick_1 == 12 or nature_pick_1 == 14 or nature_pick_1 == 15):
        speed_nature = 1.1
    if (nature_pick_1 == 11):
        atk_nature = 0.9
    elif (nature_pick_1 == 12):
        def_nature = 0.9
    elif (nature_pick_1 == 14):
        speed_nature = 0.9
    else:
        spec_def_nature = 0.9
    if (nature_pick_1 == 16 or nature_pick_1 == 17 or nature_pick_1 == 18 or nature_pick_1 == 20):
        spec_atk_nature = 1.1
    if (nature_pick_1 == 16):
        atk_nature = 0.9
    elif (nature_pick_1 == 17):
        def_nature = 0.9
    elif (nature_pick_1 == 18):
        speed_nature = 0.9
    else:
        spec_def_nature = 0.9
    if (nature_pick_1 == 21 or nature_pick_1 == 22 or nature_pick_1 == 23 or nature_pick_1 == 24):
        spec_def_nature = 1.1
    if (nature_pick_1 == 16):
        atk_nature = 0.9
    elif (nature_pick_1 == 17):
        def_nature = 0.9
    elif (nature_pick_1 == 18):
        speed_nature = 0.9
    else:
        spec_atk_nature = 0.9

    print("[1] Attack         [2] Defense") 
    print("[3] Special Attack [4] Special Defense") 
    print("[5] Speed\n")
    opt = int(input("Which stat do you want to check? "))
    mod = 0
    if opt == 1:
        mod = atk_nature
    elif opt == 2:
        mod = def_nature
    elif opt == 3:
        mod = spec_atk_nature
    elif opt == 4:
        mod = spec_def_nature
    elif opt == 5:
        mod = speed_nature

    EV_Desired_Choice = int(input("Enter desired increase: "))

    print("This is the amount of needed EV for your pokemon: ",
            CalculateEv.Class_EV.desired(base, evv, ivv, opt, lvl, EV_Desired_Choice, mod))
    exit()

elif choice == 2:
    stats_name = [ "Hp", "Attack", "Defense", "Special Attack", "Special Defense", "Speed"]
    print("Welcome to Pokemon Calculator!\n")
    base = [6]
    ivv = [6]
    evv = [0, 0, 0, 0, 0, 0, 0]
    evs = 0
    pokemon = str(input("Enter Your Pokemon's Name: "))
    lvl = int(input("Enter Your Pokemon's Level: "))
    if (lvl < 0 or lvl > 100):
        print("Your Pokemon's Level Can only reach lvl max 100!")
        sleep(1)
        exit()
    print("[1]hardy   [2]lonely  [3]brave    [4]adamant  [5]naughty\n"
          "[6]bold    [7]docile  [8]relaxed  [9]impish   [10]lax\n"
          "[11]timid  [12]hasty  [13]serious [14]jolly   [15]naive\n"
          "[16]modest [17]mild   [18]quiet   [19]bashful [20]rash\n"
          "[21]calm   [22]gentle [23]sassy   [24]careful [25]quirky")

    nature_pick = int(input("Pick Pokemon's Nature: "))
    if (nature_pick == 1 or nature_pick == 7 or nature_pick == 13 or nature_pick == 19 or nature_pick == 25):
        atk_nature = 1
        def_nature = 1
        spec_atk_nature = 1
        spec_def_nature = 1
        speed_nature = 1
    if (nature_pick == 2 or nature_pick == 3 or nature_pick == 4 or nature_pick == 5):
        atk_nature = 1.1
    if (nature_pick == 2):
        def_nature = 0.9
    elif (nature_pick == 3):
        speed_nature = 0.9
    elif (nature_pick == 4):
        spec_atk_nature = 0.9
    else:
        spec_def_nature = 0.9
    if (nature_pick == 6 or nature_pick == 8 or nature_pick == 9 or nature_pick == 10):
        def_nature = 1.1
    if (nature_pick == 6):
        atk_nature = 0.9
    elif (nature_pick == 8):
        speed_nature = 0.9
    elif (nature_pick == 9):
        spec_atk_nature = 0.9
    else:
        spec_def_nature = 0.9
    if (nature_pick == 11 or nature_pick == 12 or nature_pick == 14 or nature_pick == 15):
        speed_nature = 1.1
    if (nature_pick == 11):
        atk_nature = 0.9
    elif (nature_pick == 12):
        def_nature = 0.9
    elif (nature_pick == 14):
        speed_nature = 0.9
    else:
        spec_def_nature = 0.9
    if (nature_pick == 16 or nature_pick == 17 or nature_pick == 18 or nature_pick == 20):
        spec_atk_nature = 1.1
    if (nature_pick == 16):
        atk_nature = 0.9
    elif (nature_pick == 17):
        def_nature = 0.9
    elif (nature_pick == 18):
        speed_nature = 0.9
    else:
        spec_def_nature = 0.9
    if (nature_pick == 21 or nature_pick == 22 or nature_pick == 23 or nature_pick == 24):
        spec_def_nature = 1.1
    if (nature_pick == 16):
        atk_nature = 0.9
    elif (nature_pick == 17):
        def_nature = 0.9
    elif (nature_pick == 18):
        speed_nature = 0.9
    else:
        spec_atk_nature = 0.9
    
    print("Input Your Pokemon's Base Stats")
    for x in range(1, 7):
        base.append(int(input("Input " + stat[x] + ": ")))

    print("Input IV's on each Stats")
    for y in range(1, 7):
        ivv.append(int(input("Input Your Pokemon's " + stat[y] + " IV: ")))
        if (ivv[y] < 0 or ivv[y] > 31):
            print("You can only set IVs from 0 to 31!")
            sleep(2)
            print("System is closing!")
            sleep(3)
    
EV_or_Stats = int(input("Input for [1] Single EV Stat or [2] All the stats?\n"))
if (EV_or_Stats == 1):
    print("Which Stat would you like to input?\n[1]HP [2]Attack [3]Defense [4]Spec Attack [5]Spec defense [6]Speed")
    Input_Choice_Stats = int(input("Choice: "))
    How_Much_EV = int(input("Input how much EV: "))
    if (Input_Choice_Stats < 0 or Input_Choice_Stats > 255):
        print("You can only set EVs from 0 to 255 and with a total of 510 EV!")
        sleep(2)
        print("System is closing!")
        sleep(3)
        exit()
    for p in range(1, 7):
        if (p == Input_Choice_Stats):
            evv.insert(p, How_Much_EV)
elif (EV_or_Stats == 2):
    print("Input EV's on each Stats")
    for z in range(1, 7):
        evv.append(int(input("Input " + stat[z] + " Ev: ")))
        if (evv[z] < 0 or evv[z] > 255):
            print("You can only set Evs from 0 to 255 and with a total of 510 Ev!")
            sleep(3)
            print("System is closing!")
            sleep(3)
            exit()
    evs = evs + evv[z]
    if (evs > 510):
        print("You can only set Evs to a total of 510 Ev!")
        sleep(3)
        print("System is closing!")
        sleep(3)
        exit()

else:
    print("Invalid Input!")
    exit()

print("Here's the stats of your Pokemon: " + pokemon)
print("HP: ", CalculateStat.Class_Status.hpReturn(base, ivv, evv, lvl))
print("Attack: ", CalculateStat.Class_Status.attackReturn(base, ivv, evv, lvl, atk_nature))
print("Defense: ", CalculateStat.Class_Status.defenseReturn(base, ivv, evv, lvl, def_nature))
print("Special Attack: ", CalculateStat.Class_Status.spattackReturn(base, ivv, evv, lvl, spec_atk_nature))
print("Special Defense: ", CalculateStat.Class_Status.spdefenseReturn(base, ivv, evv, lvl, spec_def_nature))
print("Speed: ", CalculateStat.Class_Status.speedReturn(base, ivv, evv, lvl, speed_nature))