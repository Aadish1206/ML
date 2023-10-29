from collections import deque

def predictPartyVictory(senate):
    radiant = deque()
    dire = deque()
    n = len(senate)

    
    for i, party in enumerate(senate):
        if party == 'R':
            radiant.append(i)
        else:
            dire.append(i)

    while radiant and dire:
        r = radiant.popleft()
        d = dire.popleft()

        
        if r < d:
            radiant.append(r + n)
        else:
            dire.append(d + n)

    return "Radiant" if radiant else "Dire"


senate = "RD"
result = predictPartyVictory(senate)
print(result)
