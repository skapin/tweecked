import tweepy
import os
import logging

from dotenv import load_dotenv
load_dotenv(dotenv_path='.env-dev')


def init_logging():
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG if bool(os.getenv('DEBUG_MODE')) else logging.WARNING)
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.DEBUG)
    logger.addHandler(stream_handler)


LOG = logging.getLogger(__name__)

LAST_DIRECT_MESSAGE = ''

auth = tweepy.OAuth1UserHandler(consumer_key=os.getenv('API_KEY'),
                                consumer_secret=os.getenv('API_KEY_SECRET'),
                                access_token=os.getenv('ACCESS_TOKEN'),
                                access_token_secret=os.getenv('ACCESS_TOKEN_SECRET'))


api = tweepy.API(auth)

LOG.info('===[START]===')
if __name__ == '__main__':
    LOG.info('===[START]===')
    public_tweets = api.home_timeline()
    for tweet in public_tweets:
        LOG.info(tweet.text)
    LOG.info('===[END]===')
