class Persona:
    def __init__(self, Id, nombre, edad, correo):
        self.Id = Id
        self.nombre = nombre
        self.edad = edad
        self.correo = correo

    def mostrar_info(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Correo: {self.correo}"

    def to_dict(self):
        return {
            "Id": self.Id,
            "nombre": self.nombre,
            "edad": self.edad,
            "correo": self.correo
        }
