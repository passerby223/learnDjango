-- 查询数据-基本查询
-- 查询出students表的所有数据
select *
from students;
-- 查询出classes表的所有数据
SELECT *
FROM classes;
-- 下述查询会直接计算出表达式的结果。虽然SELECT可以用作计算，但它并不是SQL的强项。
-- 但是，不带FROM子句的SELECT语句有一个有用的用途，就是用来判断当前到数据库的连接是否有效。
-- 许多检测工具会执行一条SELECT 1;来测试数据库连接。
SELECT 100 + 200;
select 1;
-- 查询分数在80分以上的学生记录
select *
from students
where score >= 85;
-- 查询分数在85分以上的男生
select *
from students
where score >= 85
  and gender = 'M';
