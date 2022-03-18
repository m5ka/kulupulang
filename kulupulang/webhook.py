from urllib.parse import urljoin

from discord_webhook import DiscordEmbed, DiscordWebhook
from django.conf import settings


def _send_webhook(title=None, description=None, url=None):
    webhook = DiscordWebhook(url=settings.DISCORD_WEBHOOK_URL)
    embed = DiscordEmbed(
        title=title,
        description=description,
        url=url,
        color=settings.DISCORD_WEBHOOK_COLOR,
    )
    webhook.add_embed(embed)
    webhook.execute()


def send_batch_passed_webhook(batch=None):
    if not batch:
        raise ValueError('A batch must be given')
    _send_webhook(
        title='Batch passed',
        description=batch.name,
        url=urljoin(
            settings.PUBLIC_URL,
            batch.get_absolute_url(),
        )
    )
