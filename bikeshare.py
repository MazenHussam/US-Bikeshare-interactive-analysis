import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.core.algorithms import value_counts

CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York': 'new_york_city.csv',
              'Washington': 'washington.csv' }

# Month, city and day getter functions
def get_month():
    month = input ("Which month would you like to analyze from [all, january, february, ... , june]\n")
    month= month.title()
    return month
def get_city():
    city = input("Which of this cities Chicago, New york, Washington you want to analyze? \n")
    city= city.title()
    return city
def get_day():
    day = input ("Which day would you like to analyze from [all, sunday, monday, ... , saturday]\n")
    day = day.title()
    return day

def get_filters():
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = get_city()
    cities = ['Chicago','New York', 'Washington']
    while (city not in cities):
         print('Please enter a vaild input \n')
         city = get_city()
    # get user input for month (all, january, february, ... , june)
    month = get_month()
    months = ['All','January','February','March','April','May','June']
    while(month not in months):
        print('Please enter a vaild input \n')
        month = get_month()
    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = get_day()
    days = ['All','Monday', 'Tuesday', 'Wednesday', 'Thrusday', 'Friday', 'Sunday','Saturday']
    while(day not in days):
        print('Please enter a vaild input \n')
        day = get_day()

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df= pd.read_csv(CITY_DATA[city])
    df["Start Time"]= pd.to_datetime(df["Start Time"])

    df['month']=df['Start Time'].dt.month_name()
    df['day']=df['Start Time'].dt.day_name()

    if month != 'All':
        df = df[df['month']== month]
    
    if day != 'All':
        df = df[df['day']== day]

    return df

def raw_data(df):
    answer = input ("Would you like to view a perview of the raw data before calculating the statistics? \nYes/No \n")
    answer = answer.lower()
    answers= ['yes','no']
    while answer not in answer:
        answer = input('Please enter a vaild input \n')
    if answer == 'yes':
        #to display all the columns in dataframe head
        pd.set_option("display.max_columns", None)
        print(df.head(5))
    else: print("skipping....")

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print("The most common month is ",df['month'].value_counts().idxmax())

    # display the most common day of week

    print("The most common day of week is ",df['day'].value_counts().idxmax())


    # display the most common start hour
    df['Start Hour']=df['Start Time'].dt.hour
    print("The most common hour of the day is ",df['Start Hour'].value_counts().idxmax())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print("The most common used start station is ",df['Start Station'].value_counts().idxmax(),)

    # display most commonly used end station
    print("The most common used end station is ",df["End Station"].value_counts().idxmax())

    # display most frequent combination of start station and end station trip
    print("The most used start station and end station trip is ", df.groupby(['Start Station','End Station']).size().idxmax())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print("Total travel duration = ",df['Trip Duration'].sum(),' minutes')


    # display mean travel time
    print('The average travel time is ', df['Trip Duration'].mean(), ' minutes')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print("The count of user type:\n",df['User Type'].value_counts())
    print('~'*40)
    # Display counts of gender
    if city != 'Washington':
        df['Gender'].value_counts().plot(kind='barv')
        plt.show()
        # gender = df['Gender'].value_counts()
        # plt.pie(gender)
        print('The count of users gender:\n',df['Gender'].value_counts())
        print('~'*40)
    # Display earliest, most recent, and most common year of birth
        print('The minimum year of birth for the user is ', df['Birth Year'].min(),'\n')
        print('The maximum year of birth for the user is ', df['Birth Year'].max(),'\n')
        print('The most common year of birth is ', int(df['Birth Year'].value_counts().idxmax()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        raw_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
