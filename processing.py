import re

def preprocess_text(text):
    """
    Preprocesses the input text by standardizing punctuation, removing non-Bangla characters,
    and reducing consecutive spaces to a single space.

    Parameters:
        text (str): The input text to preprocess.
    
    Returns:
        str: The preprocessed text.
    """
    # Replace fancy quotes with standard ones
    text = re.sub(r"[‘’“”]", "'", text)
    # Remove non-Bangla characters except quotes and spaces
    text = re.sub(r"[^\u0980-\u09FF\s']", "", text)
    # Reduce consecutive spaces to a single space
    text = re.sub(r"\s+", " ", text).strip()
    return text

def preprocess_file(input_file, output_file):
    """
    Reads text from an input file, preprocesses it, and saves the output to another file.
    
    Parameters:
        input_file (str): Path to the input text file.
        output_file (str): Path to save the preprocessed text.
    """
    try:
        # Read the input text file
        with open(input_file, "r", encoding="utf-8") as file:
            raw_text = file.read()
        
        # Preprocess the text
        processed_text = preprocess_text(raw_text)
        
        # Save the preprocessed text to the output file
        with open(output_file, "w", encoding="utf-8") as file:
            file.write(processed_text)
        
        print(f"Preprocessed text has been saved to {output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    input_file = "consolidated_text.txt"  # Replace with your input text file
    output_file = "processed_consolidated_text.txt"  # Replace with your desired output file
    preprocess_file(input_file, output_file)
