from sqlalchemy import and_
from sqlalchemy.orm import sessionmaker
from configuracion import engine
from crear_base_entidades import Facultad, Carrera, Profesor, RecursoAcademico

Session = sessionmaker(bind=engine)
session = Session()

print("=" * 60)
print("RECURSOS DE TIPO 'video' publicados en 2024")
print("=" * 60)
recursos = session.query(RecursoAcademico).filter(
    and_(RecursoAcademico.tipo == 'video', RecursoAcademico.fecha_publicacion.like('2024%'))
).all()
for r in recursos:
    print(r)
    print(f"  Profesor: {r.profesor.nombres} {r.profesor.apellidos}")
    print(f"  Carrera: {r.profesor.carrera.nombre}")
    print("-" * 60)

print()
print("=" * 60)
print("PROFESORES de 'Auditoría y Control Interno' en Contabilidad y Auditoría")
print("=" * 60)
carrera_ca = session.query(Carrera).filter(Carrera.codigo == 'CA').first()
profesores = session.query(Profesor).filter(
    and_(Profesor.especialidad == 'Auditoría y Control Interno', Profesor.carrera == carrera_ca)
).all()
for p in profesores:
    print(p)
    print(f"  Correo: {p.correo}")
    print(f"  Carrera: {p.carrera.nombre}")
    for r in p.recursos:
        print(f"  Recurso: {r.titulo} ({r.tipo})")
    print("-" * 60)
