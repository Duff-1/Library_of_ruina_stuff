import random, pygame, dice

def clashing():
    count = 0
    unop = 0
    p1_rolls = dice.main()
    p2_rolls = dice.main()
    if len(p1_rolls) > len(p2_rolls):
        unop = 1
        for i in range(len(p2_rolls)):
            if p1_rolls[i] > p2_rolls[i]:
                print(f"p1 outrolled {p2_rolls[i]} with {p1_rolls[i]}")
            elif p1_rolls[i] < p2_rolls[i]:
                print(f"p2 outrolled {p1_rolls[i]} with {p2_rolls[i]}")
            else:
                print("clash tie")
            count += 1
    else:
        unop = 2
        for i in range(len(p1_rolls)):
            if p1_rolls[i] > p2_rolls[i]:
                print(f"p1 outrolled {p2_rolls[i]} with {p1_rolls[i]}")
            elif p1_rolls[i] < p2_rolls[i]:
                print(f"p2 outrolled {p1_rolls[i]} with {p2_rolls[i]}")
            else:
                print("clash tie")
            count += 1
    
    print(p1_rolls, p2_rolls)

    if len(p1_rolls) == len(p2_rolls):
        pass
    else:
        if unop == 1:
            for i in range(count,len(p1_rolls)):
                print(f"p1 unopposed {p1_rolls[i]}")
        else:
            for i in range(count,len(p2_rolls)):
                print(f"p2 unopposed {p2_rolls[i]}")



clashing()
            