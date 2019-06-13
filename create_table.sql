create table if not exists Building (
  id INT not null auto_increment,
  identify_number varchar(50) not null,
  address varchar(30),
  owner varchar(50),
  primary key(id)
) engine = innodb;

