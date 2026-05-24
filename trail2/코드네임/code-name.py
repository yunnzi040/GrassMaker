MAX_N = 5

codenames = []
scores = []
for _ in range(MAX_N):
    codename, score = input().split()
    codenames.append(codename)
    scores.append(int(score))

# Please write your code here.
class Agents:
    def __init__(self, codename, score):
        self.c = codename
        self.s = score

agents = [Agents(codenames[i], scores[i]) for i in range(5)]

min_agent = agents[0]

for i in range(1, 5):
    if agents[i].s < min_agent.s:
        min_agent = agents[i]

print(f"{min_agent.c} {min_agent.s}")