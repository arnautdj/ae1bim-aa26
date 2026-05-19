from sqlalchemy.orm import sessionmaker
from configuracion import engine
from crear_base_entidades import Facultad, Carrera, Profesor, RecursoAcademico

Session = sessionmaker(bind=engine)
session = Session()

print("=" * 60)
print("PROFESORES ORDENADOS POR APELLIDOS (A-Z)")
print("=" * 60)
profesores = session.query(Profesor).order_by(Profesor.apellidos).all()
for p in profesores:
    print(p)
    print(f"  Carrera: {p.carrera.nombre}")
    print("-" * 60)

print()
print("=" * 60)
print("RECURSOS ACADÉMICOS ORDENADOS POR FECHA DE PUBLICACIÓN (más reciente primero)")
print("=" * 60)
recursos = session.query(RecursoAcademico).order_by(RecursoAcademico.fecha_publicacion.desc()).all()
for r in recursos:
    print(r)
    print(f"  Profesor: {r.profesor.nombres} {r.profesor.apellidos}")
    print("-" * 60)
