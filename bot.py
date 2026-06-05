import logging

from hello_bot import HelloBot

def main() -> None:
    logging.basicConfig(level=logging.INFO, format="[%(asctime)s] %(levelname)s: %(message)s")
    bot = HelloBot(prefix="!", ext_dir="cogs")
    bot.run()


if __name__ == "__main__":
    main()