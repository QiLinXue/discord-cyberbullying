use heroku_5e695080c7ef107;

drop table if exists badwords;
drop table if exists userList;

create table if not exists badwords (
    word    text not null,
    badness int  not null
);

create table if not exists userList (
    userID      text not null,
    username    text not null
);

INSERT INTO badwords (word, badness) VALUE ("fuck",1);
-- INSERT INTO userList (userID, username) VALUE ("fuck","asd");
-- INSERT INTO userList (userID, username) VALUE ("fuck","asd");
-- UPDATE userList SET userID = "asdf" WHERE userID = "fuck";