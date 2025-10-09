# __init__.py
from .orders.animator_service import AnimatorService
from .orders.agency_service import AgencyService
from .orders.event_service import EventService
from .orders.location_service import LocationService
from .orders.speciality_service import SpecialityService
from .orders.event_type_service import TypeService
from .orders.wedding_service import WeddingService
from .orders.birthday_service import BirthdayService
from .orders.kidparty_service import KidpartyService
from .orders.firstsep_service import FirstsepService
from .orders.christmass_service import ChristmassService
from .orders.newyear_service import NewyearService
from .orders.event_wedding_service import EventWeddingService
from .orders.event_birthday_service import EventBirthdayService
from .orders.event_kidparty_service import EventKidpartyService
from .orders.event_firstsep_service import EventFirstsepService
from .orders.event_christmass_service import EventChristmassService
from .orders.event_newyear_service import EventNewyearService

animator_service = AnimatorService()
agency_service = AgencyService()
event_service = EventService()
location_service = LocationService()
speciality_service = SpecialityService()
type_service = TypeService()
wedding_service = WeddingService()
birthday_service = BirthdayService()
kidparty_service = KidpartyService()
firstsep_service = FirstsepService()
christmass_service = ChristmassService()
newyear_service = NewyearService()
event_wedding_service = EventWeddingService()
event_birthday_service = EventBirthdayService()
event_kidparty_service = EventKidpartyService()
event_firstsep_service = EventFirstsepService()
event_christmass_service = EventChristmassService()
event_newyear_service = EventNewyearService()