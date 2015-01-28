import pymssql
import getpass

def pprint(cursor, query, use_headings=False):
	headings = list()

	if use_headings:
		#Find the select line.
		q_lines = query.split('\n')
		select = None
		for qline in q_lines:
			if qline.lower().find('select') > -1:
				select = qline

		sameline_from = select.lower().find('from')
		if sameline_from:
			headings = headings[:sameline_from]
		headings = select.split(',')

		cleaned = [headings[0].split(' ')[1]]
		cleaned.extend(headings[1:])

		headings = [ map(lambda x: x.strip(), cleaned) ]


	if use_headings:
		headings.extend(list(cursor))
		result = map(lambda r: map(lambda x: str(x), r), headings)
	else:
		result = map(lambda r: map(lambda x: str(x), r), list(cursor))
	
	cols = [0] * len(result[0])

	for row in result:
		cur_cols = list()
		
		#Find the width of each column. (With padding)
		for e in row:
			cur_cols.append(len(str(e)))
		#If the width of the current row's column is greater than the geatest so far, replace it.
		for i,cur in enumerate(cur_cols):
			if cur > cols[i]:
				cols[i] = cur

	l = sum(cols)+(len(cols)*4)

	#Print header line.
	print ('='*l)

	#Rows.
	for rn, row in enumerate(result):
		line = '| '
		for i, e in enumerate(row):
			line += ' '+str(e)

			#Add padding if the current entry isn't as long as the longest entry in the column.
			col_diff = cols[i] - len(str(e))
			if col_diff > 0:
				line += ' '*col_diff
			
			line += ' |'

		print line
		
		if rn < len(result) - 1:
			print ('-'*l)

	#Print footer line.
	print ('-'*l)

h = raw_input('Enter host:')
u = raw_input('Enter user:')
p = getpass.getpass('Enter password:')
d = raw_input('Use which database?:')

connection = pymssql.connect(host=h, user=u, password=p, database=d)

cursor = connection.cursor()

end = False
while not end:
	path = str(raw_input("Enter a path to an SQL file\n('EXIT' to quit, 'MANUAL' to enter a query by hand): ")).strip()
	q = ['']

	if path == 'EXIT':
		end = True
		break
	
	elif path == 'MANUAL':
		print "Enter your query now, when you are done type 'EXE'"
		i = ''

		while i != 'EXE':
			q[0] = q[0]+' '+i
			i = raw_input()


	else:
		with open(path,'r') as f:
			q = f.read()
			q = q.split('---')
			q = map(lambda x: '--'+x, q)


	print '\n'
	for i,t in enumerate(q):
		print 'QUERY '+str(i+1)
		cursor.execute(t)
		pprint(cursor, t)
		print '\n'