import pandas as pd
import mysql.connector

test = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="sphi123",
    database="test"
)
cursor = test.cursor()

reader = pd.read_csv("sales_transaction.csv")
for i, row in reader.iterrows():
    print('counter ', i)
    Id = row.ID
    cusId = row.CUSTOMERID
    trans = row.TRANSACTIONDATE
    inv = row.INVOICETYPE
    sal = row.SALESORDERNUMBER
    bil = row.BILLINGINVOICENUMBER
    mat = row.MATERIALID
    order = row.ORDEREDQUANTITY
    zz = row.ZZWI11
    product = row.PRODUCTGROUP
    mag = row.MAGRV
    ProductCat = row.PRODUCTCATEGORY
    ReturnAmount = row.RETURNAMOUNT
    sale = row.SALE
    billed = row.BILLEDAMOUNT
    insert_query = """insert into sales_transaction (ID,	CUSTOMERID,TRANSACTIONDATE,	INVOICETYPE,	SALESORDERNUMBER,	BILLINGINVOICENUMBER,	MATERIALID,	ORDEREDQUANTITY,	ZZWI11,	PRODUCTGROUP,	MAGRV,	PRODUCTCATEGORY,	RETURNAMOUNT,	SALE,	BILLEDAMOUNT
) values ('{}',{},'{}','{}',{},'{}',{},{},{},'{}','{}','{}',{},{},{});""".format(
        Id,
        cusId,
        trans,
        inv,
        sal,
        bil,
        mat,
        order,
        zz,
        product,
        mag,
        ProductCat,
        ReturnAmount,
        sale,
        billed
    )
    # print(insert_query)
    try:
        cursor.execute(insert_query)
    except Exception as e:
        print(e, insert_query)

test.commit()
# print(cursor.rowcount, "record inserted.")
