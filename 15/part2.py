import multiprocessing as mp
import time

def run_task(i, target_range, lines, box_limit):
    start, end = target_range
    for row in range(start, end):
        row_covered = {}
        for line in lines:

            sensor, beacon = parse_line(line.split(" "))
            radius = manhat(sensor, beacon)
            start_pos = tuple(map(lambda x: x - radius, sensor))
            end_pos = tuple(map(lambda x: x + radius, sensor))

            for col in range(start_pos[0], end_pos[0] + 1):
                mandist = manhat(sensor, (col, row))
                if mandist <= radius:
                    if col not in row_covered and (col, row) != beacon:
                        row_covered[col] = 1
        
        print(row, len(row_covered))
        # end = (time.time() / 1e9)
        # print(start - end)
            
    return

def parse_line(tokens):
    sensor_x = int(tokens[2].replace(",", "").split("=")[-1].strip())
    sensor_y = int(tokens[3].replace(":", "").split("=")[-1].strip())

    beacon_x = int(tokens[8].replace(",", "").split("=")[-1].strip())
    beacon_y = int(tokens[9].split("=")[-1].strip())

    return (sensor_x, sensor_y), (beacon_x, beacon_y)

def manhat(a, b):
    return (abs(a[1] - b[1]) + abs(a[0] - b[0]))

if __name__ == "__main__":
    with open("./data.txt", "r") as file:
        lines = file.readlines()
        box_limit = 4_000_000

        # threads = []
        # step = box_limit // 20
        # for i in range(0, box_limit, step):
        #     print("Thread ", i // step, " started")
        #     target_range = (i, i + step)
        #     new_thread = mp.Process(target=run_task, args=(i // step, target_range, lines, box_limit))
        #     new_thread.start()
        
        # for thread in threads:
        #     thread.join()
        sensor_distance = {}
        for line in lines:
            sensor, beacon = parse_line(line.split(" "))
            radius = manhat(sensor, beacon)
            sensor_distance[(sensor[0], sensor[1])] = radius

        x_mult = 4_000_000
        visited = set()
        for sensor, radius in sensor_distance.items():
            sx, sy = sensor

            for side in range(4):
                for i in range(radius + 1):
                    if side == 0:
                        cx = sx + radius + 1 - i
                        cy = sy + i
                    elif side == 1:
                        cx = sx - i
                        cy = sy + radius + 1 - i
                    elif side == 2:
                        cx = sx - radius - 1 + i
                        cy = sy - i
                    else:
                        cx = sx + i
                        cy = sy - radius - 1 + i
                    
                    if (0 <= cx <= box_limit) and (0 <= cy <= box_limit) and (cx, cy) not in visited:
                        found = all((abs(cx - otherx) + abs(cy - othery)) > other_distance 
                                for (otherx, othery), other_distance in sensor_distance.items())
                    
                    if found:
                        print("Found Solution")
                        print((x_mult * cx) + cy)
                        exit()
                    else:
                        visited.add((cx, cy))
