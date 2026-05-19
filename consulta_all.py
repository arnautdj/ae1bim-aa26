from sqlalchemy.orm import sessionmaker
from configuracion import engine
from crear_base_entidades import Facultad, Carrera, Profesor, RecursoAcademico

Session = sessionmaker(bind=engine)
session = Session()

print("================================================")
print("TODAS LAS FACULTADES Y SUS CARRERAS")
print("================================================")
facultades = session.query(Facultad).all()
for f in facultades:
    print(f"Facultad: {f.nombre}")
    for c in f.carreras:
        print(f"  Carrera: {c.nombre}")
    print("--------------------------------------------")

print()
print("================================================")
print("TODOS LOS PROFESORES")
print("================================================")
profesores = session.query(Profesor).all()
for p in profesores:
    print(f"Profesor: {p.nombres} {p.apellidos}")
    print(f"  Carrera: {p.carrera.nombre}")
    print("--------------------------------------------")

print()
print("================================================")
print("TODOS LOS RECURSOS ACADÉMICOS")
print("================================================")
recursos = session.query(RecursoAcademico).all()
for r in recursos:
    print(f"Recurso: {r.titulo} ({r.tipo})")
    print(f"  Profesor: {r.profesor.nombres} {r.profesor.apellidos}")
    print("--------------------------------------------")
