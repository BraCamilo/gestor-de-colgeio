from Modelos.persona import Persona

class Estudiante(Persona):
    def __init__(self, Id, nombre, edad, correo, Curso=None):
        super().__init__(Id, nombre, edad, correo)
        self.Curso = Curso

    def to_dict(self):
        return {
            "Id": self.Id,
            "nombre": self.nombre,
            "edad": self.edad,
            "correo": self.correo,
            "Curso": self.Curso,
        }
    
    @staticmethod
    def from_dict(data):
        return Estudiante(
            data["Id"],
            data["nombre"],
            data["edad"],
            data["correo"],
            data.get("Curso"),
        )
    
    def mostrar_info(self):
        return F"{super().mostrar_info()} Curso: {self.Curso}"
    


