create table `registered_person`(
ID bigint(10)  auto_increment primary key,
lastname varchar(20) not null,
firstname varchar(20) not null,
middlename varchar(20),
suffixname varchar(10),
age varchar(20) not null,
gender varchar(20) not null,
house_street varchar(20) not null,
barangay varchar(20) not null,
town_city varchar(20) not null,
province varchar(20) not null,
contactnum varchar(11)  not null,
email varchar(20) unique not null);

create table `registered_est`(
ID bigint(10)  auto_increment primary key,
estname varchar(20) not null,
estowner varchar(20) not null,
house_street varchar(20) not null,
barangay varchar(20) not null,
town_city varchar(20) not null,
province varchar(20) not null,
contactnum varchar(11) unique not null,
email varchar(20) unique not null);


# kasi dito makukuha na natin lahat mga data gamit ang mga foreign key

create table `Logs`(
ID bigint(6) auto_increment primary key,
`date` date not null,
`time` time not null,
registered_personID bigint(20) not null,
ID_from_est1 bigint(20) not null,
foreign key (registered_personId) references registered_person(ID),
foreign key (ID_from_est1) references registered_est(ID)
); 

# dito mapupunta data ng establishment

