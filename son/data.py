
import sqlite3


def fetchdata():
    connection = sqlite3.connect('urunler.db')
    connection.execute("CREATE TABLE IF NOT EXISTS urunler(id INTEGER PRIMARY KEY,  firmaadi TEXT, adres TEXT, tarih TEXT, \
        tarih2  TEXT, urunadi TEXT, miktar TEXT, plaka TEXT, numara TEXT, aciklama TEXT);")
    connection.commit()
    connection.close()

fetchdata()