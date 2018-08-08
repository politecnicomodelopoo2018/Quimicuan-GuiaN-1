from Python_SQL import DB

class Reino(object):
    id = None
    descripcion = None
    caracteristica = None


    def SetDescripcion(self, Descripcion):
        self.descripcion = Descripcion

    def SetCaracteristica(self, Caracteristica):
        self.caracteristica = Caracteristica

    def Insert(self):
        cursor = DB().run("INSERT INTO Reino (Descripcion_Reino, Caracteristica_Reino) VALUES ('%s', '%s')" % (self.descripcion, self.caracteristica))

        self.id = cursor.lastrowid

    def Update(self, DescRemp, CaractRemp, idUpdate):
        DB().run("UPDATE Reino SET Descripcion_Reino = ('%s'), Caracteristica_Reino = ('%s')  WHERE idReino = ('%d')" % (DescRemp, CaractRemp, idUpdate))

    def Delete(self, idDelete):
        DB().run("DELETE FROM Reino WHERE idReino = ('%d')" % (idDelete))

    @staticmethod
    def GetReinos():
        listaAux=[]
        cursor = DB().run("SELECT * FROM Reino")
        for item in cursor:
            unReino = Reino()
            unReino.id = item["idReino"]
            unReino.descripcion = item["Descripcion_Reino"]
            unReino.caracteristica = item["Caracteristica_Reino"]
            listaAux.append(unReino)

        return listaAux