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
select id i, score p, name n
from students;
-- 投影查询进行条件查询
select id i, score p, name n
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