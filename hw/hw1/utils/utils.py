import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd

# Format of the csv file:
# Date,Bathroom,Living Room,Kitchen
# 01-01-23,30.4,30.22,29.73

# Да се генерира изображение на линеен график с температурите
# за месец януари и да се върне името на генерирания график
def get_temperatures(csv_file):

    # Load the csv file into a pandas dataframe
    df = pd.read_csv(csv_file)

    # Convert the 'Date' column to datetime format
    df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%y')

    # Filter the dataframe to only include January temperatures
    january_temperatures = df[df['Date'].dt.month == 1]
    
    # Generate a line plot of the temperatures
    january_temperatures.plot(x='Date', y=['Bathroom', 'Living Room', 'Kitchen'])
    plt.savefig('static/january_temperatures.png')

    # Return the filename of the generated plot
    return 'january_temperatures.png'

# Да се пресметне средно аритметично на температурите през
# месец януари и да се върне стаята с най-висока средна
# температура.
def get_highest_average_temperature(csv_file):
    # Load the csv file into a pandas dataframe
    df = pd.read_csv(csv_file)

    # convert the 'Date' column to datetime format
    df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%y')

    # filter the dataframe to only include January temperatures
    january_temperatures = df[df['Date'].dt.month == 1]

    # calculate the mean temperature for each room
    mean_temperatures = january_temperatures.mean()

    # return the room with the highest mean temperature
    return mean_temperatures.idxmax()