from sqlalchemy import or_
from sqlalchemy.orm import sessionmaker
from configuracion import engine
from crear_base_entidades import Facultad, Carrera, Profesor, RecursoAcademico

Session = sessionmaker(bind=engine)
session = Session()

print("================================================")
print("PROFESORES: Ingeniería de Software o Inteligencia Artificial")
print("================================================")
profesores = session.query(Profesor).filter(
    or_(
        Profesor.especialidad == 'Ingeniería de Software',
        Profesor.especialidad == 'Inteligencia Artificial y Minería de Datos'
    )
).all()
for p in profesores:
    print(f"Profesor: {p.nombres} {p.apellidos}")
    print(f"  Carrera: {p.carrera.nombre}")
    print(f"  Facultad: {p.carrera.facultad.nombre}")
    print("--------------------------------------------")

print()
print("================================================")
print("RECURSOS DE TIPO: libro o guía didáctica")
print("================================================")
recursos = session.query(RecursoAcademico).filter(
    or_(RecursoAcademico.tipo == 'libro', RecursoAcademico.tipo == 'guía didáctica')
).all()
for r in recursos:
    print(f"Recurso: {r.titulo} ({r.tipo})")
    print(f"  Profesor: {r.profesor.nombres} {r.profesor.apellidos}")
    print("--------------------------------------------")
