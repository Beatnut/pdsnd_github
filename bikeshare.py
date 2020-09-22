"""Refactoring"""

import time
import pandas as pd
import numpy as np


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }




def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! It\'s me Oliver. You know may now me from movies like Bikeshare what a blast.. But let\'s explore some US bikeshare data!')

    while True:
        start = input('You want to have some fun? \n "yes" or "no" ?\n')
        if start == 'yes':
            print('yippiiie')
        if start == 'no':
            print('We all want fun...Try again:\n')
            continue
        else:
            break
    while True:
          city = input("Choose your city new york city, chicago or washington?\n").lower()

          if city not in ("new york city", "chicago", "washington"):
            print("What was it again? Tell me your city")
            continue
          else:
            break


    while True:
          month = input("Which month would you like to filter by? January, February, March, April, May, June or type 'all' if you do not have any preference?\n").lower()
          if month not in ("january", "february", "march", "april", "may", "june", "all"):
            print("Sorry, I didn't catch that. Try again.")
            continue
          else:
            break


    while True:
          day = input("Which day you want to look at: Monday, Tuesday, Wednesday, Thursday, Friday or Saturday? You can type also 'all'.\n").lower()
          if day not in ("sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "all"):
            print("Sorry, I didn't catch that. Try again.")
            continue
          else:
            break

    print('.'*40)
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


#load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

#convert teh start time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

#extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

# filter by month if applicable
    if month != 'all':
 # use the index of months List to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
#filter by month to create the new dataframe
        df = df[df['month'] == month]

 # filter by day of week if applicable
    if day != 'all':
 # filter by day of wekk to create new df
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('Most popular month:', popular_month)
    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('Most popular day:', popular_day)
    # TO DO: display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print('Most popular Start Hour:', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start = df['Start Station'].mode()[0]

    # TO DO: display most commonly used end station
    popular_end = df['End Station'].mode()[0]

    # TO DO: display most frequent combination of start station and end station trip
    most_freq_station_comb = df['Start Station'] + ' to ' + df['End Station']
    most_station =  most_freq_station_comb.mode()[0]

    print('Most popular trip:', most_station)
    print('Most popular Start:', popular_start)
    print('Most popular End:', popular_end)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-.-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = sum(df['Trip Duration'])
    print("Total travel time:", total_travel/86400, "Days")


    mean_travel = df["Trip Duration"].mean()
    print("Mean travel time:", mean_travel/60, "Minutes")

    # TO DO: display mean travel time


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("\nUser stats:\n", user_types)
    # TO DO: Display counts of gender
    if 'Gender' not in df:
        print('No Gender data for this city.')
    else:
        gender = df['Gender'].value_counts()
        print("\nGender stats:", gender)

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' not in df:
        print("\nNo Birth Year data for this city.")
    else:
        earliest = df['Birth Year'].max()
        print("\nyear of birth of the youngest driver:",earliest)

        #worked not properly
        #most_recent = df.at[0, 'Birth Year']
        #print("\nMost recent year of birth:", most_recent)
        most_recent = df['Birth Year'].iloc[0]
        print("\nMost recent year of birth:", most_recent)

        most_year = df['Birth Year'].mode()[0]
        print("\nMost common year of birth:", most_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    """Displays raw data of bikeshare ."""

    row1 = 0
    row2 = 5
    raw_data = input("\n Wanna see the raw data? Type 'yes' or 'no'\n").lower()
    while True:
        if raw_data == 'no':
            return
        if raw_data == 'yes':
            print(df.iloc[row1: row2])
            row1 += 5
            row2 += 5

        raw_data = input("\n Wanna see 5 more lines? Type 'yes' or 'no'\n").lower()

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        #new
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
