import requests
from bs4 import BeautifulSoup
import pandas as pd

# Function to scrape bard spells from the given URL
def scrape_bard_spells(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    spell_levels = soup.find('div', class_='yui-content').find_all('div')
    
    data = []
    headers = ['Spell Name', 'School', 'Casting Time', 'Range', 'Duration', 'Components']

    for level in spell_levels:
        table = level.find('table')
        if not table:
            continue
        
        # Get all rows in the table
        rows = table.find_all('tr')

        # Extract data from the rest of the rows
        for row in rows[1:]:
            cols = row.find_all('td')
            cols = [col.text.strip() for col in cols]
            if len(cols) < 7:
                cols.append('')
            data.append(cols)           

    # Create a DataFrame from the data
    df = pd.DataFrame(data, columns=headers)
    return df

# URL of the bard spells page
url = "http://dnd5e.wikidot.com/spells:bard"

# Scrape the data
bard_spells_df = scrape_bard_spells(url)

# Save the data to a CSV file
csv_file_path = "bard_spells.csv"
bard_spells_df.to_csv(csv_file_path, index=False)

print(f"Data saved to {csv_file_path}")
