import sqlite3

conn = sqlite3.connect("db.sqlite3")


def init():
    c = conn.cursor()
    sql = "create table if not exists content(isbn text, title text);"
    c.execute(sql)
    sql = "create table if not exists links(url text, mimetype text, isbn text, FOREIGN KEY (isbn) REFERENCES content (isbn) ON DELETE CASCADE ON UPDATE NO ACTION);"
    c.execute(sql)


init()
