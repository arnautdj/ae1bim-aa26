from sqlalchemy import or_
from sqlalchemy.orm import sessionmaker
from configuracion import engine
from crear_base_entidades import Facultad, Carrera, Profesor, RecursoAcademico

Session = sessionmaker(bind=engine)
session = Session()

print("=" * 60)
print("PROFESORES: Ingeniería de Software o Inteligencia Artificial")
print("=" * 60)
profesores = session.query(Profesor).filter(
    or_(
        Profesor.especialidad == 'Ingeniería de Software',
        Profesor.especialidad == 'Inteligencia Artificial y Minería de Datos'
    )
).all()
for p in profesores:
    print(p)
    print(f"  Carrera: {p.carrera.nombre}")
    print(f"  Facultad: {p.carrera.facultad.nombre}")
    print("-" * 60)

print()
print("=" * 60)
print("RECURSOS DE TIPO: libro o guía didáctica")
print("=" * 60)
recursos = session.query(RecursoAcademico).filter(
    or_(RecursoAcademico.tipo == 'libro', RecursoAcademico.tipo == 'guía didáctica')
).all()
for r in recursos:
    print(r)
    print(f"  Profesor: {r.profesor.nombres} {r.profesor.apellidos}")
    print(f"  Especialidad: {r.profesor.especialidad}")
    print("-" * 60)
