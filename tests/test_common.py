# Common Tests
from dogelib import much, wow


class TestMuch:
  def test_rainbow_iter(self):
    for palette in ["basic", "bg", "ex"]:
      print(palette)
      iterator = much._rainbow_iter(palette=palette)

      # + 1 makes sure that it loops
      for _ in range(len(much._colors[palette]) + 1):
        i = next(iterator)
        print(_, i)

    # Maybe find better way?
    assert True
  
  def test_rainbow(self):
    solutions = {
      "basic": "\033[31mt\033[33me\033[32ms\033[36mt\033[0m",
      "bg": "\033[41mt\033[43me\033[42ms\033[46mt\033[0m",
      "ex": "\033[91mt\033[93me\033[92ms\033[96mt\033[0m"
    }
    for palette in solutions:
      assert solutions[palette] == much.rainbow("test", palette=palette)
  
  # Maybe test color by setting the random seed?


class TestWow:
  def test_whitespace(self):
    for i in range(5):
      test = wow._whitespace()
      assert test.isspace() or test == ""

  # Hard to capture MOTD, figure out something?

  def test_facs(self, capsys):
    wow.facs()

    assert capsys.readouterr().out == "\033[4mhttps://meme.fandom.com/wiki/Doge\033[0m\n"