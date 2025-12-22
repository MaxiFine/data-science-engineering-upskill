# DAX EXAMPLES ON PROFITS AND SALES

- ProfitsOnProductsFromCustomers = (SUM('Apocolypse Store'[Price]) - SUM('Apocolypse Store'[Production Cost])) * SUM('Apocolypse Sales'[Units Sold])

- CountOfSales = COUNT('Apocolypse Sales'[Order ID]) 

## New Column on tables for Profits Calculations

- GeneralProfit_Column = (SUM('Apocolypse Store'[Price]) - SUM('Apocolypse Store'[Production Cost])) * SUM('Apocolypse Sales'[Units Sold])

- ProfitsOnEachProduct = Profits_by_Products_SUMx = SUMX('Apocolypse Sales', ('Apocolypse Store'[Price] - 'Apocolypse Store'[Production Cost]) * 'Apocolypse Sales'[Units Sold])
