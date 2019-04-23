import psycopg2
import pandas as pd

conn = psycopg2.connect(database="",
                        user="postgres",
                        password="",
                        host="192.168.1.200",
                        port="5432")
# print("Opened database successfully")


cursor = conn.cursor()
cursor.execute("ROLLBACK")

reader = pd.read_csv("data.csv")
for i, row in reader.iterrows():
    print('counter ', i)
    country = row.Country
    zone = row.Zone
    state = row.State
    region = row.Region
    area = row.Area
    depot = row.Depot
    tier = row.Tier
    district = row.District
    city = row.City
    cityCode = row.CityCode
    category = row.Categorization
    employ_responsible = row.EmployeeResponsible
    insert_query = """insert into territorydetails (Country,Zone,State,
     Region,Area,Depot,Tier,District,City,CityCode,Categorization,EmployeeResponsible)
      values ('{}','{}','{}','{}','{}','{}',{},'{}','{}','{}','{}','{}');""".format(
        country,
        zone,
        state,
        region,
        area,
        depot
        , tier,
        district,
        city,
        cityCode,
        category,
        employ_responsible

    )
    #print(insert_query)
    try:
        cursor.execute(insert_query)
    except Exception as e:
        print(e, insert_query)
conn.commit()
#print(cursor.rowcount, "record inserted.")

