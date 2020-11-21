import random

history=[]
m='alive'
x=0
def challenge_1():
    global history
    global history_list
    print('Suddenly you are attacked by a bear.')
    print('You start to run but the bear goes after your son Jimmy.')
    print('You have 2 options.')
    print('a. Get your rifle and kill the bear.')
    print('b. Run and leave Jimmy behind.')
    x=input('What will you choose? ')
    if x=='a':
        print('You kill the bear and survive.')
        history.append('1')
        return 'alive'
    elif x=='b':
        print('You run but the bear chases you down and kills you and Jimmy anyway.')
        history.append('D')
        return 'dead'
    else:
        print('You fail to choose quickly and die.')
        history.append('D')
        return 'dead'


def challenge_2():
    global history
    global history_list
    print('On your way you meet a mystic.')
    print('He tells you to choose a number between 1 and 10.')
    print('If you choose the unlucky number, you will die.')
    x=input('What will you choose? ')
    if int(x)<1 or int(x)>10:
        print('You disobeyed the mystic and died.')
        history.append('D')
        return 'dead'
    elif x=='7':
        print('Unfortunately, that was the unlucky number, and the mystic used his magic to kill you.')
        history.append('D')
        return 'dead'
    else:
        print('You chose a safe number and survived.')
        history.append('2')
        return 'alive'

def challenge_3():
    global history
    global history_list
    print('On your way you step in an enchanted area.')
    print('At the center you see a table with two chalices full of wine on it.')
    print('A note attached to the table tells you that one of them is poisoned.')
    print('The note informs you that you need to drink from the safe one to escape the enchantment.')
    print('a. Left chalice.')
    print('b. Right chalice.')
    x=input('Which one will you choose? ')
    if x=='b':
        print('You picked the poisoned wine and died.')
        history.append('D')
        return 'dead'
    elif x=='a':
        print('You picked the safe wine and survived. Hooray!')
        history.append('3')
        return 'alive'
    else:
        print('You tried to run and were killed by the enchantment.')
        history.append('D')
        return 'dead'

print("You are a farmer on the way to Oregon with his family.")
print('')
while m=='alive' and x<5:
    u=random.randint(1,3)
    if u==1:
        m=challenge_1()
    elif u==2:
        m=challenge_2()
    elif u==3:
        m=challenge_3()
    x=x+1
    print('')

if m=='alive':
    print("Congratulations! You reached Oregon!")
    print('You lived happily ever after ...')
    history.append('W')
else:
    print("GAME OVER")

with open('history.csv','a') as w:
    w.write(" ### ")
    for i in history:
        w.write(i+" ")
    w.write("### ")