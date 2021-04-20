# Windows specific
import platform
from types import ModuleType

from dogelib import colorama as t_colorama


def test_colorama():
  if platform.system() == "Windows":
    assert isinstance(t_colorama, ModuleType)
