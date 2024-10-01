import time

class Timer:
    def __init__(self, duration: int):
        self.duration = duration
        self.start_time = time.time()

    def time_left(self):
        """Return the amount of time left in seconds."""
        elapsed = time.time() - self.start_time
        return max(0, self.duration - elapsed)

    def is_time_up(self):
        """Check if the timer has run out."""
        return self.time_left() <= 0
