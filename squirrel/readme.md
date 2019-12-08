# Squirrel in Central Park
>Project Group www, Section 2
>UNI: yf2510
![](https://img.theculturetrip.com/1440x/wp-content/uploads/2018/06/34752989530_da5858956a_h.jpg)

## Goal
The goal for this project is to build an application for keeping track of all the known squirrels. This application includes data for each of the 3,023 sightings, including location coordinates, age, primary and secondary fur color, elevation, activities, communications, and interactions between squirrels and with humans in Central Park, New York. By using this data, this application can display the location of the squirrel sightings on an OpenStreets map and the charateristics of all squirrel sightings with links to edit each.
## The link to the server running our application
    https://yf2510.appspot.com/map/

## Data source for download: 
 https://data.cityofnewyork.us/api/views/vfnx-vebw/rows.csv?accessType=DOWNLOAD

## Functions this application:
* 1
  * displays the location of the squirrel sightings 
    https://yf2510.appspot.com/map/

* 2
  * add squirrel sightings
    https://yf2510.appspot.com/sightings/add/

* 3
  * edit squirrel sightings
    https://yf2510.appspot.com/sightings/

* 4
  * check general stats about the sightings
    https://yf2510.appspot.com/sightings/stats/

* 5 
  * import csv into app
```sh
python manage.py import_squirrel_data /path/to/file.csv
```
* 6
  * export csv into app
```sh
python manage.py export_squirrel_data /path/to/file.csv
```

## set up
* install Django
```sh
pip install -U pip
pip install Django
```
* install Pandas
```sh
pip install pandas
```

