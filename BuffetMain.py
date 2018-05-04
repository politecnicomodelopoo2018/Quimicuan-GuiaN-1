from BuffetPersona import Alumno
from BuffetPersona import Profesor
from BuffetPlato import Plato
from BuffetPedido import Pedido
from BuffetBuffet import Buffet

A = True
Jorge = Alumno()
Pruchi = Profesor()
Buffes = Buffet()
Plato1 = Plato()
Pedido1 = Pedido()

while A:

    Opcion = None

    Opcion = int(input())

    if Opcion == 1: ##AgAlumno

        Nombre = input()
        Jorge.SetNombre(Nombre)

        Apellido = input()
        Jorge.SetApellido(Apellido)

        Division = input()
        Jorge.SetDivision(Division)

        Buffes.Persona.append(Jorge)

        print("<AlumnoAgregado>")

    if Opcion == 2: ##AgProf

        Nombre = input()
        Pruchi.SetNombre(Nombre)

        Apellido = input()
        Pruchi.SetApellido(Apellido)

        Descuento = input()
        Pruchi.SetDescuento(Descuento)

        Buffes.Persona.append(Pruchi)

        print("<ProfesorAgregado>")

    if Opcion == 3: ##ModPersona

        Nombre = input()
        for item in Buffes.Persona:
            if item.Nombre == Nombre:

                print("<AlumnoEncontrado>")

                Nombre = input()
                item.Nombre = Nombre

                print("<NombreCambiado>")

                Apellido = input()
                item.Apellido = Apellido

                print("<ApellidoCambiado>")

                if type(item) is Alumno:

                    print("<EntroAlType>")

                    Division = input()
                    item.Division = Division

                    print("<AlumnoModificado>")

                if type(item) is Profesor:

                    print("<EntroAlType>")

                    Descuento = input()
                    item.Descuento = Descuento

                    print("<ProfesorModificado>")

    if Opcion == 4: ##AgPlato

        Nombre = input()
        Plato1.Nombre = Nombre

        Precio = int(input())
        Plato1.Precio = Precio

        Buffes.plato.append(Plato1)

        print("<PlatoAgregado>")

    if Opcion == 5: ##ModPlato

        Nombre = input()
        for item in Buffes.plato:
            if item.Nombre == Nombre:
                Nombre = input()
                item.Nombre = Nombre
                Precio = int(input())
                item.Precio = Precio

                print("<PlatoModificado>")

    if Opcion == 6: ##DelPersona

        Nombre = input()
        for item in Buffes.Persona:
            if item.Nombre == Nombre:
                Buffes.Persona.remove(item)

                print("<PersonaEliminada>")

    if Opcion == 7: ##DelPlato

        Nombre = input()
        for item in Buffes.plato:
            if item.Nombre == Nombre:
                Buffes.plato.remove(item)

                print("<PlatoEliminado>")

    if Opcion == 8: ##AgPedido

        Pedido1.Persona = Jorge
        Pedido1.Plato = Plato1

        Fecha = input()
        Pedido1.Fecha = Fecha

        Hora = input()
        Pedido1.Hora = Hora

        Buffes.Pedido.append(Pedido1)

        print("<PedidoAgregado>")

    if Opcion == 9: ##ModPedido

        if Pedido1.Persona == Jorge:
            if Pedido1.Plato == Plato1:

                Fecha = input()
                Pedido1.Fecha = Fecha

                Hora = input()
                Pedido1.Hora = Hora

                print("<PedidoModificado>")

    if Opcion == 10: ##DelPedido

        for item in Buffes.Pedido:
            if item.Persona == Jorge:
                if item.Plato == Plato1:
                    Buffes.Pedido.remove(item)

                    print("<PedidoEliminado>")

    if Opcion == 11: ##ListPlatos

        Cont = 0

        Fecha = input()
        for item in Buffes.Pedido:
            if item.Fecha == Fecha:

                print(item.Plato.Nombre)

                item.GetPrecioDesc()

                print("<Plato " + Cont+" Listado>")