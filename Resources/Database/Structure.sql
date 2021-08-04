create database if not exists datadev;

create table postcodes (
    id bigint unsigned auto_increment primary key,
    district varchar(30) null,
    county varchar(50) null,
    parish varchar(200) null,
    longitude varchar(200) null,
    latitude varchar(200) null
);

create table districts (
    id bigint unsigned auto_increment primary key,
    district varchar(30) unique not null,
    scrapped tinyint default 0
)