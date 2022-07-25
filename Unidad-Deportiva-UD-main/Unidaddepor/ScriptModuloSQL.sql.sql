/*==============================================================*/
/* DBMS name:      ORACLE Version 11g                           */
/* Created on:     18/07/2022 10:55:54 p. m.                    */
/*==============================================================*/


alter table DEPORTE_TIPODEPORTE
   drop constraint FK_DEPORTE__RELDEP_DE_DEPORTE;

alter table DEPORTE_TIPODEPORTE
   drop constraint FK_DEPORTE__RELTIPODE_TIPODEPO;

alter table EMPLEADO
   drop constraint FK_EMPLEADO_RELPERSON_PERSONA;

alter table EMPLEADO_CARGO
   drop constraint FK_EMPLEADO_RELCARGO__CARGO;

alter table EMPLEADO_CARGO
   drop constraint FK_EMPLEADO_RELEMP_EM_EMPLEADO;

alter table EMPLEADO_CURSO
   drop constraint FK_EMPLEADO_RELCURSO__CURSO;

alter table EMPLEADO_CURSO
   drop constraint FK_EMPLEADO_RELEMPLEA_EMPLEADO;

alter table ESTUDIANTE
   drop constraint FK_ESTUDIAN_RELPERSON_PERSONA;

alter table MATERIAL
   drop constraint FK_MATERIAL_RELEST_MA_ESTADO;

alter table MATERIAL_PRACTICA
   drop constraint FK_MATERIAL_RELMAT_MA_MATERIAL;

alter table MATERIAL_PRACTICA
   drop constraint FK_MATERIAL_RELPRA_MA_PRACTICA;

alter table PERSONA
   drop constraint FK_PERSONA_RELTIPODO_TIPODOCU;

alter table PRACTICA
   drop constraint FK_PRACTICA_RELCUR_PR_CURSO;

alter table PRACTICA
   drop constraint FK_PRACTICA_RELDEP_PR_DEPORTE;

alter table PRACTICA
   drop constraint FK_PRACTICA_RELESP_PR_ESPACIO;

alter table PRACTICA
   drop constraint FK_PRACTICA_RELESTUDI_ESTUDIAN;

alter table PRACTICA
   drop constraint FK_PRACTICA_RELPRA_ES_ESTADOPR;

alter table PRACTICA
   drop constraint FK_PRACTICA_RELTIPOPR_TIPOPRAC;

alter table TIPODEPORTE
   drop constraint FK_TIPODEPO_RELPRACTI_ESTUDIAN;

drop table CARGO cascade constraints;

drop table CURSO cascade constraints;

drop table DEPORTE cascade constraints;

drop index RELTIPODEP_DEPTIPODEP_FK;

drop index RELDEP_DEPTIPODEP_FK;

drop table DEPORTE_TIPODEPORTE cascade constraints;

drop table EMPLEADO cascade constraints;

drop index RELCARGO_EMPCAR_FK;

drop index RELEMP_EMPCAR_FK;

drop table EMPLEADO_CARGO cascade constraints;

drop index RELCURSO_EMPCUR_FK;

drop index RELEMPLEADO_EMPCUR_FK;

drop table EMPLEADO_CURSO cascade constraints;

drop table ESPACIO cascade constraints;

drop table ESTADO cascade constraints;

drop table ESTADOPRACTICA cascade constraints;

drop index RELESTUDIANTE_PERSONA_FK;

drop table ESTUDIANTE cascade constraints;

drop index RELEST_MAT_FK;

drop table MATERIAL cascade constraints;

drop index RELMAT_MATPRA_FK;

drop index RELPRA_MATPRA_FK;

drop table MATERIAL_PRACTICA cascade constraints;

drop table PERSONA cascade constraints;

drop index RELPRA_ESTPRA_FK;

drop index RELESP_PRA_FK;

drop index RELDEP_PRA_FK;

drop index RELTIPOPRA_PRA_FK;

drop index RELCUR_PRA_FK;

drop index RELEST_PRA2_FK;

drop index RELEST_PRA1_FK;

drop table PRACTICA cascade constraints;

drop table TIPODEPORTE cascade constraints;

drop table TIPODOCUMENTO cascade constraints;

drop table TIPOPRACTICA cascade constraints;

/*==============================================================*/
/* Table: CARGO                                                 */
/*==============================================================*/
create table CARGO 
(
   IDCARGO              VARCHAR2(4)          not null,
   constraint PK_CARGO primary key (IDCARGO)
);

/*==============================================================*/
/* Table: CURSO                                                 */
/*==============================================================*/
create table CURSO 
(
   IDCURSO              INTEGER              not null,
   NOMBRECURSO          VARCHAR2(40)         not null,
   CAPACIDAD            INTEGER              not null,
   constraint PK_CURSO primary key (IDCURSO)
);

/*==============================================================*/
/* Table: DEPORTE                                               */
/*==============================================================*/
create table DEPORTE 
(
   IDDEPORTE            INTEGER              not null,
   NOMBREDEPORTE        VARCHAR2(20)         not null,
   DESCRIPCIONDEPORTE   VARCHAR2(100)        not null,
   constraint PK_DEPORTE primary key (IDDEPORTE)
);

/*==============================================================*/
/* Table: DEPORTE_TIPODEPORTE                                   */
/*==============================================================*/
create table DEPORTE_TIPODEPORTE 
(
   IDDEPORTE_TIPODEPORTE INTEGER              not null,
   IDDEPORTEFK2         INTEGER              not null,
   IDTIPODEPORTEFK      INTEGER              not null,
   constraint PK_DEPORTE_TIPODEPORTE primary key (IDDEPORTE_TIPODEPORTE)
);

/*==============================================================*/
/* Index: RELDEP_DEPTIPODEP_FK                                  */
/*==============================================================*/
create index RELDEP_DEPTIPODEP_FK on DEPORTE_TIPODEPORTE (
   IDDEPORTEFK2 ASC
);

/*==============================================================*/
/* Index: RELTIPODEP_DEPTIPODEP_FK                              */
/*==============================================================*/
create index RELTIPODEP_DEPTIPODEP_FK on DEPORTE_TIPODEPORTE (
   IDTIPODEPORTEFK ASC
);

/*==============================================================*/
/* Table: EMPLEADO                                              */
/*==============================================================*/
create table EMPLEADO 
(
   IDEMPLEADO           INTEGER              not null,
   IDPERSONAFK2         INTEGER              not null,
   DEPENDENCIA          VARCHAR2(30)         not null,
   constraint PK_EMPLEADO primary key (IDEMPLEADO)
);

/*==============================================================*/
/* Table: EMPLEADO_CARGO                                        */
/*==============================================================*/
create table EMPLEADO_CARGO 
(
   IDEMPLEADO_CARGO     INTEGER              not null,
   IDEMPLEADOFK         INTEGER              not null,
   IDCARGOFK            VARCHAR2(4)          not null,
   FECHAINICIO          DATE                 not null,
   constraint PK_EMPLEADO_CARGO primary key (IDEMPLEADO_CARGO)
);

/*==============================================================*/
/* Index: RELEMP_EMPCAR_FK                                      */
/*==============================================================*/
create index RELEMP_EMPCAR_FK on EMPLEADO_CARGO (
   IDEMPLEADOFK ASC
);

/*==============================================================*/
/* Index: RELCARGO_EMPCAR_FK                                    */
/*==============================================================*/
create index RELCARGO_EMPCAR_FK on EMPLEADO_CARGO (
   IDCARGOFK ASC
);

/*==============================================================*/
/* Table: EMPLEADO_CURSO                                        */
/*==============================================================*/
create table EMPLEADO_CURSO 
(
   IDEMPLEADO_CURSO     INTEGER              not null,
   IDEMPLEADOFK2        INTEGER              not null,
   IDCURSOFK2           INTEGER              not null,
   constraint PK_EMPLEADO_CURSO primary key (IDEMPLEADO_CURSO)
);

/*==============================================================*/
/* Index: RELEMPLEADO_EMPCUR_FK                                 */
/*==============================================================*/
create index RELEMPLEADO_EMPCUR_FK on EMPLEADO_CURSO (
   IDEMPLEADOFK2 ASC
);

/*==============================================================*/
/* Index: RELCURSO_EMPCUR_FK                                    */
/*==============================================================*/
create index RELCURSO_EMPCUR_FK on EMPLEADO_CURSO (
   IDCURSOFK2 ASC
);

/*==============================================================*/
/* Table: ESPACIO                                               */
/*==============================================================*/
create table ESPACIO 
(
   IDESPACIO            INTEGER              not null,
   NOMBREESPACIO        VARCHAR2(30)         not null,
   SEDE                 VARCHAR2(40)         not null,
   DIRECCIONESPACIO     VARCHAR2(50)         not null,
   constraint PK_ESPACIO primary key (IDESPACIO)
);

/*==============================================================*/
/* Table: ESTADO                                                */
/*==============================================================*/
create table ESTADO 
(
   IDESTADO             NUMBER(1)            not null,
   ESTADO               VARCHAR2(20)         not null,
   constraint PK_ESTADO primary key (IDESTADO)
);

/*==============================================================*/
/* Table: ESTADOPRACTICA                                        */
/*==============================================================*/
create table ESTADOPRACTICA 
(
   IDESTADOPRACTICA     INTEGER              not null,
   ESTADOPRACTICA       VARCHAR2(15)         not null,
   DESCRIPCIONESTADO    VARCHAR2(50)         not null,
   constraint PK_ESTADOPRACTICA primary key (IDESTADOPRACTICA)
);

/*==============================================================*/
/* Table: ESTUDIANTE                                            */
/*==============================================================*/
create table ESTUDIANTE 
(
   IDESTUDIANTE         NUMBER(11)           not null,
   IDPERSONAFK          INTEGER              not null,
   PROYECTOCURRICULAR   VARCHAR2(30)         not null,
   constraint PK_ESTUDIANTE primary key (IDESTUDIANTE)
);

/*==============================================================*/
/* Index: RELESTUDIANTE_PERSONA_FK                              */
/*==============================================================*/
create index RELESTUDIANTE_PERSONA_FK on ESTUDIANTE (
   IDESTUDIANTE ASC
);

/*==============================================================*/
/* Table: MATERIAL                                              */
/*==============================================================*/
create table MATERIAL 
(
   IDMATERIAL           INTEGER              not null,
   IDESTADOFK           NUMBER(1)            not null,
   NOMBREMATERIAL       VARCHAR2(30)         not null,
   MARCA                VARCHAR2(20)         not null,
   FECHAADQUISICION     DATE                 not null,
   constraint PK_MATERIAL primary key (IDMATERIAL)
);

/*==============================================================*/
/* Index: RELEST_MAT_FK                                         */
/*==============================================================*/
create index RELEST_MAT_FK on MATERIAL (
   IDESTADOFK ASC
);

/*==============================================================*/
/* Table: MATERIAL_PRACTICA                                     */
/*==============================================================*/
create table MATERIAL_PRACTICA 
(
   IDMATERIAL_PRACTICA  INTEGER              not null,
   IDPRACTICAFK         INTEGER              not null,
   IDMATERIALFK         INTEGER              not null,
   constraint PK_MATERIAL_PRACTICA primary key (IDMATERIAL_PRACTICA)
);

/*==============================================================*/
/* Index: RELPRA_MATPRA_FK                                      */
/*==============================================================*/
create index RELPRA_MATPRA_FK on MATERIAL_PRACTICA (
   IDPRACTICAFK ASC
);

/*==============================================================*/
/* Index: RELMAT_MATPRA_FK                                      */
/*==============================================================*/
create index RELMAT_MATPRA_FK on MATERIAL_PRACTICA (
   IDMATERIALFK ASC
);

/*==============================================================*/
/* Table: PERSONA                                               */
/*==============================================================*/
create table PERSONA 
(
   IDPERSONA            INTEGER              not null,
   IDTIPODOCUMENTOFK    VARCHAR2(3)          not null,
   NOMBRE               VARCHAR2(30)         not null,
   APELLIDO             VARCHAR2(30)         not null,
   CORREO               VARCHAR2(60)         not null,
   TELEFONO             INTEGER              not null,
   constraint AK_PERSONA_PERSONA unique (IDPERSONA)
);

/*==============================================================*/
/* Table: PRACTICA                                              */
/*==============================================================*/
create table PRACTICA 
(
   IDPRACTICA           INTEGER              not null,
   IDESTUDIANTEPRACTICANTE NUMBER(11)           not null,
   IDESTUDIANTEPASANTE  NUMBER(11),
   IDCURSOFK            INTEGER              not null,
   IDTIPOPRACTICAFK     VARCHAR2(3)          not null,
   IDDEPORTEFK          INTEGER              not null,
   IDESPACIOFK          INTEGER              not null,
   IDESTADOPRACTICAFK   INTEGER              not null,
   HORA                 DATE                 not null,
   FECHA                DATE                 not null,
   DURACION             DATE                 not null,
   constraint PK_PRACTICA primary key (IDPRACTICA)
);

/*==============================================================*/
/* Index: RELEST_PRA1_FK                                        */
/*==============================================================*/
create index RELEST_PRA1_FK on PRACTICA (
   IDESTUDIANTEPRACTICANTE ASC
);

/*==============================================================*/
/* Index: RELEST_PRA2_FK                                        */
/*==============================================================*/
create index RELEST_PRA2_FK on PRACTICA (
   IDESTUDIANTE ASC
);

/*==============================================================*/
/* Index: RELCUR_PRA_FK                                         */
/*==============================================================*/
create index RELCUR_PRA_FK on PRACTICA (
   IDCURSOFK ASC
);

/*==============================================================*/
/* Index: RELTIPOPRA_PRA_FK                                     */
/*==============================================================*/
create index RELTIPOPRA_PRA_FK on PRACTICA (
   IDTIPOPRACTICAFK ASC
);

/*==============================================================*/
/* Index: RELDEP_PRA_FK                                         */
/*==============================================================*/
create index RELDEP_PRA_FK on PRACTICA (
   IDDEPORTEFK ASC
);

/*==============================================================*/
/* Index: RELESP_PRA_FK                                         */
/*==============================================================*/
create index RELESP_PRA_FK on PRACTICA (
   IDESPACIOFK ASC
);

/*==============================================================*/
/* Index: RELPRA_ESTPRA_FK                                      */
/*==============================================================*/
create index RELPRA_ESTPRA_FK on PRACTICA (
   IDESTADOPRACTICAFK ASC
);

/*==============================================================*/
/* Table: TIPODEPORTE                                           */
/*==============================================================*/
create table TIPODEPORTE 
(
   IDTIPODEPORTE        INTEGER              not null,
   IDESTUDIANTE         NUMBER(11),
   CLASIFICACION        VARCHAR2(25)         not null,
   DESCRIPCIONTIPODEPORTE VARCHAR2(100)        not null,
   constraint PK_TIPODEPORTE primary key (IDTIPODEPORTE)
);

/*==============================================================*/
/* Table: TIPODOCUMENTO                                         */
/*==============================================================*/
create table TIPODOCUMENTO 
(
   IDTIPODOCUMENTO      VARCHAR2(3)          not null,
   NOMBREDOCUMENTO      VARCHAR2(30)         not null,
   constraint AK_IDENTIFIER_1_TIPODOCU unique (IDTIPODOCUMENTO)
);

/*==============================================================*/
/* Table: TIPOPRACTICA                                          */
/*==============================================================*/
create table TIPOPRACTICA 
(
   IDTIPOPRACTICA       VARCHAR2(3)          not null,
   DESCRIPCIONTIPOPRACTICA VARCHAR2(100)        not null,
   constraint PK_TIPOPRACTICA primary key (IDTIPOPRACTICA)
);

alter table DEPORTE_TIPODEPORTE
   add constraint FK_DEPORTE__RELDEP_DE_DEPORTE foreign key (IDDEPORTEFK2)
      references DEPORTE (IDDEPORTE);

alter table DEPORTE_TIPODEPORTE
   add constraint FK_DEPORTE__RELTIPODE_TIPODEPO foreign key (IDTIPODEPORTEFK)
      references TIPODEPORTE (IDTIPODEPORTE);

alter table EMPLEADO
   add constraint FK_EMPLEADO_RELPERSON_PERSONA foreign key (IDPERSONAFK2)
      references PERSONA (IDPERSONA);

alter table EMPLEADO_CARGO
   add constraint FK_EMPLEADO_RELCARGO__CARGO foreign key (IDCARGOFK)
      references CARGO (IDCARGO);

alter table EMPLEADO_CARGO
   add constraint FK_EMPLEADO_RELEMP_EM_EMPLEADO foreign key (IDEMPLEADOFK)
      references EMPLEADO (IDEMPLEADO);

alter table EMPLEADO_CURSO
   add constraint FK_EMPLEADO_RELCURSO__CURSO foreign key (IDCURSOFK2)
      references CURSO (IDCURSO);

alter table EMPLEADO_CURSO
   add constraint FK_EMPLEADO_RELEMPLEA_EMPLEADO foreign key (IDEMPLEADOFK2)
      references EMPLEADO (IDEMPLEADO);

alter table ESTUDIANTE
   add constraint FK_ESTUDIAN_RELPERSON_PERSONA foreign key (IDESTUDIANTE)
      references PERSONA (IDPERSONA);

alter table MATERIAL
   add constraint FK_MATERIAL_RELEST_MA_ESTADO foreign key (IDESTADOFK)
      references ESTADO (IDESTADO);

alter table MATERIAL_PRACTICA
   add constraint FK_MATERIAL_RELMAT_MA_MATERIAL foreign key (IDMATERIALFK)
      references MATERIAL (IDMATERIAL);

alter table MATERIAL_PRACTICA
   add constraint FK_MATERIAL_RELPRA_MA_PRACTICA foreign key (IDPRACTICAFK)
      references PRACTICA (IDPRACTICA);

alter table PERSONA
   add constraint FK_PERSONA_RELTIPODO_TIPODOCU foreign key (IDTIPODOCUMENTOFK)
      references TIPODOCUMENTO (IDTIPODOCUMENTO);

alter table PRACTICA
   add constraint FK_PRACTICA_RELCUR_PR_CURSO foreign key (IDCURSOFK)
      references CURSO (IDCURSO);

alter table PRACTICA
   add constraint FK_PRACTICA_RELDEP_PR_DEPORTE foreign key (IDDEPORTEFK)
      references DEPORTE (IDDEPORTE);

alter table PRACTICA
   add constraint FK_PRACTICA_RELESP_PR_ESPACIO foreign key (IDESPACIOFK)
      references ESPACIO (IDESPACIO);

alter table PRACTICA
   add constraint FK_PRACTICA_RELESTUDI_ESTUDIAN foreign key (IDESTUDIANTEPRACTICANTE)
      references ESTUDIANTE (IDESTUDIANTE);

alter table PRACTICA
   add constraint FK_PRACTICA_RELPRA_ES_ESTADOPR foreign key (IDESTADOPRACTICAFK)
      references ESTADOPRACTICA (IDESTADOPRACTICA);

alter table PRACTICA
   add constraint FK_PRACTICA_RELTIPOPR_TIPOPRAC foreign key (IDTIPOPRACTICAFK)
      references TIPOPRACTICA (IDTIPOPRACTICA);

alter table TIPODEPORTE
   add constraint FK_TIPODEPO_RELPRACTI_ESTUDIAN foreign key (IDESTUDIANTE)
      references ESTUDIANTE (IDESTUDIANTE);

