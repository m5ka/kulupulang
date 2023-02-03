import random

from django.core.management.base import BaseCommand
from faker import Faker

from kulupulang.models.base.choices import PartOfSpeech, WordClass
from kulupulang.models.dictionary import Batch


class Command(BaseCommand):
    def fake_definition(self, fake):
        return ", ".join([fake.word() for _ in range(random.randint(1, 3))])

    def handle(self, *args, **options):
        fake = Faker()
        for _ in range(50):
            batch = Batch.objects.create(
                name=fake.sentence(nb_words=4).lower()[:-1],
                description=fake.paragraph(),
                passed=True,
            )
            print(f"Batch: {batch}")
            for _ in range(20):
                word = batch.word_set.create(
                    headword=fake.word(),
                    pos=random.choice(PartOfSpeech.CHOICES)[0],
                    cls=random.choice(WordClass.CHOICES)[0],
                    definition=self.fake_definition(fake),
                    etymology=fake.sentence(nb_words=5).lower()[:-1],
                    notes=fake.paragraph(),
                    passed=True,
                )
                print(f"-> Word: {word.headword} = {word.definition}")
            batch.save()
