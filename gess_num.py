import random




print("think about ... ")

ans = random.randint(1, 100)

print()
print("enter youre gess: ")
gess = -1
etem_caunt = 0


while gess != ans:
    etem_caunt += 1
    gess = int(input())
    if gess > ans:
        print("to much, its youre ", etem_caunt, " etempt")
    elif gess < ans:
        print("to litel", etem_caunt, " etempt")
    
    if etem_caunt == 5:
        print("you run of etemts \n >> you lose")
        break

if etem_caunt < 5:
    print(" >> you won!")