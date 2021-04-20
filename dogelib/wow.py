from random import randint

from .much import color

try:
  from doge.core import main as doge_main
except ModuleNotFoundError:
  doge_main = None


def _whitespace():
  return "".join(" " for i in range(randint(0, 5)))

def motd():
  if doge_main:
    doge_main()
  else:
    for i in ["stahp", "so scare", "no doge", "much sadness", "wow do pip install doge"]:
      print("\033[1m" + color(_whitespace() + i, palette="ex"))

def facs():
  print("\033[4mhttps://meme.fandom.com/wiki/Doge\033[0m")