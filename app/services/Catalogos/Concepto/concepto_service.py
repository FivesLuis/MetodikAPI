from app.procedures.Catalogos.Conceptos.conceptos_procedures import (
    ver_Conceptos, act_Concepto, ver_ConceptoID)

def verConceptos(data):
    return ver_Conceptos(data)

def actConcepto(data):
    return act_Concepto(data)

def verConceptoID(ID):
    return ver_ConceptoID(ID)