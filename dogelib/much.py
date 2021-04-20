from random import randint

_colors = {
  "basic": [31, 33, 32, 36, 34, 35],
  "bg": [41, 43, 42, 46, 44, 45],
  "ex": [91, 93, 92, 96, 94, 95]
}

def _rainbow_iter(palette="basic"):
  while True:
    for i in _colors[palette]:
      yield i

def rainbow(text:str, palette="basic"):
  value = ""
  rotation = _rainbow_iter(palette)

  for i in text:
    value += f"\033[{next(rotation)}m{i}"
  
  rotation.close()
  value += "\033[0m"

  return value

def color(text:str, palette="basic"):
  return f"\033[{_colors[palette][randint(0, len(_colors[palette]) - 1)]}m{text}\033[0m"
