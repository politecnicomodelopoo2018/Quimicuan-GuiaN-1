from Python_SQL import DB

class Poder(object):
    id = None
    descripcion = None


    def SetDescripcion(self, Descripcion):
        self.descripcion = Descripcion

    def Insert(self):
        cursor = DB().run("INSERT INTO Poder (Descripcion_Poder) VALUES ('%s')" % (self.descripcion))

        self.id = cursor.lastrowid

    def Update(self, DescRemp, idUpdate):
        DB().run("UPDATE Poder SET Descripcion_Poder = ('%s') WHERE idPoder = ('%d')" % (DescRemp, idUpdate))

    def Delete(self, idDelete):
        DB().run("DELETE FROM Poder WHERE idPoder = ('%d')" % (idDelete))

    @staticmethod
    def GetPoderes():
        listaAux=[]
        cursor = DB().run("SELECT * FROM Poder")
        for item in cursor:
            unPoder=Poder()
            unPoder.id = item["idPoder"]
            unPoder.descripcion = item["Descripcion_Poder"]
            listaAux.append(unPoder)

        return listaAux