from typing import List
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.animator import Animator
import sqlalchemy

class AnimatorDAO(GeneralDAO):
    _domain_type = Animator

    def __init__(self):
        super().__init__()