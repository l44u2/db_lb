from typing import List, Dict, Any
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.event_birthday import EventBirthday
import sqlalchemy

class EventBirthdayDAO(GeneralDAO):
    _domain_type = EventBirthday

    def get_birthdays_by_event(self, event_id: int) -> List[Dict[str, Any]]:
        result = self._session.execute(
            sqlalchemy.text("""
                SELECT b.* FROM birthday b
                JOIN event_birthday eb ON b.id = eb.birthday_id
                WHERE eb.event_id = :event_id
            """),
            {"event_id": event_id}
        ).mappings().all()
        return [dict(row) for row in result]