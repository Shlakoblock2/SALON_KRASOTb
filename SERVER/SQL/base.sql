create table Users(
	id integer PRIMARY KEY autoincrement,
	login varchar(16) not null unique,
	password varchar(16) not null,
	power_level integer
);

create table Service(
	id integer primary key autoincrement,
	name varchar (250)
);

create table Applications(
	id integer primary key autoincrement,
	add_date Date,
	UserID integer,
	serviceID integer,
	comments varchar (250),
	date_completion date,
	foreign key(UserID) references Users(id),
	foreign key(serviceID) references service(id)
);