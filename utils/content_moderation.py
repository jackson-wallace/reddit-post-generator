import re

TRIGGER_REPLACEMENTS = {
    "kill": "unalive",
    "killing": "unaliving",
    "sex": "intimacy",
    "sexually": "intimately",
    "rape": "rope",
    "raped": "roping",
    "raping": "roping",
    "anal": "back door stuff",
    "anus": "back door",
    "analingus": "back door stuff",
    "ballsack": "family jewel bag",
    "balls": "family jewels",
    "bitch": "female dog",
    "bitches": "female dogs",
    "tits": "melons",
    "tit": "melon",
    "boobs": "cowboy pillows",
    "boob": "cowboy pillow,",
    "blowjob": "brain",
    "blow job": "brain",
    "blowjobs": "beejers",
    "blew": "beejered",
    "boner": "tent pole",
    "boners": "tent poles",
    "dick": "vein cane",
    "dicks": "vein cane",
    "cock": "vein cane",
    "cocks": "vein canes",
    "sexual assault": "sa",
    "sexually assaulted": "saed",
    "fucked": "screwed",
    "pedophile": "minor attracted person",
    "pedophiles": "minor attracted people",
    "death": "eternal departure",
    "deaths": "eternal departures",
    "died": "passed away",
    "fucking": "freaking",
}


def replace_trigger_words(content):
    def replace_word(match):
        word = match.group(0)
        # Retain the original casing for the first letter of the replacement word
        replacement = TRIGGER_REPLACEMENTS[word.lower()]
        if word[0].isupper():
            replacement = replacement[0].upper() + replacement[1:]
        return replacement

    # Using a regex pattern to match any word in the trigger list
    pattern = (
        r"\b(?:"
        + "|".join(re.escape(key) for key in TRIGGER_REPLACEMENTS.keys())
        + r")\b"
    )
    cleaned_content = re.sub(pattern, replace_word, content, flags=re.IGNORECASE)
    return cleaned_content
