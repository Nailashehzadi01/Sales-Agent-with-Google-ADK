import pytest
import pandas as pd
import os
from datetime import datetime
from agent.data_handler import DataHandler

@pytest.fixture
def data_handler(tmp_path):
    data_file = tmp_path / "test_data.csv"
    handler = DataHandler(file_path=str(data_file))
    yield handler
    if os.path.exists(data_file):
        os.remove(data_file)

def test_data_handler_initialization(data_handler):
    assert os.path.exists(data_handler.file_path)
    
    # Verify headers were created
    df = pd.read_csv(data_handler.file_path)
    expected_columns = [
        'lead_id', 'name', 'age', 'country', 
        'interest', 'status', 'last_updated'
    ]
    assert all(col in df.columns for col in expected_columns)

def test_add_lead(data_handler):
    lead_id = "test_123"
    name = "Test User"
    
    assert data_handler.add_lead(lead_id, name)
    assert not data_handler.add_lead(lead_id, name)  # Duplicate
    
    lead_data = data_handler.get_lead(lead_id)
    assert lead_data['name'] == name
    assert lead_data['status'] == 'pending'
    assert pd.isna(lead_data['age'])

def test_update_lead(data_handler):
    lead_id = "test_456"
    name = "Update Test"
    data_handler.add_lead(lead_id, name)
    
    updates = {
        'age': '30',
        'country': 'USA',
        'status': 'in_progress'
    }
    assert data_handler.update_lead(lead_id, updates)
    
    lead_data = data_handler.get_lead(lead_id)
    assert lead_data['age'] == '30'
    assert lead_data['country'] == 'USA'
    assert lead_data['status'] == 'in_progress'
    assert pd.notna(lead_data['last_updated'])

def test_get_all_leads(data_handler):
    leads = {
        "lead_1": "User One",
        "lead_2": "User Two"
    }
    
    for lead_id, name in leads.items():
        data_handler.add_lead(lead_id, name)
    
    all_leads = data_handler.get_all_leads()
    assert len(all_leads) == 2
    assert all_leads["lead_1"]['name'] == "User One"
    assert all_leads["lead_2"]['name'] == "User Two"