from environs import Env

env = Env()
env.read_env()

# Token from BotFather
BOT_TOKEN = env.str("BOT_TOKEN")
# List of admins
ADMINS = env.list("ADMINS")
# Host's IP
IP = env.str("ip")
