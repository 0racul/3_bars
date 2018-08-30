import json
import math
import argparse

def load_data(filepath):
    with open(filepath, "r") as file:
        data_from_json = json.loads(file.read())
    return data_from_json


def get_biggest_bar(loaded_bars):

    bar_names = []
    bar_seats = []
    max_seat = 0

    for cut_bar_number in range(len(loaded_bars)):

        bar = loaded_bars[cut_bar_number]
        bar_seats.append(bar.get("SeatsCount"))
        max_seat = max(bar_seats)
        bar_names.append(bar.get("Name"))

    cut_bars = list(zip(bar_names, bar_seats))

    for cut_bar_number in range(len(cut_bars)):
        cut_bar = cut_bars[cut_bar_number]
        if cut_bar[1] == max_seat:
            return cut_bar
        else:
            continue


def get_smallest_bar(loaded_bars):

    bar_names = []
    bar_seats = []
    min_seat = 0

    for loaded_bar_number in range(len(loaded_bars)):

        bar = loaded_bars[loaded_bar_number]
        bar_seats.append(bar.get("SeatsCount"))
        min_seat = min(bar_seats)
        bar_names.append(bar.get("Name"))

    cut_bars = list(zip(bar_names, bar_seats))

    for cut_bar_number in range(len(cut_bars)):

        cut_bar = cut_bars[cut_bar_number]
        if cut_bar[1] == min_seat:
            return cut_bar
        else:
            continue


def find_nearest_bar(loaded_bars, current_longitude, current_latitude):

    bars_with_distances = []
    distances = []

    for bar_number in range(len(loaded_bars)):

        current_bar = loaded_bars[bar_number]
        bar_latitude = float(current_bar["Latitude_WGS84"])
        bar_longitude = float(current_bar["Longitude_WGS84"])

        distance_to_bar = math.sqrt((bar_latitude - current_latitude)**2 +
                                    (bar_longitude - current_longitude)**2)

        bars_with_distances.append({"Name": current_bar["Name"],
                                    "Latitude": bar_latitude,
                                    "Longitude": bar_longitude,
                                    "Address": current_bar["Address"],
                                    "Distance": distance_to_bar})
        distances.append(bars_with_distances[bar_number]["Distance"])

    min_distance = min(distances)
    needed_bar_index = distances.index(min_distance)
    needed_bar = bars_with_distances[needed_bar_index]

    return needed_bar


def parser_parser():
    global parser
    parser = argparse.ArgumentParser()
    parser.add_argument("-path", "--path_to_file", help="Path to the json file")
    parser.add_argument("-cur_long", "--current_longitude", help="Your current longitude - only digits pls")
    parser.add_argument("-cur_lat", "--current_latitude", help="Your current latitude - only digits pls")

    pars_result = parser.parse_args()

    return vars(pars_result)


if __name__ == "__main__":

    current_longitude = 0
    current_latitude = 0

    pars_result = parser_parser()

    path_to_file = pars_result.get("path_to_file")
    longitude = float(pars_result.get("current_longitude"))
    latitude = float(pars_result.get("current_latitude"))

    loaded_bars = load_data(path_to_file)

    find = find_nearest_bar(loaded_bars, longitude, latitude)
    biggest = get_biggest_bar(loaded_bars)
    smallest = get_smallest_bar(loaded_bars)

#    print("Biggest bar in Moscow " + str(biggest))
#    print("Smallest bar " + str(smallest))
#    print("Nearest bar to your loc " + str(find))


    print("Biggest bar in Moscow {}, Smallest bar {},Nearest bar to your loc {}".format(str(biggest), str(smallest), str(find)))
