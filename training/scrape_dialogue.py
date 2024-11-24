from bs4 import BeautifulSoup
import requests
import imsdb_clean as imsdb
import re
import script_to_data

FILE = 'dialogue.txt'   #text will be saved to this file





#GET AND CLEAN URLS
raw_links = imsdb.get_urls_with_target("https://imsdb.com/TV/Seinfeld.html", "seinfeld")
links_TV_Script_T = imsdb.replace_spaces_with_hyphen(raw_links)   #ads cause links to return with " " instead of - like they should for this site
links_Script_T = imsdb.remove_from_urls(links_TV_Script_T, "TV-")   #remove random bs
links_T = imsdb.remove_from_urls(links_Script_T, "-Script")         #remove random bs
links = imsdb.replace_txt_in_urls(links_T, "Transcripts", "transcripts")



for link in links:
    
    url = "https://imsdb.com" + link.strip()
    print("URL:", url)
    # Fetch the webpage content
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        
        script_text = soup.get_text()
        
        #print(clean_text[:10000])
        

        # Replace newlines and multiple spaces with a single space
        #single_line_text = " ".join(clean_text.split())

        # Print the single-line text
        #print(single_line_text)
        # Path to your text file
        
        

        # Pass your text to parse
        
        script_to_data.convert(script_text)

        

        
    else:
        print(f"Failed to fetch webpage: {response.status_code}")