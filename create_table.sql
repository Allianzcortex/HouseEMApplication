
use BEMApplication;

create table if not exists Building (
  id INT not null auto_increment,
  identify_number varchar(50) not null,
  address varchar(30),
  owner varchar(50),
  primary key(id)
) engine = innodb;


create table if not exists AllEMeterIndex(
  id varchar(50),
  primary key(id)
) engine = innodb;

insert into AllEMeterIndex (id) values(1);
insert into AllEMeterIndex (id) values(2);
insert into AllEMeterIndex (id) values(3);
insert into AllEMeterIndex (id) values(4);
insert into AllEMeterIndex (id) values(5);
insert into AllEMeterIndex (id) values(6);
insert into AllEMeterIndex (id) values(7);
insert into AllEMeterIndex (id) values(8);
insert into AllEMeterIndex (id) values(9);
insert into AllEMeterIndex (id) values(10);


-- add meter
create table if not exists EMeter (
  id INT not null auto_increment,
  EM_identify_number varchar(50) not null,
  EM_date DATE,
  EM_count varchar(50),
  EM_tot_max varchar(50),
  EM_tot_min varchar(50),
  primary key(id)
) engine = innodb;

-- add relationship
create table if not exists B_EM_Relationship (
  id INT not null auto_increment,
  building_identify_number varchar(50),
  EM_identify_number varchar(50),
  primary key(id)
) engine = innodb;

