create table if not exists Building (
  id INT not null auto_increment,
  identify_number varchar(50) not null,
  address varchar(30),
  owner varchar(50),
  primary key(id)
) engine = innodb;

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

