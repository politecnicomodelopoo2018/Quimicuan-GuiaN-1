from Python_SQL import DB
from Py_SQL_Poder import Poder

DB().SetConnection('127.0.0.1','root', 'alumno', 'quinteros')

MenuPoder = None
unPoder = Poder()
MenuDios = None



""""while MenuPoder != 4:

    print("----------------------------")
    print("Poder -> Alta -> 0")
    print("Poder -> Baja -> 1")
    print("Poder -> Modificacion -> 2")
    print("Poder -> ListaDePoderes -> 3")
    print("Salir Del Programa -> 5")
    print("----------------------------")

    MenuPoder = int(input())

    if MenuPoder == 0:

        print("Descripcion Del Poder")

        Descripcion = input()
        unPoder.SetDescripcion(Descripcion)
        unPoder.Insert()


    if MenuPoder == 2:

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

    if MenuPoder == 1:

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

    if MenuPoder == 3:

        print("----------------------------")

        print("Lista De Poderes")

        print("----------------------------")

        listaPoderes = Poder.GetPoderes()

        for item in listaPoderes:
            print(" ID -> " + str(item.id) + " | " + item.descripcion)
            print("----------------------------")

        input() """"""