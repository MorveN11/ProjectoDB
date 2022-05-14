from src.Utils import Numbers
from src.Lib import BornPlace, CivilStatus, Dates, Email, EmploymentStatus, Names, Results, Observations, Zones
from src.DataBase import PostgresDB
import random


def insertClients(rang):
    for i in range(rang):
        PostgresDB.clientInsert(Names.names1[random.randint(0, len(Names.names1) - 1)],
                                Names.names2[random.randint(0, len(Names.names2) - 1)],
                                Names.lastNames1[random.randint(0, len(Names.lastNames1) - 1)],
                                Names.lastNames2[random.randint(0, len(Names.lastNames2) - 1)],
                                Numbers.generateNumCell(),
                                Numbers.generateRandomNit())
        PostgresDB.livePlaceInsert(Numbers.generateNumViv(), Zones.generateZones(), random.randint(1, 4),
                                   PostgresDB.getCountTable("cliente"))


def generatePostulants(rang, chargeId):
    for i in range(rang):
        name = Names.names1[random.randint(0, len(Names.names1) - 1)]
        PostgresDB.postulantInsert(name,
                                   Names.names2[random.randint(0, len(Names.names2) - 1)],
                                   Names.lastNames1[random.randint(0, len(Names.lastNames1) - 1)],
                                   Names.lastNames2[random.randint(0, len(Names.lastNames2) - 1)],
                                   Numbers.generateNumCell(),
                                   Email.generate(name),
                                   Numbers.generateCI(),
                                   BornPlace.generate(),
                                   Dates.dates(),
                                   CivilStatus.generate(),
                                   chargeId)


def insertSupplier(rang):
    for i in range(rang):
        PostgresDB.supplierInsert(Names.names1[random.randint(0, len(Names.names1) - 1)],
                                  Names.names2[random.randint(0, len(Names.names2) - 1)],
                                  Names.lastNames1[random.randint(0, len(Names.lastNames1) - 1)],
                                  Names.lastNames2[random.randint(0, len(Names.lastNames2) - 1)],
                                  Numbers.generateNumCell())


def insertEmployee(rang, cargo):
    for i in range(rang):
        PostgresDB.employeeInsert(random.randint(0, 30),
                                  EmploymentStatus.generate(),
                                  random.randint(1, 3000),
                                  cargo)
        name = Names.names1[random.randint(0, len(Names.names1) - 1)]
        PostgresDB.dataEmployeeInsert(name,
                                      Names.names2[random.randint(0, len(Names.names2) - 1)],
                                      Names.lastNames1[random.randint(0, len(Names.lastNames1) - 1)],
                                      Names.lastNames2[random.randint(0, len(Names.lastNames2) - 1)],
                                      Numbers.generateNumCell(),
                                      Email.generate(name),
                                      Numbers.generateCSE(),
                                      Numbers.generateCI(),
                                      BornPlace.generate(),
                                      Dates.dates(),
                                      CivilStatus.generate(),
                                      PostgresDB.getCountTable("empleado"))


def insertPerformance(rang):
    for i in range(rang):
        PostgresDB.performanceInsert(i + 1,
                                     (i + 1) * 50)


def insertService(service, utility, buyUnit, costCUnit, amount):
    insertSupplier(1)
    PostgresDB.purchaseUnitInsert(buyUnit, costCUnit, PostgresDB.getCountTable("proveedor"))
    cost = amount * costCUnit
    buyUnitId = PostgresDB.getCountTable("unidad_compra")
    PostgresDB.importInsert(cost, amount, buyUnitId)
    costSale = costCUnit + ((costCUnit * utility) / 100)
    PostgresDB.serviceInsert(service, utility, costSale, buyUnitId)


def insertPostulants(rang):
    for i in range(rang):
        cargos = [1, 4, 6, 10, 11, 13, 18, 17]
        charge = cargos[random.randint(0, len(cargos) - 1)]

        name1 = Names.names1[random.randint(0, len(Names.names1) - 1)]
        name2 = Names.names2[random.randint(0, len(Names.names2) - 1)]
        lastName1 = Names.lastNames1[random.randint(0, len(Names.lastNames1) - 1)],
        lastName2 = Names.lastNames2[random.randint(0, len(Names.lastNames2) - 1)],
        cellphone = Numbers.generateNumCell()
        email = Email.generate(name1)
        ci = Numbers.generateCI(),
        bornPlace = BornPlace.generate(),
        birthDay = Dates.dates()
        civilStatus = CivilStatus.generate()

        PostgresDB.postulantInsert(name1, name2, lastName1, lastName2, cellphone, email, ci, bornPlace,
                                   birthDay, civilStatus, charge)

        employeesHHRR = PostgresDB.getCountTable("empleado WHERE id_cargo = 13")
        availableEmployee = PostgresDB.selectHumanResource()[random.randint(0, (employeesHHRR - 1))][0]
        result = Results.worGenerate()
        observation = ""
        if result == "aceptado":
            observation = Observations.aceptGenerate()
        elif result == "rechazado":
            observation = Observations.rechGenerate()

        PostgresDB.interviewInsert(observation, result, Dates.contractDate(), availableEmployee,
                                   PostgresDB.getCountTable("postulante"))
        if result == "aceptado":
            PostgresDB.employeeInsert(random.randint(0, 30),
                                      EmploymentStatus.generate(),
                                      random.randint(1, 3000),
                                      charge)
            PostgresDB.dataEmployeeInsert(name1, name2, lastName1, lastName2, cellphone, email, Numbers.generateCSE(),
                                          ci, bornPlace, birthDay, civilStatus, PostgresDB.getCountTable("empleado"))


def insertZone(rang):
    for i in range(rang):
        zone1 = Zones.zones[i]
        extention1 = Zones.extentions[i]
        antiquity1 = random.randint(0, 70)
        PostgresDB.zoneInsert(zone1, extention1, antiquity1)


def insertHomeType(rang):
    for i in range(rang):
        homeTypeList = ["D", "I", "C", "E"]
        home_type = homeTypeList[i]
        diferentiator = (i + 1) * 50
        PostgresDB.typeLiveInsert(home_type, diferentiator)


def insertDepts():
    PostgresDB.departamentInsert("Contabilidad", "Realiza debe y haber")
    PostgresDB.departamentInsert("Recursos Humanos", "Control del personal")
    PostgresDB.departamentInsert("Atencion al cliente", "Relacion con el cliente")
    PostgresDB.departamentInsert("Limpieza", "Mantener limpio los establecimientos")
    PostgresDB.departamentInsert("Seguridad", "Mantener seguro los establecimientos")
    PostgresDB.departamentInsert("Direccion General", "Dirigir y manejar la empresa")


def insertCharges():
    PostgresDB.chargeInsert("Contador", 2100, 1)
    PostgresDB.chargeInsert("Gerente General", 40000, 6)
    PostgresDB.chargeInsert("Subgerente", 20000, 6)
    PostgresDB.chargeInsert("Mantenimiento", 2500, 4)
    PostgresDB.chargeInsert("Jefe", 3000, 5)
    PostgresDB.chargeInsert("Cuidante", 2500, 5)
    PostgresDB.chargeInsert("Sereno", 1800, 5)
    PostgresDB.chargeInsert("Portero", 1800, 5)
    PostgresDB.chargeInsert("Encargado", 10000, 6)
    PostgresDB.chargeInsert("Secretario", 2000, 1)
    PostgresDB.chargeInsert("Asistente", 5000, 1)
    PostgresDB.chargeInsert("Jefe", 10000, 2)
    PostgresDB.chargeInsert("Asistente", 5000, 2)
    PostgresDB.chargeInsert("Analista", 7000, 2)
    PostgresDB.chargeInsert("Asistente", 5000, 3)
    PostgresDB.chargeInsert("Supervisor de Operaciones", 4500, 3)
    PostgresDB.chargeInsert("Servicio al cliente", 3000, 3)
    PostgresDB.chargeInsert("Cajero", 2200, 3)


def insertTotalEmployes():
    insertEmployee(5, 1)
    insertEmployee(1, 2)
    insertEmployee(2, 3)
    insertEmployee(10, 4)
    insertEmployee(1, 5)
    insertEmployee(3, 6)
    insertEmployee(3, 7)
    insertEmployee(2, 8)
    insertEmployee(1, 9)
    insertEmployee(3, 10)
    insertEmployee(5, 11)
    insertEmployee(1, 12)
    insertEmployee(3, 13)
    insertEmployee(5, 14)
    insertEmployee(5, 15)
    insertEmployee(2, 16)
    insertEmployee(4, 17)
    insertEmployee(6, 18)


def insertTotalServicios():
    insertService("Agua", 20.4, "L", 5, 40000)
    insertService("Luz", 42.7, "W", 8, 200000)
    insertService("Gas", 38.5, "Cm3", 10, 300000)


def insertSalary():
    for i in range(PostgresDB.getCountTable("empleado")):
        PostgresDB.salaryInsert(random.randint(2000, 6000), random.randint(325, 500), (i+1))


def insertGrades():
    for i in range(PostgresDB.getCountTable("empleado")):
        grade = random.randint(0, 100)
        if grade > 51:
            PostgresDB.gradesInsert(grade, random.randint(1, 18), "Aceptado", (i+1))
        elif grade <= 51:
            PostgresDB.gradesInsert(grade, random.randint(1, 18), "Rechazado", (i+1))


def insertClientService():
    for i in range(PostgresDB.getCountTable("cliente")):
        for j in range(random.randint(1, 3)):
            PostgresDB.clientServiceInsert((i+1), (j+1), random.randint(1, 9999999))


def insertEmployeePerformance():
    for i in range(PostgresDB.getCountTable("empleado")):
        PostgresDB.employerPerformanceInsert((i+1), random.randint(1, 10), Observations.aceptGenerate())


def insertClientEmployer():
    for i in range(PostgresDB.getCountTable("cliente")):
        for j in range(random.randint(1, 5)):
            PostgresDB.clientEmployerInsert((i+1), (j+1), random.randint(100, 3000), random.randint(1, 5),
                                            random.randint(200, 500), Dates.contractDate(),
                                            "Paga tus facturas a tiempo")
