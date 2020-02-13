import string
CHARACTERS_TYPES = {
    "characters": list(string.ascii_letters),
    "digits": list(string.digits),
    "punctuations":  list(string.punctuation),
}

CHARACTERS_TYPES["all"] = CHARACTERS_TYPES.get("characters") + CHARACTERS_TYPES.get("digits") + \
                          CHARACTERS_TYPES.get("punctuations")
