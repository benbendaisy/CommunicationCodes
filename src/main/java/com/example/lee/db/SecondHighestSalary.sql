Select IFNULL((SELECT distinct Salary AS SecondHighestSalary FROM Employee ORDER BY Salary DESC LIMIT 1,1), null);

select MAX(Salary) as SecondHighestSalary from Employee where Salary < (select MAX(Salary) from Employee);