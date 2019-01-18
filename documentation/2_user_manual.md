# User Manual
## Main Functionality
When a user types a message that is deemed offensive, the bot will pick up on it and report it in the `reporting` channel, where the vital informations are relayed to the `administration` channel. Furthermore, users with the role `Seidelion` are also able to manually report a message by using the id ([developer mode](https://discordia.me/developer-mode) must be enabled to access the id).

In the administration channel, Seidelions are able to thumbs up and thumbs down. If a user thumbs up, the offensive message will be deleted. Furthermore, the custom server classifier will be trained using this data.

Note that in a server's infancy, the accuracy of this custom classifier will not be good but will get better wih more classification data. The classifier is served in a pickle file which will be stored in the folder.