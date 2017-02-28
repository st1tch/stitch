import pymysql

#query = 'select distinct %s from problem_table'
def db_recv(conn, query, *args):
    conn.execute(query % args)
    return conn.fetchall()

#query = 'select distinct {} from problem_table'
def db_recv2(conn, query, *args):
    conn.execute(query.format(*list(args)))
    return conn.fetchall()

db_conn1 = pymysql.connect(host='kimtae.xyz', port=23306, user='stitch', password='stitch1004', db='ladybug_db', charset='utf8')
db1 = db_conn1.cursor(pymysql.cursors.DictCursor)

category = []
for idx in db_recv(db1, query, 'category')
    category.append(idx['category'])
category.sort()
print category
#db1.execute('commit')
