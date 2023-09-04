
# import sqlite3

# db = sqlite3.connect('test.db')

# sql = db.cursor()

# sql.execute('CREATE TABLE IF NOT EXISTS data (ad TEXT, soyad TEXT, yas INT)')

# sql.execute("INSERT INTO data (ad,soyad,yas) VALUES ('Fuad','Aliyev', 20)")

# db.commit()

# sql.execute("SELECT * FROM data ")

# for i in sql:
#     print(i)   ekrana çıxarmağın bir yolu


# print(sql.fetchall()) hamısını çıxardır
# print(sql.fetchone()) 1ni çıxardır , neyi isteyirsense ulduzun yerine onu yaz
# db.commit()

# sql.execute("SELECT * FROM data WHERE ad = 'Fuad'")

# print(sql.fetchone())

# db.commit()

# sql.execute("UPDATE data SET ad = 'Aslan' ")

# db.commit()

# ad = 'Nuray'

# soyad = 'Necefli'

# yas = 22

# sql.execute(f"INSERT INTO data (ad,soyad,yas) VALUES ('{ad}','{soyad}','{yas}') " )

# db.commit()



# sql.execute("DELETE FROM data ")

# db.commit()          hamisini silir


# ad = input(' ad secin : ')

# sql.execute(f"DELETE FROM data WHERE ad == '{ad}' ")

# db.commit() 




# import sqlite3

# db = sqlite3.connect('data.db')

# sql = db.cursor()

# sql.execute("""
            
#             CREATE TABLE IF NOT EXISTS test (ID INTEGER PRIMARY KEY AUTOINCREMENT , metn TEXT )
            
#             """)

# sql.execute("INSERT INTO test (metn) VALUES ('Hello World') ")

# db.commit()

# sql.execute(" SELECT * FROM data WHERE ID = 2")

# print(sql.fetchone())   ID ile cixarmaq


# sql.execute("INSERT INTO test(metn) VALUES ('Python')  ")

# db.commit()


# sql.execute("INSERT INTO test(metn) VALUES ('GO')")



# sql.execute(" SELECT * FROM test ORDER BY ID DESC ")

# for x in sql:
#     print(x)      #TERMINALA SIRALAMANI TERSDEN GOSTERIR

# db.commit()


# sql.execute(" SELECT * FROM test LIMIT 0,2")

# for x in sql:
#     print(x) 

# db.commit()




# sql.execute(" SELECT DICTINCT FROM test " )

# for x in sql:
#     print(x)       IKI DENE OLANLARDAN 1 DENE CIXARDIR

# db.commit()




# sql.execute("DROP TABLE test")

# db.commit()   herseyi silir


# sql.execute(" SELECT COUNT (*) FROM data")

# for x in sql:
#     print(x)    sayir


# import sqlite3

# from random import randint

# db = sqlite3.connect(' data.db ')

# sql = db.cursor()

# sql.execute( " CREATE TABLE IF NOT EXISTS data ( login TEXT, password INT, cash INT)")

# # sql.execute( " CREATE TABLE IF NOT EXISTS data1 ( login TEXT, metn TEXT, email TEXT)")

# sql.execute( " SELECT * FROM data,data1 WHERE data.login == data1.login")

# print(sql.fetchall())



import sqlite3

db = sqlite3.connect(' atm.db ')

sql = db.cursor()

sql.execute (" CREATE TABLE IF NOT EXISTS atm ( pin INT, cash INT) ")
 
pin = int(input(" pin kodu daxil edin: "))

sql.execute( f" SELECT pin FROM atm WHERE pin == '{pin}' ")

if pin in sql.fetchone():

    while True:

        secim = int(input("""
                        
        (1) balansi yoxla \n
                        
        (2) Kartdan pul cixar \n
                        
        (3) Karta medaxil et \n    
                        
        (4) Pini deyis \n

        (5) cixis et \n                                  
                        
                        """))
        
        if secim == 1:

            

            sql.execute( f"SELECT cash FROM atm WHERE pin ='{pin}' " )

            print(sql.fetchone())

            break


        if secim == 2:

            cash =int(input(" meblegi daxil edin"))

            sql.execute( f" UPDATE atm SET cash = cash - '{cash}' WHERE pin = '{pin}' ")

            db.commit()

            print('mebleg +' +str(cash))

            break
        if secim == 3:

            cash =int(input(" meblegi daxil edin"))

            sql.execute( f" UPDATE atm SET cash = cash - '{cash}' WHERE pin = '{pin}' ")

            db.commit()

            sql.execute(f" SELECT cash FROM atm WHERE pin = '{pin}' " )

            for x in sql:
                print(' Umumi mebleg' + str(x))

            break

        if secim == 4:
            pass1 = int(input('pini daxil edin : '))
            pass2 = int(input('pini daxil edin : '))

            if pass1 == pass2:

                sql.execute(f"UPDATE atm SET pin == '{pass2}' WHERE pin == '{pin}' " )

                db.commit()

                print('ugurla deyisdirildi')
            
            else:
                print('daxil etdiyiniz pin kodlar eyni deyil')


            break

        if secim == 5:
            
            sql.execute( "DELETE FROM atm WHERE pin = '{pin}' ")

            db.commit()

            print("ugurla cixis etdiniz")

            break

        




            

            
           

else:
    print("pin yalnisdir") 

