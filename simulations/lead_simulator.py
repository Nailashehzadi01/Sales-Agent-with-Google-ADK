import time
from datetime import datetime
from typing import Dict, List, Optional, Any
from agent.agent import SalesAgent
from agent.utils import generate_lead_id

class LeadSimulator:
    """Simulates lead interactions with the sales agent for testing purposes."""
    
    def __init__(self, agent: SalesAgent):
        """Initialize the simulator with an agent instance.
        
        Args:
            agent: SalesAgent instance to interact with
        """
        self.agent = agent
        self.leads: Dict[str, Dict[str, Any]] = {}
    
    def create_lead(self, name: str, lead_id: Optional[str] = None) -> str:
        """Create a new simulated lead.
        
        Args:
            name: Lead's name
            lead_id: Optional custom lead ID
            
        Returns:
            str: Generated or provided lead ID
        """
        lead_id = lead_id or generate_lead_id()
        self.leads[lead_id] = {
            'name': name,
            'status': 'pending',
            'responses': [],
            'created_at': datetime.now(),
            'completed': False
        }
        self.agent.trigger_agent(lead_id, name)
        return lead_id
    
    def simulate_response(self, lead_id: str, response: str) -> Optional[str]:
        """Simulate a lead responding to the agent.
        
        Args:
            lead_id: ID of the lead
            response: Response text
            
        Returns:
            Optional[str]: Agent's reply or None if invalid
        """
        if lead_id not in self.leads:
            return None
        
        # Get the agent's response
        agent_reply = self.agent.handle_response(lead_id, response)
        
        # Store the interaction
        interaction = {
            'time': datetime.now(),
            'lead_said': response,
            'agent_said': agent_reply
        }
        self.leads[lead_id]['responses'].append(interaction)
        
        # Update completion status
        if agent_reply and "Thank you for providing" in agent_reply:
            self.leads[lead_id]['completed'] = True
            self.leads[lead_id]['status'] = 'secured'
        elif agent_reply and "no problem" in agent_reply:
            self.leads[lead_id]['completed'] = True
            self.leads[lead_id]['status'] = 'no_response'
        
        return agent_reply
    
    def simulate_conversation(self, lead_id: str, answers: List[str], 
                            delay: float = 0.5) -> List[str]:
        """Simulate a complete conversation with a lead.
        
        Args:
            lead_id: ID of the lead
            answers: List of answers to provide
            delay: Delay between responses (seconds)
            
        Returns:
            List[str]: Conversation history
        """
        if lead_id not in self.leads:
            return []
        
        conversation = []
        # Initial response (to consent question)
        initial_reply = self.simulate_response(lead_id, 'yes')
        if initial_reply:
            conversation.append(f"Agent: {initial_reply}")
            time.sleep(delay)
        
        # Answer all questions
        for answer in answers:
            reply = self.simulate_response(lead_id, answer)
            if reply:
                conversation.append(f"Agent: {reply}")
                time.sleep(delay)
            else:
                break
        
        return conversation
    
    def simulate_no_response(self, lead_id: str):
        """Simulate a lead not responding.
        
        Args:
            lead_id: ID of the lead
        """
        if lead_id in self.leads:
            print(f"Lead {self.leads[lead_id]['name']} (ID: {lead_id}) has not responded")
    
    def get_lead_status(self, lead_id: str) -> Optional[str]:
        """Get the current status of a lead.
        
        Args:
            lead_id: ID of the lead
            
        Returns:
            Optional[str]: Current status or None if not found
        """
        if lead_id in self.leads:
            return self.leads[lead_id]['status']
        return None