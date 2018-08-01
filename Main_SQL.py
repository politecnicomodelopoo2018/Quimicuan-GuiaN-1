from Python_SQL import DB
from Py_SQL_Poder import Poder

DB().SetConnection('127.0.0.1','root', 'alumno', 'quinteros')

Poder = Poder()

print("Poder -> Alta -> 0")
print("Poder -> Baja -> 1")
print("Poder -> Modificacion ->2")

Menu = None

while Menu != 3 :

    Menu = int(input())

    if Menu == 0:

        print("Descripcion Del Poder")

        Descripcion = input()

        Poder.SetDescripcion(Descripcion)
        Poder.Insert()

        runDB = DB().run("SELECT * FROM Poder")

    if Menu == 2:



        print("ID Del Poder A Modificar")

        idUpdate = int(input())

        print("Nueva Descripcion")

        DescRemp = input()

        Poder.Update(DescRemp, idUpdate)

    if Menu == 1:

        print("ID Del Poder A Eliminar")

        idDelete = int(input())

        Poder.Delete(idDelete)