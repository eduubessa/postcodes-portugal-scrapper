drop database if exists datadev;

create database if not exists datadev;

use datadev;

drop table if exists districts;
drop table if exists counties;
drop table if exists parishes;
drop table if exists postcodes;

create table districts (
    id bigint unsigned auto_increment primary key,
    district varchar(30) not null,
    counties int default 0,
    parish int default 0,
    scrapped tinyint default 0
);

create table counties (
    id bigint unsigned auto_increment primary key,
    district_id bigint unsigned not null,
    county varchar(50) not null,
    parish int default 0,
    scrapped tinyint default 0
);

create table parishes (
    id bigint unsigned auto_increment primary key,
    district_id bigint unsigned not null,
    county_id bigint unsigned not null,
    parish varchar(50) default 0,
    scrapped tinyint default 0
);

create table postcodes (
    id bigint unsigned auto_increment primary key,
    district_id bigint unsigned not null,
    county_id bigint unsigned not null,
    parish_id bigint unsigned not null,
    postcode varchar(50) not null,
    address varchar(100) not null,
    location varchar(150) not null,
    coords varchar(30) not null
);

truncate postcodes;

select * from districts;
select * from counties;
select * from parishes;
select * from postcodes;

select count(*) from postcodes;