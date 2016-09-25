import logging
import os

LOG = logging.getLogger(__name__)
LOG.setLevel(logging.DEBUG)
# logging to a file
formatter = logging.Formatter(
    '%(asctime)s [%(name)s]  %(levelname)s: %(message)s')

# logging to the console
formatter = logging.Formatter('%(message)s')
ch = logging.StreamHandler()
if not os.environ.get("DEBUG", False):
    ch.setLevel(logging.INFO)
else:
    ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)
LOG.addHandler(ch)
