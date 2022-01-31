def all_subclasses(cls):
    return set(cls.__subclasses__()).union(
        [s for c in cls.__subclasses__() for s in all_subclasses(c)])


def base_receiver(signal, sender, **kwargs):
    def _decorator(func):
        signals = signal if isinstance(signal, (list, tuple)) else (signal,)
        for s in signals:
            for subclass in all_subclasses(sender):
                s.connect(func, subclass, **kwargs)
        return func
    return _decorator
