import requests

# TODO Update config, refactor get functions 

def get_theatres():
    url = "https://www.cineplex.com/api/v1/theatres?language=en-us&range=100000&skip=0&take=1"
    response = requests.get(url).json()
    theatres_data = response['data']
    return theatres_data


def get_is_event():
    for film in films:
        if film['isEvent'] == True:
            is_event_yes_lst.append(film)
        else: 
            pass
    return is_event_yes_lst

# Consider pulling only isEvent='true' (type str)
def get_films():
    url = 'https://www.cineplex.com/api/v1/movies?language=en-us&marketLanguageCodeFilter=true&movieType=1&showTimeType=0&showtimeStatus=0&skip=0&take=1000'
    response = requests.get(url).json()
    films_data = response['data']
    return films_data

def make_dates_lst():
    pass
    # get currentdate add 4 weeks
    # return array of dates

# FYI date argument is in form yyyy-mm-dd
def get_showtimes(locationId, filmId, date):
    pass
    # for film in films
    # check if film is screening at the list of locations found in theatres_data
    # if yes, check for showtimes for each day in array of dates
    # maybe write to a dictionary
    # Example
    # [{film_name: 'spirited away', 
    #    theatre_name 'yonge_dundas':
    #        showtimes:['date and time, date and time]}];

def make_summary():
    pass

def main():
    get_theatres()
    get_films()
    print(make_summary())

if __name__ == "__main__":
    main()
