from bs4 import BeautifulSoup
import pandas as pd

# Load the HTML content. Change path
with open(r"change_to_path.html", "r", encoding="utf-8") as file:
    html_content = file.read()

# Parse the HTML with BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Assuming the data is inside div tags (adjust as needed)
data = []
for item in soup.find_all('div', class_="_2ph_ _a6-h _a6-i"):
    full_name = item.text.strip().split()
    first_name = full_name[0] if full_name else ''
    last_name = full_name[-1] if len(full_name) > 1 else ''
    middle_name = ' '.join(full_name[1:-1]) if len(full_name) > 2 else ''
    date_div = item.find_next('div', class_="_a72d")
    date_time = date_div.text.strip() if date_div else 'Unknown'
    data.append({
        'First Name': first_name,
        'Middle Name': middle_name,
        'Last Name': last_name,
        'DateTime': date_time
    })

# Convert the list of dictionaries into a pandas DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file. Set path.
csv_file_path = r"your_path.csv"
df.to_csv(csv_file_path, index=False)