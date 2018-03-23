
class Empresa(object):
    def __init__(self):
            self.Empleados = []

    def SetEmpleados(self, Empleado):
            self.Empleados.append(Empleado)

    def GetPorcentajeAsistencia(self):
            Año = input()
            Mes = input()
            PorcentajeEmpresa = 0
            for item in self.Empleados:
                PorcentajeEmpresa += item.GetPorcentajeAsistencia(Año, Mes)
            PorcentajeEmpresa / self.Empleados.len(Empresa.Empleados)
            return PorcentajeEmpresa
