import mysql.connector as MySQLdb
def register (username, user_password, name, gender):
    try:
        db_connection = MySQLdb.connect(user='root',password='',
                                         host='localhost',database='tb_pygame')
        cursor = db_connection.cursor()
        sql = "INSERT INTO tbl_user(username, password, full_name, gender) VALUES (%s,%s,%s,%s)"
        val=(username, user_password, name, gender)
        cursor.execute(sql, val)

        db_connection.commit()
        user_id=cursor.lastrowid
        db_connection.close()

        if user_id:
            return True
    except Exception as e:
        print("Database error occurred")
        print (e)
    finally:
        # db_connection.close()
        pass
    return False   
# register('jevins', '1234', 'Jevins', 'male')

def login(username, user_password): # username and user_password are parametres of the function login
    try:
        db_connection = MySQLdb.connect(user='root',password='',
                                         host='localhost',database='tb_pygame') # MySQLdb.connect is a systen defined function for connecting to the database
        cursor = db_connection.cursor()
        sql = "select * from tbl_user where username = %s and password = %s"
        val=(username, user_password)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if result:
            return True # return is the output of the function

    except Exception as e:
        print("Database error occured")
        print (e)
    return False

# Save_score is the name of the function
# Def keyword is used to define a function
# Score and username are parameters (input) to the function
def save_score(score, username): 

    try:
        db_connection = MySQLdb.connect(user='root' , password='' , host='localhost' , database='tb_pygame')
        cursor = db_connection.cursor()
        sql = "SELECT user_id FROM tbl_user WHERE username = '" + username + "'"
        print(sql)
        cursor.execute(sql)
        results = cursor.fetchall()
        userid = results [0][0]
        
        sql = "INSERT INTO tbl_score VALUES(null, %s , %s , now())"
        val=(str(userid), str(score))
        cursor.execute(sql, val)

        db_connection.commit()
        score_id=cursor.lastrowid
        db_connection.close()
        if score_id:
            return True
    except Exception as e:
        print("Database error occurred")
        print(e)
    return False # Return is the output of the function
    

 


def high_scores():
    try:
        db_connection = MySQLdb.connect(user='root' , password='' , host='localhost' , database='tb_pygame')
        cursor = db_connection.cursor()
        sql = "SELECT full_name, score, game_day_time FROM tbl_score join tbl_user on user_id=fk_user_id ORDER By score DESC LIMIT 10"
        cursor.execute(sql)
        results = cursor.fetchall()
        txt = "         <b><u><HIGH SCORES</u></b>              <br>"
        txt += "<b>Name         Score           Date            Time</b><br>"
        for row in results:
            txt+=str(row [0])+"         "+str(row[1])+"         "+str(row[2])[:10]+"            "+str(row[2])[10:]+"<br>"

        return txt 
        db_connection.close()            
    except Exception as e:
        print("Database error occurred")
        print(e)
    return False


# lst = ['g' , 'm', 'k']
# length = 3
# lst[0] = 'g'
# lst[1] = 'm'
# lst[2] = 'k'
# lst[3] = Error