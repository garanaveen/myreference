
import re
import sys
from datetime import datetime

# List of month abbreviations for parsing
MONTHS = {
    "Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04", "May": "05", 
    "Jun": "06", "Jul": "07", "Aug": "08", "Sep": "09", "Oct": "10", 
    "Nov": "11", "Dec": "12"
}

def convert_to_24_hour(time_str, am_pm):
    """Convert 12-hour time format to 24-hour."""
    time_format = "%I:%M"
    time_obj = datetime.strptime(time_str, time_format)
    if am_pm == "PM" and time_obj.hour != 12:
        time_obj = time_obj.replace(hour=time_obj.hour + 12)
    elif am_pm == "AM" and time_obj.hour == 12:
        time_obj = time_obj.replace(hour=0)
    return time_obj.strftime("%H:%M")

def convert_timestamp(line):
    """Convert a timestamp to the desired format."""
    
    # Pattern 1: Full date with time (e.g., "Thu 12 Sep 2024 04:22:31 PM CDT")
    match1 = re.match(r'^[A-Za-z]{3} (\d{2}) ([A-Za-z]{3}) (\d{4}) (\d{2}):(\d{2}):\d{2} (AM|PM)', line)
    if match1:
        day, month, year, hour, minute, am_pm = match1.groups()
        time_24hr = convert_to_24_hour(f"{hour}:{minute}", am_pm)
        return f"[{year}-{MONTHS[month]}-{day} {time_24hr}]"
    
    # Pattern 2: Short date with time (e.g., "28 Mar 2023 11:33:33 AM CDT")
    match2 = re.match(r'^(\d{2}) ([A-Za-z]{3}) (\d{4}) (\d{2}):(\d{2}):\d{2} (AM|PM)', line)
    if match2:
        day, month, year, hour, minute, am_pm = match2.groups()
        time_24hr = convert_to_24_hour(f"{hour}:{minute}", am_pm)
        return f"[{year}-{MONTHS[month]}-{day} {time_24hr}]"
    
    # Pattern 3: Date only (e.g., "26 Mar 2024")
    match3 = re.match(r'^(\d{2}) ([A-Za-z]{3}) (\d{4})', line)
    if match3:
        day, month, year = match3.groups()
        return f"[{year}-{MONTHS[month]}-{day} 09:00]"
    
    # Pattern 4: Date only, no spaces (e.g., "26MAR2024")
    match4 = re.match(r'^(\d{2})([A-Za-z]{3})(\d{4})', line)
    if match4:
        day, month, year = match4.groups()
        return f"[{year}-{MONTHS[month.capitalize()]}-{day} 09:00]"
    
    # If no timestamp is found, return None to indicate no change
    return None

def process_file(file_name):
    with open(file_name, 'r') as infile:
        lines = infile.readlines()
    
    with open(file_name, 'w') as outfile:
        for line in lines:
            # Check if we can convert the timestamp
            timestamp = convert_timestamp(line)
            if timestamp:
                new_line = line.replace(line[:len(timestamp)], timestamp, 1)
            else:
                new_line = line  # Leave line unchanged if no timestamp
            outfile.write(new_line)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <filename>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    process_file(input_file)

