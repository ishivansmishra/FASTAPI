from pydantic import BaseModel, EmailStr
from typing import List, Dict, Optional
class Patient(BaseModel):
    name:str
    email: EmailStr
    age :int
    weight : float
    married : bool = False
    allergies : Optional[List[str]] = None
    contact_details: Dict[str,str]

def insert_patient_name(patient : Patient):
    print(patient.name)
    print(patient.email)
    print(patient.age)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print('inserted')

Patient_info = {
    'name':'shivansh',
    'email':'123@email.com',
    'age':22,
    'weight': 50.2,
    'contact_details': { 'phone':'12345'}
    }

patient1 = Patient(**Patient_info)

insert_patient_name(patient1)