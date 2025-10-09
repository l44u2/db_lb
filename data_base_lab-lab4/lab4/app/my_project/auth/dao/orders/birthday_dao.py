from typing import List, Dict, Any
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.birthday import Birthday
import sqlalchemy

class BirthdayDAO(GeneralDAO):
    _domain_type = Birthday