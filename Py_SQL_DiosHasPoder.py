from Python_SQL import DB

class DHP(object):
    idDios = None
    idPoder = None
    Cantidad = None

    def SetidDios(self, idDios):
        self.idDios = idDios

    def SetidPoder(self, idPoder):
        self.idPoder = idPoder

    def SetCantidad(self, Cant):
        self.Cantidad = Cant

    def Insert(self):
        DB().run("INSERT INTO Dios_has_Poder (Dios_idDios, Poder_idPoder, Cantidad) VALUES ('%s', '%s', '%s')" % (self.idDios, self.idPoder, self.Cantidad))

    def Delete(self, idDios, idPoder):
        DB().run("DELETE FROM Dios_has_Poder WHERE Dios_idDios = ('%d') AND Poder_idPoder = ('%d')" % (int(idDios), int(idPoder)))

    def Update(self, idDiosRemp, idPoderRemp, idDios, idPoder, Cant):
        DB().run("UPDATE Dios_has_Poder SET Dios_idDios = ('%s'), Poder_idPoder = ('%s'), Cantidad = ('%s') WHERE Dios_idDios = ('%d') AND Poder_idPoder = ('%d')" % (int(idDios), int(idPoder), int(Cant), int(idDiosRemp), int(idPoderRemp)))

    @staticmethod
    def GetDHP():
        listaAux = []
        cursor = DB().run("SELECT * FROM Dios_has_Poder")
        for item in cursor:
            unDHP = DHP()
            unDHP.idDios = item["Dios_idDios"]
            unDHP.idPoder = item["Poder_idPoder"]
            unDHP.Cantidad = item["Cantidad"]
            listaAux.append(unDHP)

        return listaAux