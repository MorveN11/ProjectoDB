CREATE TABLE IF NOT EXISTS public.departamento
(
    id_departamento smallserial NOT NULL,
    departamento character varying(30) COLLATE pg_catalog."default" NOT NULL,
    funciones character varying(50) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT departamento_pkey PRIMARY KEY (id_departamento)
);


CREATE TABLE IF NOT EXISTS public.cargo
(
    id_cargo serial NOT NULL,
    cargo character varying(30) COLLATE pg_catalog."default" NOT NULL,
    sueldo integer NOT NULL,
    id_departamento smallint NOT NULL,
    CONSTRAINT cargo_pkey PRIMARY KEY (id_cargo),
    CONSTRAINT cargo_id_departamento_fkey FOREIGN KEY (id_departamento)
        REFERENCES public.departamento (id_departamento) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
);


CREATE TABLE IF NOT EXISTS public.empleado
(
    id_empleado bigserial NOT NULL,
    dias_vacacionales smallint DEFAULT 0,
    estado_laboral character varying(15) COLLATE pg_catalog."default" DEFAULT 'activo'::character varying,
    dias_trabajados bigint DEFAULT 0,
    id_cargo integer NOT NULL,
    CONSTRAINT empleado_pkey PRIMARY KEY (id_empleado),
    CONSTRAINT empleado_id_cargo_fkey FOREIGN KEY (id_cargo)
        REFERENCES public.cargo (id_cargo) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
);


CREATE TABLE IF NOT EXISTS public.tipo_vivienda
(
    id_tipo_vivienda smallserial NOT NULL,
    tipo character varying(15) COLLATE pg_catalog."default" NOT NULL,
    diferenciador integer NOT NULL,
    CONSTRAINT tipo_vivienda_pkey PRIMARY KEY (id_tipo_vivienda)
);


CREATE TABLE IF NOT EXISTS public.zona
(
    id_zona smallserial NOT NULL,
    zona character varying(15) COLLATE pg_catalog."default" NOT NULL,
    extension_ha integer NOT NULL,
    antiguedad_dias integer NOT NULL,
    CONSTRAINT zona_pkey PRIMARY KEY (id_zona)
);

CREATE TABLE IF NOT EXISTS public.sueldo
(
    id_sueldo bigserial NOT NULL,
    sueldo integer NOT NULL,
    aportes_afps double precision NOT NULL,
    id_empleado bigint NOT NULL,
    CONSTRAINT sueldo_pkey PRIMARY KEY (id_sueldo),
    CONSTRAINT sueldo_id_empleado_key UNIQUE (id_empleado),
    CONSTRAINT sueldo_id_empleado_fkey FOREIGN KEY (id_empleado)
        REFERENCES public.empleado (id_empleado) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
);

CREATE TABLE IF NOT EXISTS public.cliente
(
    id_cliente bigserial NOT NULL,
    nombre_1 character varying(30) COLLATE pg_catalog."default" NOT NULL,
    nombre_2 character varying(30) COLLATE pg_catalog."default" DEFAULT '-'::character varying,
    apellido_1 character varying(30) COLLATE pg_catalog."default" NOT NULL,
    apellido_2 character varying(30) COLLATE pg_catalog."default" DEFAULT '-'::character varying,
    telefono character varying(20) COLLATE pg_catalog."default" NOT NULL,
    nit integer DEFAULT 0,
    CONSTRAINT cliente_pkey PRIMARY KEY (id_cliente)
);

CREATE TABLE IF NOT EXISTS public.vivienda
(
    id_vivienda bigserial NOT NULL,
    numero character varying(10) COLLATE pg_catalog."default" NOT NULL,
    id_zona smallint NOT NULL,
    id_tipo_vivienda smallint NOT NULL,
    id_cliente bigint NOT NULL,
    CONSTRAINT vivienda_pkey PRIMARY KEY (id_vivienda),
    CONSTRAINT vivienda_id_cliente_key UNIQUE (id_cliente),
    CONSTRAINT vivienda_id_cliente_fkey FOREIGN KEY (id_cliente)
        REFERENCES public.cliente (id_cliente) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT vivienda_id_tipo_vivienda_fkey FOREIGN KEY (id_tipo_vivienda)
        REFERENCES public.tipo_vivienda (id_tipo_vivienda) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT vivienda_id_zona_fkey FOREIGN KEY (id_zona)
        REFERENCES public.zona (id_zona) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
);

CREATE TABLE IF NOT EXISTS public.postulante
(
    id_postulante bigserial NOT NULL,
    nombre_1 character varying(30) COLLATE pg_catalog."default" NOT NULL,
    nombre_2 character varying(30) COLLATE pg_catalog."default" DEFAULT '-'::character varying,
    apellido_1 character varying(30) COLLATE pg_catalog."default" NOT NULL,
    apellido_2 character varying(30) COLLATE pg_catalog."default" DEFAULT '-'::character varying,
    telefono character varying(15) COLLATE pg_catalog."default" DEFAULT 0,
    correo_electronico character varying(40) COLLATE pg_catalog."default" NOT NULL,
    numero_carnet_identidad character varying(20) COLLATE pg_catalog."default" NOT NULL,
    lugar_nacimiento character varying(30) COLLATE pg_catalog."default" NOT NULL,
    fecha_nacimiento date NOT NULL,
    estado_civil character varying(20) COLLATE pg_catalog."default" NOT NULL,
    id_cargo_solicitado smallint NOT NULL,
    CONSTRAINT postulante_pkey PRIMARY KEY (id_postulante)
);


CREATE TABLE IF NOT EXISTS public.rendimiento
(
    id_rendimiento smallserial NOT NULL,
    rendimiento smallint NOT NULL,
    bono_bs integer NOT NULL,
    CONSTRAINT rendimiento_pkey PRIMARY KEY (id_rendimiento)
);

CREATE TABLE IF NOT EXISTS public.proveedor
(
    id_proveedor smallserial NOT NULL,
    nombre_1 character varying(30) COLLATE pg_catalog."default" NOT NULL,
    nombre_2 character varying(30) COLLATE pg_catalog."default" DEFAULT '-'::character varying,
    apellido_1 character varying(30) COLLATE pg_catalog."default" NOT NULL,
    apellido_2 character varying(30) COLLATE pg_catalog."default" DEFAULT '-'::character varying,
    telefono character varying(20) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT proveedor_pkey PRIMARY KEY (id_proveedor)
);

CREATE TABLE IF NOT EXISTS public.unidad_compra
(
    id_unidad_compra smallserial NOT NULL,
    unidad character varying(8) COLLATE pg_catalog."default" NOT NULL,
    costocu double precision NOT NULL,
    id_proveedor smallint NOT NULL,
    CONSTRAINT unidad_compra_pkey PRIMARY KEY (id_unidad_compra),
    CONSTRAINT unidad_compra_id_proveedor_key UNIQUE (id_proveedor),
    CONSTRAINT unidad_compra_id_proveedor_fkey FOREIGN KEY (id_proveedor)
        REFERENCES public.proveedor (id_proveedor) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
);

CREATE TABLE IF NOT EXISTS public.importe
(
    id_importe smallserial NOT NULL,
    costo_total double precision NOT NULL,
    cantidad integer NOT NULL,
    id_unidad_compra smallint NOT NULL,
    CONSTRAINT importe_pkey PRIMARY KEY (id_importe),
    CONSTRAINT importe_id_unidad_compra_key UNIQUE (id_unidad_compra),
    CONSTRAINT importe_id_unidad_compra_fkey FOREIGN KEY (id_unidad_compra)
        REFERENCES public.unidad_compra (id_unidad_compra) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
);

CREATE TABLE IF NOT EXISTS public.servicio
(
    id_servicio smallserial NOT NULL,
    nombre character varying(30) COLLATE pg_catalog."default" NOT NULL,
    utilidad double precision NOT NULL,
    costo_ventacu double precision NOT NULL,
    id_importe smallint NOT NULL,
    CONSTRAINT servicio_pkey PRIMARY KEY (id_servicio),
    CONSTRAINT servicio_id_importe_key UNIQUE (id_importe),
    CONSTRAINT servicio_id_importe_fkey FOREIGN KEY (id_importe)
        REFERENCES public.importe (id_importe) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
);

CREATE TABLE IF NOT EXISTS public.calificaciones
(
    id_calificaciones bigserial NOT NULL,
    calificacion double precision NOT NULL,
    id_cargo_promover smallint NOT NULL,
    resultado character varying(50) COLLATE pg_catalog."default" NOT NULL,
    id_empleado bigint NOT NULL,
    CONSTRAINT calificaciones_pkey PRIMARY KEY (id_calificaciones),
    CONSTRAINT calificaciones_id_empleado_fkey FOREIGN KEY (id_empleado)
        REFERENCES public.empleado (id_empleado) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
);


CREATE TABLE IF NOT EXISTS public.cliente_empleado
(
    id_cliente bigint NOT NULL,
    id_empleado bigint NOT NULL,
    consumo integer NOT NULL,
    rep_formulario smallint NOT NULL,
    total_pagado integer NOT NULL,
    fecha date NOT NULL,
    comunicado character varying(200) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT cliente_empleado_pkey PRIMARY KEY (id_cliente, id_empleado),
    CONSTRAINT cliente_empleado_id_cliente_fkey FOREIGN KEY (id_cliente)
        REFERENCES public.cliente (id_cliente) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT cliente_empleado_id_empleado_fkey FOREIGN KEY (id_empleado)
        REFERENCES public.empleado (id_empleado) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
);

CREATE TABLE IF NOT EXISTS public.cliente_servicio
(
    id_cliente bigint NOT NULL,
    id_servicio smallint NOT NULL,
    n_medidor character varying(20) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT cliente_servicio_pkey PRIMARY KEY (id_cliente, id_servicio),
    CONSTRAINT cliente_servicio_id_cliente_fkey FOREIGN KEY (id_cliente)
        REFERENCES public.cliente (id_cliente) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT cliente_servicio_id_servicio_fkey FOREIGN KEY (id_servicio)
        REFERENCES public.servicio (id_servicio) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
);

CREATE TABLE IF NOT EXISTS public.datos
(
    id_datos bigserial NOT NULL,
    nombre1 character varying(200) COLLATE pg_catalog."default" NOT NULL,
    nombre2 character varying(200) COLLATE pg_catalog."default" DEFAULT '-'::character varying,
    apellido1 character varying(200) COLLATE pg_catalog."default" NOT NULL,
    apellido2 character varying(200) COLLATE pg_catalog."default" DEFAULT '-'::character varying,
    telefono character varying(200) COLLATE pg_catalog."default" NOT NULL,
    correo_electronico character varying(200) COLLATE pg_catalog."default" DEFAULT '-'::character varying,
    codigo_seguro integer NOT NULL,
    numero_carnet_identidad integer NOT NULL,
    lugar_nacimiento character varying(200) COLLATE pg_catalog."default" NOT NULL,
    fecha_nacimiento date NOT NULL,
    estado_civil character varying(200) COLLATE pg_catalog."default" NOT NULL,
    id_empleado bigint NOT NULL,
    CONSTRAINT datos_pkey PRIMARY KEY (id_datos),
    CONSTRAINT datos_id_empleado_key UNIQUE (id_empleado),
    CONSTRAINT datos_id_empleado_fkey FOREIGN KEY (id_empleado)
        REFERENCES public.empleado (id_empleado) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
);

CREATE TABLE IF NOT EXISTS public.empleado_rendimiento
(
    id_empleado bigint NOT NULL,
    id_rendimiento smallint NOT NULL,
    descripcion character varying(100) COLLATE pg_catalog."default" DEFAULT '-'::character varying,
    CONSTRAINT empleado_rendimiento_pkey PRIMARY KEY (id_empleado, id_rendimiento),
    CONSTRAINT empleado_rendimiento_id_empleado_key UNIQUE (id_empleado),
    CONSTRAINT empleado_rendimiento_id_empleado_fkey FOREIGN KEY (id_empleado)
        REFERENCES public.empleado (id_empleado) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT empleado_rendimiento_id_rendimiento_fkey FOREIGN KEY (id_rendimiento)
        REFERENCES public.rendimiento (id_rendimiento) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
);

    
CREATE TABLE IF NOT EXISTS public.entrevista
(
    id_entrevista bigserial NOT NULL,
    observaciones character varying(200) COLLATE pg_catalog."default" DEFAULT '-'::character varying,
    resultado character varying(50) COLLATE pg_catalog."default" NOT NULL,
    fecha date NOT NULL,
    id_empleado bigint NOT NULL,
    id_postulante bigint NOT NULL,
    CONSTRAINT entrevista_pkey PRIMARY KEY (id_entrevista),
    CONSTRAINT entrevista_id_postulante_key UNIQUE (id_postulante),
    CONSTRAINT entrevista_id_empleado_fkey FOREIGN KEY (id_empleado)
        REFERENCES public.empleado (id_empleado) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT entrevista_id_postulante_fkey FOREIGN KEY (id_postulante)
        REFERENCES public.postulante (id_postulante) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
);

CREATE TABLE IF NOT EXISTS public.historial_datos
(
    id_datos bigint NOT NULL,
    nombre_1 character varying(30) COLLATE pg_catalog."default" NOT NULL,
    nombre_2 character varying(30) COLLATE pg_catalog."default" DEFAULT '-'::character varying,
    apellido_1 character varying(30) COLLATE pg_catalog."default" NOT NULL,
    apellido_2 character varying(30) COLLATE pg_catalog."default" DEFAULT '-'::character varying,
    telefono character varying(30) COLLATE pg_catalog."default" NOT NULL,
    numero_carnet integer NOT NULL,
    date_op timestamp without time zone NOT NULL
);

CREATE TABLE IF NOT EXISTS public.historial_empleados_rendimientos
(
    id_empleado integer NOT NULL,
    id_rendimiento integer NOT NULL,
    descripcion character varying(200) COLLATE pg_catalog."default" DEFAULT '-'::character varying,
    fecha timestamp without time zone NOT NULL
);


CREATE TABLE IF NOT EXISTS public.historial_importes
(
    id_importe smallint NOT NULL,
    costo_total double precision NOT NULL,
    cantidad integer NOT NULL,
    id_unidad_compra smallint NOT NULL,
    date_op timestamp without time zone NOT NULL
);

CREATE TABLE IF NOT EXISTS public.historial_proveedores
(
    id_proveedor smallint NOT NULL,
    nombre_1 character varying(30) COLLATE pg_catalog."default" NOT NULL,
    nombre_2 character varying(30) COLLATE pg_catalog."default" DEFAULT '-'::character varying,
    apellido_1 character varying(30) COLLATE pg_catalog."default" NOT NULL,
    apellido_2 character varying(30) COLLATE pg_catalog."default" DEFAULT '-'::character varying,
    telefono character varying(30) COLLATE pg_catalog."default" NOT NULL,
    date_op timestamp without time zone NOT NULL
);

CREATE TABLE IF NOT EXISTS public.historial_servicios
(
    id_servicio smallint NOT NULL,
    nombre character varying(30) COLLATE pg_catalog."default" NOT NULL,
    utilidad double precision NOT NULL,
    costo_ventacu double precision NOT NULL,
    id_importe smallint NOT NULL,
    date_op timestamp without time zone NOT NULL
);

CREATE TABLE IF NOT EXISTS public.historial_sueldos
(
    id_sueldo bigint NOT NULL,
    sueldo integer NOT NULL,
    aportes_afps double precision NOT NULL,
    id_empleado bigint NOT NULL,
    date_op timestamp without time zone NOT NULL
);

CREATE TABLE IF NOT EXISTS public.historial_unidades_compra
(
    id_unidad_compra smallint NOT NULL,
    unidad character varying(30) COLLATE pg_catalog."default" NOT NULL,
    costocu double precision NOT NULL,
    id_proveedor smallint NOT NULL,
    date_op timestamp without time zone NOT NULL
);


CREATE OR REPLACE FUNCTION public.backup()
    RETURNS trigger
    LANGUAGE 'plpgsql'
    COST 100
    VOLATILE NOT LEAKPROOF
AS $BODY$
	BEGIN
		IF (TG_OP = 'DELETE') THEN
			INSERT INTO historial_rendimiento SELECT OLD.*, now();
		END IF;
		RETURN NULL;
	END;
$BODY$;

CREATE OR REPLACE FUNCTION public.share_emp()
    RETURNS trigger
    LANGUAGE 'plpgsql'
    COST 100
    VOLATILE NOT LEAKPROOF
AS $BODY$
	BEGIN	
		IF(TG_OP = 'DELETE') THEN
			INSERT INTO historial_datos_empleados SELECT OLD.id_datos, OLD.nombre1, OLD.nombre2, OLD.apellido1, 
				OLD.apellido2, OLD.telefono, OLD.numero_carnet_identidad, now();
		ELSEIF(TG_OP = 'UPDATE') THEN
			INSERT INTO historial_datos_empleados SELECT OLD.id_datos, OLD.nombre1, OLD.nombre2, OLD.apellido1, 
				OLD.apellido2, OLD.telefono, OLD.numero_carnet_identidad, now();
		END IF;
		RETURN NULL;
	END;
$BODY$;

CREATE OR REPLACE FUNCTION public.share_import()
    RETURNS trigger
    LANGUAGE 'plpgsql'
    COST 100
    VOLATILE NOT LEAKPROOF
AS $BODY$
	BEGIN
        IF(NEW.cantidad is not null AND NEW.cantidad != OLD.cantidad) THEN
          IF(TG_OP = 'DELETE') THEN
              INSERT INTO historial_importes SELECT OLD.*, now();
          ELSEIF(TG_OP = 'UPDATE') THEN
              INSERT INTO historial_importes SELECT OLD.*, now();
          END IF;
        END IF;
        RETURN NULL;
	END;
$BODY$;

CREATE OR REPLACE FUNCTION public.share_service()
    RETURNS trigger
    LANGUAGE 'plpgsql'
    COST 100
    VOLATILE NOT LEAKPROOF
AS $BODY$
	BEGIN	
		IF(TG_OP = 'DELETE') THEN
			INSERT INTO historial_servicios SELECT OLD.*, now();
		ELSEIF(TG_OP = 'UPDATE') THEN
			INSERT INTO historial_servicios SELECT OLD.*, now();
		END IF;
		RETURN NULL;
	END;
$BODY$;

CREATE OR REPLACE FUNCTION public.share_sueldo()
    RETURNS trigger
    LANGUAGE 'plpgsql'
    COST 100
    VOLATILE NOT LEAKPROOF
AS $BODY$
	BEGIN	
		IF(TG_OP = 'DELETE') THEN
			INSERT INTO historial_sueldos SELECT OLD.*, now();
		ELSEIF(TG_OP = 'UPDATE') THEN
			INSERT INTO historial_sueldos SELECT OLD.*, now();
		END IF;
		RETURN NULL;
	END;
$BODY$;

CREATE OR REPLACE FUNCTION public.share_sup()
    RETURNS trigger
    LANGUAGE 'plpgsql'
    COST 100
    VOLATILE NOT LEAKPROOF
AS $BODY$
	BEGIN	
		IF(TG_OP = 'DELETE') THEN
			INSERT INTO historial_proveedores SELECT OLD.*, now();
		ELSEIF(TG_OP = 'UPDATE') THEN
			INSERT INTO historial_proveedores SELECT OLD.*, now();
		END IF;
		RETURN NULL;
	END;
$BODY$;

CREATE OR REPLACE FUNCTION public.share_unit_b()
    RETURNS trigger
    LANGUAGE 'plpgsql'
    COST 100
    VOLATILE NOT LEAKPROOF
AS $BODY$
	BEGIN	
		IF(TG_OP = 'DELETE') THEN
			INSERT INTO historial_unidad_compra SELECT OLD.*, now();
		ELSEIF(TG_OP = 'UPDATE') THEN
			INSERT INTO historial_unidad_compra SELECT OLD.*, now();
		END IF;
		RETURN NULL;
	END;
$BODY$;


CREATE OR REPLACE FUNCTION public.upd_importe()
    RETURNS trigger
    LANGUAGE 'plpgsql'
    COST 100
    VOLATILE NOT LEAKPROOF
AS $BODY$
DECLARE

	total_cost FLOAT;
	cost_cu FLOAT;
	amount FLOAT;
	
BEGIN   
	IF(TG_OP = 'UPDATE') THEN
		IF(NEW.cantidad is not null AND NEW.cantidad != OLD.cantidad) THEN
			cost_cu = (SELECT unicomp.costocu FROM unidad_compra AS unicomp WHERE unicomp.id_unidad_compra = OLD.id_importe);	
			UPDATE importe SET costo_total = (cost_cu*NEW.cantidad) WHERE id_importe = OLD.id_importe;
		END IF;
	END IF;
	RETURN NULL;
END;
$BODY$;

CREATE OR REPLACE FUNCTION public.upd_servicio()
    RETURNS trigger
    LANGUAGE 'plpgsql'
    COST 100
    VOLATILE NOT LEAKPROOF
AS $BODY$
DECLARE
    cost_cu FLOAT;
    utility FLOAT;
    newcostcu FLOAT;
    
BEGIN   
    IF(TG_OP = 'UPDATE') THEN
        IF(NEW.utilidad is not null AND NEW.utilidad != OLD.utilidad) THEN
			cost_cu = (SELECT costocu FROM servicio, importe, unidad_compra WHERE servicio.id_importe = importe.id_importe AND importe.id_unidad_compra = unidad_compra.id_unidad_compra AND servicio.id_servicio = OLD.id_servicio);
			utility = (SELECT utilidad FROM servicio WHERE id_servicio = OLD.id_servicio);
			newcostcu = cost_cu+((cost_cu*utility)/100);
			UPDATE servicio SET costo_ventacu = newcostcu WHERE id_servicio = OLD.id_servicio;
        END IF;
    END IF;
    RETURN NULL;
END;
$BODY$;

CREATE OR REPLACE FUNCTION public.upd_unida_compra()
    RETURNS trigger
    LANGUAGE 'plpgsql'
    COST 100
    VOLATILE NOT LEAKPROOF
AS $BODY$
DECLARE
    id_UC SMALLINT;
    costo_compra FLOAT;
    amount INT;
    import_id SMALLINT;
    utility FLOAT;
    costo_venta FLOAT;
BEGIN   
    IF(TG_OP = 'UPDATE') THEN
        id_UC = OLD.id_unidad_compra;
        costo_compra = NEW.costocu;
        amount = (SELECT i.cantidad FROM importe AS i WHERE i.id_importe = id_UC);
        import_id = (SELECT i.id_importe FROM importe AS i WHERE i.id_importe = id_UC);
        UPDATE importe AS imp SET costo_total = (costo_compra*amount) WHERE imp.id_importe = import_id;
        utility = (SELECT s.utilidad FROM servicio AS s WHERE s.id_servicio = import_id);
        costo_venta = (costo_compra + ((costo_compra*utility)/100));
        UPDATE servicio AS serv SET costo_ventacu = costo_venta WHERE serv.id_servicio = import_id;
    END IF;
    RETURN NULL;
END;
$BODY$;


CREATE TRIGGER share_data_emp
    AFTER INSERT OR DELETE OR UPDATE 
    ON public.datos
    FOR EACH ROW
    EXECUTE FUNCTION public.share_emp();
   
CREATE TRIGGER share_info
    AFTER DELETE
    ON public.empleado_rendimiento
    FOR EACH ROW
    EXECUTE FUNCTION public.backup();
   
CREATE TRIGGER share_data_impt
    AFTER INSERT OR DELETE OR UPDATE 
    ON public.importe
    FOR EACH ROW
    EXECUTE FUNCTION public.share_import();

CREATE TRIGGER update_import
    AFTER INSERT OR DELETE OR UPDATE 
    ON public.importe
    FOR EACH ROW
    EXECUTE FUNCTION public.upd_importe();
   
CREATE TRIGGER share_data_sup
    AFTER INSERT OR DELETE OR UPDATE 
    ON public.proveedor
    FOR EACH ROW
    EXECUTE FUNCTION public.share_sup();

CREATE TRIGGER share_data_serv
    AFTER INSERT OR DELETE OR UPDATE 
    ON public.servicio
    FOR EACH ROW
    EXECUTE FUNCTION public.share_service();
   
CREATE TRIGGER update_serv
    AFTER INSERT OR DELETE OR UPDATE 
    ON public.servicio
    FOR EACH ROW
    EXECUTE FUNCTION public.upd_servicio();
  
CREATE TRIGGER share_data_suel
    AFTER INSERT OR DELETE OR UPDATE
    ON public.sueldo
    FOR EACH ROW
    EXECUTE FUNCTION public.share_sueldo();
    
CREATE TRIGGER share_data_uni
    AFTER INSERT OR DELETE OR UPDATE
    ON public.unidad_compra
    FOR EACH ROW
    EXECUTE FUNCTION public.share_unit_b();

CREATE TRIGGER update_uc
    AFTER INSERT OR DELETE OR UPDATE
    ON public.unidad_compra
    FOR EACH ROW
    EXECUTE FUNCTION public.upd_unida_compra();
