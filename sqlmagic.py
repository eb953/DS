import csv, sqlite3, pandas

con = sqlite3.connect("socioeconomic.db")
cur = con.cusor() 