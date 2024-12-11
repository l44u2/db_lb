USE lab4;

INSERT INTO `lab4`.`animator` (`name`, `surname`) VALUES 
('John', 'Doe'),
('Jane', 'Smith'),
('Paul', 'Jones'),
('Lisa', 'White'),
('Mark', 'Brown');

INSERT INTO `lab4`.`speciality` (`speicality_type`) VALUES 
('Clown'),
('Magician'),
('Juggler'),
('Singer'),
('Dancer');

INSERT INTO `lab4`.`agency` (`name`, `speciality_id`) VALUES 
('FunTime Events', 1),
('Magic Moments', 2),
('Joyful Occasions', 3),
('Happy Times', 4),
('Party People', 5);

INSERT INTO `lab4`.`location` (`house`, `street`) VALUES 
('123', 'Main St'),
('456', 'Elm St'),
('789', 'Oak St'),
('101', 'Pine St'),
('202', 'Maple St');

INSERT INTO `lab4`.`type` (`type`) VALUES 
('Wedding'),
('Birthday'),
('Kid Party'),
('First Bell'),
('Christmas');

INSERT INTO `lab4`.`event` (`animator_id`, `agency_id`, `location_id`, `type_id`) VALUES 
(1, 1, 1, 1),
(2, 2, 2, 2),
(3, 3, 3, 3),
(4, 4, 4, 4),
(5, 5, 5, 5);

INSERT INTO `lab4`.`wedding` (`event_date`, `duration`, `value`) VALUES 
('2024-12-31', '05:00:00', 1000),
('2025-01-01', '06:00:00', 1500),
('2024-10-10', '04:00:00', 1200),
('2025-02-20', '05:30:00', 1800),
('2024-08-15', '03:45:00', 1100);

INSERT INTO `lab4`.`event_wedding` (`event_id`, `wedding_id`) VALUES 
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5);

INSERT INTO `lab4`.`birthday` (`event_date`, `duration`, `value`) VALUES 
('2024-06-15', '04:00:00', 500),
('2024-07-20', '03:00:00', 600),
('2024-05-10', '04:30:00', 700),
('2024-09-25', '05:00:00', 800),
('2024-11-30', '02:45:00', 450);

INSERT INTO `lab4`.`event_birthday` (`event_id`, `birthday_id`) VALUES 
(2, 1),
(1, 2),
(3, 3),
(4, 4),
(5, 5);

INSERT INTO `lab4`.`kidparty` (`event_date`, `duration`, `value`) VALUES 
('2024-08-10', '02:00:00', 300),
('2024-09-25', '03:00:00', 400),
('2024-10-05', '02:30:00', 350),
('2024-11-15', '03:15:00', 450),
('2024-12-01', '02:45:00', 320);

INSERT INTO `lab4`.`event_kidparty` (`event_id`, `kidparty_id`) VALUES 
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5);

INSERT INTO `lab4`.`firstsep` (`event_date`, `duration`, `value`) VALUES 
('2024-09-01', '03:00:00', 450),
('2025-09-01', '04:00:00', 550),
('2024-09-02', '03:30:00', 500),
('2024-09-03', '04:15:00', 600),
('2025-09-04', '04:45:00', 650);

INSERT INTO `lab4`.`event_firstsep` (`event_id`, `firstsep_id`) VALUES 
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5);

INSERT INTO `lab4`.`christmass` (`event_date`, `duration`, `value`) VALUES 
('2024-12-25', '04:00:00', 600),
('2025-12-25', '05:00:00', 700),
('2024-12-26', '04:30:00', 650),
('2024-12-27', '05:30:00', 750),
('2025-12-28', '05:45:00', 800);

INSERT INTO `lab4`.`event_christmass` (`event_id`, `christmass_id`) VALUES 
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5);

INSERT INTO `lab4`.`newyear` (`event_date`, `duration`, `value`) VALUES 
('2024-12-31', '05:00:00', 800),
('2025-12-31', '06:00:00', 900),
('2024-12-30', '05:30:00', 850),
('2024-12-29', '06:15:00', 950),
('2025-12-28', '06:45:00', 1000);

INSERT INTO `lab4`.`event_newyear` (`event_id`, `newyear_id`) VALUES 
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5);

DROP PROCEDURE IF EXISTS get_events_after_animator;
DELIMITER //
CREATE PROCEDURE get_events_after_animator(IN animator_id INT)
BEGIN
    SELECT e.id AS event_id, t.type AS event_type, l.street, l.house
    FROM `event` e
    JOIN `type` t ON e.type_id = t.id
    JOIN `location` l ON e.location_id = l.id
    WHERE e.animator_id = animator_id;
END //
DELIMITER ;

DROP PROCEDURE IF EXISTS get_animator_after_event;
DELIMITER //
CREATE PROCEDURE get_animator_after_event(IN event_id INT)
BEGIN
    SELECT a.id AS animator_id, a.name, a.surname
    FROM `animator` a
    JOIN `event` e ON a.id = e.animator_id
    WHERE e.id = event_id;
END //
DELIMITER ;

DROP PROCEDURE IF EXISTS get_events_after_agency;
DELIMITER //
CREATE PROCEDURE get_events_after_agency(IN agency_id INT)
BEGIN
    SELECT e.id AS event_id, t.type AS event_type, l.street, l.house
    FROM `event` e
    JOIN `type` t ON e.type_id = t.id
    JOIN `location` l ON e.location_id = l.id
    WHERE e.agency_id = agency_id;
END //
DELIMITER ;

DROP PROCEDURE IF EXISTS get_agency_after_event;
DELIMITER //
CREATE PROCEDURE get_agency_after_event(IN event_id INT)
BEGIN
    SELECT ag.id AS agency_id, ag.name, s.speciality_type
    FROM `agency` ag
    JOIN `speciality` s ON ag.speciality_id = s.id
    JOIN `event` e ON ag.id = e.agency_id
    WHERE e.id = event_id;
END //
DELIMITER ;

DROP PROCEDURE IF EXISTS get_events_after_type;
DELIMITER //
CREATE PROCEDURE get_events_after_type(IN type_id INT)
BEGIN
    SELECT e.id AS event_id, a.name AS animator_name, a.surname AS animator_surname, l.street, l.house
    FROM `event` e
    JOIN `animator` a ON e.animator_id = a.id
    JOIN `location` l ON e.location_id = l.id
    WHERE e.type_id = type_id;
END //
DELIMITER ;

DROP PROCEDURE IF EXISTS get_type_after_event;
DELIMITER //
CREATE PROCEDURE get_type_after_event(IN event_id INT)
BEGIN
    SELECT t.id AS type_id, t.type AS event_type
    FROM `type` t
    JOIN `event` e ON t.id = e.type_id
    WHERE e.id = event_id;
END //
DELIMITER ;

DROP PROCEDURE IF EXISTS get_events_after_location;
DELIMITER //
CREATE PROCEDURE get_events_after_location(IN location_id INT)
BEGIN
    SELECT e.id AS event_id, t.type AS event_type, a.name AS animator_name, a.surname AS animator_surname
    FROM `event` e
    JOIN `type` t ON e.type_id = t.id
    JOIN `animator` a ON e.animator_id = a.id
    WHERE e.location_id = location_id;
END //
DELIMITER ;

DROP PROCEDURE IF EXISTS get_location_after_event;
DELIMITER //
CREATE PROCEDURE get_location_after_event(IN event_id INT)
BEGIN
    SELECT l.id AS location_id, l.street, l.house
    FROM `location` l
    JOIN `event` e ON l.id = e.location_id
    WHERE e.id = event_id;
END //
DELIMITER ;

DROP PROCEDURE IF EXISTS get_agencies_after_speciality;
DELIMITER //
CREATE PROCEDURE get_agencies_after_speciality(IN speciality_id INT)
BEGIN
    SELECT ag.id AS agency_id, ag.name
    FROM `agency` ag
    WHERE ag.speciality_id = speciality_id;
END //
DELIMITER ;

DROP PROCEDURE IF EXISTS get_speciality_after_agency;
DELIMITER //
CREATE PROCEDURE get_speciality_after_agency(IN agency_id INT)
BEGIN
    SELECT s.id AS speciality_id, s.speciality_type
    FROM `speciality` s
    JOIN `agency` ag ON s.id = ag.speciality_id
    WHERE ag.id = agency_id;
END //
DELIMITER ;

DROP PROCEDURE IF EXISTS get_events_by_date_range;
DELIMITER //
CREATE PROCEDURE get_events_by_date_range(IN start_date DATE, IN end_date DATE)
BEGIN
    SELECT e.id AS event_id, t.type AS event_type, e.animator_id, e.agency_id, l.street, l.house
    FROM `event` e
    JOIN `type` t ON e.type_id = t.id
    JOIN `location` l ON e.location_id = l.id
    WHERE e.id IN (
        SELECT event_id FROM `event_wedding` WHERE event_date BETWEEN start_date AND end_date
        UNION
        SELECT event_id FROM `event_birthday` WHERE event_date BETWEEN start_date AND end_date
        UNION
        SELECT event_id FROM `event_kidparty` WHERE event_date BETWEEN start_date AND end_date
        UNION
        SELECT event_id FROM `event_firstsep` WHERE event_date BETWEEN start_date AND end_date
        UNION
        SELECT event_id FROM `event_christmass` WHERE event_date BETWEEN start_date AND end_date
        UNION
        SELECT event_id FROM `event_newyear` WHERE event_date BETWEEN start_date AND end_date
    );
END //
DELIMITER ;

