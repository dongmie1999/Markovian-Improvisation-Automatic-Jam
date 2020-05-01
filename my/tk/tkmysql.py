import pymysql

def submit(stock,good,provider):
    db = pymysql.connect("localhost", "root", "2333", "final", charset='utf8' )
    cursor = db.cursor()
      
    sql = "INSERT INTO Stock (StockID,ProductID,ProviderID) VALUES ("
    sql = sql+str(stock)+",'"+good+"','"+provider+"')"
    print(sql)
    
    try:
        cursor.execute(sql)
        db.commit()
        print("sql done")
    except:
        db.rollback()
        print("sql defend")
    
    db.close()

def select():#在数据库的表中查找名为sn的歌曲的分数
    db = pymysql.connect("localhost", "root", "2333", "final", charset='utf8' )
    cursor = db.cursor()
    
    # SQL 查询语句
    select = "SELECT * FROM Provider"

    PID = []
    try:
        cursor.execute(select)
        results = cursor.fetchall()
        for row in results:#按照字段顺序
            PID.append(row[0])
        return PID
    except:
        print ("Error: unable to fecth data")
        
    # 关闭数据库连接
    db.close()

#s =select()
#print(s)



