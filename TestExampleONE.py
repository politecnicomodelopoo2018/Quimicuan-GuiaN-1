from TestExampleONEPersona import Persona
from TestExampleONERegistro import Registro

Registro1 = Registro()

PesoR1 = input()
AlturaR1 = input()
AñoR1 = input()
MesR1 = input()
DiaR1 = input()

Registro1.SetPeso(PesoR1)
Registro1.SetAltura(AlturaR1)
Registro1.SetAñoReg(AñoR1)
Registro1.SetMesReg(MesR1)
Registro1.SetDiaReg(DiaR1)

Registro2 = Registro()

PesoR2 = input()
AlturaR2 = input()
AñoR2 = input()
MesR2 = input()
DiaR2 = input()

Registro2.SetPeso(PesoR2)
Registro2.SetAltura(AlturaR2)
Registro2.SetAñoReg(AñoR2)
Registro2.SetMesReg(MesR2)
Registro2.SetDiaReg(DiaR2)

Persona1 = Persona()

Nombre1 = input()
Apellido1 = input()
FechaNac1 = input()

Persona1.SetNombre(Nombre1)
Persona1.SetApellido(Apellido1)
Persona1.SetFechaNac(FechaNac1)

Persona1.AgregarRegistro(Registro1)
Persona1.AgregarRegistro(Registro2)

AñoR = input()
MesR = input()
DiaR = input()

Persona1.GetRegistro(DiaR, MesR, AñoR)

Año = input()

Persona1.PromedioReg(Año)

AñoPrim = input()
AñoSegun = input()

Persona1.AlturaAños(AñoPrim, AñoSegun)



