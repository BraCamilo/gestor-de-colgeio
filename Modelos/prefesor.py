from Modelos.persona import Persona

class profesor(Persona):
    def __init__(self, Id, nombre, especialidad):
        super().__init__(Id, nombre, None, None,)
        self.especialidad = especialidad

    def to_dict(self):
        return super().to_dict()
        data[especialidad] = self.especialidad
        return data
    
