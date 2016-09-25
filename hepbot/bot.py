import logging
import os

LOG = logging.getLogger(__name__)

template = """
API_TOKEN = "{API_TOKEN}"
DEFAULT_REPLY = "Sorry but I did not understand you"
PLUGINS = [
{PLUGINS}
]

"""

PLUGINS = ['slackbot.plugins']

LOCATION = os.path.dirname(__file__)
SETUP_FILE = os.path.join(LOCATION, 'slackbot_settings.py')


def setup():
    LOG.info("Setting up")
    API_TOKEN = os.environ.get('API_TOKEN', '')
    if not API_TOKEN:
        LOG.error('Could not find API_TOKEN...exiting')
        import sys
        sys.exit(-1)
    plugins = os.environ.get('PLUGINS', '')

    if plugins:
        PLUGINS.extend(plugins.split(','))

    plugins = ['"{0}"'.format(p) for p in PLUGINS]
    file_content = template.format(
        API_TOKEN=API_TOKEN,
        PLUGINS=',\n'.join(plugins)
    )

    with open(SETUP_FILE, 'w+') as f:
        f.write(file_content)


def run():
    # run setup
    setup()
    # run bot
    from slackbot.bot import Bot
    bot = Bot()
    LOG.info('Starting bot...press CTRL+C to stop')
    bot.run()

if __name__ == '__main__':
    run()
