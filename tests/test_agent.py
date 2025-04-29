import pytest
from freezegun import freeze_time
from datetime import datetime, timedelta
from agent.agent import SalesAgent
from agent.data_handler import DataHandler

@pytest.fixture
def sales_agent(tmp_path):
    data_file = tmp_path / "test_leads.csv"
    agent = SalesAgent(data_file=str(data_file))
    yield agent
    agent.stop()

def test_agent_initialization(sales_agent):
    assert sales_agent is not None
    assert isinstance(sales_agent.data_handler, DataHandler)
    assert not sales_agent.running

def test_agent_start_stop(sales_agent):
    sales_agent.start()
    assert sales_agent.running
    assert sales_agent.follow_up_thread is not None
    sales_agent.stop()
    assert not sales_agent.running

@freeze_time("2023-01-01 12:00:00")
def test_lead_lifecycle(sales_agent):
    # Test lead creation
    lead_id = "test_123"
    assert sales_agent.trigger_agent(lead_id, "John Doe")
    
    # Test initial response handling
    response = sales_agent.handle_response(lead_id, "yes")
    assert "What is your age?" in response
    
    # Test question responses
    response = sales_agent.handle_response(lead_id, "30")
    assert "Which country are you from?" in response
    
    response = sales_agent.handle_response(lead_id, "USA")
    assert "What product or service are you interested in?" in response
    
    response = sales_agent.handle_response(lead_id, "Cloud Services")
    assert "Thank you for providing" in response
    
    # Verify data was stored correctly
    lead_data = sales_agent.data_handler.get_lead(lead_id)
    assert lead_data['age'] == '30'
    assert lead_data['country'] == 'USA'
    assert lead_data['interest'] == 'Cloud Services'
    assert lead_data['status'] == 'secured'

@freeze_time("2023-01-01 12:00:00")
def test_follow_up_system(sales_agent):
    sales_agent.start()
    
    # Create a lead that doesn't complete the conversation
    lead_id = "test_follow_up"
    sales_agent.trigger_agent(lead_id, "Follow Up Test")
    sales_agent.handle_response(lead_id, "yes")  # Consent
    sales_agent.handle_response(lead_id, "25")   # Answer age
    
    # Advance time by 25 hours
    with freeze_time("2023-01-02 13:00:00"):
        # This would normally happen in the background thread
        sales_agent.check_for_follow_ups()
        
        # Verify the lead is still in progress
        lead_data = sales_agent.data_handler.get_lead(lead_id)
        assert lead_data['status'] == 'in_progress'
    
    sales_agent.stop()