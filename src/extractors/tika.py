import enum
import typing
from pathlib import Path


class OutputType(str, enum.Enum):
    XHTML = "XHTML"
    STR = "STR"


def extract_content(path: typing.Union[Path, str], output_format: OutputType = OutputType.STR) -> str:
    import tika
    from tika import parser
    parsed = parser.from_file(f"{path}", xmlContent=output_format == OutputType.XHTML)
    return parsed['content']
