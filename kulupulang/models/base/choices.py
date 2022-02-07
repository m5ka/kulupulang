class PartOfSpeech:
    NOUN = 'noun'
    VERB = 'verb'
    PARTICLE = 'particle'
    PRONOUN = 'pronoun'
    ADJECTIVE = 'adjective'
    ADVERB = 'adverb'
    DETERMINER = 'determiner'
    ROOT = 'root'
    AFFIX = 'affix'
    CHOICES = (
        (NOUN, 'noun'),
        (VERB, 'verb'),
        (PARTICLE, 'particle'),
        (PRONOUN, 'pronoun'),
        (ADJECTIVE, 'adjective'),
        (ADVERB, 'adverb'),
        (DETERMINER, 'determiner'),
        (ROOT, 'root'),
        (AFFIX, 'affix'),
    )


class WordClass:
    AKULU = 'akulu'
    IKULU = 'ikulu'
    KULU = 'kulu'
    NKULU = 'nkulu'
    VAR = 'var'
    PAUC = 'pauc'
    PLUR = 'plur'
    CHOICES = (
        (AKULU, 'animate kulupu'),
        (IKULU, 'inanimate kulupu'),
        (KULU, 'kulupu (any)'),
        (NKULU, 'non-kulupu'),
        (VAR, 'variable gender'),
        (PAUC, 'paucal'),
        (PLUR, 'plural'),
    )
