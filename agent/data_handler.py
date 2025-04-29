import csv
import os
from typing import Dict, Optional, List
import pandas as pd

class DataHandler:
    def __init__(self, file_path: str = 'leads.csv'):
        self.file_path = file_path
        self._ensure_file_exists()

    def _ensure_file_exists(self):
        """Ensure the CSV file exists with the correct headers."""
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([
                    'lead_id', 'name', 'age', 'country', 
                    'interest', 'status', 'last_updated'
                ])

    def add_lead(self, lead_id: str, name: str) -> bool:
        """Add a new lead with initial information."""
        if not lead_id or not name:
            return False
        
        df = self._read_data()
        
        if lead_id in df['lead_id'].values:
            return False
        
        new_data = {
            'lead_id': [lead_id],
            'name': [name],
            'age': [None],
            'country': [None],
            'interest': [None],
            'status': ['pending'],
            'last_updated': [pd.Timestamp.now()]
        }
        
        new_df = pd.DataFrame(new_data)
        df = pd.concat([df, new_df], ignore_index=True)
        self._write_data(df)
        return True

    def update_lead(self, lead_id: str, updates: Dict[str, str]) -> bool:
        """Update lead information."""
        if not lead_id or not updates:
            return False
        
        df = self._read_data()
        
        if lead_id not in df['lead_id'].values:
            return False
        
        for column, value in updates.items():
            if column in df.columns:
                df.loc[df['lead_id'] == lead_id, column] = value
        
        # Always update the timestamp
        df.loc[df['lead_id'] == lead_id, 'last_updated'] = pd.Timestamp.now()
        
        self._write_data(df)
        return True

    def get_lead(self, lead_id: str) -> Optional[Dict[str, str]]:
        """Get lead information."""
        if not lead_id:
            return None
        
        df = self._read_data()
        lead_data = df[df['lead_id'] == lead_id]
        
        if lead_data.empty:
            return None
        
        return lead_data.iloc[0].to_dict()

    def get_all_leads(self) -> Dict[str, Dict[str, str]]:
        """Get all leads information."""
        df = self._read_data()
        return {row['lead_id']: row.to_dict() for _, row in df.iterrows()}

    def _read_data(self) -> pd.DataFrame:
        """Read the CSV data."""
        return pd.read_csv(self.file_path)

    def _write_data(self, df: pd.DataFrame):
        """Write data to CSV."""
        df.to_csv(self.file_path, index=False)