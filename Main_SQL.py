from Python_SQL import DB
from Py_SQL_Poder import Poder
from Py_SQL_Dios import Dios
from Py_SQL_Reino import Reino
from Py_SQL_Criatura import Criatura
from Py_SQL_DiosHasPoder import DHP

DB().SetConnection('127.0.0.1', 'root', 'alumno', 'quinteros')

Menu = None
unPoder = Poder()
unDios = Dios()
unReino = Reino()
unaCriatura = Criatura()
unDHP = DHP()


while Menu != 20:

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
    print("Criatura -> Alta -> 12")
    print("Criatura -> baja -> 13")
    print("Criatura -> Modificacion -> 14")
    print("Criatura -> ListaDeCriaturas -> 15")
    print("DHP -> Alta -> 16")
    print("DHP -> Baja -> 17")
    print("DHP -> Modificacion -> 18")
    print("DHP -> Lista De DHP's -> 19")
    print("Salir Del Programa -> 20")
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

        idReinoDelete = int(input())

        Pasaje = 0

        cursor = DB().run("SELECT * FROM Ciatura WHERE Reino_idReino = ('%d')" % (idReinoDelete))
        sasa = cursor.fetchall()
        if len(sasa) > 0:
            print("Un Reino No Puede Ser Eliminado Si Hay Criaturas Viviendo En El")
            Pasaje = 1
            input()

        cursor = DB().run("SELECT * FROM Dios WHERE Reino_idReino = ('%d')" % (idReinoDelete))
        sasa = cursor.fetchall()
        if len(sasa) > 0:
            print("Un Reino No Puede Ser Eliminado Si Hay Dioses Viviendo En El")
            Pasaje = 1
            input()

        if Pasaje == 0:
            unReino.Delete(idReinoDelete)


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

        PasajeCreacionDios = 0
        idReino = input()

        cursor = DB().run("SELECT * FROM Reino WHERE idReino = ('%d')" % (idReino))
        sasa = cursor.fetchall()
        if len(sasa) > 0:
            print("Reino Inexistente")
            PasajeCreacionDios = 1
            input()

        if PasajeCreacionDios == 0:
            unDios.SetidReino(idReino)

            unDios.Insert()

    if Menu == 5:
        print("----------------------------")

        print("Lista De Dioses")

        print("----------------------------")

        listaDioses = Dios.GetDioses()

        for item in listaDioses:
            print(" ID -> " + str(item.id) + " | " + item.Nombre + " | " + item.Deidad + " | " + item.Tipo + " | " + str(item.idReino))
            print("----------------------------")

        print("ID Del Dios A Eliminar")

        idDelete = int(input())
        PasajeDios = 0

        cursor = DB().run("SELECT * FROM Dios_has_Poder WHERE Dios_idDios = ('%d')" % (idDelete))
        sasa = cursor.fetchall()
        if len(sasa) > 0:
                print("No Se Puede Eliminar Un Dios Si Este Tiene Un Poder")
                PasajeDios = 1
                input()
        if PasajeDios == 0:
            unDios.Delete(idDelete)

    if Menu == 6:
        print("----------------------------")

        print("Lista De Dioses")

        print("----------------------------")

        listaDioses = Dios.GetDioses()

        for item in listaDioses:
            print(" ID -> " + str(item.id) + " | " + item.Nombre + " | " + item.Deidad + " | " + item.Tipo + " | " + str(item.idReino))
            print("----------------------------")

        print("ID Del Dios A Modificar")

        idUpdate = int(input())

        print("Nuevo Nombre")

        NombreRemp = input()

        print("Nueva Deidad")

        DeidadRemp = input()

        print("Nuevo Tipo")

        TipoRemp = input()

        print("Nuevo Reino")

        idReinoUpdate = input()

        unDios.Update(NombreRemp, DeidadRemp, TipoRemp, idReinoUpdate, idUpdate)

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
        PasajePoder = 0

        cursor = DB().run("SELECT * FROM Dios_has_Poder WHERE Poder_idPoder = ('%d')" % (idDelete))
        sasa = cursor.fetchall()
        if len(sasa) > 0:
                print("No Se Puede Eliminar Un Poder Si Es De Un Dios")
                PasajePoder = 1
                input()
        if PasajePoder == 0:
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

    if Menu == 12:
        print("Nombre De La Criatura")

        Nombre = input()
        unaCriatura.SetNombre(Nombre)

        print("Descripcion De La Criatura")

        Descripcion = input()
        unaCriatura.SetDescripcion(Descripcion)

        print("Traduccion De La Criatura")

        Traduccion = input()
        unaCriatura.SetTraduccion(Traduccion)

        print("ID Del Reino Al Que Pertenece")

        idReino = input()
        PasajeCreacionCriatura = 0

        cursor = DB().run("SELECT * FROM Ciatura WHERE Reino_idReino = ('%d')" % (idReino))
        sasa = cursor.fetchall()
        if len(sasa) > 0:
            print("Reino Inexistente")
            PasajeCreacionCriatura = 1
            input()

        if PasajeCreacionCriatura == 0:
            unaCriatura.SetidReino(idReino)

            unaCriatura.Insert()

    if Menu == 13:
        print("----------------------------")

        print("Lista De Criaturas")

        print("----------------------------")

        listaCriaturas = Criatura.GetCriaturas()

        for item in listaCriaturas:
            print(" ID -> " + str(item.id) + " | " + item.Nombre + " | " + item.Descripcion + " | " + item.Traduccion + " | " + str(item.idReino))
            print("----------------------------")

        print("ID De La Criatura A Eliminar")

        idDelete = int(input())

        unaCriatura.Delete(idDelete)

    if Menu == 14:
        print("----------------------------")

        print("Lista De Criaturas")

        print("----------------------------")

        listaCriaturas = Criatura.GetCriaturas()

        for item in listaCriaturas:
            print(" ID -> " + str(item.id) + " | " + item.Nombre + " | " + item.Descripcion + " | " + item.Traduccion + " | " + str(item.idReino))
            print("----------------------------")

        print("ID De La Criatura A Modificar")

        idUpdate = int(input())

        print("Nuevo Nombre")

        NombreRemp = input()

        print("Nueva Descripcion")

        DescRemp = input()

        print("Nueva Traduccion")

        TraductRemp = input()

        print("Nuevo Reino")

        idReinoRemp = input()

        unaCriatura.Update(NombreRemp, DescRemp, TraductRemp, idReinoRemp, idUpdate)

    if Menu == 15:
        print("----------------------------")

        print("Lista De Criaturas")

        print("----------------------------")

        listaCriaturas = Criatura.GetCriaturas()

        for item in listaCriaturas:
            print(" ID -> " + str(item.id) + " | " + item.Nombre + " | " + item.Descripcion + " | " + item.Traduccion + " | " + str(item.idReino))
            print("----------------------------")
        input()

    if Menu == 16:
        print("----------------------------")

        print("Lista De Dioses")

        print("----------------------------")

        listaDioses = Dios.GetDioses()

        for item in listaDioses:
            print(" ID -> " + str(item.id) + " | " + item.Nombre + " | " + item.Deidad + " | " + item.Tipo + " | " + str(item.idReino))
            print("----------------------------")

        print("----------------------------")

        print("Lista De Poderes")

        print("----------------------------")

        listaPoderes = Poder.GetPoderes()

        for item in listaPoderes:
            print(" ID -> " + str(item.id) + " | " + item.descripcion)
            print("----------------------------")

        input()

        print("ID Del Dios")

        idDios = input()
        unDHP.SetidDios(idDios)

        print("ID Del Poder")

        idPoder = input()
        unDHP.SetidPoder(idPoder)

        print("Cantidad De Poder")

        Cantidad = input()

        unDHP.SetCantidad(Cantidad)

        PasajeDHP = 0

        cursor = DB().run("SELECT * FROM Dios WHERE idDios = ('%d')" % (int(idDios)))
        sasa = cursor.fetchall()
        if len(sasa) > 0:
            PasajeDHP += 1

        cursor = DB().run("SELECT * FROM Poder WHERE idPoder = ('%d')" % (int(idPoder)))
        sasa = cursor.fetchall()
        if len(sasa) > 0:
            PasajeDHP += 1

        if PasajeDHP == 2:
            print("Este Dios Ya Tiene Ese Poder")
            input()

        if PasajeDHP != 2:
            unDHP.Insert()

    if Menu == 17:
        print("----------------------------")

        print("Lista DHP")

        print("----------------------------")

        listaDHP = DHP.GetDHP()

        for item in listaDHP:
            print(" ID-Dios-> " + str(item.idDios) + " ID-Poder-> " + str(item.idPoder) + " Cantidad-> " + str(item.Cantidad) + "%")
            print("----------------------------")

        input()

        print("ID Dios")

        idDiosDelete = input()

        print("ID Poder")

        idPoderDelete = input()

        unDHP.Delete(idDiosDelete, idPoderDelete)

    if Menu == 18:
        print("----------------------------")

        print("Lista DHP")

        print("----------------------------")

        listaDHP = DHP.GetDHP()

        for item in listaDHP:
            print(" ID-Dios-> " + str(item.idDios) + " ID-Poder-> " + str(item.idPoder) + " Cantidad-> " + str(
                item.Cantidad) + "%")
            print("----------------------------")

        input()

        print("ID Dios Inicial")

        idDiosUpdate = input()

        print("ID Poder Inicial")

        idPoderUpdate = input()

        print("ID Dios Remplazo")

        idDiosNuevo = input()

        print("ID Poder Remplazo")

        idPoderNuevo = print("Lista DHP")

        print("----------------------------")

        listaDHP = DHP.GetDHP()
        input()

        print("Nueva Cantidad")

        CantidadNueva = input()

        unDHP.Update(idDiosUpdate, idPoderUpdate, idDiosNuevo, idPoderNuevo, CantidadNueva)


    if Menu == 19:
        print("----------------------------")

        print("Lista DHP")

        print("----------------------------")

        listaDHP = DHP.GetDHP()

        for item in listaDHP:
            print(" ID-Dios-> " + str(item.idDios) + " ID-Poder-> " + str(item.idPoder) + " Cantidad-> " + str(item.Cantidad) + "%")
            print("----------------------------")

        input()


    if Menu > 20:
        print("Elegir Una Opcion Valida")
        input()