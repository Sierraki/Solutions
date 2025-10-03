import sqlite3

conn = sqlite3.connect(r"x:\学习\研究生\代码数据库\else\123.sqlite")


def fun(a=str):
    # 创建游标
    cursor = conn.cursor()
    # 执行 SQL 语句
    cursor.execute(a)

    # 获取结果
    rows = cursor.fetchall()
    for row in rows:
        print(row)


fun("update users set age=1 where id=1")
fun("select *" "from users")
