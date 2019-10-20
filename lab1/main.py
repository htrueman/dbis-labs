from cassandra import ConsistencyLevel
from cassandra.cluster import Cluster
from cassandra.query import SimpleStatement
from cassandra.auth import PlainTextAuthProvider

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


def get_query_list_from_file(filename):
    with open(filename, 'r') as file:
        data = file.read()
        return [query.strip() for query in data.split(';') if query.strip()]


def execute_query_list(query_list, consistency_level):
    for q in query_list:
        statement = SimpleStatement(
            q,
            consistency_level=consistency_level,
        )
        connection.execute(statement)


def main():
    create = get_query_list_from_file('create.cql')
    execute_query_list(create, ConsistencyLevel.ALL)

    work = get_query_list_from_file('work.cql')
    execute_query_list(work, ConsistencyLevel.ONE)

    drop = get_query_list_from_file('drop.cql')
    execute_query_list(drop, ConsistencyLevel.QUORUM)


if __name__ == '__main__':
    main()
