## Required Configs
 - `BOT_TOKEN` - Get from [@BotFather](https://t.me/BotFather)
 - `API_ID` - Get it from [telegram.org](https://my.telegram.org/auth)
 - `API_HASH` - Get it from [telegram.org](https://my.telegram.org/auth)
 - `AUTH_USERS` - Authorised user's ID to use [Admin Commands](https://github.com/nacbots/broadcastbot#admin-commands) {Split 💔 with a space}.
 - `DB_URL` - MongoDB Database URI get it from [mongodb.com](https://mongodb.com)
	- This for Saving UserIDs. When you will Broadcast, bot will forward the Broadcast to DB Users.

## Optional Configs
 - `LOG_CHANNEL` - Log Channel ID to get new user notifications.
	- This for some getting user info. If any new User added to DB, Bot will send Log to that Logs Channel. You can use same DB Channel ID.
 - `BROADCAST_AS_COPY` - Value should be `True` or `False`.
	- If `True` broadcast messages will be forwarder *As Copy*. If `False` broadcast messages will be forwarded with Forward Tag.
 - `DB_NAME` - [mongodb.com](https://mongodb.com) Collection name to be used.

## User's Commands 😉

```
start - Start the bot 🥲
settings - Customise settings
```

## Admin Commands 🤫

```
stats - Total User Number in Database
broadcast - Reply to Message to Broadcast
ban_user - Ban A User with time & reason
unban_user - Unban a User
banned_users - Show Banned Users
```
