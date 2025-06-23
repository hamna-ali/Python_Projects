# import csv
#
# with open("weather_data.csv") as data_file:
# 	data = csv.reader(data_file)
# 	temperatures = []
# 	print(data)
# 	for row in data:
# 		if row[1] != "temp":
# 			temperatures.append(int(row[1]))
#
# print(temperatures)
# import pandas
# data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(type(data["temp"]))
# temp_list = data["temp"].to_list()
# avg = sum(temp_list) / len(temp_list)
# print(avg)
import pandas

# print(data["temp"].mean())
# print(data["temp"].max())
# print(data.condition)
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
data = pandas.read_csv("Squirrel census.csv")
count_Gray = len(data["Primary Fur Color"] == "Gray")
print(count_Gray)

count_Cinnamon = len(data["Primary Fur Color"] == "Cinnamon")
print(count_Cinnamon)

count_Black = len(data["Primary Fur Color"] == "Black")
print(count_Black)


data_dict = {
	"Fur Color" : ["Gray", "Cinnamon","Black"],
	"Count" : [count_Gray,count_Cinnamon,count_Black]

}

df = pandas.DataFrame(data_dict)
print(df)
df.to_csv("Squirrel")