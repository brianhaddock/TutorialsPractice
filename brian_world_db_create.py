import sqlite3

c = sqlite3.connect("D:\\Users\\Brian\\OneDrive\\Projects\\Python\\brian_world.db")

c.execute("insert into actions values (NULL, 'dog growl')")
c.execute("insert into actions values (NULL, 'dog barkl')")
c.execute("insert into actions values (NULL, 'dog bitel')")
c.execute("insert into actions values (NULL, 'dog lick')")
c.execute("insert into actions values (NULL, 'dog whimper')")
c.execute("insert into actions values (NULL, 'dog howl')")
c.execute("insert into actions values (NULL, 'dog sleep')")
c.execute("insert into actions values (NULL, 'dog eat')")

c.commit()