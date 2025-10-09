from typing import List
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.location import Location
import sqlalchemy

class LocationDAO(GeneralDAO):
    _domain_type = Location