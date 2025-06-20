
CREATE TABLE IF NOT EXISTS Train (
	TrainNumber	INT,
	TrainName	VARCHAR(100),
	PremiumFair	DECIMAL(10, 2),
	GeneralFair	DECIMAL(10, 2),
	SourceStation	VARCHAR(100),
	DestinationStation	VARCHAR(100),
	PRIMARY KEY(TrainNumber)
);
CREATE TABLE IF NOT EXISTS TrainStatus (
	TrainDate	DATE,
	TrainName	VARCHAR(100),
	PremiumSeatsAvailable	INT,
	GenSeatsAvailable	INT,
	PremiumSeatsOccupied	INT,
	GenSeatsOccupied	INT,
	FOREIGN KEY(TrainName) REFERENCES Train(TrainName)
);
CREATE TABLE IF NOT EXISTS Passenger (
	first_Name	VARCHAR(50),
	last_Name	VARCHAR(50),
	address	TEXT,
	city	VARCHAR(100),
	county	VARCHAR(100),
	phone	VARCHAR(15),
	SSN	VARCHAR(11),
	bdate	DATE,
	PRIMARY KEY(SSN)
);
CREATE TABLE IF NOT EXISTS Booked (
	Passenger_SSN	VARCHAR(11),
	Train_Number	INT,
	Ticket_Type	VARCHAR(20),
	status	VARCHAR(20),
	FOREIGN KEY(Passenger_SSN) REFERENCES Passenger(SSN),
	FOREIGN KEY(Train_Number) REFERENCES Train(TrainNumber)
);
INSERT INTO Train VALUES (1,'Orient Express',800,600,' Paris',' Istanbul');
INSERT INTO Train VALUES (2,'Flying Scottsman',4000,3500,' Edinburgh',' London');
INSERT INTO Train VALUES (3,'Golden Arrow',980,860,' Victoria',' Dover');
INSERT INTO Train VALUES (4,'Golden Chariot',4300,3800,' Bangalore',' Goa');
INSERT INTO Train VALUES (5,'Maharaja Express',5980,4510,' Delhi',' Mumbai');
INSERT INTO TrainStatus VALUES ('2022-02-19','Orient Express',10,10,0,0);
INSERT INTO TrainStatus VALUES ('2022-02-20','Flying Scottsman',8,5,2,5);
INSERT INTO TrainStatus VALUES ('2022-02-21','Maharaja Express',7,6,3,4);
INSERT INTO TrainStatus VALUES ('2022-02-21','Golden Chariot',6,3,4,7);
INSERT INTO TrainStatus VALUES ('2022-02-22','Golden Arrow',8,7,2,3);
INSERT INTO TrainStatus VALUES ('2022-03-10','Golden Arrow',8,5,2,5);
INSERT INTO TrainStatus VALUES ('2022-02-21','Maharaja Express',7,6,3,4);
INSERT INTO TrainStatus VALUES ('2022-02-21','Flying Scottsman',5,5,5,5);
INSERT INTO Passenger VALUES ('James','Butt','6649 N Blue Gum St','New Orleans','Orleans','504-845-1427','264816896','1968-10-10');
INSERT INTO Passenger VALUES ('Josephine','Darakjy','4 B Blue Ridge Blvd','Brighton','Livingston','810-374-9840','240471168','1975-11-01');
INSERT INTO Passenger VALUES ('Art','Venere','8 W Cerritos Ave #54','Bridgeport','Gloucester','856-264-4130','285200976','1982-11-13');
INSERT INTO Passenger VALUES ('Lenna','Paprocki','639 Main St','Anchorage','Anchorage','907-921-2010','309323096','1978-08-09');
INSERT INTO Passenger VALUES ('Donette','Foller','34 Center St','Hamilton','Butler','513-549-4561','272610795','1990-06-11');
INSERT INTO Passenger VALUES ('Simona','Morasca','3 Mcauley Dr','Ashland','Ashland','419-800-6759','250951162','1994-08-15');
INSERT INTO Passenger VALUES ('Mitsue','Tollner','7 Eads St','Chicago','Cook','773-924-8565','272913578','1984-07-04');
INSERT INTO Passenger VALUES ('Leota','Dilliard','7 W Jackson Blvd','San Jose','Santa Clara','408-813-1105','268682534','1991-05-09');
INSERT INTO Passenger VALUES ('Sage','Wieser','5 Boston Ave #88','Sioux Falls','Minnehaha','605-794-4895','310908858','1982-02-25');
INSERT INTO Passenger VALUES ('Kris','Marrier','228 Runamuck Pl #2808','Baltimore','Baltimore City','410-804-4694','322273872','1956-04-04');
INSERT INTO Passenger VALUES ('Minna','Amigon','2371 Jerrold Ave','Kulpsville','Montgomery','215-422-8694','256558303','1995-09-09');
INSERT INTO Passenger VALUES ('Abel','Maclead','37275 St  Rt 17m M','Middle Island','Suffolk','631-677-3675','302548590','1960-11-05');
INSERT INTO Passenger VALUES ('Kiley','Caldarera','25 E 75th St #69','Los Angeles','Los Angeles','310-254-3084','284965676','1981-05-09');
INSERT INTO Passenger VALUES ('Graciela','Ruta','98 Connecticut Ave Nw','Chagrin Falls','Geauga','440-579-7763','277292710','1982-02-25');
INSERT INTO Passenger VALUES ('Cammy','Albares','56 E Morehead St','Laredo','Webb','956-841-7216','331160133','1956-04-04');
INSERT INTO Passenger VALUES ('Mattie','Poquette','73 State Road 434 E','Phoenix','Maricopa','602-953-6360','331293204','1995-09-09');
INSERT INTO Passenger VALUES ('Meaghan','Garufi','69734 E Carrillo St','Mc Minnville','Warren','931-235-7959','290123298','1960-11-02');
INSERT INTO Passenger VALUES ('Gladys','Rim','322 New Horizon Blvd','Milwaukee','Milwaukee','414-377-2880','286411536','1991-05-09');
INSERT INTO Passenger VALUES ('Yuki','Whobrey','1 State Route 27','Taylor','Wayne','313-341-4470','294860856','1985-02-25');
INSERT INTO Passenger VALUES ('Fletcher','Flosi','394 Manchester Blvd','Rockford','Winnebago','815-426-5657','317434088','1961-04-04');
INSERT INTO Booked VALUES ('264816896',3,'Premium','Booked');
INSERT INTO Booked VALUES ('240471168',2,'General','Booked');
INSERT INTO Booked VALUES ('285200976',4,'Premium','Booked');
INSERT INTO Booked VALUES ('285200976',2,'Premium','Booked');
INSERT INTO Booked VALUES ('317434088',2,'Premium','Booked');
INSERT INTO Booked VALUES ('310908858',2,'General','Booked');
INSERT INTO Booked VALUES ('322273872',2,'General','Booked');
INSERT INTO Booked VALUES ('256558303',3,'Premium','WaitL');
INSERT INTO Booked VALUES ('302548590',2,'General','WaitL');
INSERT INTO Booked VALUES ('284965676',3,'Premium','WaitL');
INSERT INTO Booked VALUES ('277292710',3,'General','WaitL');
INSERT INTO Booked VALUES ('331160133',3,'General','WaitL');
INSERT INTO Booked VALUES ('331293204',3,'General','WaitL');
INSERT INTO Booked VALUES ('290123298',3,'General','WaitL');
INSERT INTO Booked VALUES ('286411536',4,'Premium','Booked');
INSERT INTO Booked VALUES ('294860856',4,'Premium','Booked');
INSERT INTO Booked VALUES ('317434088',4,'Premium','Booked');
INSERT INTO Booked VALUES ('310908858',4,'Premium','Booked');
INSERT INTO Booked VALUES ('322273872',4,'Premium','Booked');
INSERT INTO Booked VALUES ('256558303',4,'Premium','Booked');
INSERT INTO Booked VALUES ('302548590',4,'Premium','Booked');
INSERT INTO Booked VALUES ('284965676',4,'General','Booked');
INSERT INTO Booked VALUES ('277292710',4,'General','Booked');
INSERT INTO Booked VALUES ('331160133',4,'General','Booked');
INSERT INTO Booked VALUES ('331293204',4,'General','Booked');
COMMIT;
