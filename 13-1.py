
with open("13.txt") as f:
    earliest = int(f.readline())
    buses = [int(x) for x in f.readline().split(',') if x != 'x']

i = earliest
stopped = {}
while len(stopped) < len(buses):
    for idx, b in enumerate(buses):
        if idx in stopped: continue
        if i % b == 0:
            stopped[idx] = i
    i += 1

#print(stopped)

best_bus = min(stopped.values())
best_bus_id = [x for x, v in stopped.items() if v == best_bus][0]
#print(best_bus, best_bus_id, buses[best_bus_id])
print('part1', (best_bus - earliest) * buses[best_bus_id])
