SELECT * FROM PRACTICAS2
 SELECT*FROM ESTUDIANTES
 
 USE new_schema
 
  

CREATE TABLE EMPRESAS (
    id_empresa int PRIMARY KEY,
    nombre VARCHAR(45),
    tipo VARCHAR(45),
    descripcion VARCHAR(45)
);
 
 CREATE TABLE ESTUDIANTES(
	id_estudiante INT PRIMARY KEY,
	nombre VARCHAR(45),
    carrera varchar(45),
    nacimiento DATE
 );
 
 CREATE TABLE TUTORES(
	id_tutor INT PRIMARY KEY,
    nombre VARCHAR(45),
    correo VARCHAR(45),
	telefono VARCHAR(45)
 );
 
 CREATE TABLE PRACTICAS(
 
	id_practica INT PRIMARY KEY,
	id_estudiante INT,
    id_empresa INT,
    horas INT,
    fecha DATE,
    descripcion VARCHAR(100),
    id_tutor INT,
    
	FOREIGN KEY (id_empresa) REFERENCES EMPRESAS(id_empresa),
	FOREIGN KEY (id_estudiante) REFERENCES ESTUDIANTES(id_estudiante),
	FOREIGN KEY (id_tutor) REFERENCES TUTORES(id_tutor)

    );
    INSERT INTO ESTUDIANTES (id_estudiante, nombre, carrera, nacimiento) VALUES
(101, 'Ana Pérez', 'Ingeniería en Sistemas', '2002-05-14'),
(102, 'Carlos Ramírez', 'Medicina', '2001-08-22'),
(103, 'Lucía Torres', 'Ingeniería Ambiental', '2003-01-11');

    
    INSERT INTO EMPRESAS (id_empresa, nombre, tipo, descripcion) VALUES
(1, 'Tech Solutions', 'Tecnología', 'Empresa de desarrollo de software'),
(2, 'Green World', 'Ambiental', 'Consultora ambiental'),
(3, 'MediHealth', 'Salud', 'Clínica privada');

    INSERT INTO TUTORES (id_tutor, nombre, correo, telefono) VALUES
(201, 'Ing. Mario López', 'mario.lopez@uni.edu', '0999999991'),
(202, 'Dra. Marta Ruiz', 'marta.ruiz@uni.edu', '0999999992'),
(203, 'Ing. Pablo Salas', 'pablo.salas@uni.edu', '0999999993');

INSERT INTO PRACTICAS (id_practica, id_estudiante, id_empresa, horas, fecha, descripcion, id_tutor) VALUES
(1, 101, 1, 120, '2025-07-01', 'Desarrollo de sistema web para la empresa.', 201),
(2, 102, 3, 150, '2025-06-15', 'Apoyo en área de pediatría.', 202),
(3, 103, 2, 100, '2025-05-10', 'Monitoreo de calidad ambiental.', 203);


SELECT*FROM PRACTICAS
SELECT*FROM ESTUDIANTES
SELECT*FROM TUTORES
SELECT*FROM EMPRESAS




    