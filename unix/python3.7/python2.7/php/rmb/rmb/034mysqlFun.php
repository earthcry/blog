MySQL�е�����ϵͳ����

	����SELECCT��䣬���Ӿ� where order by having �� UPDATE DELETE�� 

	�����п��Խ��ֶ�����Ϊ�������ã�������ֵ��������ж�Ӧ��ÿһ�м�¼

һ���ַ�������
	
	php���õĺ�����MySQl�д�Ҳ�ṩ

	1 . CONCAT(S1,S2....SN): �Ѵ���Ĳ������ӳ�һ���ַ���
	2.  INSERT(str, x, y, insert): ���ַ���Xλ�ÿ�ʼ��y���ַ��������滻Ϊ�ַ���insert
	3. LOWER(str) UPPER(str): ���ַ���תΪС����д
	4. LEFT(str, x) RIGHT(str, x): �ֱ𷵻�����ߵ�X�ַ��������ұߵ�X���ַ�������ڶ�������ΪNULL��ʲôҲ������
	5. LPAD(str, n, pad), RPAD(str,n,pad): ���ַ���pad��str����ߺ����ѱ߽�����䣬ֱ������Ϊn���ַ�����

	6. TRIM��str�� LTRIM(str) Rtrim(str): ȥ���ַ������ߣ���ߺ��ұ��ַ����Ŀո�
	7. replace(str, a,b)�����ַ���b�滻�ַ���str�е����г��ֵ��ַ���a
	8. strcmp(s1, s2):���S1��S2С������-1�� ���S1��S2���򷵻�1�� ���S1==S2 0
	9. substring(str, x, y): �����ַ����еĵ�xλ����y���ַ������ȵ��ַ���
	
	
������ֵ����
	ABS(x)������X�ľ���ֵ
	ceil(x): ���ش���X����С����  2.1 2.5 2.9  3
	floor(x): ����С��X���������  2.1 2.5 2.9 2
	mod(x, y): ����x/y��ģ
	rand() 0-1֮��
	round(x,y): ���ز���X�������������yλС����ֵ
	truncate(x,y):��������x�ض�ΪyλС���Ľ��

	
�������ں���

	����PHP��ʱ��������

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
�ġ����̿��ƺ���
		
	if(value, t f)
	ifnull(value1, value2)
	case when [value1] then[result1]...else[default]end

	case when ...then
�塢��������
	database()
	version()
	user()
	inet_aton(ip)
	inet_ntoa()
	password()
	md5()
	

