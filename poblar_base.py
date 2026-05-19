from sqlalchemy.orm import sessionmaker
from configuracion import engine
from crear_base_entidades import Facultad, Carrera, Profesor, RecursoAcademico

Session = sessionmaker(bind=engine)
session = Session()

# Facultades
fac_ing = Facultad(
    nombre='Facultad de Ingeniería y Arquitectura',
    ubicacion='Edificio B, Campus San Cayetano Alto, Loja',
    decano='Dr. Marco Aurelio Rodríguez Cueva'
)

fac_jur = Facultad(
    nombre='Facultad de Ciencias Jurídicas, Políticas y Económicas',
    ubicacion='Edificio C, Campus San Cayetano Alto, Loja',
    decano='Dra. Patricia Esperanza Valdivieso Granda'
)

# Carreras
carrera_sistemas = Carrera(nombre='Ingeniería en Ciencias de la Computación', codigo='ICC')
carrera_sistemas.facultad = fac_ing

carrera_civil = Carrera(nombre='Ingeniería Civil', codigo='IC')
carrera_civil.facultad = fac_ing

carrera_admin = Carrera(nombre='Administración de Empresas', codigo='AE')
carrera_admin.facultad = fac_jur

carrera_conta = Carrera(nombre='Contabilidad y Auditoría', codigo='CA')
carrera_conta.facultad = fac_jur

# Profesores - Ingeniería en Sistemas
p1 = Profesor(
    nombres='Nelson Eduardo',
    apellidos='Salgado Reyes',
    correo='n.salgado@utpl.edu.ec',
    especialidad='Inteligencia Artificial y Minería de Datos'
)
p1.carrera = carrera_sistemas

p2 = Profesor(
    nombres='Verónica Alexandra',
    apellidos='Morocho Yunga',
    correo='v.morocho@utpl.edu.ec',
    especialidad='Ingeniería de Software'
)
p2.carrera = carrera_sistemas

# Ingeniería Civil
p3 = Profesor(
    nombres='Jorge Washington',
    apellidos='Paladines Mogrovejo',
    correo='j.paladines@utpl.edu.ec',
    especialidad='Estructuras y Hormigón Armado'
)
p3.carrera = carrera_civil

p4 = Profesor(
    nombres='Mónica Cecilia',
    apellidos='Valarezo Tandazo',
    correo='m.valarezo@utpl.edu.ec',
    especialidad='Hidráulica y Saneamiento Ambiental'
)
p4.carrera = carrera_civil

# Administración
p5 = Profesor(
    nombres='Diego Rodrigo',
    apellidos='Burneo Vallejo',
    correo='d.burneo@utpl.edu.ec',
    especialidad='Gestión Financiera y Proyectos de Inversión'
)
p5.carrera = carrera_admin

p6 = Profesor(
    nombres='Ana Lucía',
    apellidos='Campoverde Encalada',
    correo='a.campoverde@utpl.edu.ec',
    especialidad='Emprendimiento e Innovación Empresarial'
)
p6.carrera = carrera_admin

# Contabilidad
p7 = Profesor(
    nombres='Fabián Mauricio',
    apellidos='Ordóñez Pardo',
    correo='f.ordonez@utpl.edu.ec',
    especialidad='Auditoría y Control Interno'
)
p7.carrera = carrera_conta

p8 = Profesor(
    nombres='Janeth Esperanza',
    apellidos='Lozano Calva',
    correo='j.lozano@utpl.edu.ec',
    especialidad='Tributación y Derecho Fiscal'
)
p8.carrera = carrera_conta

# Recursos académicos
r1 = RecursoAcademico(
    titulo='Guía Didáctica: Fundamentos de Inteligencia Artificial',
    fecha_publicacion='2024-02-05',
    tipo='guía didáctica',
    url='https://eva.utpl.edu.ec/course/view.php?id=4821'
)
r1.profesor = p1

r2 = RecursoAcademico(
    titulo='Aprendizaje Automático con Python: de la Teoría a la Práctica',
    fecha_publicacion='2023-09-18',
    tipo='libro',
    url='https://repositorio.utpl.edu.ec/handle/123456789/19342'
)
r2.profesor = p1

r3 = RecursoAcademico(
    titulo='Metodologías Ágiles: Scrum Aplicado a Proyectos Académicos',
    fecha_publicacion='2024-04-10',
    tipo='guía didáctica',
    url='https://eva.utpl.edu.ec/course/view.php?id=5104'
)
r3.profesor = p2

r4 = RecursoAcademico(
    titulo='Pruebas de Software y Aseguramiento de la Calidad',
    fecha_publicacion='2023-11-03',
    tipo='video',
    url='https://utpl.edu.ec/recursos/pruebas-software-calidad'
)
r4.profesor = p2

r5 = RecursoAcademico(
    titulo='Control de versiones con Git para proyectos de software',
    fecha_publicacion='2024-06-03',
    tipo='video',
    url='https://www.youtube.com/watch?v=HkdAHXoRtos'
)
r5.profesor = p2

r6 = RecursoAcademico(
    titulo='Diseño Sismorresistente según la Norma Ecuatoriana de la Construcción',
    fecha_publicacion='2023-08-22',
    tipo='guía didáctica',
    url='https://eva.utpl.edu.ec/course/view.php?id=3867'
)
r6.profesor = p3

r7 = RecursoAcademico(
    titulo='Cálculo de Estructuras de Hormigón Armado: Casos Prácticos',
    fecha_publicacion='2024-01-15',
    tipo='libro',
    url='https://repositorio.utpl.edu.ec/handle/123456789/20115'
)
r7.profesor = p3

r8 = RecursoAcademico(
    titulo='Hidráulica de Canales Abiertos: Teoría y Ejercicios Resueltos',
    fecha_publicacion='2023-07-04',
    tipo='guía didáctica',
    url='https://eva.utpl.edu.ec/course/view.php?id=3490'
)
r8.profesor = p4

r9 = RecursoAcademico(
    titulo='Sistemas de Agua Potable y Alcantarillado en Zonas Rurales',
    fecha_publicacion='2024-03-28',
    tipo='video',
    url='https://utpl.edu.ec/recursos/agua-potable-rural'
)
r9.profesor = p4

r10 = RecursoAcademico(
    titulo='Evaluación Financiera de Proyectos de Inversión',
    fecha_publicacion='2023-10-30',
    tipo='guía didáctica',
    url='https://eva.utpl.edu.ec/course/view.php?id=6023'
)
r10.profesor = p5

r11 = RecursoAcademico(
    titulo='Análisis de Estados Financieros para la Toma de Decisiones',
    fecha_publicacion='2024-05-02',
    tipo='video',
    url='https://utpl.edu.ec/recursos/estados-financieros'
)
r11.profesor = p5

r12 = RecursoAcademico(
    titulo='Plan de Negocios: Guía Paso a Paso para Emprendedores Ecuatorianos',
    fecha_publicacion='2024-02-20',
    tipo='guía didáctica',
    url='https://eva.utpl.edu.ec/course/view.php?id=6257'
)
r12.profesor = p6

r13 = RecursoAcademico(
    titulo='Innovación Disruptiva en PYMES de la Región Sur del Ecuador',
    fecha_publicacion='2023-12-11',
    tipo='libro',
    url='https://repositorio.utpl.edu.ec/handle/123456789/21008'
)
r13.profesor = p6

r14 = RecursoAcademico(
    titulo='Normas Internacionales de Auditoría (NIA): Aplicación en Ecuador',
    fecha_publicacion='2023-09-07',
    tipo='guía didáctica',
    url='https://eva.utpl.edu.ec/course/view.php?id=5531'
)
r14.profesor = p7

r15 = RecursoAcademico(
    titulo='Control Interno basado en el Marco COSO 2013',
    fecha_publicacion='2024-01-25',
    tipo='libro',
    url='https://repositorio.utpl.edu.ec/handle/123456789/19887'
)
r15.profesor = p7

r16 = RecursoAcademico(
    titulo='Régimen Tributario Interno del Ecuador: Impuesto a la Renta',
    fecha_publicacion='2023-11-14',
    tipo='guía didáctica',
    url='https://eva.utpl.edu.ec/course/view.php?id=5788'
)
r16.profesor = p8

r17 = RecursoAcademico(
    titulo='Declaración del IVA y Retenciones en la Fuente: Casos Prácticos',
    fecha_publicacion='2024-04-17',
    tipo='video',
    url='https://utpl.edu.ec/recursos/iva-retenciones-fuente'
)
r17.profesor = p8

# guardar en la base de datos
session.add(fac_ing)
session.add(fac_jur)

session.add(carrera_sistemas)
session.add(carrera_civil)
session.add(carrera_admin)
session.add(carrera_conta)

session.add(p1)
session.add(p2)
session.add(p3)
session.add(p4)
session.add(p5)
session.add(p6)
session.add(p7)
session.add(p8)

session.add_all([r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, r13, r14, r15, r16, r17])
session.commit()

print("Datos guardados correctamente")
