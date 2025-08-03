UPDATE PRACTICAS
SET estado=1 
WHERE id_practica=4

SELECT* FROM ESTUDIANTES
WHERE id_empresa=4 OR 5 OR 6 OR 7 OR 8
SELECT* FROM EMPRESAS

SELECT*FROM Practicasaprobadas

DELETE FROM PRACTICAS WHERE id_empresa = 207 or 208;
DELETE FROM TUTORES WHERE id_tutor = 207 or 208;

FOREIGN KEY (id_empresa) REFERENCES EMPRESAS(id_empresa) ON DELETE CASCADE

SELECT sum(horas) from Practicasaprobadas
WHERE nombre='Carlos Ramírez'

SELECT * FROM  PracticasGLOBAL  


SHOW CREATE TABLE EMPRESAS
SHOW CREATE TABLE TUTORES
SHOW CREATE TABLE ESTUDIANTES
SHOW CREATE TABLE PRACTICAS

CREATE TABLE `EMPRESAS` (
   `id_empresa` int NOT NULL AUTO_INCREMENT,
   `nombre` varchar(45) DEFAULT NULL,
   `tipo` varchar(45) DEFAULT NULL,
   `descripcion` varchar(45) DEFAULT NULL,
   PRIMARY KEY (`id_empresa`)
 ) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci
 
 CREATE TABLE `TUTORES` (
   `id_tutor` int NOT NULL AUTO_INCREMENT,
   `nombre` varchar(45) DEFAULT NULL,
   `apellido` varchar(45) DEFAULT NULL,
   `correo` varchar(45) DEFAULT NULL,
   `telefono` varchar(45) DEFAULT NULL,
   `cedula` varchar(45) DEFAULT NULL,
   PRIMARY KEY (`id_tutor`),
   UNIQUE KEY `cedula_UNIQUE` (`cedula`)
 ) ENGINE=InnoDB AUTO_INCREMENT=216 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci

 
 CREATE TABLE `ESTUDIANTES` (
   `id_estudiante` int NOT NULL AUTO_INCREMENT,
   `nombre` varchar(45) DEFAULT NULL,
   `apellido` varchar(45) DEFAULT NULL,
   `carrera` varchar(45) DEFAULT NULL,
   `nacimiento` date DEFAULT NULL,
   `cedula` varchar(10) NOT NULL,
   PRIMARY KEY (`id_estudiante`)
 ) ENGINE=InnoDB AUTO_INCREMENT=106 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci
 
 CREATE TABLE `PRACTICAS` (
   `id_practica` int NOT NULL AUTO_INCREMENT,
   `id_estudiante` int DEFAULT NULL,
   `id_empresa` int DEFAULT NULL,
   `horas` int DEFAULT NULL,
   `fecha` date DEFAULT NULL,
   `descripcion` varchar(100) DEFAULT NULL,
   `id_tutor` int DEFAULT NULL,
   `estado` tinyint DEFAULT '0',
   PRIMARY KEY (`id_practica`),
   KEY `id_empresa` (`id_empresa`),
   KEY `id_estudiante` (`id_estudiante`),
   KEY `id_tutor` (`id_tutor`),
   CONSTRAINT `PRACTICAS_ibfk_1` FOREIGN KEY (`id_empresa`) REFERENCES `EMPRESAS` (`id_empresa`),
   CONSTRAINT `PRACTICAS_ibfk_2` FOREIGN KEY (`id_estudiante`) REFERENCES `ESTUDIANTES` (`id_estudiante`),
   CONSTRAINT `PRACTICAS_ibfk_3` FOREIGN KEY (`id_tutor`) REFERENCES `TUTORES` (`id_tutor`)
 ) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci
 
 
  INSERT INTO TUTORES (id_tutor, nombre, apellido, correo, telefono, cedula) VALUES
(1, 'Carlos', 'Mendoza', 'cmendoza@uleam.edu.ec', '0991234567', '1304567890'),
(2, 'Lucía', 'Paredes', 'lparedes@uleam.edu.ec', '0987654321', '1309876543'),
(3, 'Jorge', 'Ramírez', 'jramirez@uleam.edu.ec', '0971122334', '1312345678');


INSERT INTO ESTUDIANTES (id_estudiante, nombre, apellido, carrera, nacimiento, cedula) VALUES
(1, 'Ana', 'Torres', 'Ingeniería de Software', '2002-05-14', '1301122334'),
(2, 'Luis', 'Gómez', 'Sistemas', '2001-08-22', '1302233445'),
(3, 'María', 'López', 'Telecomunicaciones', '2003-01-10', '1303344556'),
(4, 'Pedro', 'Martínez', 'Ingeniería de Software', '2002-11-30', '1304455667');


INSERT INTO PRACTICAS (id_practica, id_estudiante, id_empresa, horas, fecha, descripcion, id_tutor, estado) VALUES
(1, 1, 1, 120, '2025-06-01', 'Desarrollo de una app móvil', 1, 1),
(2, 2, 2, 100, '2025-06-15', 'Análisis de impacto ambiental', 2, 1),
(3, 3, 3, 80, '2025-07-01', 'Automatización de reportes financieros', 3, 0),
(4, 4, 1, 150, '2025-07-10', 'Refactorización de sistema web', 1, 1);


SELECT * FROM TUTORES;
SELECT * FROM ESTUDIANTES;
SELECT * FROM EMPRESAS;
SELECT*FROM PRACTICAS




