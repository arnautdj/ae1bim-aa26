from sqlalchemy.orm import sessionmaker
from configuracion import engine
from crear_base_entidades import Facultad, Carrera, Profesor, RecursoAcademico

Session = sessionmaker(bind=engine)
session = Session()

print("=" * 60)
print("PROFESORES CON ESPECIALIDAD: Ingeniería de Software")
print("=" * 60)
profesores = session.query(Profesor).filter(Profesor.especialidad == 'Ingeniería de Software').all()
for p in profesores:
    print(p)
    print(f"  Carrera: {p.carrera.nombre}")
    print(f"  Facultad: {p.carrera.facultad.nombre}")
    print("-" * 60)

print()
print("=" * 60)
print("RECURSOS DE TIPO: guía didáctica")
print("=" * 60)
recursos = session.query(RecursoAcademico).filter(RecursoAcademico.tipo == 'guía didáctica').all()
for r in recursos:
    print(r)
    print(f"  Profesor: {r.profesor.nombres} {r.profesor.apellidos}")
    print(f"  Carrera: {r.profesor.carrera.nombre}")
    print("-" * 60)
