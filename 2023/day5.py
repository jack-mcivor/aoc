from pathlib import Path

raw = """\
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
"""
# raw = Path("2023/day5.txt").read_text()
data = raw.split('\n\n')
seeds_data = data[0]
assert seeds_data.startswith('seeds:')
seeds = tuple(int(n) for n in seeds_data.split(': ', maxsplit=1)[1].split())

maps: list[list[tuple[int, int, int]]] = []

for i, raw_map_data in enumerate(data[1:]):
    maps.append([])
    map_data = raw_map_data.splitlines()
    map_type = map_data[0]
    for map_line in map_data[1:]:
        dest_range_start_, src_range_start_, span_ = map_line.split()
        dest_range_start = int(dest_range_start_)
        src_range_start = int(src_range_start_)
        span = int(span_)
        maps[i].append((src_range_start, dest_range_start, span))


for i in range(len(maps)):
    maps[i] = tuple(maps[i])
maps = tuple(maps)

from rich.progress import track

def find_pos(pos, maps):
    # step through each map till the end
    # assume we can compose adjacent maps
    for mappings in maps:
        for src, dest, span in mappings:
            if src <= pos <= (src + span):
                pos = dest + (pos - src)
                # found, no need to check others in this map
                break
            # if nothing is found, will keep same position
    return pos

final_positions = []
for seed in seeds:
    pos = seed
    final_position = find_pos(seed, maps)
    final_positions.append(final_position)

print(min(final_positions))

# part 2
final_positions = []
seed_range_starts = seeds[::2]
seed_spans = seeds[1::2]

for seed_range_start, seed_span in zip(seed_range_starts, seed_spans, strict=True):
    for seed in track(range(seed_range_start, seed_range_start+seed_span+1), total=seed_span):
        pos = seed
        final_pos = find_pos(seed, maps)
        final_positions.append(final_pos)

print(min(final_positions))
