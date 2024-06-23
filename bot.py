import discord
import asyncio
from bybit import get_klines, calculate_rsi

TOKEN = 'MTI1NDQ1NjEyNDY5MDkyMzYxNQ.GjGNLK.-GUQ4VRM2yHbw5BPPCqPYqlxOzV_FnwhrMq34E'
CHANNEL_ID = 1254462204325925001


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    channel = client.get_channel(CHANNEL_ID)
    await channel.send('Bot is now online and monitoring RSI.')
    while True:
        df = get_klines()
        df = calculate_rsi(df)
        latest_rsi = df['rsi'].iloc[-1]
        if latest_rsi > 70:
            await channel.send(f'RSI over 70: {latest_rsi}')
        elif latest_rsi < 30:
            await channel.send(f'RSI below 30: {latest_rsi}')
        await asyncio.sleep(3600)  # Wait for 1 hour

client.run(TOKEN)
