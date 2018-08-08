from Python_SQL import DB

class Dios(object):
    id = None
    Nombre = None
    Deidad = None
    Tipo = None
    idReino = None


    def SetNombre(self, Nombre):
        self.Nombre = Nombre

    def SetDeidad(self, Deidad):
        self.Deidad = Deidad

    def SetTipo(self, Tipo):
        self.Tipo = Tipo

    def SetidReino(self, idReino):
        self.idReino = idReino

    def Insert(self):
        cursor = DB().run("INSERT INTO Dios (Nombre_Dios, Deidad_Dios, Tipo_Dios, Reino_idReino) VALUES ('%s', '%s', '%s', '%s')" % (self.Nombre, self.Deidad, self.Tipo, self.idReino))
        self.id = cursor.lastrowid

    def Update(self, Nombre, Deidad, Tipo, idReino, idUpdate):
        DB().run("UPDATE Dios SET Nombre_Dios = ('%s'), Deidad_Dios = ('%s'), Tipo_Dios = ('%s'), Reino_idReino = ('%s') WHERE idDios = ('%d')" % (Nombre, Deidad, Tipo, idReino, idUpdate))

    def Delete(self, idDelete):
        DB().run("DELETE FROM Dios WHERE idDios = ('%d')" % (idDelete))

    @staticmethod
    def GetDioses():
        listaAux=[]
        cursor = DB().run("SELECT * FROM Dios")
        for item in cursor:
            unDios=Dios()
            unDios.id = item["idDios"]
            unDios.Nombre = item["Nombre_Dios"]
            unDios.Deidad = item["Deidad_Dios"]
            unDios.Tipo = item["Tipo_Dios"]
            unDios.idReino = item["Reino_idReino"]
            listaAux.append(unDios)

        return listaAux