import oracledb
import config_univ as c
oracledb.init_oracle_client()
conn = oracledb.connect(
    user = c.username,
    password = c.password,
    dsn = c.dsn
)

if(conn.is_healthy()):
    print("Connected to the database!")
    cur = conn.cursor()