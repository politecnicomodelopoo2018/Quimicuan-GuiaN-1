from Python_SQL import DB
from Py_SQL_Poder import Poder
from Py_SQL_Dios import Dios
from Py_SQL_Reino import Reino

DB().SetConnection('127.0.0.1','root', 'alumno', 'quinteros')

Menu = None
unPoder = Poder()
unDios = Dios()
unReino = Reino()


while Menu != 12:

    print("----------------------------")
    print("Reino -> Alta -> 0")
    print("Reino -> Baja -> 1")
    print("Reino -> Modificacion -> 2")
    print("Reino -> ListaDeReinos -> 3")
    print("Dios -> Alta -> 4")
    print("Dios -> Baja -> 5")
    print("Dios -> Modificacion -> 6")
    print("Dios -> ListaDeDioses -> 7")
    print("Poder -> Alta -> 8")
    print("Poder -> Baja -> 9")
    print("Poder -> Modificacion -> 10")
    print("Poder -> ListaDePoderes -> 11")
    print("Salir Del Programa -> 12")
    print("----------------------------")

    Menu = int(input())

    if Menu == 0:
        print("Descripcion Del Reino")

        Descripcion = input()
        unReino.SetDescripcion(Descripcion)

        print("Caracteristicas Del Reino")

        Caracteristica = input()
        unReino.SetCaracteristica(Caracteristica)

        unReino.Insert()

    if Menu == 1:
        print("----------------------------")

        print("Lista De Reinos")

        print("----------------------------")

        listaReinos = Reino.GetReinos()

        for item in listaReinos:
            print(" ID -> " + str(item.id) + " | " + item.descripcion + " | " + item.caracteristica)
            print("----------------------------")

        print("ID Del Reino Eliminar")

        idReino = int(input())

        unReino.Delete(idReino)

    if Menu == 2:
        print("----------------------------")

        print("Lista De Reinos")

        print("----------------------------")

        listaReinos = Reino.GetReinos()

        for item in listaReinos:
            print(" ID -> " + str(item.id) + " | " + item.descripcion + " | " + item.caracteristica)
            print("----------------------------")

        print("ID Del Reino A Modificar")

        idUpdate = int(input())

        print("Nueva Descripcion")

        DescripcionRemp = input()

        print("Nueva Caracteristica")

        CaracteristicaRemp = input()

        unReino.Update(DescripcionRemp, CaracteristicaRemp, idUpdate)

    if Menu == 3:
        print("----------------------------")

        print("Lista De Reinos")

        print("----------------------------")

        listaReinos = Reino.GetReinos()

        for item in listaReinos:
            print(" ID -> " + str(item.id) + " | " + item.descripcion + " | " + item.caracteristica)
            print("----------------------------")

        input()

    if Menu == 4:
        print("Nombre Del Dios")

        Nombre = input()
        unDios.SetNombre(Nombre)

        print("Deidad Del Dios")

        Deidad = input()
        unDios.SetDeidad(Deidad)

        print("Tipo De Dios")

        Tipo = input()
        unDios.SetTipo(Tipo)

        print("ID Del Reino Al Que Pertenece")

        idReino = input()
        unDios.SetidReino(idReino)

        unDios.Insert()

    if Menu == 5:
        print("----------------------------")

        print("Lista De Dioses")

        print("----------------------------")

        listaDioses = Dios.GetDioses()

        for item in listaDioses:
            print(" ID -> " + str(item.id) + " | " + item.Nombre + " | " + item.Deidad + " | " + item.Tipo)
            print("----------------------------")

        print("ID Del Dios A Eliminar")

        idDelete = int(input())

        unDios.Delete(idDelete)

    if Menu == 6:
        print("----------------------------")

        print("Lista De Dioses")

        print("----------------------------")

        listaDioses = Dios.GetDioses()

        for item in listaDioses:
            print(" ID -> " + str(item.id) + " | " + item.Nombre + " | " + item.Deidad + " | " + item.Tipo + " | " + item.idReino)
            print("----------------------------")

        print("ID Del Dios A Modificar")

        idUpdate = int(input())

        print("Nuevo Nombre")

        NombreRemp = input()

        print("Nueva Deidad")

        DeidadRemp = input()

        print("Nuevo Tipo")

        TipoRemp = input()

        unDios.Update(NombreRemp, DeidadRemp, TipoRemp,  idUpdate)

    if Menu == 7:
        print("----------------------------")

        print("Lista De Dioses")

        print("----------------------------")

        listaDioses = Dios.GetDioses()

        for item in listaDioses:
            print(" ID -> " + str(item.id) + " | " + item.Nombre + " | " + item.Deidad + " | " + item.Tipo + " | " + str(item.idReino))
            print("----------------------------")
        input()

    if Menu == 8:

        print("Descripcion Del Poder")

        Descripcion = input()
        unPoder.SetDescripcion(Descripcion)
        unPoder.Insert()


    if Menu == 10:

        print("----------------------------")

        print("Lista De Poderes")

        print("----------------------------")

        listaPoderes = Poder.GetPoderes()

        for item in listaPoderes:
            print(" ID -> " + str(item.id) + " | " + item.descripcion)
            print("----------------------------")

        print("ID Del Poder A Modificar")

        idUpdate = int(input())

        print("Nueva Descripcion")

        DescRemp = input()

        unPoder.Update(DescRemp, idUpdate)

    if Menu == 9:

        print("----------------------------")

        print("Lista De Poderes")

        print("----------------------------")

        listaPoderes = Poder.GetPoderes()

        for item in listaPoderes:
            print(" ID -> " + str(item.id) + " | " + item.descripcion)
            print("----------------------------")

        print("ID Del Poder A Eliminar")

        idDelete = int(input())

        unPoder.Delete(idDelete)

    if Menu == 11:

        print("----------------------------")

        print("Lista De Poderes")

        print("----------------------------")

        listaPoderes = Poder.GetPoderes()

        for item in listaPoderes:
            print(" ID -> " + str(item.id) + " | " + item.descripcion)
            print("----------------------------")

        input()