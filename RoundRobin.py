team=[]
while True:
    q=input('Enter team name:')
    if q=='q' or q=='Q':
        break
    team.append(q)

sch=[]
for i in team:
    for j in range(len(team)):
        if i==team[j]:
            continue
        else:
            print(str(i)+' vs '+team[j])
