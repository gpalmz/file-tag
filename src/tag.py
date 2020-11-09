from dataclasses import dataclass
from typing import Optional, Union


@dataclass
class Tag:
    key: str
    value: Optional[Union[str, int]]

    def __str__(self):
        return f'{self.key}_{self.value}'
