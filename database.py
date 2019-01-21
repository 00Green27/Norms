import sqlite3 as lite
import settings

class DbHandler:
    """ """

    def __init__(self, database):
        self.database = database

    def open(self):
        self.con = lite.connect(self.database)
        self.con.text_factory = lite.OptimizedUnicode

    def close(self):
        self.con.close()

    def commit(self):
        self.con.commit()

    def execute(self, query):
        cur = self.con.cursor()

        try:
            cur.execute(query)
            return cur.fetchall()
        finally:
            cur.close()

    def vacuum(self):
        self.con.execute("VACUUM")

    def execute(self, query, params):
        cur = self.con.cursor()

        try:
            if params is None:
                cur.execute(query)
            else:
                cur.execute(query, params)
            return cur.fetchall()
        finally:
            cur.close()

    def insert1(self, query, params):
        cur = self.con.cursor()

        try:
            cur.execute(query, params)
        finally:
            cur.close()

    def nextDeptId(self):
        return self.execute("select max(id) from departments", ())[0][0] + 1

    def deleteDepts(self, params):
        self.insertMany("delete from departments where id=? and name=?", params)

        dept_ids = []
        for id, name in params:
            dept_ids.append((id,))
        self.insertMany("delete from norms where department_id = ?", dept_ids)


    def insertDepts(self, params):
        self.insertMany("insert or replace into departments(id, name) values(?, ?)", params)

    #        id = self.execute("Select last_insert_rowid()", ())
    #        print id
    #        params = []
    #        for h in xrange(1, 10):
    #            params.append((id[0][0], h, 10))
    #        self.insertMany("insert or replace into norms(department_id, hardware_id, norm) values(?,?,?)", params)

    def insert(self, query):
        cur = self.con.cursor()

        try:
            cur.execute(query)
        finally:
            cur.close()

    def deleteEquipment(self, dept_id):
        cur = self.con.cursor()

        try:
            cur.execute("delete from equipment where department_id=?", (dept_id, ))
        finally:
            cur.close()

    def insertMany(self, query, params):
        cur = self.con.cursor()

        try:
            cur.executemany(query, params)
        finally:
            cur.close()

    def insert_equipment(self, equipment):
        self.insert1("insert into equipment(number, name, inventory_number, year, cost, amount, department_id, hardware_id) values (?,?,?,?,?,?,?,?)", equipment)

    def insertEquipments(self, data, dept):
        cur = self.con.cursor()

        try:
            cur.execute("delete from equipment where department_id = ?", (dept, ))
            cur.executemany(
                "insert into equipment(number, name, inventory_number, year, cost, amount, department_id, hardware_id) values(?,?,?,?,?,?,?,?)"
                , data)
        finally:
            cur.close()


    def insertNorms(self, params):
        cur = self.con.cursor()

        try:
            dept = int(params[0][0])
            cur.execute("delete from norms where department_id = ?", (dept, ))
            cur.executemany(
                "insert or replace into norms(department_id, hardware_id, norm) values(?,?,?)"
                , params)
        finally:
            cur.close()

    def insertHardware(self, params):
        cur = self.con.cursor()

        try:
            cur.executemany(
                "update hardware set service=?, cost=? where id = ?"
                , params)
        finally:
            cur.close()

    def getDeptName(self, id):
        cur = self.con.cursor()

        try:
            cur.execute("select name from departments where id=?", (id,))
            return cur.fetchone()[0]
        finally:
            cur.close()

    def getDeptId(self, name):
        cur = self.con.cursor()

        try:
            cur.execute("select id from departments where name=?", (name,))
            return int(cur.fetchone()[0])
        finally:
            cur.close()

    def getDepts(self):
        cur = self.con.cursor()

        try:
            cur.execute("select id, name from departments")
            temp = []
            for id, name in cur.fetchall():
                temp.append([id, name])
            return temp
        finally:
            cur.close()


    def getHardware(self):
        return self.execute("select id,name from hardware order by id", None)

    def getNorms(self, dept):
        cur = self.con.cursor()

        try:
            cur.execute("select norm from norms where department_id = ? order by hardware_id", (dept,))
            return cur.fetchall()
        finally:
            cur.close()

    def getHardwareNames(self):
        cur = self.con.cursor()

        try:
            cur.execute("select name from hardware order by id")
            return cur.fetchall()
        finally:
            cur.close()

    def getHardwareInfo(self):
        cur = self.con.cursor()

        try:
            cur.execute("select service, cost from hardware order by id")
            return cur.fetchall()
        finally:
            cur.close()

    def getEquipment(self, dept):
        cur = self.con.cursor()
        try:
            cur.execute("""
SELECT e.number,
       e.name,
       e.inventory_number,
       e.year,
       CASE
         WHEN e.cost = '' THEN 0
         ELSE e.cost
       END cost,
       e.amount,
       e.hardware_id,
       h.name,
       e.id
FROM   equipment e
left join hardware h on e.hardware_id = h.id
WHERE  e.department_id = ?
order by hardware_id, year desc
				""", (dept,))
            return cur.fetchall()
        finally:
            cur.close()

    def getEquipmentByHardware(self, opt):
        cur = self.con.cursor()
        try:
            cur.execute("""
SELECT e.number,
       e.name,
       e.inventory_number,
       e.year,
       CASE
         WHEN e.cost = '' THEN 0
         ELSE e.cost
       END cost,
       e.amount,
       e.hardware_id,
       h.name,
       e.id
FROM   equipment e
left join hardware h on e.hardware_id = h.id
WHERE  e.department_id = ? and e.hardware_id = ?
order by hardware_id, year desc
				""", opt)
            return cur.fetchall()
        finally:
            cur.close()

    def getTimesheetEx(self, dept):
        cur = self.con.cursor()

        try:
            cur.execute(
                "select name, amount, norm,retirement,need,cost_for_one,cost,no_retirement_cost,retirement_cost from timesheet where department_id = ?"
                , (dept,))
            return cur.fetchall()
        finally:
            cur.close()

    def getTimesheet(self, dept):
        cur = self.con.cursor()

        try:
            #  count(coalesce(amount, 1))
            cur.execute("""
SELECT *,
        need * cost_for_one cost,
        CASE 
            WHEN (norm - amount) * cost_for_one > 0
            THEN (norm - amount) * cost_for_one
            ELSE 0
            END no_retirement_cost,
        retirement * cost_for_one retirement_cost
  FROM
          (SELECT h.name name,
                  coalesce(e.amount, 0) amount,
                  n.norm norm,
                  coalesce(r.retirement, 0) retirement,
                  CASE
                    WHEN n.norm = 0
                    THEN 0
                          ELSE n.norm - (coalesce(e.amount, 0) - coalesce(r.retirement, 0))
                          END need,
                  h.cost cost_for_one
            FROM hardware h
                    LEFT JOIN
                    (SELECT hardware_id id,
                            sum(coalesce(amount, 1)) amount
                      FROM equipment e
                      WHERE e.department_id = ?
                      GROUP BY hardware_id) e ON e.id = h.id
                    JOIN norms n ON n.hardware_id = h.id
                    LEFT JOIN
                    (SELECT h.id id,
                            sum(CASE WHEN (? - e.year) >= h.service THEN 1 ELSE 0 END) retirement
                      FROM equipment e
                              JOIN hardware h ON h.id = e.hardware_id
                      WHERE e.department_id = ?
                      GROUP BY h.id) r ON r.id = h.id
            WHERE n.department_id = ?)
 			""", (dept, settings.YEAR, dept, dept))
            return cur.fetchall()
        finally:
            cur.close()

    def getGlobalTimesheet(self):
        cur = self.con.cursor()

        try:
            cur.execute("""
SELECT  name,
        amount,
        norm,
        retirement,
        need,
        cost_for_one,
        need * cost_for_one cost,
        CASE
            WHEN (norm - amount) * cost_for_one > 0
            THEN (norm - amount) * cost_for_one
            ELSE 0
            END no_retirement_cost,
        retirement * cost_for_one retirement_cost
  FROM
          (SELECT h.name name,
                  coalesce(e.amount, 0) amount,
                  n.norm norm,
                  coalesce(r.retirement, 0) retirement,
                  CASE
                    WHEN n.norm = 0
                    THEN 0
                          ELSE n.norm - (coalesce(e.amount, 0) - coalesce(r.retirement, 0))
                          END need,
                  h.cost cost_for_one, h.id id
            FROM hardware h
                    LEFT JOIN
                    (SELECT hardware_id id,
                            count(amount) amount
                      FROM equipment e
                      GROUP BY hardware_id) e ON e.id = h.id
                    JOIN norms n ON n.hardware_id = h.id
                    LEFT JOIN
                    (SELECT h.id id,
                            sum(CASE WHEN (? - e.year) >= h.service THEN 1 ELSE 0 END) retirement
                      FROM equipment e
                              JOIN hardware h ON h.id = e.hardware_id
                      GROUP BY h.id) r ON r.id = h.id)
                      group by id
 			""", (settings.YEAR,))
            return cur.fetchall()
        finally:
            cur.close()

    def delete_hardware(self, id):
        self.execute("delete from equipment where id = ? ", (id, ))

    def getEquipments(self):
        cur = self.con.cursor()

        try:
            cur.execute("""
select name,
       coalesce(e1, 0),
       coalesce(e2, 0),
       coalesce(e3, 0),
       coalesce(e4, 0),
       coalesce(e5, 0),
       coalesce(e6, 0),
       coalesce(e7, 0),
       coalesce(e8, 0),
       coalesce(e9, 0),
       coalesce(e10, 0)
from departments dialog
left join (
select  department_id id,
        sum(case when hardware_id=1 then 1 else 0 end) as e1,
        sum(case when hardware_id=2 then 1 else 0 end) as e2,
        sum(case when hardware_id=3 then 1 else 0 end) as e3,
        sum(case when hardware_id=4 then 1 else 0 end) as e4,
        sum(case when hardware_id=5 then 1 else 0 end) as e5,
        sum(case when hardware_id=6 then 1 else 0 end) as e6,
        sum(case when hardware_id=7 then 1 else 0 end) as e7,
        sum(case when hardware_id=8 then 1 else 0 end) as e8,
        sum(case when hardware_id=9 then 1 else 0 end) as e9,
        sum(case when hardware_id=10 then 1 else 0 end) as e10
from equipment e
group by department_id
order by department_id
) e on e.id = dialog.id
 			""")
            return cur.fetchall()
        finally:
            cur.close()

    def insert(self, dept, h):
        cur = self.con.cursor()

        try:
            #cur.execute("delete from norms")
            cur.execute(
                "insert into norms(department_id, hardware_id, norm) values(?,?,0)"
                , (int(dept), int(h)))
        finally:
            cur.close()

if __name__ == '__main__':
    mydb = DbHandler('norm.db')
    mydb.open()
    #sheet = mydb.getTimesheet(2)
    #equipment = mydb.getEquipment(2)
#    for dept in xrange(1, 74):
#      for h in xrange(1, 11):
#        print dept, h
#        mydb.insert(dept, h)
#    mydb.commit()
    mydb.close()

    #for r in equipment:
    #    print(r)