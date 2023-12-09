from pathlib import Path

data = """\
Time:      7  15   30
Distance:  9  40  200
"""
data = Path("2023/day6.txt").read_text()
time_line, dist_line = data.splitlines()
times = tuple(int(t) for t in time_line.split(":")[1].strip().split())
dists = tuple(int(t) for t in dist_line.split(":")[1].strip().split())
times = tuple(int(t) for t in time_line.split(":")[1].replace(" ", "").split())
dists = tuple(int(t) for t in dist_line.split(":")[1].replace(" ", "").split())

ret = 1
for time, dist in zip(times, dists):
    beat = 0
    for speed in range(time):
        remaining_time = time - speed
        traveled = speed * remaining_time
        if traveled > dist:
            beat += 1
    ret *= beat

print(ret)
