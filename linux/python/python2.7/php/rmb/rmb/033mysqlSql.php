SQL种类

DDL DML DQL DCL

数据定义语言（DDL）： CREATE  DROP    ALTER
	用于定义和管理数据对象（库，表，索引，视图），包括数据库、数据表等。例如：CREATE、DROP、ALTER等语句。 

 INSERT UPDATE DELETE  
数据操作语言（DML）： 和表中的数据记录
	用于操作数据库对象中所包含的数据。例如：INSERT、UPDATE、DELETE语句。
SELECT  60%
数据查询语言（DQL） ：
	用于查询数据库对象中所包含的数据，能够进行单表查询、连接查询、嵌套查询，以及集合查询等各种复杂程度不同的数据库查询，并将数据返回到客户机中显示。例如：SELECT语句。 

数据控制语言（DCL）：
	是用来管理数据库的语言，包含管理权限及数据更改。例如：GRANT、REVOKE、COMMIT、ROLLBACK等语句。


对于程序员来说

	创建表（为项目设计表）

	增，删，改、查

	
	

	插入表数据insert 

	insert into 表名([字段列表]) values(值列表)，（值列表2），（值列表3）

	特点：
		1. 如果在表名后没有给出字段列表，则值列表必须列出所有字段的值，必须按表中默认的顺序插入
		2. 所有需要写字段名的地方都不加单引号或双引号，但所有值建议都要以字符形式使用
		3. 建议在插入数据时，最好给出字段列表，则值要和字段列表对象即可，可以不按表中字段的顺序

	update 表名 set 字段=‘值’［，字段2=值2 ［，/。。。］］[条件]  条件是确定要更改的记录，可以通过条件指定一条也可指定多条

	delete from 表名 [条件]

		where 

	select 

	都可以使用 各种运算符号（可以把字段当作一个变量）

	只要你想更新、删除、查找，只要写对条件就能准确找到要管理的一条或多条语句

	SELECT [ALL | DISTINCT]
		{*|table.*|[table.]field1[as alias1][,[table.]field2[as alias2]][.....]}
	FROM   表名［］，表2
	
	[WHERE...] 

	[GROUP BY....]

	[HAVING...] 

	[ORDER BY ...]

	[LIMIT count] 

	使用SELECT查询语言，目的就可以可以按你的想法将数据查出来，将结果返回给你
	
	1. 字段 要列出要查询的字段

	2. 可以为每个字段起个别名  后面会用到（关键字，多表查询） 表也可起别名（多表查询）

	3. 使用distinct作用整个查询列表，取消重复的数据，只返一个， 而不是单独的一列

	4. 在SQL语句中使用表达式的列 （算术运行符号，可以使用条件，逻辑运算符号）

		1+1
		4-1
	5. WEHERE 可以在SELECT UPDATE DELETE

	逻辑运算符号（多个条件组合）

		&&   ||  !
		AND  OR  NOT 
	比较运算符号
		= 和程序中的 ==不一样
		<=> 和=作用一相，但可以用于NULL比较,null不能用=号；
		!= <>
		<
		<=
		>
		>=
		IS NULL
		IS NOT NULL
		BETWEEN AND
		NOT BETWEEN AND
		LIKE                         _（任意一个字符）和%（0个或多个任意字符） 两个通配符号
		NOT LIKE 
 		IN
		REGEXP RLIKE

	6.多表查询（连接查询）
	

	7.嵌套查询 子查询

	8. order by 字段 [asc正序] desc倒序
	
	9. limit count/limit 0,1/

	10.统计
	group  by  字段 //cid//有重复的字段

	count()/count(*)记录个数；
	sum()
	avg()
	max()
	min()
select count(*),sum(num),avg(price),max(price),min(price) from products group by cid having sum(num)>90;
		

		
		
	







