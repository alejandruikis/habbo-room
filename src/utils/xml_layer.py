LAYER_LETTER_IDS: dict[str, int] = {
    "a": 0,
    "b": 1,
    "c": 2,
    "d": 3,
}

LAYER_ID_TO_LETTER: dict[int, str] = {
    0: "a",
    1: "b",
    2: "c",
    3: "d",
}

DIRECTION_IDS = [0, 2, 4, 6]

def get_layer_id_from_letter(letter: str) -> int:
    
    if not letter:
        return None
    return LAYER_LETTER_IDS.get(letter.lower(), -1)