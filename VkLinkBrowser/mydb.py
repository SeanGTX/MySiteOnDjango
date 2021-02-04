import sqlite3, os
from VkLinkBrowser import settings

conn = sqlite3.connect(os.path())
cursor = conn.cursor()

a = cursor.execute("SELECT * FROM sqlite_master").fetchall()

for i in range(len(a)):
    print(a[i][1] + '  0')

