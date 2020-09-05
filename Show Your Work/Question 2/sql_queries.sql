-- 2a. How many orders were shipped by Speedy Express in total?

SELECT Shippers.ShipperName, COUNT(Shippers.ShipperName) AS OrdersShipped
FROM Orders
INNER JOIN Shippers ON Orders.ShipperID=Shippers.ShipperID
WHERE ShipperName = 'Speedy Express'
GROUP BY ShipperName


-- 2b. What is the last name of the employee with the most orders?

SELECT Employees.LastName, COUNT(Orders.OrderID) AS NumOrders
FROM Orders
INNER JOIN Employees ON Orders.EmployeeID=Employees.EmployeeID
GROUP BY LastName
ORDER BY NumOrders DESC LIMIT 1


-- 2c. What product was ordered the most by customers in Germany?

SELECT Customers.Country, Products.ProductName, SUM(OrderDetails.Quantity) AS TotalOrdered
FROM Orders
INNER JOIN Customers ON Orders.CustomerID=Customers.CustomerID
INNER JOIN OrderDetails ON Orders.OrderID=OrderDetails.OrderID
INNER JOIN Products ON OrderDetails.ProductID=Products.ProductID
WHERE Country = 'Germany'
GROUP BY ProductName
ORDER BY TotalOrdered DESC LIMIT 1
