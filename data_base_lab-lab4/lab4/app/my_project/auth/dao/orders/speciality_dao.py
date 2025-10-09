from typing import List
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.speciality import Speciality
import sqlalchemy

class SpecialityDAO(GeneralDAO):
    _domain_type = Speciality