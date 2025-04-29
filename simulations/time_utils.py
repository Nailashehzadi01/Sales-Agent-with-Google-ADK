from datetime import datetime, timedelta

class TimeSimulator:
    @staticmethod
    def get_current_time() -> datetime:
        """Get the current time (can be mocked in tests)."""
        return datetime.now()
    
    @staticmethod
    def time_since(timestamp: datetime) -> timedelta:
        """Calculate time elapsed since given timestamp."""
        return TimeSimulator.get_current_time() - timestamp
    
    @staticmethod
    def is_older_than(timestamp: datetime, hours: int) -> bool:
        """Check if a timestamp is older than specified hours."""
        return TimeSimulator.time_since(timestamp) > timedelta(hours=hours)