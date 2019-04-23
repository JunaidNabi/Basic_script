import psycopg2
import pandas as pd

conn = psycopg2.connect(database="",
                            user="postgres",
                            password="",
                            host="192.168.1.200",
                            port="5432")
print("Opened database successfully")
cursor = conn.cursor()
#cursor.execute("ROLLBACK")

reader = pd.read_csv("data1.csv")
for i, row in reader.iterrows():
    print('counter ', i)
    customer = row.CustomerCode
    address = row.Address
    city = row.City
    postcode = row.PostCode
    rg = row.Rg
    sales = row.SalesOfficer

    insert_query = """insert into customermaster (CustomerCode,Address, City,PostCode,Rg,
    SalesOfficer) values ('{}','{}','{}',{},{},'{}');""".format(customer, address, city, postcode, rg, sales)
    #print(insert_query)
    try:
        cursor.execute(insert_query)
    except Exception as e:
        print(e, ">?>>>>>>   ")

conn.commit()
print(cursor.rowcount, "record inserted.")
