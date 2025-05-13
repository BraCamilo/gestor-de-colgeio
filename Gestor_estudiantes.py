import json
# Definición de la clase Estudiantes
class Estudiante:
    def __init__(self, Id, nombre, edad, correo, Curso=None):
        self.Id = Id
        self.nombre = nombre
        self.edad = edad
        self.correo = correo
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
        return f"Estudiante: {self.nombre}, Edad{self.edad}, Correo{self.correo} Curso: {self.Curso}"

# Definición de la clases en profesores
class Profesor:
    def __init__(self, Id, nombre, especialidad):
        self.Id = Id
        self.nombre = nombre
        self.especialidad = especialidad

    def to_dict(self):
        return {
            "Id": self.Id,
            "nombre": self.nombre,
            "especialidad": self.especialidad
        }
    
    @staticmethod
    def from_dict(data):
        return Profesor(
            data["Id"],
            data["nombre"],
            data["especialidad"]
        )
    def mostrar_info(self):
        return f"Profesor: {self.nombre}, Especialidad: {self.especialidad}"

# Definicion de los Cursos. 
class Curso:
    def __init__(self, Id, nombre, profesor=None):
        self.Id = Id
        self.nombre = nombre
        self.profesor = profesor #lista de objetos de profesores
        self.estudiantes = [] # lista de objetos Estudiante
   

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "profesor": self.profesor.nombre if self.profesor else None,
            "estudiantes": [e.Id for e in self.estudiantes]
        }

    @staticmethod
    def from_dict(data, profesores_dict, estudiantes_dict):
        curso = Curso(data["nombre"])
        if data["profesor"]:
            curso.profesor = profesores_dict.get(data["profesor"])
        curso.estudiantes = [estudiantes_dict[eid] for eid in data["estudiantes"]]
        return curso
    
    def mostrar_info(self):
        profesor_nombre = self.profesor.nombre if self.profesor else "No asignado"
        return f"Curso: {self.nombre}, Profesor: {profesor_nombre}, Estudiante: {self.estudiantes}"
    
# Definicion del sistema escolar
class SistemaEscolar:
    def __init__(self):
        self.estudiantes_dict = {}
        self.profesores_dict = {}
        self.cursos_dict = {}

    def registrar_estudiante(self, estudiante):
        self.estudiantes_dict[estudiante.Id] = estudiante

    def registrar_profesor(self, profesor):
        self.profesores_dict[profesor.Id] = profesor

    def registrar_curso(self, curso):
        self.cursos_dict[curso.Id] = curso

    def buscar_estudiante_por_id(self, est_id):
        return self.estudiantes_dict.get(est_id)

    def buscar_profesor_por_id(self, prof_id):
        return self.profesores_dict.get(prof_id)

    def buscar_curso_por_id(self, cur_id):
        return self.cursos_dict.get(cur_id)

    def guardar_todo_en_json(self, archivo):
        datos = {
            "estudiantes": [e.to_dict() for e in self.estudiantes_dict.values()],
            "profesores": [p.to_dict() for p in self.profesores_dict.values()],
            "cursos": [c.to_dict() for c in self.cursos_dict.values()]
        }
        with open(archivo, "w") as f:
            json.dump(datos, f, indent=4)

    def cargar_todo_desde_json(self, archivo):
        with open(archivo, "r") as f:
            datos = json.load(f)

        # Crear estudiantes y profesores
        for d in datos["estudiantes"]:
            estudiante = Estudiante.from_dict(d)
            self.estudiantes_dict[estudiante.Id] = estudiante

        for d in datos["profesores"]:
            profesor = Profesor.from_dict(d)
            self.profesores_dict[profesor.Id] = profesor

        # Crear cursos con conexión a estudiantes y profesores
        for c in datos["cursos"]:
            curso = Curso.from_dict(c, self.profesores_dict, self.estudiantes_dict)
            self.cursos_dict[curso.Id] = curso


def menu ():
    sistema = SistemaEscolar()

    while True:
        print("\n=== Menú del Sistema Escolar ===")
        print("1. Registrar estudiante")
        print("2. Registrar profesor")
        print("3. Registrar curso")
        print("4. Buscar estudiante por ID")
        print("5. Buscar profesor por ID")
        print("6. Buscar curso por ID")
        print("7. Guardar datos")
        print("8. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            Id = input("ID del estudiante: ")
            nombre = input("Nombre: ")
            edad = int(input("Edad: "))
            correo = input("Correo: ")
            curso = input("Curso: ")
            estudiante = Estudiante(Id, nombre, edad, correo, curso)
            sistema.registrar_estudiante(estudiante)
            print("Estudiante registrado.")

        elif opcion == "2":
            Id = input("ID del profesor: ")
            nombre = input("Nombre: ")
            especialidad = input("Especialidad: ")
            profesor = Profesor(Id, nombre, especialidad)
            sistema.registrar_profesor(profesor)
            print("Profesor registrado.")

        elif opcion == "3":
            Id = input("ID del curso: ")
            nombre = input("Nombre del curso: ")
            print("Profesores disponibles:")
            profesores = list(sistema.profesores_dict.values())
            for i, p in enumerate(profesores):
                print(f"{i + 1}. {p.nombre} ({p.especialidad})")
            opcion_prof = int(input("Seleccione un profesor por número: ")) - 1
            profesor = profesores[opcion_prof] if 0 <= opcion_prof < len(profesores) else None

            curso = Curso(Id, nombre, profesor)
            print("Estudiantes disponibles:")
            estudiantes = list(sistema.estudiantes_dict.values())
            for i, e in enumerate(estudiantes):
                print(f"{i + 1}. {e.nombre} ({e.Curso})")
            selecciones = input("Seleccione estudiantes (números separados por coma): ").split(",")
            for sel in selecciones:
                if sel.strip().isdigit():
                    idx = int(sel.strip()) - 1
                    if 0 <= idx < len(estudiantes):
                        curso.estudiantes.append(estudiantes[idx])
            sistema.registrar_curso(curso)
            print("Curso creado.")

        elif opcion == "4":
            est_id = input("Ingrese el ID del estudiante: ")
            estudiante = sistema.buscar_estudiante_por_id(est_id)
            if estudiante:
                print(estudiante.mostrar_info())
            else:
                print("Estudiante no encontrado.")

        elif opcion == "5":
            prof_id = input("Ingrese el ID del profesor: ")
            profesor = sistema.buscar_profesor_por_id(prof_id)
            if profesor:
                print(profesor.mostrar_info())
            else:
                print("Profesor no encontrado.")

        elif opcion == "6":
            curso_id = input("Ingrese el ID del curso: ")
            curso = sistema.buscar_curso_por_id(curso_id)
            if curso:
                print(curso.mostrar_info())
            else:
                print("Curso no encontrado.")

        elif opcion == "7":
            sistema.guardar_todo_en_json("sistema.json")
            print("💾 Datos guardados en sistema.json.")

        elif opcion == "8":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida. Intente de nuevo.")

# Ejecutar menú
if __name__ == "__main__":
    menu()