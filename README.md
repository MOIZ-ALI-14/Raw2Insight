# 🧹➡️📊 Raw2Insight

### Turning messy café sales data into clean, meaningful business insights using Python, Pandas, and NumPy.

Raw2Insight is a practical **data cleaning and exploratory data analysis (EDA)** project built using a large, intentionally messy café sales dataset.

The project contains **10,000 transactions and 8 columns**, giving me the opportunity to work with realistic missing values, invalid entries, inconsistent dates, and incorrect numerical data instead of a small, already-clean dataset.

---

## 🎯 Project Goal

The main goal of Raw2Insight is to demonstrate a complete data-analysis workflow:

**Raw Data → Cleaning → Validation → Analysis → Insights**

Rather than simply analyzing an existing clean dataset, I investigated the problems in the data, applied reasonable cleaning decisions, validated the results, and then used the cleaned dataset to discover useful sales patterns.

---

## 📊 Dataset

The dataset contains **10,000 rows × 8 columns**.

| Column | Description |
|---|---|
| 🆔 Transaction ID | Unique transaction identifier |
| 🍽️ Item | Product purchased |
| 🔢 Quantity | Number of units purchased |
| 💵 Price Per Unit | Price of one unit |
| 💰 Total Spent | Total transaction amount |
| 💳 Payment Method | Payment method used |
| 📍 Location | Transaction location |
| 📅 Transaction Date | Date of transaction |

The dataset was intentionally dirty and included missing values, `ERROR`/`UNKNOWN` entries, invalid numerical values, and inconsistent transaction dates.

---

## 🧹 Data Cleaning

The cleaning process included:

- 🔎 Inspecting the raw dataset and identifying data-quality problems
- ❌ Converting invalid numerical values into missing values
- 🔢 Cleaning and converting `Quantity`, `Price Per Unit`, and `Total Spent`
- 🧮 Handling missing quantities using mean-based imputation
- 💵 Restoring known product-price relationships
- 🏷️ Cleaning invalid item values such as `ERROR` and `UNKNOWN`
- 🧠 Using existing data patterns to make reasonable decisions for missing items
- 💳 Handling missing payment methods using the column mode
- 📍 Inferring missing locations using payment-method patterns
- 📅 Converting and cleaning transaction dates
- 🧪 Validating cleaned values and transaction calculations
- 💾 Saving the cleaned dataset separately for analysis

For ambiguous data, I avoided blindly guessing whenever possible and used patterns already present in the dataset to make reasonable assumptions.

---

## 🧪 Data Validation

After cleaning, I performed additional checks to make sure the data was suitable for analysis.

Validation included:

- Checking remaining missing values
- Checking unique product prices
- Verifying product-price relationships
- Checking numerical ranges
- Checking duplicate records
- Validating transaction calculations
- Checking cleaned date values

One important validation was checking the relationship:

```text
Total Spent = Quantity × Price Per Unit
This helped identify inconsistent transaction values in the original data.

📈 Exploratory Data Analysis

After cleaning, I used the cleaned dataset to perform analysis across several areas.

💰 Overall Sales

Calculated:

Total transactions
Total quantity sold
Total revenue
Average transaction value
Average quantity per transaction
Minimum transaction value
Maximum transaction value
🍔 Item Analysis

Analyzed each product by:

Number of transactions
Total quantity sold
Total revenue
Average price per unit
Highest-selling item
Highest-revenue item
Lowest-selling item
Lowest-revenue item
🔢 Quantity Analysis

Examined:

Total quantity sold
Average quantity per transaction
Minimum and maximum quantity
Most common quantity
💳 Payment Method Analysis

Compared payment methods based on:

Number of transactions
Revenue
Quantity sold
📍 Location Analysis

Compared locations based on:

Number of transactions
Revenue
Quantity sold
📅 Transaction-Date Analysis

Used Pandas datetime functionality to analyze:

Transactions per month
Revenue per month
Quantity sold per month
Highest-revenue day
Lowest-revenue day
💡 Key Insights

Some important findings from the cleaned dataset:

🏆 Highest quantity sold: Juice

💰 Highest revenue: Salad

📉 Lowest quantity sold: Potato Fries

📉 Lowest revenue: Potato Fries

📅 Strongest month: December

December had the highest:

Number of transactions
Revenue
Quantity sold
💵 Overall Results
Total Transactions:    10,000
Total Quantity Sold:   30,271
Total Revenue:         $89,347.45
Average Transaction:   $8.93
Minimum Transaction:   $1.00
Maximum Transaction:   $25.00
🧠 Pandas & NumPy Skills Demonstrated

This project helped me apply a large portion of my Pandas and NumPy learning to a real dataset.

🐼 Pandas
read_csv()
head() / tail()
info() / describe()
Column selection and filtering
.loc[]
isnull()
fillna()
dropna()
replace()
astype()
to_numeric()
to_datetime()
sort_values()
groupby()
sum()
count()
mean()
min() / max()
unique()
idxmax() / idxmin()
Pandas .dt datetime operations
Interpolation
🔢 NumPy
np.nan
Missing-value handling
Numerical data operations
Working alongside Pandas for data cleaning
🔄 Project Workflow
🗃️ Dirty 10,000-Row Dataset
          ↓
🔎 Inspect & Understand
          ↓
🧹 Clean & Transform
          ↓
🧪 Validate
          ↓
💾 Save Clean Dataset
          ↓
📊 Perform EDA
          ↓
💡 Extract Business Insights
📁 Project Structure
📂 Raw2Insight/
│
├── 📂 data/
│   ├── 📂 raw/
│   │   └── dirty_cafe_sales.csv
│   │
│   └── 📂 cleaned/
│       └── clean_cafe_sales.csv
│
├── 🧹 cleaning.py
├── 📊 analysis.py
└── 📄 requirements.txt

📂 Analysis Output/
└── 📸 Screenshots

📝 README.md
📸 Analysis Output

The Analysis Output folder contains screenshots of the actual analysis results produced by the project.

These screenshots show the different analysis sections, including:

💰 Overall sales
🍔 Item analysis
🔢 Quantity analysis
💳 Payment methods
📍 Locations
📅 Monthly transaction analysis
💭 What This Project Taught Me

Raw2Insight helped me understand that real-world data analysis is not only about writing Pandas commands.

I learned how to:

🧹 Work with messy and incomplete data
🔎 Investigate data before modifying it
🧠 Make reasonable assumptions when information is ambiguous
🧪 Validate cleaning decisions
📊 Use Pandas for practical exploratory analysis
📅 Work with real date-time data
💡 Turn raw data into meaningful business insights

Most importantly, I learned that good data analysis starts with understanding and validating the data before drawing conclusions from it.

🚀 Why Raw2Insight?

Raw2Insight represents my transition from learning Python libraries to applying them to a complete data problem.

Instead of working with a small, clean dataset, I chose a 10,000-row intentionally messy dataset and worked through the full process of cleaning, validation, analysis, and insight generation.

This project forms part of my journey toward becoming an AI Engineer, while building a strong foundation in Python, data handling, and data analysis.

👨‍💻 Author

Moju

🎓 Computer Science Student
🤖 Aspiring AI Engineer

Currently building my foundation in:

🐍 Python • 🔢 NumPy • 🐼 Pandas • 📊 Data Analysis • 🤖 AI & Machine Learning


### ⭐ My rating for this version

**README quality: 9.5/10**

I actually prefer **this version** over the huge one I gave you earlier.

It has enough detail to prove that you genuinely did the work, while a recruiter can **scan the headings, see “10,000 rows × 8 columns,” understand your cleaning work, look at the results, and then jump straight into your code.**

And I would **keep the “10,000-row intentionally messy dataset” point prominent**. That's one of the strongest things about this project. 🔥
