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
 ) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci
 
 CREATE TABLE `TUTORES` (
   `id_tutor` int NOT NULL AUTO_INCREMENT,
   `nombre` varchar(45) DEFAULT NULL,
   `correo` varchar(45) DEFAULT NULL,
   `telefono` varchar(45) DEFAULT NULL,
   PRIMARY KEY (`id_tutor`)
 ) ENGINE=InnoDB AUTO_INCREMENT=209 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci
 
 
 CREATE TABLE `ESTUDIANTES` (
   `id_estudiante` int NOT NULL AUTO_INCREMENT,
   `nombre` varchar(45) DEFAULT NULL,
   `carrera` varchar(45) DEFAULT NULL,
   `nacimiento` date DEFAULT NULL,
   `horastotales` int DEFAULT '0',
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
 ) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci