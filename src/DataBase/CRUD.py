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