from typing import List
from pathlib import Path


class Parser:
    extensions: List[str] = []

    def validate_extension(self, extension):
        return extension in Parser.extensions
