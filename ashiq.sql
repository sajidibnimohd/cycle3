CREATE TABLE STATION
(
"STATION_ID" VARCHAR2(50),
"S_NAME" VARCHAR2(50),
"S_CITY" VARCHAR2(50),
"S_COUNTRY" VARCHAR2(50),
PRIMARY KEY("STATION_ID")
);
drop table usertable;
create or replace procedure add_user(
userid VARCHAR2,
username varchar2,
phone varchar2,
usercity varchar2,
userdob varchar2)
is 
begin
 insert into usertable values(userid, username,phone, usercity, userdob);
end;
/
select * from usertable;
CREATE TABLE usertable
(
"user_ID" VARCHAR2(50),
"user_NAME" VARCHAR2(50),
"phone" varchar2(50),
"user_CITY" VARCHAR2(50),
"user_dob" VARCHAR2(50),
PRIMARY KEY("user_ID")
);
SELECT * FROM STATION;
INSERT INTO STATION VALUES('1001','KAKAPORA','KASHMIR','INDIA');

CREATE TABLE TRAIN
(
"TRAIN_NO" VARCHAR2(50),
"NO_OF_SEATS" VARCHAR2(50),
"PAYMENT_ID" VARCHAR2(50),
"DEP_STATION" VARCHAR2(50),
"ARR_STATION" VARCHAR2(50),
"DEP_DAT" VARCHAR2(50),
"ARR_DAT" VARCHAR2(50),
"NO_OF_STOPS" VARCHAR2(50)
"T_NAME" VARCHAR2(50),
PRIMARY KEY("SEAT_NO")
);


/
select * from user;
/
drop table payment;
CREATE TABLE PAYMENT
(
"PRICE" VARCHAR2(50),
"USER_ID" VARCHAR2(50),
"BOOKING_DATE" VARCHAR2(50),
"arrival" varchar2(50),
"departure" varchar2(50),
PRIMARY KEY("USER_ID")
);
create or replace procedure payfees(
price varchar2,
userid varchar2,
bdate varchar2,
arri varchar2,
depart varchar2)
is
begin
    insert into payment values(price,userid, bdate, arri,depart);
end;
/
select * from employee1;
select * from payment;
CREATE TABLE EMPLOYEE1
(
"E_ID" VARCHAR2(50),
"e_name" varchar2(25),
"EMAIL_ID" VARCHAR2(50),
"E_PROFN" VARCHAR2(50),
e_salary varchar2(25),
e_address varchar2(25),
"PHONE_NO" VARCHAR2(50),
PRIMARY KEY("E_ID")
);
select * from employee1;
execute add_employee('1000','Sajid','sajid@gmail.com','TC','80000','Kashmir','9898989898');
create or replace procedure add_employee(
eid varchar2,
e_name varchar2,
emailid varchar2,
prof varchar2,
sal varchar2,
address varchar2,
phone_no varchar2
)
is 
begin
    insert into  employee1 values(eid, e_name, emailid,prof,sal,address,phone_no);
end;
/
create or replace procedure del_employee(
emp_id varchar2,
phoneno varchar2)
is 
begin
delete from employee1 where e_id = emp_id and phone_no = phoneno;
end;
/
select * from employee1;
delete from employee1 where e_id = '1000' and phone_no = '9898989898';
execute del_employee('1000','989898988');
insert into employee1 values('108','adil','adil@gmail.com','TC','10000','pulwama','6609345213')
create table train_details(train_name char(15) primary key,
total_seats number(3),
reserved_seats number(3));

create table waiting_lists(slno number(3),
customer_name char(15) primary key,
train_name char(15) references train_details(train_name));

create table reservation_status(train_name char(15) references train_details(train_name),
seat_id number(3),
reserved char(2) check (reserved in('y','n')),
customer_name char(15));
 

 
SQL> declare
  2 
  2  tname char(15);
  3  tot number(3);
  4  resv number(3);
  5  cursor cur is select * from train_details;
  6 
  6  begin
  7 
  7  insert into train_details values('&train_name',&total_seats,0);
  8 
  8  open cur;
  9  loop
 10  fetch cur into tname,tot,resv;
 11  if cur%found then
 12  for i in 1..tot
 13  loop
 14  insert into reservation_status values(tname,i,'n',null);
 15  end loop;
 16  else
 17  exit;
 18  end if;
 19  end loop;
 20  commit;
 21  close cur;
 22  end;
 23  /
Enter value for train_name: AA
Enter value for total_seats: 3
old   7: insert into train_details values('&train_name',&total_seats,0);
new   7: insert into train_details values('AA',3,0);
 
CREATE OR REPLACE PROCEDURE new_station(station_id in varchar2, s_name in varchar2, s_city in varchar2, s_country in varchar2)
IS
BEGIN
  INSERT INTO station
  VALUES (station_id,s_name,s_city,s_country);
END;
/
select * from station;
desc station;
create or replace procedure add_station 
(station_id in station.station_id%type,
s_name in station.station_name%type,
s_city in station.station_city%type,
s_country in station.station_country%type)
IS
BEGIN
insert into station values(station_id,s_city,s_country);
dbms_output.put_line('station added');

end;

begin
add_station('1006','pondy','PN','India');
end;

select * from station where station_id=1006;

create or replace procedure add_station
(station_id in station.station_id%type,
station_name in station.S_NAME%type,
station_city in station.S_CITY%type,
station_country in station.S_COUNTRY%type)
IS
BEGIN
insert into station values(station_id,station_name, station_city,station_country);
dbms_output.put_line('station added');

end;/

begin
add_station('1009','pondyexpress','pondy','india');
end;
/
create table usertable (
userid varchar2 primary key,
username varchar2,
address varchar2,
dob varchar2,
phoneno number
);

create or replace procedure add_employee1
(e_id employee1.E_ID%type,
e_name employee1.e_name%type,
email_id employee1.EMAIL_ID%type,
e_profn employee1.E_PROFN%type,
e_salary employee1.E_salary%type,
e_address employee1.E_address%type,
e_phone_no employee1.E_no%type)
IS
BEGIN
insert into employee1 values(e_id,e_name,email_id,e_profn,e_salary,e_address,e_phone_no);
dbms_output.put_line('employee1 added');
end;/
begin
add_employee('108','adil','adil@gmail.com','TC','10000,'pulwama','6609345213');
end;


CREATE OR REPLACE TRIGGER EMP_INSERT
AFTER INSERT ON EMPLOYEE1
BEGIN
DBMS_OUTPUT.PUT_LINE('RECORD INSERTED.');
END;
INSERT INTO EMPLOYEE1 VALUES('112','JOHN','JOHN@GMAIL.COM','INCHARGE','20000','JAMMU','7788901239');

CREATE OR REPLACE TRIGGER RESTRICTED_INSERT
BEFORE INSERT ON EMPLOYEE1
BEGIN
   IF(TO_CHAR(SYSDATE,'HH24:MI')NOT BETWEEN '9.00'AND'18.00')THEN
       RAISE_APPLICATION_ERROR(-20123'YOU CAN ADD EMPLOYEE ONLY BETWEEN 9:00 AM AND 6:00 PM.')
END IF;

END;
/
