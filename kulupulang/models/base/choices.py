class PartOfSpeech:
    NOUN = 'noun'
    VERB = 'verb'
    PARTICLE = 'particle'
    PRONOUN = 'pronoun'
    CHOICES = (
        (NOUN, 'noun'),
        (VERB, 'verb'),
        (PARTICLE, 'particle'),
        (PRONOUN, 'pronoun'),
    )


class WordClass:
    AKULU = 'akulu'
    IKULU = 'ikulu'
    NKULU = 'nkulu'
    CHOICES = (
        (AKULU, 'animate kulupu'),
        (IKULU, 'inanimate kulupu'),
        (NKULU, 'non-kulupu'),
    )
