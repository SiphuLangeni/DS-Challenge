# Question 1  

**a. Think about what could be going wrong with our calculation. Think about a better way to evaluate this data.**  

Average order value (AOV) is a metric used to track average dollars spent on each customer order. One of its shortcomings is its sensitivity to outliers. In this case, there are a few very large orders that cause some severe right skewness to the data. Because of this, the average is not a true reflection of the purchasing habits of the customers but rather falsely inflates this number which may render it meaningless for our analysis. This suspician is confirmed by a brief look at the 5 number summary, skewness value much greater than 1 and distribution plot.  
  
**b. What metric would you report for this dataset?**  

A better metric to use would be the median order value (MOV) as median is much more robust to outliers than the mean. It is more reflective of central tendancies in data which is highly skewed. Alternatively, depending on the dataset and the distribution of the data, one could also calculate the AOV after removing outliers OR replacing outliers with the median value.  Only 141 orders (2.82\% of the data) are outliers so I am comfortable removing them for the purpose of this analysis. 

**c. What is its value?**  

**MOV** is $284.00  
**AOV** (*after outliers removed*) is $293.72  
**AOV** (*after replacing outliers with median value*) is $293.44  

***Additional notes:***  
For this dataset, it made sense to remove outliers. If the dataset had customers with very different spending patterns, it may be meaningful to identify those clusters first, then calculate the AOV for each of them individually.

<br><br/>
# Question 2
**a. How many orders were shipped by Speedy Express in total?**  

***Query:*** 

**SELECT** Shippers.ShipperName, **COUNT**(Shippers.ShipperName) **AS** OrdersShipped  
**FROM** Orders  
**INNER JOIN** Shippers **ON** Orders.ShipperID=Shippers.ShipperID  
**WHERE** ShipperName = 'Speedy Express'  
**GROUP BY** ShipperName

***Answer:***  

54
 
**b. What is the last name of the employee with the most orders?**  

***Query:***  

**SELECT** Employees.LastName, **COUNT**(Orders.OrderID) **AS** NumOrders  
**FROM** Orders  
**INNER JOIN** Employees **ON** Orders.EmployeeID=Employees.EmployeeID  
**GROUP BY** LastName  
**ORDER BY** NumOrders **DESC LIMIT** 1  

***Answer:***  

Peacock (NumOrders = 40)

**c. What product was ordered the most by customers in Germany?**  

***Query:***  

**SELECT** Customers.Country, Products.ProductName, **SUM**(OrderDetails.Quantity) **AS**  
TotalOrdered  
**FROM** Orders  
**INNER JOIN** Customers **ON** Orders.CustomerID=Customers.CustomerID  
**INNER JOIN** OrderDetails **ON** Orders.OrderID=OrderDetails.OrderID  
**INNER JOIN** Products **ON** OrderDetails.ProductID=Products.ProductID  
**WHERE** Country = 'Germany'  
**GROUP BY** ProductName  
**ORDER BY** TotalOrdered **DESC LIMIT** 1  

***Answer:***  

Boston Crab Meat (TotalOrdered = 160)