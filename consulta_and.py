from sqlalchemy import and_
from sqlalchemy.orm import sessionmaker
from configuracion import engine
from crear_base_entidades import Facultad, Carrera, Profesor, RecursoAcademico

Session = sessionmaker(bind=engine)
session = Session()

print("================================================")
print("RECURSOS DE TIPO 'video' publicados en 2024")
print("================================================")
recursos = session.query(RecursoAcademico).filter(
    and_(RecursoAcademico.tipo == 'video', RecursoAcademico.fecha_publicacion.like('2024%'))
).all()
for r in recursos:
    print(f"Recurso: {r.titulo} | Fecha: {r.fecha_publicacion}")
    print(f"  Profesor: {r.profesor.nombres} {r.profesor.apellidos}")
    print(f"  Carrera: {r.profesor.carrera.nombre}")
    print("--------------------------------------------")

print()
print("================================================")
print("PROFESORES de 'Auditoría y Control Interno' en Contabilidad y Auditoría")
print("================================================")
carrera_ca = session.query(Carrera).filter(Carrera.codigo == 'CA').first()
profesores = session.query(Profesor).filter(
    and_(Profesor.especialidad == 'Auditoría y Control Interno', Profesor.carrera == carrera_ca)
).all()
for p in profesores:
    print(f"Profesor: {p.nombres} {p.apellidos}")
    print(f"  Correo: {p.correo}")
    print(f"  Carrera: {p.carrera.nombre}")
    for r in p.recursos:
        print(f"  Recurso: {r.titulo} ({r.tipo})")
    print("--------------------------------------------")
