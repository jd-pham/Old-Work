import random as ran


class Time: # object to store and manipulate time intervals
    def __init__(self, time_str): # time should be in hh:mm format
        if ':' not in time_str:
            raise Exception()

        self.time_str = time_str    # for visual representation
        temp_arr = time_str.split(':')
        self.hrs = int(temp_arr[0])
        self.mins = int(temp_arr[1])

    def __str__(self):
        return self.time_str

    def __gt__(self, other):
        return (self.hrs > other.hrs) or \
               (self.hrs == other.hrs and self.mins > other.mins)

    def __ge__(self, other):
        return (self.hrs >= other.hrs) or \
               (self.hrs == other.hrs and self.mins >= other.mins)


class Station:
    def __init__(self, id: int, name: str):
        self.station_id = id
        self.station_name = name

        # format should be -> time: train
        self.arrival_time = dict()

    def __str__(self):
        return self.station_name

    def show_arrival_times(self):
        for time, train in sorted(self.arrival_time.items()):
            print(f'{time}: {train}')


class Train:
    def __init__(self, id: int, name: str):
        self.train_id = id
        self.train_name = name
        self.route = Route(self)    # create a route for each train

    def add_to_route(self, station: Station, arrival: str) -> bool:
        return self.route.add_stop(station=station, arrival=arrival)

    def show_route(self):
        print(self.route)

    def __str__(self):
        return self.train_name


class Route:
    def __init__(self, train: Train):
        # format --- time: station_object
        self.schedule = dict()
        self.train = train   # route must be initialized with an existing train

    # return T/F depending on successful addition
    def add_stop(self, station: Station, arrival) -> bool:
        if arrival in station.arrival_time:     # check if time interval is already taken
            return False

        station.arrival_time[arrival] = self.train
        self.schedule[arrival] = station
        return True

    def __str__(self):
        if not self.schedule:
            return ''

        res = ''
        for time, station in sorted(self.schedule.items()): # sort by time
            res += f'{time}: {station}\n'
        return res


# helper function to generate id
def generate_random_id(id_length=10) -> int:
    return int(ran.random() * 10 ** id_length)


# helper function to generate list of train objects
def generate_trains(name_list: list) -> list:
    res = []

    for name in name_list:
        train_id = generate_random_id()
        res += [Train(id=train_id, name=f'{name} Train')]
    return res


# helper function to generate list of station objects
def generate_stations(station_names: list) -> list:
    res = []
    for station in station_names:
        res += [Station(id=generate_random_id(), name=station + ' Station')]
    return res


# helper function to assign train routes to stations randomly
def schedule_routes(trains: list,
                    stations: list,
                    times: list,
                    n: int):    # n == number of stops per train
    i = 0
    while i < n:
        for j, train in enumerate(trains):
            assigned_station = stations[int(ran.random() * len(stations))]
            possible_times = [t for t in times if t not in assigned_station.arrival_time]
            assigned_time = possible_times[int(ran.random() * len(possible_times))]
            train.add_to_route(station=assigned_station, arrival=assigned_time)
        i += 1


time_intervals = []
with open('time_intervals.txt', 'r') as ti:
    ti.seek(0)
    reader = ti.readlines()
    for line in reader:
        time_intervals += [Time(line.strip())]
    ti.close()

station_names = []
with open('5_stations.txt', 'r') as s:
    s.seek(0)
    reader = s.readlines()
    for line in reader:
        station_names += [line.strip()]
    s.close()

train_colors = []
with open('train_colors.txt', 'r') as tc:
    tc.seek(0)
    reader = tc.readlines()
    for line in reader:
        train_colors += [line.strip()]
    tc.close()


trains = generate_trains(train_colors)
stations = generate_stations(station_names)

schedule_routes(trains=trains, stations=stations, times=time_intervals, n=10)

# for t in trains:
#     print(t.route)
# for s in stations:
#     print(s)
#     s.show_arrival_times()
#     print('\n\n\n\n')















