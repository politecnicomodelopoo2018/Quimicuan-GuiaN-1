from Python_SQL import DB

class Poder(object):
    id = None
    descripcion = None

    def SetId(self, id):
        self.id = id

    def SetDescripcion(self, Descripcion):
        self.descripcion = Descripcion

    def Insert(self):
        DB().run("INSERT INTO Poder VALUES (%d,'%s')" % (self.id, self.descripcion))