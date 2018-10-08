use heroku_5e695080c7ef107;

drop table if exists badwords;

create table if not exists badwords (
    word    text not null,
    badness int  not null
);