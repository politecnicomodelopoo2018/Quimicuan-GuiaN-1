from Python_SQL import DB

class Criatura(object):
    id = None
    Nombre = None
    Descripcion = None
    Traduccion = None
    idReino = None


    def SetNombre(self, Nombre):
        self.Nombre = Nombre

    def SetDescripcion(self, Descripcion):
        self.Descripcion = Descripcion

    def SetTraduccion(self, Traduccion):
        self.Traduccion = Traduccion

    def SetidReino(self, idReino):
        self.idReino = idReino

    def Insert(self):
        cursor = DB().run("INSERT INTO Ciatura (Nombre_Criatura, Descripcion_Criatura, Traduccion_Criatura, Reino_idReino) VALUES ('%s', '%s', '%s', '%s')" % (self.Nombre, self.Descripcion, self.Traduccion, self.idReino))
        self.id = cursor.lastrowid

    def Update(self, Nombre, Descripcion, Traduccion, idReino, idUpdate):
        DB().run("UPDATE Ciatura SET Nombre_Criatura = ('%s'), Descripcion_Criatura = ('%s'), Traduccion_Criatura = ('%s'), Reino_idReino = ('%s') WHERE idCiatura = ('%d')" % (Nombre, Descripcion, Traduccion, idReino, idUpdate))

    def Delete(self, idDelete):
        DB().run("DELETE FROM Ciatura WHERE idCiatura = ('%d')" % (idDelete))

    @staticmethod
    def GetCriaturas():
        listaAux=[]
        cursor = DB().run("SELECT * FROM Ciatura")
        for item in cursor:
            unaCriatura = Criatura()
            unaCriatura.id = item["idCiatura"]
            unaCriatura.Nombre = item["Nombre_Criatura"]
            unaCriatura.Descripcion = item["Descripcion_Criatura"]
            unaCriatura.Traduccion = item["Traduccion_Criatura"]
            unaCriatura.idReino = item["Reino_idReino"]
            listaAux.append(unaCriatura)

        return listaAux