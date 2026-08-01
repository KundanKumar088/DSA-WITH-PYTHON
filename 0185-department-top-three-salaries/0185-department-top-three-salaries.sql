# Write your MySQL query statement below
SELECT e1.name AS Employee , d.name as department, e1.salary as Salary
From Employee e1
JOIN Department d on e1.DepartmentID =d.Id
WHERE 3 >(select count(distinct (e2.Salary))
    FROM Employee e2
    Where e2.Salary > e1.Salary
    and  e1.DepartmentId = e2.DepartmentId) 