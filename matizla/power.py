import os
from threading import Thread
from time import sleep
import RPi.GPIO as GPIO
import logging

_LOGGER = logging.getLogger(__name__)

GPIO.setmode(GPIO.BCM)
GPIO.setup(3, GPIO.IN)


class HaltOnGPIO:
    _thread: Thread

    @staticmethod
    def _callback(state):
        _LOGGER.info(F"gpio is {state}")
        if state:
            os.system("sudo shutdown --halt now")

    @staticmethod
    def enable():
        #GPIO.add_event_detect(3, GPIO.FALLING)
        #GPIO.add_event_callback(3, HaltOnGPIO._callback)

        def loop():
            state = GPIO.input(3)
            while True:
                while GPIO.input(3) == state:
                    sleep(0.2)
                    pass
                state = not state
                HaltOnGPIO._callback(state)

        HaltOnGPIO._thread = Thread(
            target=loop
        )

        HaltOnGPIO._thread.start()

    @staticmethod
    def disable():
        # GPIO.remove_event_detect(3)
        pass
