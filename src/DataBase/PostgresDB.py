
import psycopg2


def connection():
    connect = psycopg2.connect(
        host='postgres',
        port='5432',
        user='manu',
        password='Admin123',
        database='tottem')
    return connect


def commit(connect, cursor, sql, insert):
    cursor.execute(sql, insert)
    connect.commit()
    cursor.close()
    connect.close()


def supplierInsert(name1, name2, lastName1, lastName2, cellphone):
    connect = connection()
    cursor = connect.cursor()
    sql = "INSERT INTO proveedor(nombre_1, nombre_2, apellido_1, apellido_2, telefono) " \
          "VALUES(%s, %s, %s, %s, %s)"
    insert = (name1, name2, lastName1, lastName2, cellphone)
    commit(connect, cursor, sql, insert)


def purchaseUnitInsert(unit, cost, supplierId):
    connect = connection()
    cursor = connect.cursor()
    sql = "INSERT INTO unidad_compra(unidad, costocu, id_proveedor) " \
          "VALUES(%s, %s, %s)"
    insert = (unit, cost, supplierId)
    commit(connect, cursor, sql, insert)


def importInsert(totalCost, amount, purchaseUnitId):
    connect = connection()
    cursor = connect.cursor()
    sql = "INSERT INTO importe(costo_total, cantidad, id_unidad_compra) " \
          "VALUES(%s, %s, %s)"
    insert = (totalCost, amount, purchaseUnitId)
    commit(connect, cursor, sql, insert)


def serviceInsert(name, utility, costSale, importId):
    connect = connection()
    cursor = connect.cursor()
    sql = "INSERT INTO servicio(nombre, utilidad, costo_ventacu, id_importe) " \
          "VALUES(%s, %s, %s, %s)"
    insert = (name, utility, costSale, importId)
    commit(connect, cursor, sql, insert)


def clientInsert(name1, name2, lastName1, lastName2, cellphone, nit):
    connect = connection()
    cursor = connect.cursor()
    sql = "INSERT INTO cliente(nombre_1, nombre_2, apellido_1, apellido_2, telefono, nit) " \
          "VALUES(%s, %s, %s, %s, %s, %s)"
    insert = (name1, name2, lastName1, lastName2, cellphone, nit)
    commit(connect, cursor, sql, insert)


def clientServiceInsert(clientId, serviceId, nMeasurer):
    connect = connection()
    cursor = connect.cursor()
    sql = "INSERT INTO cliente_servicio(id_cliente, id_servicio, n_medidor) " \
          "VALUES(%s, %s, %s)"
    insert = (clientId, serviceId, nMeasurer)
    commit(connect, cursor, sql, insert)


def zoneInsert(zone, extension, antiquity):
    connect = connection()
    cursor = connect.cursor()
    sql = "INSERT INTO zona(zona, extension_ha, antiguedad_dias) " \
          "VALUES(%s, %s, %s)"
    insert = (zone, extension, antiquity)
    commit(connect, cursor, sql, insert)


def typeLiveInsert(typeLive, differentiator):
    connect = connection()
    cursor = connect.cursor()
    sql = "INSERT INTO tipo_vivienda(tipo, diferenciador) " \
          "VALUES(%s, %s)"
    insert = (typeLive, differentiator)
    commit(connect, cursor, sql, insert)


def livePlaceInsert(number, zoneId, typeId, clientId):
    connect = connection()
    cursor = connect.cursor()
    sql = "INSERT INTO vivienda(numero, id_zona, id_tipo_vivienda, id_cliente) " \
          "VALUES(%s, %s, %s, %s)"
    insert = (number, zoneId, typeId, clientId)
    commit(connect, cursor, sql, insert)


def departamentInsert(department, functions):
    connect = connection()
    cursor = connect.cursor()
    sql = "INSERT INTO departamento(departamento, funciones) " \
          "VALUES(%s, %s)"
    insert = (department, functions)
    commit(connect, cursor, sql, insert)


def chargeInsert(charge, salary, departmentId):
    connect = connection()
    cursor = connect.cursor()
    sql = "INSERT INTO cargo(cargo, sueldo, id_departamento) " \
          "VALUES(%s, %s, %s, %s)"
    insert = (charge, salary, departmentId)
    commit(connect, cursor, sql, insert)


def employeeInsert(vacationDays, workStatus, workDays, chargeId):
    connect = connection()
    cursor = connect.cursor()
    sql = "INSERT INTO empleado(dias_vacacionales, estado_laboral, dias_trabajados, id_cargo) " \
          "VALUES(%s, %s, %s, %s)"
    insert = (vacationDays, workStatus, workDays, chargeId)
    commit(connect, cursor, sql, insert)


def clientEmployerInsert(clientId, employerId, consume, repFormulary, totalPaid, date, release):
    connect = connection()
    cursor = connect.cursor()
    sql = "INSERT INTO cliente_empleado(id_cliente, id_empleado, consumo, rep_formulario, " \
          "total_pagado, fecha, comunicado) " \
          "VALUES(%s, %s, %s, %s, %s, %s, %s)"
    insert = (clientId, employerId, consume, repFormulary, totalPaid, date, release)
    commit(connect, cursor, sql, insert)


def dataEmployeeInsert(name1, name2, lastName1, lastName2, cellphone, eMail, codeSecure,
                        numberCI, placeBirth, dateBirth, civilStatus, employerId):
    connect = connection()
    cursor = connect.cursor()
    sql = "INSERT INTO datos(nombre1, nombre2, apellido1, apellido2, telefono, correo_electronico, " \
          "codigo_seguro, numero_carnet_identidad, lugar_nacimiento, fecha_nacimiento, estado_civil, id_empleado) " \
          "VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    insert = (name1, name2, lastName1, lastName2, cellphone, eMail, codeSecure,
              numberCI, placeBirth, dateBirth, civilStatus, employerId)
    commit(connect, cursor, sql, insert)


def postulantInsert(name1, name2, lastName1, lastName2, cellphone, eMail,
                    numberCI, placeBirth, dateBirth, civilStatus, solicitedChargeId):
    connect = connection()
    cursor = connect.cursor()
    sql = "INSERT INTO postulante(nombre_1, nombre_2, apellido_1, apellido_2, telefono, correo_electronico, " \
          "numero_carnet_identidad, lugar_nacimiento, fecha_nacimiento, estado_civil, id_cargo_solicitado) " \
          "VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    insert = (name1, name2, lastName1, lastName2, cellphone, eMail,
              numberCI, placeBirth, dateBirth, civilStatus, solicitedChargeId)
    commit(connect, cursor, sql, insert)


def interviewInsert(observations, result, date, employerId, postulantId):
    connect = connection()
    cursor = connect.cursor()
    sql = "INSERT INTO entrevista(observaciones, resultado, fecha, id_empleado, id_postulante) " \
          "VALUES(%s, %s, %s, %s, %s)"
    insert = (observations, result, date, employerId, postulantId)
    commit(connect, cursor, sql, insert)


def salaryInsert(salary, contributionsAFPS, employerId):
    connect = connection()
    cursor = connect.cursor()
    sql = "INSERT INTO sueldo(sueldo, aportes_afps, id_empleado) " \
          "VALUES(%s, %s, %s)"
    insert = (salary, contributionsAFPS, employerId)
    commit(connect, cursor, sql, insert)


def gradesInsert(grade, chargePromoteId, result, employerId):
    connect = connection()
    cursor = connect.cursor()
    sql = "INSERT INTO calificaciones_examen(calificacion, id_cargo_promover, resultado, id_empleado) " \
          "VALUES(%s, %s, %s, %s)"
    insert = (grade, chargePromoteId, result, employerId)
    commit(connect, cursor, sql, insert)


def performanceInsert(performance, bonus):
    connect = connection()
    cursor = connect.cursor()
    sql = "INSERT INTO rendimiento(rendimiento, bono_bs) " \
          "VALUES(%s, %s)"
    insert = (performance, bonus)
    commit(connect, cursor, sql, insert)


def employerPerformanceInsert(employerId, performanceId, description):
    connect = connection()
    cursor = connect.cursor()
    sql = "INSERT INTO empleado_rendimiento(id_empleado, id_rendimiento, descripcion) " \
          "VALUES(%s, %s, %s)"
    insert = (employerId, performanceId, description)
    commit(connect, cursor, sql, insert)


def getCountTable(table):
    connect = connection()
    cursor = connect.cursor()
    sql = "SELECT count(*) FROM "+table
    cursor.execute(sql)
    count = cursor.fetchall()
    cursor.close()
    connect.close()
    return count[0][0]


def deleteAllTable(table):
    connect = connection()
    cursor = connect.cursor()
    sql = "DELETE FROM " + table
    cursor.execute(sql)
    cursor.close()
    connect.close()


def selectHumanResource():
    connect = connection()
    cursor = connect.cursor()
    sql = "SELECT id_empleado FROM empleado WHERE id_cargo = 13"
    cursor.execute(sql)
    employeesHumanResource = cursor.fetchall()
    cursor.close()
    connect.close()
    return employeesHumanResource
