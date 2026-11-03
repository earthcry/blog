MySQL中的内置系统函数

	用在SELECCT语句，及子句 where order by having 中 UPDATE DELETE， 

	函数中可以将字段名作为变量来用，变量的值就是这个列对应的每一行记录

一、字符串函数
	
	php中用的函数，MySQl中大部也提供

	1 . CONCAT(S1,S2....SN): 把传入的参数连接成一个字符串
	2.  INSERT(str, x, y, insert): 将字符串X位置开始，y个字符串长度替换为字符串insert
	3. LOWER(str) UPPER(str): 将字符串转为小或或大写
	4. LEFT(str, x) RIGHT(str, x): 分别返回最左边的X字符，和最右边的X个字符，如果第二个参数为NULL则什么也不返回
	5. LPAD(str, n, pad), RPAD(str,n,pad): 用字符串pad对str最左边和最友边进行填充，直到长度为n个字符长度

	6. TRIM（str） LTRIM(str) Rtrim(str): 去掉字符串两边，左边和右边字符串的空格
	7. replace(str, a,b)：用字符串b替换字符串str中的所有出现的字符串a
	8. strcmp(s1, s2):如果S1比S2小，返回-1， 如果S1比S2大则返回1， 如果S1==S2 0
	9. substring(str, x, y): 返回字符串中的第x位置起y个字符串长度的字符。
	
	
二、数值函数
	ABS(x)：返回X的绝对值
	ceil(x): 返回大于X的最小整数  2.1 2.5 2.9  3
	floor(x): 返回小于X的最大整数  2.1 2.5 2.9 2
	mod(x, y): 返回x/y的模
	rand() 0-1之间
	round(x,y): 返回参数X的四舍五入的有y位小数的值
	truncate(x,y):返回数字x截断为y位小数的结果

	
三、日期函数

	当用PHP的时间戳来完成

	curdate()
	curtime()
	now()
	unix_timestamp(date)
	from_unixtime
	week()
	year()
	hour()
	minute()
	.....
四、流程控制函数
		
	if(value, t f)
	ifnull(value1, value2)
	case when [value1] then[result1]...else[default]end

	case when ...then
五、其它函数
	database()
	version()
	user()
	inet_aton(ip)
	inet_ntoa()
	password()
	md5()
	

