# # import csv

# # with open("US_States_Game_CSV\weather_data.csv") as data_file:
# #    data = csv.reader(data_file)
# #    temperatures = []
# #    for row in data:
# #        if row[1] != "temp":
# #            temperatures.append(int(row[1]))
       
# #    print(temperatures)

# import pandas

# data = pandas.read_csv("US_States_Game_CSV\weather_data.csv")
# print(data["temp"])

# temp_list = data["temp"].to_list()
# print(len(temp_list))

# print(data["temp"].mean())
# print(data["temp"].max())

# # Get Data in Columns
# print(data["condition"])
# print(data.condition)

# # Get data in row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0]
# monday_temp_F = monday_temp * 9/5 + 32

import pandas

data = pandas.read_csv(r"SquirrelWeatherDataReader\2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrel_count = len(data[data["Primary Fur Color"]  == "Gray"])
red_squirrel_count = len(data[data["Primary Fur Color"]  == "Cinnamon"])
black_squirrel_count = len(data[data["Primary Fur Color"]  == "Black"])
print(grey_squirrel_count)
print(red_squirrel_count)
print(black_squirrel_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrel_count, red_squirrel_count, black_squirrel_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
