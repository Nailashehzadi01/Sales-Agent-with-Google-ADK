import uuid
from datetime import datetime, timedelta
from typing import Optional

def generate_lead_id(prefix: Optional[str] = None) -> str:
    """Generate a unique lead ID with optional prefix.
    
    Args:
        prefix: Optional prefix to add to the ID
        
    Returns:
        str: Generated lead ID
    """
    lead_id = str(uuid.uuid4())
    return f"{prefix}_{lead_id}" if prefix else lead_id

def simulate_time_advance(hours: int, current_time: Optional[datetime] = None) -> datetime:
    """Simulate time advancing for testing purposes.
    
    Args:
        hours: Number of hours to advance
        current_time: Optional starting time (defaults to now)
        
    Returns:
        datetime: New datetime after advancement
    """
    if current_time is None:
        current_time = datetime.now()
    return current_time + timedelta(hours=hours)