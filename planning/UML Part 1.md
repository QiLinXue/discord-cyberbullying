| BadWordsDB |
|---|
| +host : string <br/>+user : string <br/>+password : string <br/>+database : string <br/>+mydb : mysql.connector.connection_cext.CMySQLConnection <br/>+cursor : mysql.connector.cursor_cext.CMySQLCursor <br/> |
| +connect () : void <br/>+close () : void <br/>+escapeString(sqlString: string) : string <br/>+fetch () : string[] <br/>+printAll () : string <br/>+insert(targetWord: str, badWordArray: string[]) : void <br/>+insert(targetWord: str) : void <br/> |

| userDB |
|---|
| +host : string <br/>+user : string <br/>+password : string <br/>+database : string <br/>+mydb : mysql.connector.connection_cext.CMySQLConnection <br/>+cursor : mysql.connector.cursor_cext.CMySQLCursor <br/> |
| +connect () : void <br/>+close () : void <br/>+escapeString(sqlString: string) : string <br/>+insert(user: discord.member.Member) : void <br/>+fetch() : string[] <br/>+updateSwears(user: discord.member.Member) : void <br/>+updateRole(user: discord.member.Member, role: str) : void <br/> |