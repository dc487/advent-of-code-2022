import pathlib

def load_input():
    return pathlib.Path("./input.txt").read_text().strip("\n").splitlines()

def could_be_beacon(x, y, sensors, max_size):
    if x < 0 or y < 0 or x > max_size or y > max_size:
        return False

    for sensor in sensors:
        (sensor_x, sensor_y, beacon_x, beacon_y, distance) = sensor

        actual_distance = abs(sensor_x - x) + abs(sensor_y - y)

        if actual_distance <= distance:
            return False


    print('Beacon located at: ' + str(x) + ', ' + str(y))
    print(x * 4000000 + y)
    return True

if __name__ == "__main__":
    input = load_input()

    sensors = []

    for line in input:
        parts = line[12:].split(": closest beacon is at x=")
        sensor_parts = parts[0].split(", y=")
        sensor_x = int(sensor_parts[0])
        sensor_y = int(sensor_parts[1])

        beacon_parts = parts[1].split(", y=")
        beacon_x = int(beacon_parts[0])
        beacon_y = int(beacon_parts[1])

        distance = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)

        sensors.append((sensor_x, sensor_y, beacon_x, beacon_y, distance))

    sensed_x_positions = set()
    beacon_x_positions = set()

    row_number = 2000000

    for sensor in sensors:
        (sensor_x, sensor_y, beacon_x, beacon_y, distance) = sensor

        if beacon_y == row_number:
            beacon_x_positions.add(beacon_x)

        if abs(row_number - sensor_y) <= distance:
            sensed_x_positions.add(sensor_x)
            row_width = distance - abs(row_number - sensor_y)
            if row_width > 0:
                for x in range(row_width):
                    sensed_x_positions.add(sensor_x + x + 1)
                    sensed_x_positions.add(sensor_x - x - 1)

    invalid_x_positions = sensed_x_positions - beacon_x_positions
    print(len(invalid_x_positions))

    max_size = 4000000

    beacon_found = False
    beacon_x = 0
    beacon_y = 0

    for sensor in sensors:
        (sensor_x, sensor_y, beacon_x, beacon_y, distance) = sensor

        if beacon_found:
            break

        # loop over all points outside the sensor, and see if those points are covered by any other sensor (or outside the search)
        for i in range(distance + 2):

            x = sensor_x + i
            y = sensor_y + distance + 1 - i
            if could_be_beacon(x, y, sensors, max_size):
                beacon_found = True
                break
            
            x = sensor_x - i
            y = sensor_y + distance + 1 - i
            if could_be_beacon(x, y, sensors, max_size):
                beacon_found = True
                break
            
            x = sensor_x + i
            y = sensor_y - distance - 1 + i
            if could_be_beacon(x, y, sensors, max_size):
                beacon_found = True
                break
            
            x = sensor_x - i
            y = sensor_y - distance - 1 + i
            if could_be_beacon(x, y, sensors, max_size):
                beacon_found = True
                break


            