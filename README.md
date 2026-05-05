# ChatuseOS-Discord
Chat use your OS on Discord

Support: Every OS (maybe) and Python 3.10 or above

> [!CAUTION]
> By using this, you acknowledge that you are responsible for any potential risks, including your computer being controlled by Discord Bot users, which may also violate Discord policies. Please consider carefully!

> [!TIP]
> Run this on VM can safe for your computer

# Installation and Start
### 1. Make a new bot
1. Open [Discord Developer Portal](https://discord.com/developers/applications)
2. Click **New Application**
3. Name it
4. Go to **Bot** and enable **Message Content Intent**
5. Save it!
6. Click **Reset token** and confirm it!
7. Click **Copy**
> [!CAUTION]
> Don’t let your Discord bot token be exposed!
### 2. Download and Run it!
Open Terminal and execute this:
```bash
git clone https://github.com/anlqdev/ChatuseOS-Discord
cd ChatuseOS-Discord
python -m pip install -r requirements.txt
```
Rename file `.env.example` to `.env` and replace `Your_Token_Here` in that file with your token that you're copied!

After that, execute this on Terminal:
```bash
python main.py
```
> [!NOTE]
> If you use Python 3.13 or above, you will receive `ModuleNotFoundError` because module `audioop` has been removed. You can install it by execute this on Terminal:
> ```py
> python -m pip install audioop-lts
> ```

# Commands
Commands will use prefix `!` like `!help`. You can change it!
### Use Keyboard
| Command | Usage | Use for |
|---|---|---|
| `!press` | `!press <button>` | Press a single key |
| `!combo` | `!combo <buttons>` | Press a combination of keys |
| `!type` | `!type <message>` | Type out a message |
| `!send` | `!send <message>` | Type out a message and press Enter |
| `!hold` | `!hold <button>` | Hold a key |
| `!release` | `!release <button>` | Release a key |
### Use Mouse
| Command | Usage | Use for |
|---|---|---|
| `!move` | `!move <x> <y>` | Move the mouse to a specific position |
| `!drag` | `!drag <x> <y>` | Drag the mouse to a specific position |
| `!click` | `!click` | Perform a left mouse click |
| `!rclick` | `!rclick` | Perform a right mouse click |
| `!scroll` | `!scroll <clicks>` | Scroll the mouse wheel |
| `!midclick` | `!midclick` | Perform a middle mouse click |
### Windows
| Command | Usage | Use for |
|---|---|---|
| `!focus` | `!focus <window>` | Focus a window by its title |
### Others
| Command | Usage | Use for |
|---|---|---|
| `!ping` | `!ping` | Ping the bot! |
| `!help` | `!help <commands>` or `!help` | See help. Use `!help` to see all command and `!help <commands>` to see the command |

# One more thing...
I haven't test this before uploading on GitHub. So, if you got any error, report it to me by [make a new Issues](https://github.com/anlqdev/ChatuseOS-Discord/issues/new/choose)! Anyways, if you need support, contact me by [join this Discord server](https://discord.gg/BpwQS556Zj)!

Thanks!


---
Made by An with =)) and <3
