create database if not exists cyberbullying;
use cyberbullying;

drop table if exists badwords;

create table if not exists badwords (
    word    text not null,
    badness int  not null
);