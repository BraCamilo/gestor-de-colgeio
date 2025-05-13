from Modelos.persona import Persona

class estudiante(Persona):
    def __init__(self, Id, nombre, edad, correo, Curso=None):
        super().__init__(Id, nombre, edad, correo)
        self.Curso = Curso

    def to_dict(self):
        data = super().to_dict()
        data["Curso"] = self.Curso
        return data
    
    @staticmethod
    def from_dict(data):
        return estudiante(
            data["Id"],
            data["nombre"],
            data["edad"],
            data["correo"],
            data.get("Curso"),
        )
    
    def mostrar_info(self):
        return F"{super().mostrar_info()} Curso: {self.Curso}"
    


