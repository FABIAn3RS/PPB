SHOW CREATE TABLE PRACTICAS

CREATE TABLE `EMPRESAS` (
   `id_empresa` int NOT NULL AUTO_INCREMENT,
   `nombre` varchar(45) DEFAULT NULL,
   `tipo` varchar(45) DEFAULT NULL,
   `descripcion` varchar(45) DEFAULT NULL,
   PRIMARY KEY (`id_empresa`),
   UNIQUE KEY `nombre_UNIQUE` (`nombre`)
 ) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci
 
 CREATE TABLE `TUTORES` (
   `id_tutor` int NOT NULL AUTO_INCREMENT,
   `nombre` varchar(45) DEFAULT NULL,
   `apellido` varchar(45) DEFAULT NULL,
   `correo` varchar(45) DEFAULT NULL,
   `telefono` varchar(45) DEFAULT NULL,
   `cedula` char(10) NOT NULL,
   PRIMARY KEY (`id_tutor`),
   UNIQUE KEY `cedula_UNIQUE` (`cedula`),
   UNIQUE KEY `id_tutor_UNIQUE` (`id_tutor`)
 ) ENGINE=InnoDB AUTO_INCREMENT=219 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci
 
 
 CREATE TABLE `ESTUDIANTES` (
   `id_estudiante` int NOT NULL AUTO_INCREMENT,
   `nombre` varchar(45) NOT NULL,
   `apellido` varchar(45) NOT NULL,
   `carrera` varchar(45) DEFAULT NULL,
   `nacimiento` date NOT NULL,
   `cedula` char(10) NOT NULL,
   PRIMARY KEY (`id_estudiante`),
   UNIQUE KEY `cedula_UNIQUE` (`cedula`),
   UNIQUE KEY `id_estudiante_UNIQUE` (`id_estudiante`)
 ) ENGINE=InnoDB AUTO_INCREMENT=119 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci
 
 
 
 CREATE TABLE `PRACTICAS` (
   `id_practica` int NOT NULL AUTO_INCREMENT,
   `id_estudiante` int NOT NULL,
   `id_empresa` int NOT NULL,
   `horas` int NOT NULL,
   `fecha` date NOT NULL,
   `descripcion` varchar(100) DEFAULT NULL,
   `id_tutor` int NOT NULL,
   `estado` tinyint NOT NULL DEFAULT '0',
   PRIMARY KEY (`id_practica`),
   UNIQUE KEY `id_practica_UNIQUE` (`id_practica`),
   KEY `PRACTICAS_ibfk_1` (`id_empresa`),
   KEY `PRACTICAS_ibfk_2` (`id_estudiante`),
   KEY `PRACTICAS_ibfk_3` (`id_tutor`),
   CONSTRAINT `PRACTICAS_ibfk_1` FOREIGN KEY (`id_empresa`) REFERENCES `EMPRESAS` (`id_empresa`),
   CONSTRAINT `PRACTICAS_ibfk_2` FOREIGN KEY (`id_estudiante`) REFERENCES `ESTUDIANTES` (`id_estudiante`),
   CONSTRAINT `PRACTICAS_ibfk_3` FOREIGN KEY (`id_tutor`) REFERENCES `TUTORES` (`id_tutor`)
 ) ENGINE=InnoDB AUTO_INCREMENT=56 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci