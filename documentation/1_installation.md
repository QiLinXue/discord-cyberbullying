# Installation

## Installation

### Cloning Repository
First, clone the repository and enter in it:

```
git clone https://github.com/QiLinXue/discord-cyberbullying.git
cd discord-cyberbullying
```

Python 3.6.x is required. Though it should run on other versions of python 3, I have not tested it.

Install requirements by typing either:

```py
pip install -r requirements.txt
or
pip3 install -r requirements.txt
```

In the folder, there should be a folder named `.env.example`. Rename this file to `.env` and replace the placeholders with your:
* bot id
* bot token
* mySQL server host
* mySQL server username
* mySQL server password
* mySQL server name

Ensure there are NO spaces in the `.env` file. The steps to acquire these variables are discussed in the next few sections.

### Creating a Discord Bot
1. Go to [https://discordapp.com/developers/applications/](https://discordapp.com/developers/applications/)
2. Click `Create an application` and enter a name. Then click `Create`
3. Copy the client id into the `.env` file
4. On the `Settings` panel at the left side, click `Bot`
5. Click on `Add a Bot` and confirm.
6. Click on `Click to reveal Token`, then copy the token into the `.env` file.

### Setting up a server

Any mySQL server should work. Mine was on the cloud so I used [ClearDB MySQL] (https://w2.cleardb.net). If you have heroku, they have an [addon](https://elements.heroku.com/addons/cleardb) as well.

If you're name is Mr. Seidel, you can use the host/username/password/database details I emailed to you if you wish to save some time.

## Running the bot

### Creating a server
To run the bot, first you'll need a discord server. Feel free to use any discord server that you are already an admin of, as long as the channels `administrator` and `reporting` don't exist, and the role `Seidelion` does not exist.

To create a new server, follow the [discord guide here](https://support.discordapp.com/hc/en-us/articles/204849977-How-do-I-create-a-server-)

### Inviting the Bot
To invite your discord bot, use the url 
```
https://discordapp.com/oauth2/authorize?client_id=YOUR_CLIENT_ID&scope=bot&permissions=8
```
where you replace `YOUR_CLIENT_ID` with your bot's client id. Then, authorize the bot to the server you'll be testing on.

### Running the Script
In terminal, under the project directory, type:
```
python main.py
```
You should see `Starting up...` Wait a few moments (depending on connection) and you will see `Bot is online`

### Initializing the Server
Go to the server you created, and type in
```
!setup
```
Wait as the bot sets it up for you.
