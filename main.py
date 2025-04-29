# Updated main.py
from agent.agent import SalesAgent
from agent.utils import generate_lead_id
import time
from datetime import datetime
import sys
from typing import Dict, List, Tuple
import re
from colorama import init, Fore, Style, Back
import os
import random
import csv
import pandas as pd

# Initialize colorama for Windows
init()

class EnhancedSalesConsole:
    def __init__(self):
        self.agent = SalesAgent(data_file='leads_interactive.csv')
        self.conversation_history: Dict[str, List[str]] = {}
        self.agent_name = "SalesMind A"
        self.company_name = "TechSolutions"
        self.emoji_reactions = ["★", "⭐", "✧", "➤", "•", "→", "✓", "✔", "♦", "◆"]
        self.leads_file = 'leads_database.csv'
        
        # Modern color scheme
        self.primary_color = Back.BLUE
        self.secondary_color = Back.MAGENTA
        self.accent_color = Back.CYAN
        self.success_color = Back.GREEN
        self.error_color = Back.RED
        self.info_color = Back.WHITE
        
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        
    def print_header(self):
        self.clear_screen()
        # Modern gradient-like header
        print(f"\n{self.primary_color}{Fore.WHITE}{'═' * 70}{Style.RESET_ALL}")
        print(f"{self.secondary_color}{Fore.WHITE}{'═' * 70}{Style.RESET_ALL}")
        print(f"{self.accent_color}{Fore.WHITE}{'═' * 70}{Style.RESET_ALL}")
        print(f"{self.primary_color}{Fore.WHITE}{'╔' + '═' * 68 + '╗'}{Style.RESET_ALL}")
        print(f"{self.primary_color}{Fore.WHITE}║{' ' * 68}║{Style.RESET_ALL}")
        print(f"{self.primary_color}{Fore.WHITE}║{('Welcome to ' + self.company_name).center(68)}║{Style.RESET_ALL}")
        print(f"{self.primary_color}{Fore.WHITE}║{' ' * 68}║{Style.RESET_ALL}")
        print(f"{self.primary_color}{Fore.WHITE}║{'Your Personal AI Sales Assistant'.center(68)}║{Style.RESET_ALL}")
        print(f"{self.primary_color}{Fore.WHITE}║{' ' * 68}║{Style.RESET_ALL}")
        print(f"{self.primary_color}{Fore.WHITE}╚{'═' * 68 + '╝'}{Style.RESET_ALL}")
        print(f"{self.accent_color}{Fore.WHITE}{'═' * 70}{Style.RESET_ALL}")
        print(f"{self.secondary_color}{Fore.WHITE}{'═' * 70}{Style.RESET_ALL}")
        print(f"{self.primary_color}{Fore.WHITE}{'═' * 70}{Style.RESET_ALL}\n")
        
    def print_typing_animation(self):
        dots = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
        for frame in dots:
            sys.stdout.write(f"\r{self.info_color}{Fore.BLACK} {frame} Typing... {Style.RESET_ALL}")
            sys.stdout.flush()
            time.sleep(0.1)
        print("\r" + " " * 30 + "\r", end="")
        
    def get_random_emoji(self):
        return random.choice(self.emoji_reactions)
        
    def format_message(self, sender: str, message: str, is_system: bool = False) -> str:
        timestamp = datetime.now().strftime("%H:%M")
        emoji = self.get_random_emoji()
        if is_system:
            return f"{self.info_color}{Fore.BLACK} SYSTEM {Style.RESET_ALL} {self.accent_color}{Fore.WHITE} {message} {Style.RESET_ALL}"
        elif sender == "Agent":
            return f"{self.primary_color}{Fore.WHITE} {timestamp} {Style.RESET_ALL} {self.secondary_color}{Fore.WHITE} {self.agent_name} {emoji} {Style.RESET_ALL} {message}"
        else:
            return f"{self.info_color}{Fore.BLACK} {timestamp} You {Style.RESET_ALL} {message}"
            
    def validate_input(self, input_str: str, input_type: str) -> Tuple[bool, str]:
        if input_type == "email":
            email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
            return bool(re.match(email_pattern, input_str)), "Please enter a valid email address"
        elif input_type == "phone":
            phone_pattern = r'^\+?1?\d{9,15}$'
            return bool(re.match(phone_pattern, input_str)), "Please enter a valid phone number"
        elif input_type == "age":
            try:
                age = int(input_str)
                return 18 <= age <= 120, "Please enter a valid age between 18 and 120"
            except ValueError:
                return False, "Please enter a valid number for age"
        elif input_type == "name":
            return len(input_str.strip()) > 0, "Name cannot be empty"
        elif input_type == "country":
            return len(input_str.strip()) >= 2, "Please enter a valid country name"
        elif input_type == "budget":
            return input_str.upper() in ['A', 'B', 'C'], "Please select A, B, or C for budget range"
        elif input_type == "timeline":
            return input_str.upper() in ['A', 'B', 'C', 'D'], "Please select A, B, C, or D for timeline"
        return True, ""
            
    def show_progress_bar(self, message):
        print(f"\n{self.info_color}{Fore.BLACK} {message}... {Style.RESET_ALL}")
        width = 40
        for i in range(width + 1):
            progress = "■" * i + "□" * (width - i)
            percentage = i * 100 // width
            bar = f"{self.primary_color}{Fore.WHITE} [{progress}] {percentage}% {Style.RESET_ALL}"
            sys.stdout.write(f"\r{bar}")
            sys.stdout.flush()
            time.sleep(0.02)
        print(f"\n{self.success_color}{Fore.WHITE} ✓ Completed {Style.RESET_ALL}\n")

    def print_section_header(self, title: str):
        print(f"\n{self.secondary_color}{Fore.WHITE} {title.center(68)} {Style.RESET_ALL}")
        print(f"{self.accent_color}{Fore.WHITE}{'─' * 70}{Style.RESET_ALL}\n")

    def get_validated_input(self, prompt: str, input_type: str) -> str:
        while True:
            self.print_typing_animation()
            user_input = input(f"{self.info_color}{Fore.BLACK} {prompt}: {Style.RESET_ALL} ").strip()
            is_valid, error_message = self.validate_input(user_input, input_type)
            if is_valid:
                print(f"{self.success_color}{Fore.WHITE} ✓ {Style.RESET_ALL}")
                return user_input
            print(f"{self.error_color}{Fore.WHITE} ✗ {error_message} {Style.RESET_ALL}")

    def print_special_offer(self, title: str, items: List[str]):
        print(f"\n{self.secondary_color}{Fore.WHITE} {title} {Style.RESET_ALL}")
        for item in items:
            print(f"{self.accent_color}{Fore.WHITE} • {item} {Style.RESET_ALL}")

    def save_conversation(self, lead_name: str, lead_id: str):
        try:
            with open(f'conversation_{lead_id}.txt', 'w', encoding='utf-8') as f:
                f.write(f"Conversation with {lead_name} (ID: {lead_id})\n")
                f.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write("═"*50 + "\n\n")
                for question, answer in self.conversation_history[lead_id]:
                    f.write(f"Q: {question}\nA: {answer}\n\n")
        except Exception as e:
            print(f"{self.error_color}{Fore.WHITE} Error saving conversation: {str(e)} {Style.RESET_ALL}")

    def save_to_csv(self, lead_data: dict):
        try:
            # Define CSV headers
            headers = [
                'Lead ID', 'Name', 'Email', 'Phone', 'Age', 'Country',
                'Interest', 'Budget', 'Timeline', 'Source', 'Date Created'
            ]
            
            # Check if file exists
            file_exists = os.path.isfile(self.leads_file)
            
            # Write to CSV
            with open(self.leads_file, mode='a', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=headers)
                
                # Write headers if file doesn't exist
                if not file_exists:
                    writer.writeheader()
                
                # Write lead data
                writer.writerow(lead_data)
            
            # Show success message with file preview
            self.show_csv_preview()
            
        except Exception as e:
            print(f"{self.error_color}{Fore.WHITE} Error saving to CSV: {str(e)} {Style.RESET_ALL}")

    def show_csv_preview(self):
        try:
            # Read the CSV file
            df = pd.read_csv(self.leads_file)
            
            # Format the data
            df['Date Created'] = pd.to_datetime(df['Date Created']).dt.strftime('%Y-%m-%d %H:%M')
            df['Lead ID'] = df['Lead ID'].str[-8:]  # Show only last 8 characters
            
            # Map budget and timeline to readable format
            budget_map = {'a': 'Under $1000', 'b': '$1000-$5000', 'c': 'Above $5000'}
            timeline_map = {'a': 'Immediate', 'b': '1 Month', 'c': '3 Months', 'd': 'Exploring'}
            df['Budget'] = df['Budget'].map(budget_map)
            df['Timeline'] = df['Timeline'].map(timeline_map)
            
            # Print preview
            self.print_section_header("📊 Sales Leads Dashboard")
            print(f"{self.accent_color}{Fore.WHITE}{'═' * 100}{Style.RESET_ALL}")
            
            # Format headers
            headers = {
                'Lead ID': 'ID',
                'Name': 'Full Name',
                'Email': 'Email Address',
                'Phone': 'Contact Number',
                'Age': 'Age',
                'Country': 'Location',
                'Interest': 'Interest Area',
                'Budget': 'Budget Range',
                'Timeline': 'Purchase Timeline',
                'Source': 'Lead Source',
                'Date Created': 'Registration Date'
            }
            df = df.rename(columns=headers)
            
            # Print statistics
            total_leads = len(df)
            recent_leads = len(df.tail(5))
            print(f"\n{self.info_color}{Fore.BLACK} Database Summary:{Style.RESET_ALL}")
            print(f"{self.primary_color}{Fore.WHITE} • Total Leads: {total_leads}{Style.RESET_ALL}")
            print(f"{self.primary_color}{Fore.WHITE} • Showing Latest: {recent_leads}{Style.RESET_ALL}\n")
            
            # Create styled header
            print(f"{self.secondary_color}{Fore.WHITE}{'Recent Lead Entries':^100}{Style.RESET_ALL}")
            print(f"{self.accent_color}{Fore.WHITE}{'─' * 100}{Style.RESET_ALL}\n")
            
            # Format and display the table
            pd.set_option('display.max_columns', None)
            pd.set_option('display.width', 100)
            pd.set_option('display.max_rows', 5)
            pd.set_option('display.colheader_justify', 'center')
            
            # Print the styled table
            latest_entries = df.tail(5)
            
            # Print headers
            header_line = ""
            for col in latest_entries.columns:
                header_line += f"{col:^20} "
            print(f"{self.primary_color}{Fore.WHITE}{header_line.strip()}{Style.RESET_ALL}")
            print(f"{self.info_color}{Fore.BLACK}{'═' * 100}{Style.RESET_ALL}")
            
            # Print data rows
            for _, row in latest_entries.iterrows():
                data_line = ""
                for value in row:
                    data_line += f"{str(value):^20} "
                print(f"{self.info_color}{Fore.BLACK}{data_line.strip()}{Style.RESET_ALL}")
            
            print(f"{self.info_color}{Fore.BLACK}{'═' * 100}{Style.RESET_ALL}")
            
            # Print analytics
            if not df.empty:
                print(f"\n{self.secondary_color}{Fore.WHITE}{'Lead Analytics':^100}{Style.RESET_ALL}")
                print(f"{self.accent_color}{Fore.WHITE}{'─' * 100}{Style.RESET_ALL}")
                
                print(f"\n{self.info_color}{Fore.BLACK}Key Metrics:{Style.RESET_ALL}")
                print(f"{self.primary_color}{Fore.WHITE} • Most Active Source: {df['Lead Source'].mode().iloc[0]}{Style.RESET_ALL}")
                print(f"{self.primary_color}{Fore.WHITE} • Average Customer Age: {df['Age'].mean():.0f} years{Style.RESET_ALL}")
                print(f"{self.primary_color}{Fore.WHITE} • Popular Interest Area: {df['Interest Area'].mode().iloc[0]}{Style.RESET_ALL}")
                print(f"{self.primary_color}{Fore.WHITE} • Common Budget Range: {df['Budget Range'].mode().iloc[0]}{Style.RESET_ALL}")
                
                # Save summary to file
                summary_file = 'lead_analytics_summary.txt'
                with open(summary_file, 'w', encoding='utf-8') as f:
                    f.write(f"Sales Lead Analytics Summary\n")
                    f.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                    f.write("="*50 + "\n\n")
                    f.write(f"Total Leads: {total_leads}\n")
                    f.write(f"Most Active Source: {df['Lead Source'].mode().iloc[0]}\n")
                    f.write(f"Average Customer Age: {df['Age'].mean():.0f} years\n")
                    f.write(f"Popular Interest Area: {df['Interest Area'].mode().iloc[0]}\n")
                    f.write(f"Common Budget Range: {df['Budget Range'].mode().iloc[0]}\n")
            
            print(f"\n{self.success_color}{Fore.WHITE} ✓ Database updated successfully{Style.RESET_ALL}")
            print(f"{self.success_color}{Fore.WHITE} ✓ Analytics summary saved to {summary_file}{Style.RESET_ALL}\n")
            
        except Exception as e:
            print(f"{self.error_color}{Fore.WHITE} Error showing CSV preview: {str(e)} {Style.RESET_ALL}")

    def start_conversation(self):
        self.agent.start()
        self.print_header()
        
        # Animated welcome
        self.show_progress_bar("Initializing AI Assistant")
        print(self.format_message("Agent", "Welcome! I'm your personal AI sales assistant!"))
        time.sleep(1)
        
        # Get user information with enhanced validation
        self.print_section_header("Personal Information")
        lead_name = self.get_validated_input("What's your name", "name")
        lead_id = generate_lead_id()
        self.conversation_history[lead_id] = []
        
        print(self.format_message("System", "Starting secure chat session..."))
        self.show_progress_bar("Establishing secure connection")
        
        # Enhanced Q&A Session with categories
        self.print_section_header("Let's Get to Know You Better")
        print(self.format_message("Agent", f"Great to meet you, {lead_name}! Let's find the perfect solution for you!"))
        
        questions = [
            ("Your email address for product information", "email"),
            ("Best phone number to reach you", "phone"),
            ("Your age", "age"),
            ("Your country", "country"),
            ("Products or services you're interested in", "interest"),
            ("Preferred budget range\n" +
             f"{self.info_color}{Fore.BLACK} A) Under $1000\n B) $1000-$5000\n C) Above $5000 {Style.RESET_ALL}", "budget"),
            ("Purchase timeline\n" +
             f"{self.info_color}{Fore.BLACK} A) Immediately\n B) Within 1 month\n C) Within 3 months\n D) Just exploring {Style.RESET_ALL}", "timeline"),
            ("How did you hear about us", "source")
        ]
        
        responses = {}
        for question, q_type in questions:
            print(self.format_message("Agent", question))
            answer = self.get_validated_input("", q_type)
            responses[q_type] = answer
            self.conversation_history[lead_id].append((question, answer))
            time.sleep(0.5)
            
        # Save lead information to CSV
        lead_data = {
            'Lead ID': lead_id,
            'Name': lead_name,
            'Email': responses['email'],
            'Phone': responses['phone'],
            'Age': responses['age'],
            'Country': responses['country'],
            'Interest': responses['interest'],
            'Budget': responses['budget'],
            'Timeline': responses['timeline'],
            'Source': responses['source'],
            'Date Created': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
        # Save to CSV and show progress
        self.show_progress_bar("Saving your information")
        self.save_to_csv(lead_data)
            
        # Personalized recommendations
        self.print_section_header("Personalized Recommendations")
        print(self.format_message("Agent", f"Thanks {lead_name}! I've prepared some recommendations for you!"))
        self.show_progress_bar("Analyzing your preferences")
        
        # Special Offers
        self.print_special_offer("🎉 Special Offers Just for You!", [
            "15% OFF on your first purchase",
            "Free consultation session",
            "Exclusive bonus package",
            "Priority support access"
        ])
        
        # Refund Policy
        self.print_special_offer("💎 Our Guarantee", [
            "30-day money-back guarantee",
            "No questions asked returns",
            "100% satisfaction guaranteed",
            "24/7 customer support"
        ])
        
        # Next Steps
        self.print_section_header("Next Steps")
        next_steps = [
            "Detailed Product Information",
            "Exclusive Pricing Details",
            "Getting Started Guide",
            "Personalized Recommendations",
            "Free Consultation Schedule"
        ]
        for step in next_steps:
            print(self.format_message("System", f"✓ {step}"))
            time.sleep(0.3)
        
        # Final Questions
        self.print_section_header("Any Questions?")
        print(self.format_message("Agent", "Before we wrap up, do you have any questions? (yes/no)"))
        has_questions = input(f"{self.info_color}{Fore.BLACK} Your response: {Style.RESET_ALL} ").lower().strip()
        
        if has_questions in ['yes', 'y']:
            print(self.format_message("Agent", "I'm here to help! What would you like to know?"))
            question = input(f"{self.info_color}{Fore.BLACK} Your question: {Style.RESET_ALL} ").strip()
            print(self.format_message("Agent", "Thank you for your question! Our product specialist will provide detailed information in the follow-up email."))
        
        # Save conversation and farewell
        self.save_conversation(lead_name, lead_id)
        self.show_progress_bar("Preparing your personalized package")
        
        self.print_section_header("Thank You!")
        print(self.format_message("Agent", f"Thank you for choosing {self.company_name}, {lead_name}!"))
        print(self.format_message("Agent", "You'll receive your personalized package shortly!"))
        self.agent.stop()

def main():
    try:
        console = EnhancedSalesConsole()
        console.start_conversation()
    except KeyboardInterrupt:
        print(f"\n{Back.RED}{Fore.WHITE} Session terminated by user. {Style.RESET_ALL}")
        sys.exit(0)
    except Exception as e:
        print(f"\n{Back.RED}{Fore.WHITE} An error occurred: {str(e)} {Style.RESET_ALL}")
        sys.exit(1)

if __name__ == "__main__":
    main()