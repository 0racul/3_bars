import json
import math


def load_data(filepath):
    with open(filepath, 'r') as f:
        data = json.loads(f.read())
    return data

def biggest_bar(loaded_bars):

    bar_names = []
    bar_seats = []
    max_seat = 0

    for i in range(len(loaded_bars)):

        bar = loaded_bars[i]
        bar_seats.append(bar.get("SeatsCount"))
        max_seat = max(bar_seats)
        bar_names.append(bar.get("Name"))

    cut_bars = list(zip(bar_names, bar_seats))

    for i in range(len(cut_bars)):
        cut_bar = cut_bars[i]
        if cut_bar[1] == max_seat:
            return cut_bar
        else:
            continue


def smallest_bar(loaded_bars):

    bar_names = []
    bar_seats = []
    min_seat = 0

    for i in range(len(loaded_bars)):

        bar = loaded_bars[i]
        bar_seats.append(bar.get("SeatsCount"))
        min_seat = min(bar_seats)
        bar_names.append(bar.get("Name"))

    cut_bars = list(zip(bar_names, bar_seats))

    for i in range(len(cut_bars)):

        cut_bar = cut_bars[i]
        if cut_bar[1] == min_seat:
            return cut_bar
        else:
            continue



def find_bar(loaded_bars, current_longitude, current_latitude):

    bars_with_distances = []
    distances = []

    for i in range(len(loaded_bars)):

        current_bar = loaded_bars[i]
        bar_latitude = float(current_bar["Latitude_WGS84"])
        bar_longitude = float(current_bar["Longitude_WGS84"])
        distance_to_bar = math.sqrt((bar_latitude - current_latitude)**2 + (bar_longitude - current_longitude)**2)
        bars_with_distances.append({"Name": current_bar["Name"], "Latitude": bar_latitude, "Longitude": bar_longitude, "Address":current_bar["Address"], "Distance":distance_to_bar})
        distances.append(bars_with_distances[i]["Distance"])


    min_distance = min(distances)
    needed_bar_index = distances.index(min_distance)
    needed_bar = bars_with_distances[needed_bar_index]

    return needed_bar


if __name__ == '__main__':

    print("file path pls \n")

    current_longitude = 0
    current_latitude = 0
    dir_path = input()

    print("Input your place coordinates, longitude and latitude\n")

    longitude = float(input(current_longitude))
    latitude = float(input(current_latitude))

    loaded_bars = load_data(dir_path)

    find = find_bar(loaded_bars, longitude, latitude)
    biggest = biggest_bar(loaded_bars)
    smallest = smallest_bar(loaded_bars)

    print("Biggest bar in Moscow  " + str(biggest) + "\nSmallest bar in Moscow  " + str(smallest) + "\nNearest bar to your location " + str(find))

