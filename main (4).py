# ================== منع الأوفلاين ==================
from flask import Flask
from threading import Thread

app = Flask("")


@app.route("/")
def home():
    return "Azkar bot is alive!"


def run():
    app.run(host="0.0.0.0", port=8080)


def keep_alive():
    Thread(target=run).start()


keep_alive()

# ================== البوت ==================
import discord
from discord.ext import commands, tasks
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# ================== الإعدادات ==================
AZKAR_CHANNEL_ID = 000000000000000000  # ← حط ID الروم هنا

# ================== الأذكار الكاملة ==================
AZKAR_LIST = [
    "﴿أَلَا بِذِكْرِ اللَّهِ تَطْمَئِنُّ الْقُلُوبُ﴾ 🌿",
    "سبحان الله 🌸",
    "الحمد لله 🤍",
    "الله أكبر 💙",
    "لا إله إلا الله وحده لا شريك له، له الملك وله الحمد وهو على كل شيء قدير",
    "سبحان الله وبحمده، سبحان الله العظيم",
    "اللهم صلِّ وسلم على نبينا محمد ﷺ",
    "أستغفر الله العظيم وأتوب إليه",
    "رضيت بالله ربًا وبالإسلام دينًا وبمحمد ﷺ نبيًا",
    "اللهم اغفر لي ولوالدي وللمؤمنين والمؤمنات 🤲",
]


# ================== عند التشغيل ==================
@bot.event
async def on_ready():
    print(f"📿 Azkar Bot Online as {bot.user}")
    send_azkar.start()


# ================== إرسال ذكر كل 30 دقيقة ==================
@tasks.loop(minutes=30)
async def send_azkar():
    channel = bot.get_channel(AZKAR_CHANNEL_ID)
    if channel:
        zikr = random.choice(AZKAR_LIST)
        await channel.send(f"📿 **ذكر**\n{zikr}")


# ================== أوامر اختيارية ==================
@bot.command()
async def ذكر(ctx):
    zikr = random.choice(AZKAR_LIST)
    await ctx.send(f"📿 **ذكر**\n{zikr}")


# ================== تشغيل ==================
bot.run("TOKEN")
