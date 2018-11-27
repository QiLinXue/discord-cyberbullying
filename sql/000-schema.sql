use heroku_5e695080c7ef107;

drop table if exists badwords;
drop table if exists userList;

create table if not exists badwords (
    word    text not null,
    badness int  not null
);

create table if not exists userList (
    userID      text not null,
    username    text not null,
    swearCount      int  not null
);

-- INSERT INTO badwords (word, badness) VALUE ("fuck",1);
-- INSERT INTO userList (userID, username, swearCount) VALUE ("fuck","asd",3);

-- INSERT INTO userList (userID, username) VALUE ("fuck","asd");
-- UPDATE userList SET swearCount = swearCount + 1 WHERE userID = "fuck";