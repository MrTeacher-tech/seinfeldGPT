import re
import csv

def convert(script_text, output_file='dialogue_data.csv', unsupervised_txt_file='unsupervised_training.txt'):
    """
    Convert script text to CSV and plain text files.
    """
    def clean_text(text):
        # Remove parenthetical notes
        text = re.sub(r'\([^)]*\)', '', text)
        # Remove extra whitespaces
        return ' '.join(text.split()).strip()

    # Find where actual dialogue begins
    script_text = script_text.replace('\r', '')
    
    # Regex to find character dialogues
    dialogue_regex = re.compile(r'^\s*([A-Z]+)\n((?:(?!\n\s*[A-Z]+\n).)*)', re.MULTILINE | re.DOTALL)
    
    # Find all dialogues
    dialogues = dialogue_regex.findall(script_text)
    
    # Prepare data
    csv_data = []
    unsupervised_text = []
    
    for character, dialogue in dialogues:
        # Skip characters with names shorter than 3 characters
        if len(character) < 3:
            continue

        cleaned_dialogue = clean_text(dialogue)
        if cleaned_dialogue:
            
            
            csv_data.append([
                character, 
                cleaned_dialogue
            ])
            
            unsupervised_text.append(cleaned_dialogue)
    
    # Write CSV
    with open(output_file, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Character', 'Dialogue', 'Emotional_Context'])
        writer.writerows(csv_data)
    
    # Write unsupervised text
    with open(unsupervised_txt_file, 'a', encoding='utf-8') as f:
        f.write('\n\n'.join(unsupervised_text))
    
    #print(f"CSV saved to {output_file}")
    #print(f"Unsupervised text saved to {unsupervised_txt_file}")