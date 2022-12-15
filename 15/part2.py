def parse_line(tokens):
    sensor_x = int(tokens[2].replace(",", "").split("=")[-1].strip())
    sensor_y = int(tokens[3].replace(":", "").split("=")[-1].strip())

    beacon_x = int(tokens[8].replace(",", "").split("=")[-1].strip())
    beacon_y = int(tokens[9].split("=")[-1].strip())

    return (sensor_x, sensor_y), (beacon_x, beacon_y)

def manhat(a, b):
    return (abs(a[1] - b[1]) + abs(a[0] - b[0]))

with open("./test.txt", "r") as file:
    lines = file.readlines()
    row_covered = {}
    box_limit = 4_000_000

    for line in lines:
        sensor, beacon = parse_line(line.split(" "))
        radius = manhat(sensor, beacon)
        start_pos = tuple(map(lambda x: x - radius, sensor))
        end_pos = tuple(map(lambda x: x + radius, sensor))
        row = target_row

        for col in range(start_pos[0], end_pos[0] + 1):
            # print(col, start_pos[0], end_pos[0])
            mandist = manhat(sensor, (col, row))
            if mandist <= radius and row == target_row:
                if col not in row_covered and (col, row) != beacon:
                    row_covered[col] = 1

    print(len(row_covered.keys()))

