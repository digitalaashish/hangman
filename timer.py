"""
Timer Module

This module provides timing functionality for the Hangman game,
including countdown timers and timeout handling.
"""

import threading
import time


class GameTimer:
    """Handles timing functionality for the Hangman game"""

    def __init__(self, timeout_seconds=15):
        self.timeout_seconds = timeout_seconds
        self.is_running = False
        self.timed_out = False
        self.time_remaining = timeout_seconds
        self.timer_thread = None
        self.stop_event = threading.Event()
        self.timeout_callback = None

    def start(self):
        """Start the timer"""
        if self.is_running:
            return

        self.is_running = True
        self.timed_out = False
        self.time_remaining = self.timeout_seconds
        self.stop_event.clear()

        self.timer_thread = threading.Thread(target=self._run_timer)
        self.timer_thread.daemon = True
        self.timer_thread.start()

    def stop(self):
        """Stop the timer"""
        self.is_running = False
        self.stop_event.set()
        if self.timer_thread and self.timer_thread.is_alive():
            self.timer_thread.join(timeout=1)

    def reset(self):
        """Reset the timer"""
        self.stop()
        self.time_remaining = self.timeout_seconds
        self.timed_out = False

    def _run_timer(self):
        """Internal timer loop"""
        start_time = time.time()

        while self.is_running and not self.stop_event.is_set():
            elapsed = time.time() - start_time
            self.time_remaining = max(0, self.timeout_seconds - elapsed)

            # Check if time is up
            if self.time_remaining <= 0:
                self.timed_out = True
                self.is_running = False
                if self.timeout_callback:
                    self.timeout_callback()
                break

            # Sleep for a short interval to update display
            time.sleep(0.1)

    def set_timeout_callback(self, callback):
        """Set callback function to call when timer expires"""
        self.timeout_callback = callback

    def set_update_callback(self, callback):
        """Set callback function to call for timer updates"""
        # kept for compatibility but not used in simplified version

    def get_time_remaining(self):
        """Get remaining time in seconds"""
        return self.time_remaining

    def get_formatted_time(self):
        """Get formatted time string (MM:SS)"""
        minutes = int(self.time_remaining // 60)
        seconds = int(self.time_remaining % 60)
        return f"{minutes:02d}:{seconds:02d}"
