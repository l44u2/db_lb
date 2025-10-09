from flask import Flask
from .error_handler import err_handler_bp

def register_routes(app: Flask) -> None:
    app.register_blueprint(err_handler_bp)
    from .orders.animator_route import animator_bp
    from .orders.event_route import event_bp 
    from .orders.event_wedding_route import event_wedding_bp
    from .orders.wedding_route import wedding_bp
    from .orders.birthday_route import birthday_bp
    from .orders.christmass_route import christmass_bp
    from .orders.firstsep_route import firstsep_bp
    from .orders.kidparty_route import kidparty_bp
    from .orders.newyear_route import newyear_bp
    from .orders.agency_route import agency_bp
    from .orders.location_route import location_bp
    from .orders.event_firstsep_route import event_firstsep_bp
    from .orders.event_birthday_route import event_birthday_bp
    from .orders.event_kidparty_route import event_kidparty_bp
    from .orders.event_christmass_route import event_christmass_bp
    from .orders.event_newyear_route import event_newyear_bp
    from .orders.speciality_route import speciality_bp
    from .orders.event_type_route import event_type_bp

    app.register_blueprint(animator_bp)
    app.register_blueprint(event_bp)
    app.register_blueprint(event_wedding_bp)  
    app.register_blueprint(wedding_bp)
    app.register_blueprint(birthday_bp)
    app.register_blueprint(christmass_bp)
    app.register_blueprint(firstsep_bp)
    app.register_blueprint(kidparty_bp)
    app.register_blueprint(newyear_bp)
    app.register_blueprint(agency_bp)
    app.register_blueprint(location_bp)
    app.register_blueprint(event_firstsep_bp)
    app.register_blueprint(event_birthday_bp)
    app.register_blueprint(event_kidparty_bp)
    app.register_blueprint(event_christmass_bp)
    app.register_blueprint(event_newyear_bp)
    app.register_blueprint(speciality_bp)
    app.register_blueprint(event_type_bp)