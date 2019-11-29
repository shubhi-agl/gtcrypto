from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

auth_provider = PlainTextAuthProvider(username='admin', password='admin123')
cluster = Cluster(['35.238.43.195'], port=9042, auth_provider=auth_provider)
session = cluster.connect('bitcoin')

rows = session.execute('SELECT * from transactions;')

print(rows)

