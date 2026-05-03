import discord
from discord.ext import commands
import keyboard
import os
from dotenv import load_dotenv
import pyautogui as mouse

input("ATTENTION: By pressing the Enter key, you acknowledge that you are responsible for any potential risks, including your computer being controlled by Discord Bot users, which may also violate Discord policies. Please consider carefully. Press Ctrl + C to exit. Press Enter to continue...")

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} started!")

@bot.command()
async def ping(ctx):
    """Ping the bot!"""
    await ctx.send(f"Pong! The latency is {bot.latency:.2f} seconds.")

@bot.command()
async def press(ctx, key: str):
    '''Press a single key. Example: !press a'''
    keyboard.press_and_release(key)
    await ctx.send(f"Pressed the '{key}' key.")

@bot.command()
async def combo(ctx, *keys: str):
    '''Press a combination of keys. Example: !combo ctrl c'''
    keyboard.send(' '.join(keys))
    await ctx.send(f"Pressed the keys: {', '.join(keys)}")

@bot.command()
async def type(ctx, *, text: str):
    '''Type out a message. Example: !type Hello, world!'''
    keyboard.write(text)
    await ctx.send(f"Typed the text: {text}")

@bot.command()
async def send(ctx, *, text: str):
    '''Type out a message and press Enter. Example: !send Hello, world!'''
    keyboard.write(text)
    keyboard.press('enter')
    await ctx.send(f"Sent the message: {text}")

@bot.command()
async def hold(ctx, key: str):
    '''Hold a key. Example: !hold a'''
    keyboard.press(key)
    await ctx.send(f"Holding the '{key}' key.")

@bot.command()
async def release(ctx, key: str):
    '''Release a key. Example: !release a'''
    keyboard.release(key)
    await ctx.send(f"Released the '{key}' key.")

@bot.command()
async def move(ctx, x: int, y: int):
    '''Move the mouse to a specific position. Example: !move 100 200'''
    mouse.moveTo(x, y)
    await ctx.send(f"Moved the mouse to ({x}, {y}).")

@bot.command()
async def drag(ctx, x: int, y: int):
    '''Drag the mouse to a specific position. Example: !drag 100 200'''
    mouse.dragTo(x, y)
    await ctx.send(f"Dragged the mouse to ({x}, {y}).")

@bot.command()
async def click(ctx):
    '''Perform a left mouse click. Example: !leftclick'''
    mouse.click(button='left')
    await ctx.send("Performed a left mouse click.")

@bot.command()
async def rclick(ctx):
    '''Perform a right mouse click. Example: !rightclick'''
    mouse.click(button='right')
    await ctx.send("Performed a right mouse click.")

@bot.command()
async def scroll(ctx, clicks: int):
    '''Scroll the mouse wheel. Example: !scroll 10'''
    mouse.scroll(clicks)
    await ctx.send(f"Scrolled the mouse wheel by {clicks} clicks.")

@bot.command()
async def midclick(ctx):
    '''Perform a middle mouse click. Example: !midclick'''
    mouse.click(button='middle')
    await ctx.send("Performed a middle mouse click.")

@bot.command()
async def focus(ctx, window:str):
    '''Focus a window by its title. Example: !focus Notepad'''
    try:
        mouse.getWindowsWithTitle(window)[0].activate()
        await ctx.send(f"Focused the window with title: {window}")
    except IndexError:
        await ctx.send(f"No window found with title: {window}")

bot.run(os.getenv("DISCORD_BOT_TOKEN"))