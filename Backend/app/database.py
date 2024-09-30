import psycopg2

# def get_db():
#     connection = psycopg2.connect(
#         host="localhost",
#         database="pokergame",
#         user="postgres",
#         password="postgres"
#     )
#     return connection


def get_db():
    connection = psycopg2.connect(
        host="database",
        database="hand_history",
        user="postgres",
        password="postgres",
        port="5432",
    )
    return connection

