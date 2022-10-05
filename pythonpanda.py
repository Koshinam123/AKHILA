import pandas as pd
df = pd.read_csv("MELBOURNE_HOUSE_PRICES_LESS.csv")
#Top n number of rows 
df.head(5)
df.tail(5)
print(df.shape)
avg_price = df["Price"].mean()
print("Average house price", avg_price)
median_rooms = df["Rooms"].median()
print("Median no of rooms ", median_rooms)
mode_suburb = df["Suburb"].mode()
print("Mode no of Suburb ", mode_suburb)
standard_deviation = df['Price'].std()
print(standard_deviation)
print(df["Regionname"].value_counts())
reg_dict = dict(df["Regionname"].value_counts())
print(reg_dict)
a = list(reg_dict.keys())
b = list(reg_dict.values())
print(a)
print(b)
print(type(a))
print(type(b))
fig = plt.figure()

plt.pie(x = b, labels = a, autopct="%.2f%%")

plt.show()
fig = plt.figure()
plt.xticks(rotation=90)

plt.bar(x = a, height = b)

plt.show()
price = list(df["Price"])
dist = list(df["Distance"])
fig = plt.figure()

plt.scatter(x = dist, y = price, edgecolors= "black")

plt.xlabel("Distance")
plt.ylabel("Price")
plt.show()
x = [1, 2, 1, 4, 5, 6, 9, 3, 10, 0, 9, 8]
plt.hist(x, bins=5, edgecolor="black")
(array([3., 2., 2., 1., 4.]),
 array([ 0.,  2.,  4.,  6.,  8., 10.]),
 <a list of 5 Patch objects>)
print(min(price))
print(max(price))
fig = plt.figure()

plt.hist(x = price, bins = 50, edgecolor= "black")
plt.show()
