from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from configuracion import engine, Base


class Facultad(Base):
    __tablename__ = 'facultad'

    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    ubicacion = Column(String)
    decano = Column(String)

    carreras = relationship('Carrera', back_populates='facultad')

    def __repr__(self):
        return f"Facultad(id={self.id}, nombre='{self.nombre}', ubicacion='{self.ubicacion}', decano='{self.decano}')"


class Carrera(Base):
    __tablename__ = 'carrera'

    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    codigo = Column(String)
    facultad_id = Column(Integer, ForeignKey('facultad.id'))

    facultad = relationship('Facultad', back_populates='carreras')
    profesores = relationship('Profesor', back_populates='carrera')

    def __repr__(self):
        return f"Carrera(id={self.id}, nombre='{self.nombre}', codigo='{self.codigo}')"


class Profesor(Base):
    __tablename__ = 'profesor'

    id = Column(Integer, primary_key=True)
    nombres = Column(String)
    apellidos = Column(String)
    correo = Column(String)
    especialidad = Column(String)
    carrera_id = Column(Integer, ForeignKey('carrera.id'))

    carrera = relationship('Carrera', back_populates='profesores')
    recursos = relationship('RecursoAcademico', back_populates='profesor')

    def __repr__(self):
        return f"Profesor(id={self.id}, nombres='{self.nombres}', apellidos='{self.apellidos}', especialidad='{self.especialidad}')"


class RecursoAcademico(Base):
    __tablename__ = 'recurso_academico'

    id = Column(Integer, primary_key=True)
    titulo = Column(String)
    fecha_publicacion = Column(String)
    tipo = Column(String)
    url = Column(String)
    profesor_id = Column(Integer, ForeignKey('profesor.id'))

    profesor = relationship('Profesor', back_populates='recursos')

    def __repr__(self):
        return f"RecursoAcademico(id={self.id}, titulo='{self.titulo}', tipo='{self.tipo}', fecha='{self.fecha_publicacion}')"


Base.metadata.create_all(engine)
