from Python_SQL import DB

class Dios(object):
    id = None
    Nombre = None
    Deidad = None
    Tipo = None


    def SetNombre(self, Nombre):
        self.Nombre = Nombre

    def SetDeidad(self, Deidad):
        self.Deidad = Deidad

    def SetTipo(self, Tipo):
        self.Tipo = Tipo

    def Insert(self):
        cursor = DB().run("INSERT INTO Dios (Nombre_Dios, Deidad_Dios, Tipo_Dios ) VALUES ('%s', '%s', '%s')" % (self.Nombre, self.Deidad, self.Tipo))
        self.id = cursor.lastrowid

    def UpdateNombre(self, Nombre, Deidad, Tipo, idUpdate):
        DB().run("UPDATE Dios SET Nombre_Dios = ('%s'), Deidad_Dios = ('%s'), Tipo_Dios = ('%s') WHERE idDios = ('%d')" % (Nombre, Deidad, Tipo, idUpdate))

    def Delete(self, idDelete):
        DB().run("DELETE FROM Dios WHERE idDios = ('%d')" % (idDelete))

    @staticmethod
    def GetPoderes():
        listaAux=[]
        cursor = DB().run("SELECT * FROM Dios")
        for item in cursor:
            unDios=Dios()
            unDios.id = item["idDios"]
            unDios.Nombre = item["Nombre_Dios"]
            unDios.id = item["Deidad_Dios"]
            unDios.id = item["Tipo_Dios"]
            listaAux.append(unDios)

        return listaAux