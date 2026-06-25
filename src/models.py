from dataclasses import dataclass, field


@dataclass
class Project:
    name: str
    category: str
    status: str
    website: str = ""
    notes: str = ""
    tags: list[str] = field(default_factory=list)
