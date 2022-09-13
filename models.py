from dataclasses import dataclass

@dataclass
class Agent:
    platform: str
    paw: str
    username: str
    host: str
    role: str = ""

    def from_dict(d):
        return Agent(
            d["platform"],
            d["paw"],
            d["username"],
            d["host"]
        )