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
-- 小结
-- 使用SELECT查询的基本语句SELECT * FROM <表名>可以查询一个表的所有行和所有列的数据。
-- SELECT查询的结果是一个二维表。

-- 查询数据-条件查询
-- 查询分数在85分(包含85)以上的学生记录
select *
from students
where score >= 85;
-- 查询分数在85分(包含85)以上的男生
select *
from students
where score >= 85
  and gender = 'M';
-- 查询分数在85分(包含85)或性别是男生的学生信息
select *
from students
where score >= 85
   or gender = 'M';
-- 查询不是2班学生的学生信息
select *
from students
where not class_id = 2;
-- 上述NOT条件`NOT class_id = 2`其实等价于`class_id <> 2`，因此，NOT查询不是很常用。
select *
from students
where class_id <> 2;
-- 查询分数在80以下或者90以上，并且是男生的学生信息
select *
from students
where (score < 80 or score > 90)
  and gender = 'M';
-- 如果不加括号，条件运算按照NOT、AND、OR的优先级进行，即NOT优先级最高，其次是AND，最后是OR。加上括号可以改变优先级。
-- 常用的条件表达式
-- 条件	                表达式举例1	        表达式举例2	            说明
-- 使用=判断相等	        score = 80	        name = 'abc'	    字符串需要用单引号括起来
-- 使用>判断大于	        score > 80	        name > 'abc'	    字符串比较根据ASCII码，中文字符比较根据数据库设置
-- 使用>=判断大于或相等	score >= 80	        name >= 'abc'
-- 使用<判断小于	        score < 80	        name <= 'abc'
-- 使用<=判断小于或相等	score <= 80	        name <= 'abc'
-- 使用<>判断不相等	    score <> 80	        name <> 'abc'
-- 使用LIKE判断相似	    name LIKE 'ab%'	    name LIKE '%bc%'	%表示任意字符，例如'ab%'将匹配'ab'，'abc'，'abcd'
-- 小结
-- 通过WHERE条件查询，可以筛选出符合指定条件的记录，而不是整个表的所有记录。

-- 查询数据-投影查询
-- 使用SELECT * FROM <表名> WHERE <条件>可以选出表中的若干条记录。我们注意到返回的二维表结构和原表是相同的，即结果集的所有列与原表的所有列都一一对应。
-- 如果我们只希望返回某些列的数据，而不是所有列的数据，我们可以用SELECT 列1, 列2, 列3 FROM ...，让结果集仅包含指定列。这种操作称为投影查询。
-- 例如，从students表中返回id、score和name这三列
select id, score, name
from students;
-- 给查询列名取别名
select id as i, score as p, name as n
from students;
-- 投影查询进行条件查询
select id as i, score as p, name as n
from students
where score >= 80;
-- 小结
-- 使用SELECT *表示查询表的所有列，使用SELECT 列1, 列2, 列3则可以仅返回指定列，这种操作称为投影。
-- SELECT语句可以对结果集的列进行重命名。

-- 查询数据-排序
-- 使用SELECT查询时，查询结果集通常是按照id排序的，也就是根据主键排序。可以加上ORDER BY子句按照其他列名进行排序。
-- 按score从低到高
-- 默认的排序规则是ASC：“升序”，即从小到大。ASC可以省略，即ORDER BY score ASC和ORDER BY score效果一样。
select id, name, gender, score
from students
order by score;
-- 按score从高到低
select id, name, gender, score
from students
order by score desc;
-- 如果score列有相同的数据，要进一步排序，可以继续添加列名。例如，使用ORDER BY score DESC, gender表示先按score列倒序，如果有相同分数的，再按gender列排序
select id, name, gender, score
from students
order by score desc, gender;
-- 如果有WHERE子句，那么ORDER BY子句要放到WHERE子句后面。例如，查询一班的学生成绩，并按照倒序排序
select id, name, class_id, gender, score
from students
where class_id = 1
order by score desc;
-- 小结
-- 使用ORDER BY可以对结果集进行排序；
-- 可以对多列进行升序、倒序排序。

-- 查询数据-分页查询
-- 使用SELECT查询时，如果结果集数据量很大，比如几万行数据，放在一个页面显示的话数据量太大，不如分页显示，每次显示100条。
-- 分页实际上就是从结果集中“截取”出第M~N条记录。这个查询可以通过LIMIT <M> OFFSET <N>子句实现。
-- 按score从高到低
SELECT id, name, gender, score
FROM students
ORDER BY score DESC
limit 3 offset 0;
SELECT id, name, gender, score
FROM students
ORDER BY score DESC
limit 0, 3;
-- 上述查询LIMIT 3 OFFSET 0表示，对结果集从0号记录开始，最多取3条。注意SQL记录集的索引从0开始。
-- 如果要查询第2页，那么我们只需要“跳过”头3条记录，也就是对结果集从3号记录开始查询，把OFFSET设定为3
SELECT id, name, gender, score
FROM students
ORDER BY score DESC
limit 3 offset 3;
SELECT id, name, gender, score
FROM students
ORDER BY score DESC
limit 3, 3;
-- 类似的，查询第3页的时候，OFFSET应该设定为6
SELECT id, name, gender, score
FROM students
ORDER BY score DESC
limit 3 offset 6;
SELECT id, name, gender, score
FROM students
ORDER BY score DESC
limit 6, 3;
-- 查询第4页的时候，OFFSET应该设定为9
SELECT id, name, gender, score
FROM students
ORDER BY score DESC
limit 3 offset 9;
-- 由于第4页只有1条记录，因此最终结果集按实际数量1显示。LIMIT 3表示的意思是“最多3条记录”。
-- 分页查询的关键在于，首先要确定每页需要显示的结果数量pageSize（这里是3），然后根据当前页的索引pageIndex（从1开始），确定LIMIT和OFFSET应该设定的值
-- LIMIT总是设定为pageSize；
-- OFFSET计算公式为pageSize * (pageIndex - 1)。
-- 这样就能正确查询出第N页的记录集。
-- OFFSET设定为20
SELECT id, name, gender, score
FROM students
ORDER BY score DESC
LIMIT 3 OFFSET 20;
-- OFFSET超过了查询的最大数量并不会报错，而是得到一个空的结果集。
-- 注意
-- OFFSET是可选的，如果只写LIMIT 15，那么相当于LIMIT 15 OFFSET 0
-- 在MySQL中，`LIMIT 15 OFFSET 30`还可以简写成LIMIT 30, 15
-- 使用LIMIT <M> OFFSET <N>分页时，随着N越来越大，查询效率也会越来越低。
-- 小结
-- 使用LIMIT <M> OFFSET <N>可以对结果集进行分页，每次查询返回结果集的一部分；
-- 分页查询需要先确定每页的数量和当前页数，然后确定LIMIT和OFFSET的值。

-- 查询数据-聚合查询
-- 对于统计总数、平均数这类计算，SQL提供了专门的聚合函数，使用聚合函数进行查询，就是聚合查询，它可以快速获得结果。
select count(*)
from students;
-- -- 使用聚合查询并设置结果集的列名为num
select count(*) as nums_total
from students;
-- 使用聚合查询并设置WHERE条件
-- 统计学生表中男生人数
select count(*) as boys
from students
where gender = 'M';
-- 统计学生表中女生人数
select count(*) as girls
from students
where gender = 'F';
-- 统计学生表中分数>80的人数
select count(*) as score_more_than_80
from students
where score > 80;
-- 除了COUNT()函数外，SQL还提供了如下聚合函数
-- 函数	        说明
-- SUM	    计算某一列的合计值，该列必须为数值类型
-- AVG	    计算某一列的平均值，该列必须为数值类型
-- MAX	    计算某一列的最大值
-- MIN	    计算某一列的最小值
-- MAX()和MIN()函数并不限于数值类型。如果是字符类型，MAX()和MIN()会返回排序最后和排序最前的字符。
-- 使用聚合查询计算男生平均成绩
select avg(score) as average
from students
where gender = 'M';
-- 特别注意：如果聚合查询的WHERE条件没有匹配到任何行，COUNT()会返回0，而SUM()、AVG()、MAX()和MIN()会返回NULL
-- 返回null
select avg(score) as average
from students
where gender = 'M1';
-- 返回0
select count(*) as score_more_than_80
from students
where score > 150;
-- 每页3条记录，通过聚合查询获得总页数:CEILING(num)对num想上取整
SELECT CEILING(COUNT(*) / 3) as total_page
FROM students;
-- 分组聚合
-- 按class_id分组
select class_id, count(*) as nums
from students
group by class_id;
-- 执行上边查询语句，COUNT()的结果不再是一个，而是3个，这是因为，GROUP BY子句指定了按class_id分组。
-- 因此，执行该SELECT语句时，会把class_id相同的列先分组，再分别计算，因此，得到了3行结果。
-- 按class_id, gender分组:统计各班的男生和女生人数
select class_id, gender, count(*) as num
from students
group by class_id, gender;
-- 查询查出每个班级的平均分
select class_id, avg(score)
from students
group by class_id;
-- 查出每个班级男生和女生的平均分
select class_id, gender, avg(score)
from students
group by class_id, gender;
-- 小结
-- 使用SQL提供的聚合查询，我们可以方便地计算总数、合计值、平均值、最大值和最小值；
-- 聚合查询也可以添加WHERE条件。

-- 查询数据-多表查询
-- FROM students, classes
select *
from students,
     classes;
-- 上边查询的是两个表的数据，查询的结果也是一个二维表，它是students表和classes表的“乘积”，即students表的每一行与classes表的每一行都两两拼在一起返回。
-- 结果集的列数是students表和classes表的列数之和，行数是students表和classes表的行数之积。
-- 这种多表查询又称笛卡尔查询，使用笛卡尔查询时要非常小心，由于结果集是目标表的行数乘积，对两个各自有100行记录的表进行笛卡尔查询将返回1万条记录，
-- 对两个各自有1万行记录的表进行笛卡尔查询将返回1亿条记录。
-- set alias为列名设置别名
SELECT students.id as sid,
       students.name  sname,
       students.gender,
       students.score,
       classes.id  as cid,
       classes.name   cname
FROM students,
     classes;
-- 注意，多表查询时，要使用表名.列名这样的方式来引用列和设置别名，这样就避免了结果集的列名重复问题。
-- 但是，用表名.列名这种方式列举两个表的所有列实在是很麻烦，所以SQL还允许给表设置一个别名.
-- 给表和字段设置别名
SELECT s.id as sid,
       s.name  sname,
       s.gender,
       s.score,
       c.id as cid,
       c.name  cname
FROM students as s,
     classes as c;
-- 多表查询也是可以添加WHERE条件
select s.id as sid, s.name as sname, s.gender, s.score, c.id as cid, c.name as cname
from students as s,
     classes as c
where s.gender = 'M'
  and c.id = 1;
-- 小结
-- 使用多表查询可以获取M x N行记录；
-- 多表查询的结果集可能非常巨大，要小心使用。
-- 一般使用主键或外键进行多表关联查询，笛卡尔乘积没太多意义，而且很容易查询量爆炸，不建议使用

-- 查询数据-连接查询
-- 连接查询是另一种类型的多表查询。连接查询对多个表进行JOIN运算。
-- 简单地说，就是先确定一个主表作为结果集，然后，把其他表的行有选择性地“连接”在主表结果集上。
-- 内连接——INNER JOIN
-- 查询学生表中所有学生所在的班级名称
select s.name as student_name, c.name as class_name
from students as s
         inner join classes as c on s.class_id = c.id;
-- INNER JOIN查询的写法
-- 先确定主表，仍然使用FROM <表1>的语法；
-- 再确定需要连接的表，使用INNER JOIN <表2>的语法；
-- 然后确定连接条件，使用ON <条件...>，这里的条件是s.class_id = c.id，表示students表的class_id列与classes表的id列相同的行需要连接；
-- 可选：加上WHERE子句、ORDER BY等子句。
-- 查询学生表中所有男生所在的班级名称
select s.name as student_name, c.name as class_name
from students as s
         inner join classes as c on s.class_id = c.id
where s.gender = 'M';
-- 查询学生表中一班所有男生的平均成绩
select avg(s.score) as avg_score
from students as s
         inner join classes as c on s.class_id = c.id
where s.class_id = 1
  and s.gender = 'M';
-- 查询学生表中一班的平均成绩
select avg(s.score) as avg_score
from students as s
         inner join classes as c on s.class_id = c.id
where s.class_id = 1;
-- OUTER JOIN外连接
-- RIGHT OUTER JOIN
select s.name as student_name, c.name as class_name
from students as s
         right outer join classes as c on s.class_id = c.id;
-- 执行上述RIGHT OUTER JOIN可以看到，和INNER JOIN相比，RIGHT OUTER JOIN多了一行，多出来的一行是“四班”，但是，学生相关的列如name、gender、score都为NULL。
-- 这也容易理解，因为根据ON条件s.class_id = c.id，classes表的id=4的行正是“四班”，但是，students表中并不存在class_id=4的行。
-- INNER JOIN、RIGHT OUTER JOIN、LEFT OUTER JOIN和FULL OUTER JOIN的区别：
-- INNER JOIN只返回同时存在于两张表的行数据，由于students表的class_id包含1，2，3，classes表的id包含1，2，3，4，所以，INNER JOIN根据条件s.class_id = c.id返回的结果集仅包含1，2，3。
-- RIGHT OUTER JOIN返回右表都存在的行。如果某一行仅在右表存在，那么结果集就会以NULL填充剩下的字段。
-- LEFT OUTER JOIN则返回左表都存在的行。
-- FULL OUTER JOIN会把两张表的所有记录全部选择出来，并且，自动把对方不存在的列填充为NULL。
-- 小结
-- JOIN查询需要先确定主表，然后把另一个表的数据“附加”到结果集上；
-- INNER JOIN是最常用的一种JOIN查询，它的语法是SELECT ... FROM <表1> INNER JOIN <表2> ON <条件...>；
-- JOIN查询仍然可以使用WHERE条件和ORDER BY排序。