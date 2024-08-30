import sqlalchemy
from sqlalchemy import create_engine, text

connection_string = "mysql+pymysql://2euWq46C4YeBhJn.root:SpPtMF1WLTUKH37N@gateway01.ap-southeast-1.prod.aws.tidbcloud.com/host?charset=utf8mb4"
engine = create_engine(connection_string,
connect_args={
    "ssl":{
        "ssl_ca":"<CA_PATH>",
    }
})

with engine.connect() as conn: 
    result = conn.execute(text("select * from p"))
    result_all = result.all()
    first_result = result_all[0]
    first_result_dict = dict(result_all[0]._mapping)
    print(first_result_dict)
    print(type(first_result_dict))