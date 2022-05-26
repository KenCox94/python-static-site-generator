import re
from collections.abc import Mapping
from yaml import load, FullLoader


class Content(Mapping):
    __delimeter = "^(?:-|\+){3}\s*$"
    __regex = re.compile(__delimeter, re.MULTILINE)
