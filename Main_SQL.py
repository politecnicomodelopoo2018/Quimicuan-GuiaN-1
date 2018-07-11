from Python_SQL import DB
from Py_SQL_Poder import Poder

DB().SetConnection('127.0.0.1','root', 'alumno', 'quinteros')

Poder = Poder()

Poder.SetId(1)
Poder.SetDescripcion("Rayo")
Poder.Insert()

runDB = DB().run("SELECT * FROM Poder")