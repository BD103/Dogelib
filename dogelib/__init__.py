import platform

try:
  import colorama
except ModuleNotFoundError:
  colorama = None
finally:
  if colorama and platform.system() == "Windows":
    colorama.init()
