import time
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

from hyo2.abc.lib.progress.cli_progress import CliProgress

progress = CliProgress()

progress.start(title='Test Bar', text='Doing stuff', min_value=100, max_value=300, init_value=100)

time.sleep(.1)

progress.update(value=150, text='Updating')

time.sleep(.1)

progress.add(quantum=50, text='Updating')

time.sleep(.1)

print("canceled? %s" % progress.canceled)

progress.end()
