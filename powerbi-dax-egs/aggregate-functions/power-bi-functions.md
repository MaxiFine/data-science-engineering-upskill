## DAX NOTES

# AGGREGATE FUNCTIONS NOTES

- LINK: https://learn.microsoft.com/en-us/dax/aggregation-functions-dax

When you need SUM and how
SUM: Adds all the numbers in column
SUM('Apocalypse Sales'[Units sold])

Profits = (SUM('Apocolypse Store'[Price]) - SUM('Apocolypse Store'[Production Cost])) * SUM('Apocolypse Sales'[Units Sold])

When you need SUMX and how
SUMX(Table, Expression)
Returns the sum of an expression evaluated for each row in a table.

DATE/CALENDAR Computations
WEEKDAY(Date, [ReturnType])
Returns a number from 1 to 7 identifying the day of the week of a date.

