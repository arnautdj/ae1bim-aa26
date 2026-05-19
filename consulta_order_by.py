from sqlalchemy.orm import sessionmaker
from configuracion import engine
from crear_base_entidades import Facultad, Carrera, Profesor, RecursoAcademico

Session = sessionmaker(bind=engine)
session = Session()

print("================================================")
print("PROFESORES ORDENADOS POR APELLIDOS (A-Z)")
print("================================================")
profesores = session.query(Profesor).order_by(Profesor.apellidos).all()
for p in profesores:
    print(f"Profesor: {p.nombres} {p.apellidos}")
    print("--------------------------------------------")

print()
print("================================================")
print("RECURSOS ACADÉMICOS ORDENADOS POR FECHA DE PUBLICACIÓN (más reciente primero)")
print("================================================")
recursos = session.query(RecursoAcademico).order_by(RecursoAcademico.fecha_publicacion.desc()).all()
for r in recursos:
    print(f"Recurso: {r.titulo} | Fecha: {r.fecha_publicacion}")
    print(f"  Profesor: {r.profesor.nombres} {r.profesor.apellidos}")
    print("--------------------------------------------")
