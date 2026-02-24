import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Lohesh14!"
)
mycursor = mydb.cursor()
mycursor.execute("USE flip")

def newuser(uname,psw):
    mycursor.execute(f"SELECT * FROM flipkart WHERE username='{uname}'")
    if mycursor.fetchall():
      #  print("user already exists")
        return False
        
    mycursor.execute(
        "INSERT INTO flipkart (username,password) VALUES (%s,%s)",
        (uname,psw)
    )
    mydb.commit()
    return True

def loginuser(uname,psw):
    mycursor.execute(f"SELECT password FROM flipkart WHERE username='{uname}'")
    p = mycursor.fetchone()
    if p and psw==p[0]:
        print("User verified!")
        return True
    return False