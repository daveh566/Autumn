import sentry_sdk
from sentry_sdk.integrations.redis import RedisIntegration

from Autumn.config import get_str_key
from Autumn.utils.logger import log

log.info("Starting sentry.io integraion...")

sentry_sdk.init(get_str_key("SENTRY_API_KEY"), integrations=[RedisIntegration()])
