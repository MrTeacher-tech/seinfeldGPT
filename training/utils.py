import re
from typing import Optional

def clean_text(text: str) -> str:
    """
    Clean and normalize script text
    """
    if not text:
        return ""
        
    # Remove multiple consecutive newlines
    text = re.sub(r'\n{3,}', '\n\n', text)
    
    # Remove multiple spaces
    text = re.sub(r'\s+', ' ', text)
    
    # Normalize character name separators
    text = re.sub(r'\s*:\s*', ':', text)
    
    return text.strip()

def validate_input(text: str) -> bool:
    """
    Validate script text format
    Returns True if the text contains at least one valid character-dialogue pair
    """
    if not text or not isinstance(text, str):
        return False
        
    # Check for at least one character name in caps followed by dialogue
    basic_pattern = r'[A-Z][A-Z\s]+:.+'
    return bool(re.search(basic_pattern, text))

def extract_character_name(line: str) -> Optional[str]:
    """
    Extract character name from a line of text
    Returns None if no valid character name is found
    """
    match = re.match(r'^([A-Z][A-Z\s]+):', line)
    return match.group(1).strip() if match else None
