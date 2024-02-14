from dotenv import dotenv_values

env = dotenv_values(".env")

PORT = int(env["PORT"])
DEBUG = bool(int(env["DEBUG"]))
