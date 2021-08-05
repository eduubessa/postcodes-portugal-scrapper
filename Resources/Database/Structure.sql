drop database if exists datadev;

create database if not exists datadev;

use datadev;

drop table if exists postcodes;
drop table if exists districts;
drop table if exists counties;

create table postcodes (
    id bigint unsigned auto_increment primary key,
    postcode varchar(10) not null,
    district varchar(30) not null,
    county varchar(50) not null,
    parish varchar(200) not null,
    longitude varchar(200) null,
    latitude varchar(200) null
);

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

create table counties (
    id bigint unsigned auto_increment primary key,
    district_id bigint unsigned not null,
    county_id bigint unsigned not null,
    parish int default 0,
    scrapped tinyint default 0
);

select * from districts;
select * from counties;