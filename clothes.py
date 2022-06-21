import sqlite3
import csv
import os.path

save_path = '/Users/user/Desktop/unnowedformesecondname'

os.path.join

class Сlothes:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

    days_options = (
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
    )

    materials_options = [
        "leather",
        "cotton ",
        "linen  ",
        "wool   "
    ]

    color_options = [
        "black  ",
        "white  ",
        "red    "
    ]

    cntroforigin_options = [
        "Ukraine",
        "Poland ",
        "Spain  ",
        "India  ",
        "China  "
    ]

    def addcolor(self, color):
        self.color_options.append(color)

    def addmaterials(self, mater):
        self.materials_options.append(mater)

    def addcntryoforigin(self, origin):
        self.cntroforigin_options.append(origin)

    def sorted(self):
        self.cntroforigin_options.sort()
        self.materials_options.sort()
        self.color_options.sort()

    def rev(self):
        self.cntroforigin_options.reverse()
        self.materials_options.reverse()
        self.color_options.reverse()

    def delcolor(self, color):
        self.color_options.pop(color)

    def delmaterials(self, mater):
        self.materials_options.pop(mater)

    def delcntryoforigin(self, origin):
        self.cntroforigin_options.pop(origin)

    # ============================== Lab 5 =============================================================================

    def textfile(self, x):
        completeName = os.path.join(save_path, "info.txt")
        try :
            f = open(completeName, "a+")
            result1 = self.cursor.execute(
            "SELECT `name`, `materials`, `dayofbuy`, `countryoforigin`, `color` FROM `JacketsBD` WHERE `id` = ?", (x,))
            result1 = ', '.join(result1.fetchall()[0])
            f.write("Файл номер " + str(x) + " " + result1 + "\n")
        except:
            f = open(completeName, "w+")
            result1 = self.cursor.execute("SELECT `name`, `materials`, `dayofbuy`, `countryoforigin`, `color` FROM `JacketsBD` WHERE `id` = ?", (x,))
            result1 = ', '.join(result1.fetchall()[0])
            f.write("Файл номер " + str(x) + " " +result1)

    def csvfile(self, x):
        try:
            completeName = os.path.join(save_path, "info.csv")
            with open(completeName, 'w', newline='') as csvfile:
                result1 = self.cursor.execute(
                    "SELECT `name`, `materials`, `dayofbuy`, `countryoforigin`, `color` FROM `JacketsBD` WHERE `id` = ?",
                    (x,))
                result1 = result1.fetchall()
                writer = csv.writer(csvfile)
                writer.writerows(result1)

        except:
            with open(completeName, newline='') as csvfile:
                result1 = self.cursor.execute(
                    "SELECT `name`, `materials`, `dayofbuy`, `countryoforigin`, `color` FROM `JacketsBD` WHERE `id` = ?",
                    (x,))
                result1 = result1.fetchall()
                writer = csv.writer(csvfile)
                writer.writerows(result1)

    def binfile(self, x):
        completeName = os.path.join(save_path, "info.bin")
        try:
            with open(completeName, 'wb') as binfile:
                result1 = self.cursor.execute(
                    "SELECT `name`, `materials`, `dayofbuy`, `countryoforigin`, `color` FROM `JacketsBD` WHERE `id` = ?",
                    (x,))
                result1 = ', '.join(result1.fetchall()[0])
                b = bytes(result1, 'utf-8')
                binfile.write(b)
        except:
            with open(completeName) as binfile:
                result1 = self.cursor.execute(
                    "SELECT `name`, `materials`, `dayofbuy`, `countryoforigin`, `color` FROM `JacketsBD` WHERE `id` = ?",
                    (x,))
                result1 = ', '.join(result1.fetchall()[0])
                b = bytes(result1, 'utf-8')
                binfile.write(b)

class Jackets(Сlothes):
    def display_full_name(self, val, photo, entry, mat, day, count, col):
        self.cursor = self.conn.cursor()

        self.cursor.execute(
            "insert into `JacketsBD` (`name`, `photo`, `materials`, `dayofbuy`, `countryoforigin`, `color`) values (?,?,?,?,?,?)",
            (val, photo, mat, day, count, col))
        self.conn.commit()
        entry.delete(0, 'end')

    def checkres1(self, y):
        result1 = self.cursor.execute(
            "SELECT `name`, `materials`, `dayofbuy`, `countryoforigin`, `color` FROM `JacketsBD` WHERE `id` = ?", (y,))
        result1 = '\n'.join(result1.fetchall()[0])
        return result1

    def checkres2(self, y):
        result2 = self.cursor.execute("SELECT (`photo`) FROM `JacketsBD` WHERE `id` = ?", (y,))
        return result2.fetchone()[0]
