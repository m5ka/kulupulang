from .models import Batch
from .webhook import send_batch_passed_webhook


def promote_oven_to_dictionary_task():
    for batch in Batch.objects.in_oven().all():
        if batch.check_passed():
            batch.pass_batch()
            send_batch_passed_webhook(batch)
