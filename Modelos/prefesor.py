from Modelos.persona import Persona

class Profesor(Persona):
    def __init__(self, Id, nombre, especialidad):
        super().__init__(Id, nombre, None, None,)
        self.especialidad = especialidad

    
