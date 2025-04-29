# AI Sales Agent Console 🤖

A professional, interactive sales agent console powered by AI that helps manage and track sales leads efficiently. This application provides a modern, feature-rich interface for sales lead management with real-time analytics and secure data storage.

## 🌟 Features

- **Interactive AI Sales Agent**: Engages with potential customers in a natural, conversational manner
- **Professional Data Collection**: Gathers essential lead information systematically
- **Secure Data Storage**: Saves lead information in a structured CSV database
- **Real-time Analytics**: Provides instant insights and statistics about leads
- **Beautiful CLI Interface**: Modern, color-coded interface with progress bars and animations
- **Automated Lead Management**: Generates unique IDs and timestamps for each lead
- **Analytics Dashboard**: Visual representation of lead data with key metrics
- **Export Capabilities**: Saves analytics summaries and conversation histories

## 📋 Requirements

- Python 3.8 or higher
- Required packages (install via requirements.txt):
  - google-cloud-dialogflow-cx: For natural language processing and conversation handling
  - pandas: For data manipulation and analysis
  - python-dateutil: For advanced date handling
  - pytest: For unit testing
  - freezegun: For time-based testing
  - pytest-cov: For test coverage reporting
  - numpy: For numerical operations
  - scikit-learn: For data analytics
  - matplotlib: For data visualization
  - seaborn: For enhanced visualizations
  - colorama: For terminal color formatting
  - tabulate: For formatted table display

## 🚀 Quick Start

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd sales-agent
   ```

2. **Set Up Virtual Environment (Recommended)**
   ```bash
   python -m venv venv
   # On Windows
   .\venv\Scripts\activate
   # On Unix or MacOS
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**
   ```bash
   python main.py
   ```

## 📁 Project Structure and File Explanations

```
sales-agent/
├── agent/                     # Core AI agent functionality
│   ├── __init__.py           # Package initializer
│   ├── agent.py              # Main AI agent implementation
│   ├── data_handler.py       # Data processing utilities
│   ├── session_manager.py    # Conversation session management
│   └── utils.py              # Helper functions
├── simulations/              # Testing and simulation tools
│   ├── __init__.py          # Package initializer
│   ├── lead_simulator.py     # Lead generation simulator
│   └── time_utils.py        # Time manipulation utilities
├── tests/                    # Test suite
│   ├── __init__.py          # Package initializer
│   ├── test_agent.py        # Agent tests
│   ├── test_data_handler.py # Data handler tests
│   └── test_session_manager.py # Session tests
├── venv/                     # Virtual environment
├── .gitignore               # Git ignore rules
├── pyvenv.cfg               # Python venv configuration
├── conversation_[ID].txt    # Saved conversations
├── demo_leads.csv           # Sample lead data
├── lead_analytics_summary.txt # Analytics report
├── leads_database.csv       # Main leads storage
├── leads_interactive.csv    # Active session data
└── main.py                  # Application entry point
```

### Detailed File Descriptions

#### 1. `main.py`
The core application file that contains:
- `EnhancedSalesConsole` class: Main interface controller
  - Handles user interactions and data collection
  - Manages color schemes and display formatting
  - Processes lead information
  - Generates analytics and reports
  - Saves conversations and lead data
  - Implements input validation
  - Creates progress animations and visual feedback

Key Features:
- Color-coded interface using Colorama
- Input validation for all user data
- Progress bars and animations
- Real-time data preview
- Analytics dashboard
- Conversation history tracking
- Special offers display
- Secure data handling

#### 2. `requirements.txt`
Dependencies management file containing:
- All required Python packages
- Specific version numbers for compatibility
- Development and production dependencies

#### 3. `leads_database.csv`
Primary data storage file that:
- Stores all lead information in CSV format
- Contains structured columns for:
  - Lead ID: Unique identifier for each lead
  - Personal Information: Name, email, phone
  - Demographics: Age, location
  - Interest Data: Product interests, budget
  - Timeline: Purchase timeline
  - Source: Lead acquisition source
  - Timestamps: Creation and modification dates

#### 4. `agent/agent.py`
AI agent implementation file:
- Handles natural language processing
- Manages conversation flow
- Implements response generation
- Controls agent personality and behavior
- Handles context management
- Processes user intents
- Manages conversation state

#### 5. `agent/utils.py`
Utility functions file containing:
- Helper functions for data processing
- ID generation utilities
- Data validation functions
- File handling utilities
- Date and time utilities
- String formatting functions
- Error handling utilities

#### 6. `conversations/` Directory
Conversation storage directory that:
- Stores individual conversation files
- Names files using lead IDs
- Contains full conversation histories
- Includes timestamps and metadata
- Maintains conversation context
- Enables conversation recovery
- Facilitates analysis and reporting

## 💼 Features in Detail

### Lead Information Collection
- **Name and Contact Details**
  - Full name validation
  - Email format checking
  - Phone number verification
- **Age and Location**
  - Age range validation
  - Geographic location tracking
- **Product Interest Areas**
  - Multiple interest tracking
  - Priority ranking
- **Budget Range**
  - Predefined budget categories
  - Custom range options
- **Purchase Timeline**
  - Immediate to long-term tracking
  - Follow-up scheduling
- **Lead Source**
  - Marketing channel tracking
  - Referral source analysis

### Data Visualization
- **Professional Table Display**
  - Formatted using tabulate
  - Color-coded information
  - Sortable columns
- **Progress Indicators**
  - Real-time progress bars
  - Status animations
  - Completion indicators
- **Real-time Analytics**
  - Live data updates
  - Trend analysis
  - Performance metrics

### Analytics and Reporting
- **Lead Analytics**
  - Total lead count
  - Conversion rates
  - Source effectiveness
- **Customer Demographics**
  - Age distribution
  - Geographic spread
  - Interest patterns
- **Performance Metrics**
  - Response rates
  - Engagement levels
  - Conversion timeline

### Data Export Capabilities
- **CSV Database**
  - Structured data export
  - Regular backups
  - Data integrity checks
- **Analytics Summaries**
  - Periodic reports
  - Custom analytics
  - Trend analysis
- **Conversation Histories**
  - Complete interaction logs
  - Timeline tracking
  - Context preservation

## 🔧 Configuration

### Color Scheme Configuration
The application uses a modern color scheme customizable in `main.py`:
- **Primary Color (Blue)**: Main interface elements
- **Secondary Color (Magenta)**: Highlights and accents
- **Accent Color (Cyan)**: Special elements
- **Success Color (Green)**: Positive feedback
- **Error Color (Red)**: Warnings and errors
- **Info Color (White)**: General information

### Display Settings
Customizable display options:
- Terminal width adaptation
- Color intensity levels
- Animation speed
- Text formatting
- Table layouts
- Progress bar styles

## 📊 Database Structure

The `leads_database.csv` file structure:
- **Lead ID**: Unique identifier (auto-generated)
- **Full Name**: Customer's complete name
- **Email Address**: Valid email contact
- **Contact Number**: Formatted phone number
- **Age**: Validated age value
- **Location**: Geographic location
- **Interest Area**: Product/Service interest
- **Budget Range**: Financial capacity
- **Purchase Timeline**: Expected purchase window
- **Lead Source**: Acquisition channel
- **Registration Date**: Timestamp



## 📑 Complete Project Structure

```
sales-agent/
├── agent/                     # Core AI agent functionality
│   ├── __init__.py           # Package initializer
│   ├── agent.py              # Main AI agent implementation
│   ├── data_handler.py       # Data processing utilities
│   ├── session_manager.py    # Conversation session management
│   └── utils.py              # Helper functions
├── simulations/              # Testing and simulation tools
│   ├── __init__.py          # Package initializer
│   ├── lead_simulator.py     # Lead generation simulator
│   └── time_utils.py        # Time manipulation utilities
├── tests/                    # Test suite
│   ├── __init__.py          # Package initializer
│   ├── test_agent.py        # Agent tests
│   ├── test_data_handler.py # Data handler tests
│   └── test_session_manager.py # Session tests
├── venv/                     # Virtual environment
├── .gitignore               # Git ignore rules
├── pyvenv.cfg               # Python venv configuration
├── conversation_[ID].txt    # Saved conversations
├── demo_leads.csv           # Sample lead data
├── lead_analytics_summary.txt # Analytics report
├── leads_database.csv       # Main leads storage
├── leads_interactive.csv    # Active session data
└── main.py                  # Application entry point
```

## 📂 Detailed File & Directory Explanations

### 1. Agent Directory (`/agent/`)
Core AI functionality and data handling.

#### `__init__.py`
- Purpose: Initializes the agent package
- Usage: Automatically loaded when importing agent modules
- Common Issues: Import errors if missing
- Solution: Create if missing with proper imports

#### `agent.py`
- Purpose: Main AI agent implementation
- Key Features:
  - Natural language processing
  - Conversation flow management
  - Response generation
  - Context handling
- Common Issues:
  - Memory leaks in long conversations
  - Response delays
- Solutions:
  - Implement conversation cleanup
  - Add response caching
- Usage Example:
```python
from agent.agent import SalesAgent
agent = SalesAgent()
agent.start_conversation()
```

#### `data_handler.py`
- Purpose: Manages all data operations
- Features:
  - CSV file operations
  - Data validation
  - Error handling
  - Data transformation
- Common Issues:
  - File permission errors
  - Data corruption
- Solutions:
  - Implement file locking
  - Add data backups
- Usage Example:
```python
from agent.data_handler import DataHandler
handler = DataHandler()
handler.save_lead(lead_data)
```

#### `session_manager.py`
- Purpose: Manages conversation sessions
- Features:
  - Session creation/deletion
  - State management
  - Context preservation
- Common Issues:
  - Session timeouts
  - Memory overflow
- Solutions:
  - Implement session cleanup
  - Add session persistence
- Usage Example:
```python
from agent.session_manager import SessionManager
session = SessionManager()
session.create_new_session()
```

#### `utils.py`
- Purpose: Helper functions and utilities
- Features:
  - ID generation
  - Data validation
  - Time utilities
- Common Issues:
  - Duplicate IDs
  - Validation errors
- Solutions:
  - Implement UUID
  - Enhanced validation rules

### 2. Simulations Directory (`/simulations/`)
Testing and development tools.

#### `lead_simulator.py`
- Purpose: Generates test lead data
- Features:
  - Random lead generation
  - Scenario simulation
  - Load testing
- Usage Example:
```python
from simulations.lead_simulator import LeadSimulator
simulator = LeadSimulator()
test_leads = simulator.generate_leads(10)
```

#### `time_utils.py`
- Purpose: Time-related utilities
- Features:
  - Time manipulation
  - Date formatting
  - Timezone handling

### 3. Tests Directory (`/tests/`)
Comprehensive test suite.

#### `test_agent.py`
- Purpose: AI agent unit tests
- Coverage:
  - Conversation flow
  - Response generation
  - Error handling
- Running Tests:
```bash
pytest tests/test_agent.py -v
```

#### `test_data_handler.py`
- Purpose: Data operations tests
- Coverage:
  - File operations
  - Data validation
  - Error handling
- Running Tests:
```bash
pytest tests/test_data_handler.py -v
```

### 4. Data Files

#### `leads_database.csv`
- Purpose: Main lead storage
- Structure:
```csv
Lead ID,Name,Email,Phone,Age,Location,Interest,Budget,Timeline,Source,Date
UUID,Text,Email,Phone,Int,Text,Text,Enum,Enum,Text,DateTime
```
- Common Issues:
  - File locking
  - Corruption
- Solutions:
  - Regular backups
  - Transaction logging

#### `lead_analytics_summary.txt`
- Purpose: Analytics reports
- Content:
  - Lead statistics
  - Conversion rates
  - Performance metrics

## 🚀 Complete Setup Guide

### 1. Environment Setup
```bash
# Clone repository
git clone <repository-url>
cd sales-agent

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
.\venv\Scripts\activate
# Unix/MacOS:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Configuration
1. Copy `.env.example` to `.env`
2. Set required environment variables:
```env
AI_MODEL_KEY=your_key_here
DATABASE_PATH=./leads_database.csv
DEBUG_MODE=False
```

### 3. Database Initialization
```bash
python -c "from agent.data_handler import init_db; init_db()"
```

### 4. Running the Application
```bash
python main.py
```

## 🔧 Troubleshooting Guide

### Common Issues and Solutions

1. **Import Errors**
   - Issue: `ModuleNotFoundError`
   - Solution: 
     ```bash
     pip install -r requirements.txt
     ```

2. **Database Access Errors**
   - Issue: `PermissionError`
   - Solution:
     - Check file permissions
     - Close other applications
     - Run as administrator

3. **Memory Issues**
   - Issue: High memory usage
   - Solution:
     - Enable garbage collection
     - Implement session cleanup
     ```python
     import gc
     gc.collect()
     ```

4. **Performance Issues**
   - Issue: Slow response times
   - Solution:
     - Enable caching
     - Optimize database queries
     - Implement connection pooling

## 🔄 Maintenance and Updates

### Regular Maintenance Tasks
1. Database cleanup
```bash
python scripts/cleanup_db.py
```

2. Log rotation
```bash
python scripts/rotate_logs.py
```

3. Cache clearing
```bash
python scripts/clear_cache.py
```

### Update Procedure
1. Pull latest changes
```bash
git pull origin main
```

2. Update dependencies
```bash
pip install -r requirements.txt --upgrade
```

3. Run database migrations
```bash
python scripts/migrate_db.py
```

## 📊 Monitoring and Analytics

### Performance Monitoring
- CPU usage tracking
- Memory utilization
- Response time metrics
- Error rate monitoring

### Analytics Dashboard
- Lead conversion rates
- Agent performance metrics
- User engagement statistics
- System health indicators

## 🔒 Security Considerations

1. Data Protection
   - Encryption at rest
   - Secure file permissions
   - Regular security audits

2. Access Control
   - Role-based access
   - Session management
   - Authentication logging

3. Compliance
   - GDPR compliance
   - Data retention policies
   - Privacy protection

## 📈 Scaling Guidelines

1. Horizontal Scaling
   - Load balancing
   - Database sharding
   - Cache distribution

2. Vertical Scaling
   - Resource optimization
   - Performance tuning
   - Memory management
