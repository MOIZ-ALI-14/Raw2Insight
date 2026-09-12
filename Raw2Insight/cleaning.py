import numpy as np
import pandas as pd

# importing the dirty csv file
raw_dataframe = pd.read_csv("data/raw/dirty_cafe_sales.csv")


# first I want to see some starting rows and ending rows
# this helps me get an idea of how the data looks before cleaning
starting_data = raw_dataframe.head(15)
print(starting_data)

ending_data = raw_dataframe.tail(15)
print(ending_data)


# checking the basic structure of the dataframe
# I kept these commented because I don't need to print them every time
# print("\nDataframe shape:", raw_dataframe.shape)
# print("\nDataframe columns:", raw_dataframe.columns)
# print("\nDataframe info:")
# print(raw_dataframe.info())
# print("\nDataframe description:")
# print(raw_dataframe.describe())


# checking how many actual missing values are in each column
missing_values = raw_dataframe.isnull().sum()
print("\nMissing values in each column:")
print(missing_values)


# Quantity, Price Per Unit and Total Spent should be numbers
# but some values are stored as strings or contain invalid values
# errors="coerce" changes invalid values into NaN
raw_dataframe["Quantity"] = pd.to_numeric(raw_dataframe["Quantity"], errors="coerce")

raw_dataframe["Price Per Unit"] = pd.to_numeric(
    raw_dataframe["Price Per Unit"], errors="coerce"
)

raw_dataframe["Total Spent"] = pd.to_numeric(
    raw_dataframe["Total Spent"], errors="coerce"
)


# checking the unique values after converting them to numbers
# this helps me see if there are still strange values
print(raw_dataframe["Quantity"].unique())
print(raw_dataframe["Price Per Unit"].unique())
print(raw_dataframe["Total Spent"].unique())


# Quantity has some missing values
# I am using the mean to fill them instead of deleting those rows
raw_dataframe["Quantity"] = raw_dataframe["Quantity"].fillna(
    raw_dataframe["Quantity"].mean()
)

# quantity represents the number of items, so I want whole numbers
raw_dataframe["Quantity"] = raw_dataframe["Quantity"].astype(int)

# checking the values and making sure no missing values are left
print(raw_dataframe["Quantity"].unique())
print(raw_dataframe["Quantity"].isnull().sum())


# filling missing Price Per Unit values with the mean for now
raw_dataframe["Price Per Unit"] = raw_dataframe["Price Per Unit"].fillna(
    raw_dataframe["Price Per Unit"].mean()
)

# checking the values and missing values after filling
print(raw_dataframe["Price Per Unit"].unique())
print(raw_dataframe["Price Per Unit"].isnull().sum())


# the price should depend on the item
# so I am correcting the price where the item is known
# instead of keeping a wrong price or the mean price
# as i asumed there are countable items in data and each has unique price

raw_dataframe.loc[
    (raw_dataframe["Item"] == "Coffee") & (raw_dataframe["Price Per Unit"] != 2.00),
    "Price Per Unit",
] = 2.00

raw_dataframe.loc[
    (raw_dataframe["Item"] == "Cake") & (raw_dataframe["Price Per Unit"] != 3.00),
    "Price Per Unit",
] = 3.00

raw_dataframe.loc[
    (raw_dataframe["Item"] == "Cookie") & (raw_dataframe["Price Per Unit"] != 1.00),
    "Price Per Unit",
] = 1.00

raw_dataframe.loc[
    (raw_dataframe["Item"] == "Salad") & (raw_dataframe["Price Per Unit"] != 5.00),
    "Price Per Unit",
] = 5.00

raw_dataframe.loc[
    (raw_dataframe["Item"] == "Smoothie") & (raw_dataframe["Price Per Unit"] != 4.00),
    "Price Per Unit",
] = 4.00

raw_dataframe.loc[
    (raw_dataframe["Item"] == "Sandwich") & (raw_dataframe["Price Per Unit"] != 4.00),
    "Price Per Unit",
] = 4.00

raw_dataframe.loc[
    (raw_dataframe["Item"] == "Juice") & (raw_dataframe["Price Per Unit"] != 3.00),
    "Price Per Unit",
] = 3.00

raw_dataframe.loc[
    (raw_dataframe["Item"] == "Tea") & (raw_dataframe["Price Per Unit"] != 1.50),
    "Price Per Unit",
] = 1.50


# Total Spent should be Quantity multiplied by Price Per Unit
# so I am calculating it again using the cleaned values
raw_dataframe["Total Spent"] = (
    raw_dataframe["Quantity"] * raw_dataframe["Price Per Unit"]
)

# checking the new total values and making sure there are no missing ones
print(raw_dataframe["Total Spent"].unique())
print(raw_dataframe["Total Spent"].isnull().sum())


# keeping prices and totals at 2 decimal places
# because these are money values
raw_dataframe["Price Per Unit"] = raw_dataframe["Price Per Unit"].round(2)
raw_dataframe["Total Spent"] = raw_dataframe["Total Spent"].round(2)


# cleaning the Item column
# ERROR and UNKNOWN are not useful item names, so I am changing them to NaN
raw_dataframe["Item"] = raw_dataframe["Item"].replace(["ERROR", "UNKNOWN"], np.nan)

print(raw_dataframe["Item"].unique())


# some item names are missing, but their price can help me identify the item
# using the price to fill the missing item values
# i will use only unique prices(only four) to fill nan items because 4.00 comes for
# sandwich and smoothie, similarly, 3.00 comes for juice and cake also and 2.95 that
# is imputed value is not defined yet for a specific item

raw_dataframe.loc[
    (raw_dataframe["Item"].isna()) & (raw_dataframe["Price Per Unit"] == 5.00), "Item"
] = "Salad"

raw_dataframe.loc[
    (raw_dataframe["Item"].isna()) & (raw_dataframe["Price Per Unit"] == 1.50), "Item"
] = "Tea"

raw_dataframe.loc[
    (raw_dataframe["Item"].isna()) & (raw_dataframe["Price Per Unit"] == 1.00), "Item"
] = "Cookie"

raw_dataframe.loc[
    (raw_dataframe["Item"].isna()) & (raw_dataframe["Price Per Unit"] == 2.00), "Item"
] = "Coffee"


# checking some rows to see if the missing items were filled correctly
print(raw_dataframe.tail(50))
print(raw_dataframe.head(50))


# checking which items appear under each price
# this helps me find the remaining item values that can be identified by price
print(raw_dataframe.groupby("Price Per Unit")["Item"].value_counts())


# filling more missing item names using their known prices
raw_dataframe.loc[
    (raw_dataframe["Item"].isna()) & (raw_dataframe["Price Per Unit"] == 4.0), "Item"
] = "Sandwich"

raw_dataframe.loc[
    (raw_dataframe["Item"].isna()) & (raw_dataframe["Price Per Unit"] == 3.0), "Item"
] = "Juice"

# checking if any missing values are still left
print(raw_dataframe.isnull().sum())


# checking each item and the prices connected to it
# this helps me find any remaining item that can be identified
print(raw_dataframe.groupby("Item")["Price Per Unit"].unique())

# as only around 60 nan values among 10,000 has been left so i can use
# a new item for this data cleaning
# Potato Fries has a price of 2.95 in this dataset
# so I can use that price to fill the remaining missing item
raw_dataframe.loc[
    (raw_dataframe["Item"].isna()) & (raw_dataframe["Price Per Unit"] == 2.95), "Item"
] = "Potato Fries"

# checking the missing values again
print(raw_dataframe.isnull().sum())


# checking the different payment methods before cleaning
print(raw_dataframe["Payment Method"].unique())


# ERROR and UNKNOWN are not valid payment methods
# so I am changing them to NaN
raw_dataframe["Payment Method"] = raw_dataframe["Payment Method"].replace(
    ["ERROR", "UNKNOWN"], np.nan
)

print(raw_dataframe["Payment Method"].unique())
print(raw_dataframe["Payment Method"].isnull().sum())


# finding the most common payment method
# I will use it to fill the missing payment methods
mode_payment = raw_dataframe["Payment Method"].mode()[0]

raw_dataframe["Payment Method"] = raw_dataframe["Payment Method"].fillna(mode_payment)

# checking that there are no missing payment methods now
print(raw_dataframe["Payment Method"].isnull().sum())

# checking some rows and the final missing values after this cleaning step
print(raw_dataframe.tail(50))
print(raw_dataframe.head(50))
print(raw_dataframe.isnull().sum())


# checking the different location values before cleaning
print(raw_dataframe["Location"].unique())


# replacing ERROR and UNKNOWN with NaN
# so I can handle the missing locations separately
raw_dataframe["Location"] = raw_dataframe["Location"].replace(
    ["ERROR", "UNKNOWN"], np.nan
)

print(raw_dataframe["Location"].unique())
print(raw_dataframe["Location"].isnull().sum())


# checking the relationship between location and payment method
# to see if payment method can help me decide the missing location
print(raw_dataframe.groupby("Location")["Payment Method"].value_counts())


# if the location is missing and the payment method is Digital Wallet or Credit Card,
# I am using Takeaway based on the pattern found in the data
raw_dataframe.loc[
    (raw_dataframe["Location"].isna())
    & (
        (raw_dataframe["Payment Method"] == "Digital Wallet")
        | (raw_dataframe["Payment Method"] == "Credit Card")
    ),
    "Location",
] = "Takeaway"


# if the location is missing and the payment method is Cash,
# I am using In-store based on the pattern found in the data
raw_dataframe.loc[
    (raw_dataframe["Location"].isna()) & ((raw_dataframe["Payment Method"] == "Cash")),
    "Location",
] = "In-store"


# checking the rows and missing values after cleaning Location
print(raw_dataframe.tail(50))
print(raw_dataframe.head(50))
print(raw_dataframe.isnull().sum())


# checking missing dates before converting the column
print(raw_dataframe["Transaction Date"].isnull().sum())


# converting Transaction Date from strings to datetime
# invalid date values will become NaT because of errors="coerce"
raw_dataframe["Transaction Date"] = pd.to_datetime(
    raw_dataframe["Transaction Date"], errors="coerce"
)

# checking how many missing dates are left after conversion
print(raw_dataframe["Transaction Date"].isnull().sum())


# sorting the data by date before interpolation
# this puts the valid dates in chronological order
raw_dataframe = raw_dataframe.sort_values(by="Transaction Date", ascending=True)


# filling missing dates by linear interpolation
# this estimates the missing date using the surrounding date values
raw_dataframe["Transaction Date"] = raw_dataframe["Transaction Date"].interpolate(
    method="linear"
)

# checking the data and missing values after date cleaning
print(raw_dataframe.head(50))
print(raw_dataframe.tail(50))
print(raw_dataframe.isnull().sum())


# checking the final unique values and data types of every column
# this helps me make sure the columns contain the type of data I expect

print(raw_dataframe["Transaction ID"].unique())
print(raw_dataframe["Transaction ID"].dtype)

print(raw_dataframe["Item"].unique())
print(raw_dataframe["Item"].dtype)

print(raw_dataframe["Quantity"].unique())
print(raw_dataframe["Quantity"].dtype)

print(raw_dataframe["Price Per Unit"].unique())
print(raw_dataframe["Price Per Unit"].dtype)

print(raw_dataframe["Total Spent"].unique())
print(raw_dataframe["Total Spent"].dtype)

print(raw_dataframe["Payment Method"].unique())
print(raw_dataframe["Payment Method"].dtype)

print(raw_dataframe["Location"].unique())
print(raw_dataframe["Location"].dtype)

print(raw_dataframe["Transaction Date"].unique())
print(raw_dataframe["Transaction Date"].dtype)


# checking for completely duplicated rows
print("Duplicate rows:", raw_dataframe.duplicated().sum())

# checking if the same Transaction ID appears more than once
print("Duplicate Transaction IDs:", raw_dataframe["Transaction ID"].duplicated().sum())


# checking if Total Spent is actually equal to Quantity multiplied by Price Per Unit
check = (
    raw_dataframe["Total Spent"]
    == raw_dataframe["Quantity"] * raw_dataframe["Price Per Unit"]
)

# ~check flips True to False and False to True
# sum() counts the True values, so this gives the number of incorrect totals
print("Incorrect Total Spent:", (~check).sum())


# recalculating Total Spent again to make sure every row has the correct value
# as 13 values were wrong calculated
raw_dataframe["Total Spent"] = (
    raw_dataframe["Quantity"] * raw_dataframe["Price Per Unit"]
)


# checking the totals again after recalculating them
check = (
    raw_dataframe["Total Spent"]
    == raw_dataframe["Quantity"] * raw_dataframe["Price Per Unit"]
)

print("Incorrect Total Spent:", (~check).sum())


# checking the first and last transaction dates
print(raw_dataframe["Transaction Date"].min())
print(raw_dataframe["Transaction Date"].max())

# checking if any missing dates are still left
print(raw_dataframe["Transaction Date"].isna().sum())


# final sorting
# first sort by date, then Transaction ID, then Item
# this makes the cleaned data more organized
# ignore_index=True gives the rows new index numbers after sorting
raw_dataframe = raw_dataframe.sort_values(
    by=["Transaction Date", "Transaction ID", "Item"],
    ascending=[True, True, True],
    ignore_index=True,
)

print(raw_dataframe.head(50))
print(raw_dataframe.tail(50))


# =========================
# FINAL DATA QUALITY CHECK
# =========================

# checking the final number of rows and columns
print("\nFinal shape:", raw_dataframe.shape)


# checking if any missing values are still present
print("\nMissing values:")
print(raw_dataframe.isnull().sum())


# checking for completely duplicated rows
print("\nDuplicate rows:")
print(raw_dataframe.duplicated().sum())


# checking for duplicate Transaction IDs
print("\nDuplicate Transaction IDs:")
print(raw_dataframe["Transaction ID"].duplicated().sum())


# checking the final data types of all columns
print("\nData types:")
print(raw_dataframe.dtypes)


# checking the complete date range of the cleaned data
print("\nDate range:")
print(raw_dataframe["Transaction Date"].min())
print(raw_dataframe["Transaction Date"].max())


# checking if there are any zero or negative quantities
print("\nInvalid quantities:")
print((raw_dataframe["Quantity"] <= 0).sum())


# checking if there are any zero or negative prices
print("\nInvalid prices:")
print((raw_dataframe["Price Per Unit"] <= 0).sum())


# final check to make sure Total Spent is correct
print("\nIncorrect totals:")

valid_total = (
    raw_dataframe["Total Spent"]
    == raw_dataframe["Quantity"] * raw_dataframe["Price Per Unit"]
)

# flip the True/False values and count the incorrect rows
print((~valid_total).sum())

# checking the basic structure of the dataframe
print("\nDataframe shape:", raw_dataframe.shape)
print("\nDataframe columns:", raw_dataframe.columns)
print("\nDataframe info:")
print(raw_dataframe.info())
print("\nDataframe description:")
print(raw_dataframe.describe())

# i have run this cleaned data save line once, and file has been created in data folder
# now no need to run it again that's why i made it a comment
# raw_dataframe.to_csv("data/cleaned/clean_cafe_sales.csv", index=False)
