# Anti Cyberbullying Bot
[![Build Status](https://travis-ci.com/QiLinXue/discord-cyberbullying.svg?branch=master)](https://travis-ci.com/QiLinXue/discord-cyberbullying)
[![CodeFactor](https://www.codefactor.io/repository/github/qilinxue/discord-cyberbullying/badge)](https://www.codefactor.io/repository/github/qilinxue/discord-cyberbullying)
[![Waffle.io - Columns and their card count](https://badge.waffle.io/QiLinXue/discord-cyberbullying.svg?columns=all)](https://waffle.io/QiLinXue/discord-cyberbullying)

**Python discord bot** that aims to use machine learning to detect and remove cyberbullying messages such as hate speech. I aim to implement natural language processing (NLP) so it doesn't just loop through a list of banned words, but actually tries to understand it.

*Will* be documented eventually. Currently a work in progress.

## Installation

Python 3.6.x is required. Though it should run on other versions of python 3, I have not tested it.

First, clone the repository and enter in it:

```
git clone https://github.com/QiLinXue/discord-cyberbullying.git
cd discord-cyberbullying
```

Then, install requirements:

```
pip install -r requirements.txt
```

In the folder, there should be a folder named `.env.example`. Rename this file to `.env` and replace the placeholders with your private bot token, and database username and password. Any mySQL database should work, and a bot can be created at https://discordapp.com/developers/applications/. Under settings, click Bot. Then click "Build a Bot". Then click "Click to Reveal Token". DO NOT share this token with anyone.

Ensure there are NO spaces in the `.env` file. Before running, make sure to invite the bot into your server first.

To run, type:

```
python main.py
```
