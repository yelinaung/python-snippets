import time
import logging


class Timer:
    def __init__(self):
        self.start = time.time()

    def restart(self):
        self.start = time.time()

    def get_time_hhmmss(self):
        end = time.time()
        m, s = divmod(end - self.start, 60)
        h, m = divmod(m, 60)
        return "%02d:%02d:%02d" % (h, m, s)


def test():
    logging.getLogger().setLevel(logging.INFO)
    logging.info("starting the timer")
    my_timer = Timer()
    print("Starting ...")
    print("Going to sleep")
    time.sleep(3)
    print("waking up in the middle")
    time.sleep(3)
    print("I am done")
    logging.info("It took %s", my_timer.get_time_hhmmss())


if __name__ == '__main__':
    test()
