from Python_SQL import DB

class Poder(object):
    id = None
    descripcion = None

    def SetDescripcion(self, Descripcion):
        self.descripcion = Descripcion

    def Insert(self):
        DB().run("INSERT INTO Poder (Descripcion_Poder) VALUES ('%s')" % (self.descripcion))

    def Update(self, DescRemp, idUpdate):
        DB().run("UPDATE Poder SET Descripcion_Poder = ('%s') WHERE idPoder = ('%d')" % (DescRemp, idUpdate))

    def Delete(self, idDelete):
        DB().run("DELETE FROM Poder WHERE idPoder = ('%d')" % (idDelete))