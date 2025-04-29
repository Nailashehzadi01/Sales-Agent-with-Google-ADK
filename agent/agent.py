from typing import Dict, Optional, List
import threading
import time
from datetime import datetime, timedelta
from .data_handler import DataHandler
from .session_manager import SessionManager

class SalesAgent:
    def __init__(self, data_file: str = 'leads.csv'):
        self.data_handler = DataHandler(data_file)
        self.session_manager = SessionManager()
        self.running = False
        self.follow_up_thread = None
        self.follow_up_interval = 60  # seconds between follow-up checks

    def start(self):
        """Start the agent and follow-up monitoring."""
        if self.running:
            return
        
        self.running = True
        self._start_follow_up_monitor()
        print("Sales Agent started and monitoring for follow-ups...")

    def stop(self):
        """Stop the agent and clean up."""
        if not self.running:
            return
        
        self.running = False
        if self.follow_up_thread and self.follow_up_thread.is_alive():
            self.follow_up_thread.join()
        print("Sales Agent stopped.")

    def _start_follow_up_monitor(self):
        """Start a background thread to monitor for follow-ups."""
        def follow_up_monitor():
            while self.running:
                self.check_for_follow_ups()
                time.sleep(self.follow_up_interval)

        self.follow_up_thread = threading.Thread(target=follow_up_monitor)
        self.follow_up_thread.daemon = True
        self.follow_up_thread.start()

    def trigger_agent(self, lead_id: str, name: str) -> bool:
        """Trigger the agent for a new lead."""
        if not lead_id or not name:
            return False
        
        # Add lead to data storage
        if not self.data_handler.add_lead(lead_id, name):
            print(f"Lead {lead_id} already exists")
            return False
        
        # Create a new session
        self.session_manager.create_session(lead_id, {'name': name})
        
        # Send initial message
        initial_message = (
            f"Hey {name}, thank you for filling out the form. "
            "I'd like to gather some information from you. Is that okay?"
        )
        print(f"Message sent to {name} (ID: {lead_id}): {initial_message}")
        
        return True

    def handle_response(self, lead_id: str, response: str) -> Optional[str]:
        """Handle a lead's response and return the next message if any."""
        if not lead_id or not response:
            return None
        
        lead_data = self.data_handler.get_lead(lead_id)
        if not lead_data:
            return None
        
        session = self.session_manager.get_session(lead_id)
        if not session:
            return None
        
        # Handle initial consent
        if session['state'] == 'initial':
            return self._handle_initial_response(lead_id, lead_data, session, response)
        
        # Handle question responses
        elif session['state'] == 'questioning':
            return self._handle_question_response(lead_id, lead_data, session, response)
        
        return None

    def _handle_initial_response(self, lead_id: str, lead_data: Dict, 
                               session: Dict, response: str) -> Optional[str]:
        """Handle the initial consent response."""
        if response.lower() in ['yes', 'y', 'sure', 'ok', 'okay']:
            self.session_manager.update_session(lead_id, {'state': 'questioning'})
            self.data_handler.update_lead(lead_id, {'status': 'in_progress'})
            next_question = self.session_manager.get_next_question(lead_id)
            if next_question:
                return next_question['text']
        else:
            self.data_handler.update_lead(lead_id, {'status': 'no_response'})
            self.session_manager.end_session(lead_id)
            return "Alright, no problem. Have a great day!"
        return None

    def _handle_question_response(self, lead_id: str, lead_data: Dict,
                                session: Dict, response: str) -> Optional[str]:
        """Handle responses to questions."""
        current_question = session['current_question']
        if not current_question:
            return None
        
        # Record the answer
        self.session_manager.record_answer(lead_id, current_question, response)
        
        # Update data storage
        updates = {current_question: response}
        if current_question == 'interest':  # Last question
            updates['status'] = 'secured'
        self.data_handler.update_lead(lead_id, updates)
        
        # Get next question
        next_question = self.session_manager.get_next_question(lead_id)
        if next_question:
            return next_question['text']
        else:
            self.session_manager.end_session(lead_id)
            return "Thank you for providing all the information! We'll be in touch soon."

    def check_for_follow_ups(self):
        """Check for leads that need follow-up messages."""
        inactive_sessions = self.session_manager.check_inactive_sessions(hours=24)
        
        for lead_id, session in inactive_sessions.items():
            lead_data = self.data_handler.get_lead(lead_id)
            if lead_data and lead_data['status'] == 'in_progress':
                # Send follow-up message
                follow_up = (
                    "Just checking in to see if you're still interested. "
                    "Let me know when you're ready to continue."
                )
                print(f"Follow-up sent to {lead_data['name']} (ID: {lead_id}): {follow_up}")
                
                # Update last activity to prevent immediate follow-up
                self.session_manager.update_session(lead_id, {})