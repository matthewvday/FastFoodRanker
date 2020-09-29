import mysql.connector

if __name__ == '__main__':
    mydb = mysql.connector.connect(
        host="fastfoodranker.c8xlhqhgdgzu.us-east-2.rds.amazonaws.com",
        #user="",
        #password="",
        database="FastFoodRanker"
    )

    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM reviews")

    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)