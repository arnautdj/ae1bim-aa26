from sqlalchemy.orm import sessionmaker
from configuracion import engine
from crear_base_entidades import Facultad, Carrera, Profesor, RecursoAcademico

Session = sessionmaker(bind=engine)
session = Session()

print("=" * 60)
print("TODAS LAS FACULTADES Y SUS CARRERAS")
print("=" * 60)
facultades = session.query(Facultad).all()
for f in facultades:
    print(f)
    for c in f.carreras:
        print(f"  -> {c}")
    print("-" * 60)

print()
print("=" * 60)
print("TODOS LOS PROFESORES")
print("=" * 60)
profesores = session.query(Profesor).all()
for p in profesores:
    print(p)
    print(f"  Carrera: {p.carrera.nombre}")
    print("-" * 60)

print()
print("=" * 60)
print("TODOS LOS RECURSOS ACADÉMICOS")
print("=" * 60)
recursos = session.query(RecursoAcademico).all()
for r in recursos:
    print(r)
    print(f"  Profesor: {r.profesor.nombres} {r.profesor.apellidos}")
    print("-" * 60)
