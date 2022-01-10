# DataScience-Project1

### Goal
The goal of this assignment is to familiarize you with the Python programming language and also expose you to real data.

### What to do -- bike.py
You are asked to complete a Python program, called `bike_pitt.py` that will access live data from the [HealthyRidePGH website](https://healthyridepgh.com/) and provide answers to specific queries about shared bike availability in the Pittsburgh region.

The program conatins a class, `Bike`, that has three arguments in its constructor, `baseURL`, `station_info` and `station_status`. These arguments are used to define URLs for specific data feeds, namely information about individual stations and the status of every station. You can create an instance of the `Bike` class by calling its constructor with appropriate URL fragments, and call its methods to run the different parts of the assignment.

### Method #1: Total bikes available
The method `total_bikes` will compute and return how many bikes are currently available over all stations in the entire HealthRidePGH network.

Sample invocation:
```
result = instance.total_bikes()
```

The variable `result` should have an **integer** value like `123`.

### Method #2: Total docks available
The method `total_docks` will compute and return how many docks are currently available over all stations in the entire HealthRidePGH network.

Sample invocation:
```
result = instance.total_docks()
```

The variable `result` should have an **integer** value like `123`.

### Method #3: Percentage of docks available in a specific station
The method `percent_avail` will compute and return how many docks are currently available for the specified station as a percentage over the total number of bikes and docks available. In this case, the station_id is given as a parameter.

Sample invocation:
```
result = instance.percent_avail(342885)
```

The variable `result` should have a **string** value like `76%`.

In our example, the num_bikes_available was 4, the num_docks_available was 13, so the percent available was 13/(4+13), i.e., 76%. You should appropriately round the percentage to be an integer. To simplify things, always round down (floor), i.e., return the highest integer that is not greater than the number you try to round. Also, keep in mind that the `%` sign follows the number without any spaces. Finally, if the station ID is invalid, the method should return an empty string.

### Method #4: Names of three closest HealthyRidePGH stations.
The method `closest_stations` will return the station_ids and the names of the three closest HealthyRidePGH stations based just on latitude and longtitude (of the stations and of the specified location). The first parameter is the latitude and the second parameter is the longtitude.

Sample invocation:
```
result = instance.closest_stations(40.444618, -79.954707)
```

The variable `result` should have a **dictionary** value of **strings** mapped to **strings** like `{'342885': 'Schenley Dr at Schenley Plaza (Carnegie Library Main)', 342887: 'Fifth Ave & S Dithridge St', 342882: 'Fifth Ave & S Bouquet St'}`.

Note that in order to compute distances between two points, you must use the provided `distance()` method of the class. The `distance` method takes four arguments, `lat1`, `lon1`, `lat2` and `lon2` that correspond to two latitude-longitude coordinate pairs, and returns the distance between the two points.

### Method #5: Name of the closest HealthyRidePGH station with available bikes
The method `closest_bike` will return the station_id and the name of the closest HealthyRidePGH station that has available bikes, given a specific latitude and longitude. The first parameter is the latitude and the second parameter is the longitude.

Sample invocation:
```
result = instance.closest_bike(40.444618, -79.954707)
```

The variable `result` should have a **dictionary** value of **strings** mapped to **strings** like `{'342887': 'Fifth Ave & S Dithridge St'}`. The dictionary must have a single item that corresponds to the closest station.


### Method #6: The number of bikes available at a bike station 
The method `station_bike_avail` will return the station_id and the number of bikes available at the station, given a specific latitude and longitude. The first parameter is the latitude and the second parameter is the longitude.

Sample invocation:
```
result = instance.station_bike_avail(40.444618, -79.954707)
```

The variable `result` should have a **dictionary** value of **integers** mapped to **strings** like `{'342887': 4}`. The dictionary must have a single item that corresponds to the station with the exact coordinates. In this example, the result is the station with ID 342887 that has 4 bikes available. Also, if a station with the exact given coordinates doesn't exist, you must return an empty dictionary.
