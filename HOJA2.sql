SELECT*FROM PRACTICAS
SELECT*FROM ESTUDIANTES
PRACTICAS
SET SQL_SAFE_UPDATES = 0;

select* FROM EMPRESAS
select* FROM TUTORES

CREATE OR REPLACE VIEW  PracticasGLOBAL_con_estado AS

SELECT PRACTICAS.id_practica,
CONCAT_WS (' ',ESTUDIANTES.nombre,ESTUDIANTES.apellido) AS nombres_estudiante ,ESTUDIANTES.cedula,
EMPRESAS.nombre AS empresa,
PRACTICAS.horas,PRACTICAS.fecha,PRACTICAS.descripcion,PRACTICAS.estado
, CONCAT_WS(' ',TUTORES.nombre,TUTORES.apellido) AS nombres_tutor   
FROM PRACTICAS 
INNER JOIN EMPRESAS ON PRACTICAS.id_empresa=EMPRESAS.id_empresa
INNER JOIN ESTUDIANTES ON PRACTICAS.id_estudiante=ESTUDIANTES.id_estudiante
INNER JOIN TUTORES ON PRACTICAS.id_tutor=TUTORES.id_tutor

 

CREATE OR REPLACE VIEW  Nombres_tutores AS 
SELECT TUTORES.id_tutor,
 CONCAT_WS(' ',TUTORES.nombre,TUTORES.apellido) AS nombre_tutor,
 TUTORES.correo,
 TUTORES.telefono,
 TUTORES.cedula
 FROM  TUTORES
 
 CREATE OR REPLACE VIEW  Nombres_estudiantes AS 
 SELECT id_estudiante,
  CONCAT_WS(' ',nombre, apellido) AS nombre_tutor,
  carrera,
  nacimiento,
  cedula
  from ESTUDIANTES


 CREATE OR REPLACE VIEW reportes AS 
 SELECT ESTUDIANTES.cedula , PRACTICAS.horas , PRACTICAS.estado, ESTUDIANTES.nombre, ESTUDIANTES.apellido FROM PRACTICAS 
 INNER JOIN ESTUDIANTES 
 WHERE ESTUDIANTES.id_estudiante=PRACTICAS.id_estudiante
ESTUDIANTES
 



 

