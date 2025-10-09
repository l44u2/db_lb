from typing import List
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.event import Event
import sqlalchemy

class EventDAO(GeneralDAO):
    _domain_type = Event

    def get_events_by_date_range(self, start_date: str, end_date: str) -> List[Event]:
        result = self._session.execute(
            sqlalchemy.text("""
                SELECT * FROM event 
                WHERE event_date BETWEEN :start_date AND :end_date
            """),
            {"start_date": start_date, "end_date": end_date}
        ).mappings().all()
        return [self._domain_type(**row) for row in result]

    def get_animator_after_event(self, event_id: int) -> List[Event]:
        result = self._session.execute(
            sqlalchemy.text("""
                SELECT * FROM event 
                WHERE id = :event_id
            """),
            {"event_id": event_id}
        ).mappings().all()
        return [self._domain_type(**row) for row in result]

    def get_agency_after_event(self, event_id: int) -> List[Event]:
        result = self._session.execute(
            sqlalchemy.text("""
                SELECT * FROM event 
                WHERE id = :event_id
            """),
            {"event_id": event_id}
        ).mappings().all()
        return [self._domain_type(**row) for row in result]

    def get_events_by_animator(self, animator_id: int) -> List[Event]:
        result = self._session.execute(
            sqlalchemy.text("""
                SELECT * FROM event 
                WHERE animator_id = :animator_id
            """),
            {"animator_id": animator_id}
        ).mappings().all()
        return [self._domain_type(**row) for row in result]

    def get_events_by_agency(self, agency_id: int) -> List[Event]:
        result = self._session.execute(
            sqlalchemy.text("""
                SELECT * FROM event 
                WHERE agency_id = :agency_id
            """),
            {"agency_id": agency_id}
        ).mappings().all()
        return [self._domain_type(**row) for row in result]

    def get_events_by_location(self, location_id: int) -> List[Event]:
        result = self._session.execute(
            sqlalchemy.text("""
                SELECT * FROM event 
                WHERE location_id = :location_id
            """),
            {"location_id": location_id}
        ).mappings().all()
        return [self._domain_type(**row) for row in result]

    def get_events_by_type(self, type_id: int) -> List[Event]:
        result = self._session.execute(
            sqlalchemy.text("""
                SELECT * FROM event 
                WHERE type_id = :type_id
            """),
            {"type_id": type_id}
        ).mappings().all()
        return [self._domain_type(**row) for row in result]