import sys
import logging
from matizla import core

logging.basicConfig(
    stream=sys.stdout,
    level=logging.INFO,
    format='%(levelname)s:%(name)s:%(funcName)s:[%(lineno)d]   %(message)s'
)
_LOGGER = logging.getLogger(__name__)

def main():
    _LOGGER.info("Starting matizla...")
    core.run()

if __name__ == "__main__":
    sys.exit(main())