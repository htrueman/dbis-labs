from cassandra.auth import PlainTextAuthProvider
from cassandra.cluster import Cluster
from cassandra.query import BatchStatement


cluster = Cluster(auth_provider=PlainTextAuthProvider(username='cassandra', password='cassandra'))
connection = cluster.connect()

connection.execute(
    '''
        CREATE KEYSPACE IF NOT EXISTS lecture_vcs WITH replication = {
            'class': 'SimpleStrategy',
            'replication_factor': '1'
        };
    '''
)

batch_list = [
    '''
    UPDATE lecture_vcs.users
    SET
        data = {"role": 'teacher', "date_registered": '2019-10-10'},
        email = 'temp@mail.com'
    WHERE user_id = 1;
    ''',
    '''
    UPDATE lecture_vcs.groups
    SET user_email = 'temp@mail.com'
    WHERE group_id = 2 and group_name = 'km-62' and user_id = 1;
    '''
]


def execute_batch(statement_list):
    batch = BatchStatement()
    for q in statement_list:
        batch.add(q)
    connection.execute(batch)


if __name__ == '__main__':
    execute_batch(batch_list)
