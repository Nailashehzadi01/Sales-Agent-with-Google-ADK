from datetime import datetime, timedelta
from typing import Dict, Any, Optional
import threading
from copy import deepcopy

class SessionManager:
    def __init__(self):
        self.sessions = {}
        self.lock = threading.Lock()
        self.questions = [
            {'key': 'age', 'text': 'What is your age?'},
            {'key': 'country', 'text': 'Which country are you from?'},
            {'key': 'interest', 'text': 'What product or service are you interested in?'}
        ]

    def create_session(self, lead_id: str, initial_data: Dict[str, Any] = None) -> bool:
        """Create a new session for a lead."""
        if not lead_id:
            return False
        
        with self.lock:
            if lead_id in self.sessions:
                return False
            
            self.sessions[lead_id] = {
                'data': initial_data or {},
                'state': 'initial',
                'last_activity': datetime.now(),
                'current_question': None,
                'questions': deepcopy(self.questions),
                'completed': False
            }
            return True

    def get_session(self, lead_id: str) -> Optional[Dict[str, Any]]:
        """Get a lead's session data."""
        if not lead_id:
            return None
        
        with self.lock:
            return deepcopy(self.sessions.get(lead_id))

    def update_session(self, lead_id: str, updates: Dict[str, Any]) -> bool:
        """Update a lead's session data."""
        if not lead_id:
            return False
        
        with self.lock:
            if lead_id not in self.sessions:
                return False
            
            self.sessions[lead_id].update(updates)
            self.sessions[lead_id]['last_activity'] = datetime.now()
            return True

    def get_next_question(self, lead_id: str) -> Optional[Dict[str, str]]:
        """Get the next question for a lead."""
        if not lead_id:
            return None
        
        with self.lock:
            session = self.sessions.get(lead_id)
            if not session or session['completed']:
                return None
            
            # Find the first unanswered question
            for question in session['questions']:
                if question['key'] not in session['data']:
                    session['current_question'] = question['key']
                    return deepcopy(question)
            
            # All questions answered
            session['completed'] = True
            session['current_question'] = None
            return None

    def record_answer(self, lead_id: str, key: str, value: str) -> bool:
        """Record an answer to a question."""
        if not lead_id or not key:
            return False
        
        with self.lock:
            if lead_id not in self.sessions:
                return False
            
            self.sessions[lead_id]['data'][key] = value
            self.sessions[lead_id]['last_activity'] = datetime.now()
            return True

    def check_inactive_sessions(self, hours: int = 24) -> Dict[str, Dict[str, Any]]:
        """Get sessions inactive for more than specified hours."""
        with self.lock:
            threshold = datetime.now() - timedelta(hours=hours)
            inactive = {
                lead_id: deepcopy(session) 
                for lead_id, session in self.sessions.items() 
                if (session['last_activity'] < threshold and 
                    not session['completed'] and
                    session['state'] != 'initial')
            }
            return inactive

    def end_session(self, lead_id: str) -> bool:
        """End a lead's session."""
        if not lead_id:
            return False
        
        with self.lock:
            if lead_id in self.sessions:
                del self.sessions[lead_id]
                return True
            return False