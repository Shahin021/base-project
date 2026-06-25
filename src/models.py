from dataclasses import dataclass


@dataclass
class Project:
    name: str
    category: str
    status: str
    website: str = ""
    notes: str = ""
