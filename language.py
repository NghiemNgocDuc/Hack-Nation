MAP = {"english":"en","español":"es","français":"fr"}
def normalize(code: str) -> str:
    return MAP.get(code, code)
