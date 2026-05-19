from .loader import load_document
import re
import spacy

chunking_research = "https://www.geeksforgeeks.org/data-analysis/how-to-chunk-text-data-a-comparative-analysis/"

city_that_remembered_rain = "data/sample/the_city_that_remembered_rain.md"
the_library_at_the_edge_of_tomorrow = "data/sample/the_library_at_the_edge_of_tomorrow.txt"
the_lantern_archive_novel = "data/sample/the_lantern_archive_novel.pdf"
empty_novel = "data/sample/empty.txt"
broken_path = "hello"

def fix_sized_text_chunk(text: str, chunk_size: int) -> list[str]:
  
  """
  Divides text into pre-defined chunked size

  Args: 
    - text (str): text to be chunked
    - chunk_size (int): pre-defined chunk size

  Return: 
    - List of chunked size
  """

  # String are immutable
  chunked_text = []

  while len(text) > 0: 
    
    sliced_text = text[:chunk_size] # Get first chunk
    chunked_text.append(sliced_text) # Add them into chunked list
    text = text[chunk_size:] # Remove the first chunk and update to the text
  
  return chunked_text

def split_sentences_punctuation(text):
    """
    Splits text into sentences using punctuation marks.
    
    Parameters:
    text (str): The input text to be split.
    
    Returns:
    list: A list of sentences.
    """
    # Regular expression to split sentences based on punctuation marks
    sentences = re.split(r'(?<=[.!?]) +', text)
    return sentences

def split_sentences_spacy(text: str) -> list[str]:
    """
    Splits text into sentences using SpaCy NLP library.
    
    Parameters:
    text (str): The input text to be split.
    
    Returns:
    list: A list of sentences.
    """

    chunked_text = []
    # Load SpaCy's English model
    nlp = spacy.load('en_core_web_sm')
    
    # Process the text
    doc = nlp(text)
    
    # Extract sentences
    chunked_text = [sentence for sentence in doc.sents]
    return chunked_text

def recursive_chunk(text, max_size, level=0) -> str:
    """
    Recursively chunk the text into smaller parts using a set of separators.
    
    Parameters:
    text (str): The input text to be chunked.
    max_size (int): The maximum desired chunk size.
    level (int): The current recursion level (used for debugging purposes).
    
    Returns:
    list: A list of text chunks.
    """
    # Define separators for different levels of chunking
    separators = [r'(?<=[.!?]) +', r'\s+']  # Sentence level, word level

    if text <= max_size:
       return list[text]
    
    # Choose the appropriate seperators
    
    pass

if __name__ == "__main__":
  text = load_document(the_library_at_the_edge_of_tomorrow) 

  chunked_text = split_sentences_spacy(text)
  
  for i, chunk in enumerate(chunked_text):
     print(f"Chunk {i + 1}\n{chunk}\n")
  


