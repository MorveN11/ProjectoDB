from src.Utils import Utility

chargesl = "Gerente_General,Sub_Gerente,Encargados,Supervisor,Analista,Asesor,Asistente,Supervisor_Operaciones," \
          "Servicio_Cliente,Cajeros,Secretaria"
charges = Utility.joinNames(chargesl)
accountingDeptl = "Encargado_Contabilidad,Asistente_Contabilidad"
accountingDept = Utility.joinNames(accountingDeptl)
humanResourcesDeptl = "Encargados_Recursos_humano,Asistente_Recursos_Humanos"
humanResourcesDept = Utility.joinNames(humanResourcesDeptl)
clientAttentionDeptl = "Encargados_Atencion_Cliente,Asistente_Atencion_Cliente," \
                      "Supervisor_Operaciones_Atencion_cliente,Servicio_Cliente,Cajeros"
clientAttentionDept = Utility.joinNames(clientAttentionDeptl)


def __init__(self):
    self.charges = charges
    self.accountingDept = accountingDept
    self.humanResourcesDept = humanResourcesDept
    self.clientAttentionDept = clientAttentionDept
