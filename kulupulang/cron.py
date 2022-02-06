from .models import Batch


def promote_oven_to_dictionary_task():
    for batch in Batch.objects.in_oven().all():
        if batch.check_passed():
            batch.pass_batch()
