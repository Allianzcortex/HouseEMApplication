# HouseEMApplication
An application that can attach house and EM(Electricity Meter)

#### How to Run It ?

- execute the command `flask app.py run`

- open the file `templates/index.html`

#### TODO

- remove hard-coded variables

- add more explanations for MySQL and [create_table.sql](create_table.sql)

---

There are many ways to implement the 1-to-many relationship between building and em. I choose to only show the people available
ems(i.e. if an em is attached with a building , then it won't show in the drop-down menu)
 
Mainly there can be some misunderstandings, for example, if a building is attached with a meter which never has the metrics, should we regard it as null value or just discard it? I choose to represent all of them as the null value so users can know there is a link between two of them.

For deploy: I put the project into a DigitalOcean server. The front-end is served by `Nginx`, the backed is simply configured by `nohup`

---

And one more design thinking is :
The Electricity Meters can only be chosen but cannot be typed, so there is a table specifically designed for storing all available EMs.

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

Only Manager can add new Electricity Meters from MySQL Database, and users can only choose existed items from the drop-down menu.

 open the developer tool, there will be network request/response.

