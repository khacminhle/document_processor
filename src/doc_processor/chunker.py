from .loader import load_document
import re
import spacy

def fixed_text_chunk_with_overlap(text: str, chunk_size: int, chunk_overlap: int) -> list[dict]:

  
  """
  Divides text into pre-defined chunked size

  Args: 
    - text (str): text to be chunked
    - chunk_size (int): pre-defined chunk size

  Return: 
    - List of chunked size
  """

  def word_splitter(text: str) -> list[str]: 
     word_splits = re.split(r'\s+', text)
     return word_splits
  
  word_splits = word_splitter(text)
  text_chunks = []
  counter = 0 # Use this for chunk id
  for i in range(0, len(word_splits), chunk_size):
     
     counter += 1 # Increase counter

     # Chunking process
     chunk = word_splits[max(i - chunk_overlap, 0): chunk_size + i]
     word_concat = " ".join(chunk) # Join word together
     char_count = len(word_concat) # char count
     
     text_chunks.append(
        {
           "chunk_id": counter, 
           "text": word_concat, 
           "char_count": char_count
        }
     )

  return text_chunks 

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

def recursive_chunk(text: str, max_size:int, level=0) -> str:
    """
    Recursively chunk the text into smaller parts using a set of separators.
    
    Parameters:
    text (str): The input text to be chunked.
    max_size (int): The maximum desired chunk size.
    level (int): The current recursion level (used for debugging purposes).
    
    Returns:
    list: A list of text chunks.
    """

    # If text is already smaller than max size
    # return it
    if len(text) <= (max_size):
       return list[text]
    
    # Define separators for different levels of chunking
    separators = [r'(?<=[.!?]) +', r'\s+']  # Sentence level, word level

    # Select the appropriate separator based on the recursion level
    separator = separators[min(level, len(separators) - 1)]
    
    chunks = re.split(separator, text) # Return list [chunked]
    
    final_chunks = []
    current_chunk = ""

    for chunk in chunks: 
      if len(chunk) >= max_size:
         level += 1
         current_chunk = recursive_chunk(chunk, max_size, level)
         final_chunks.extend(current_chunk)
      else:
         final_chunks.append(chunk)

    return final_chunks

if __name__ == "__main__":
   doc_file_path = "data/sample/the_city_that_remembered_rain.md"
   text = load_document(doc_file_path)
   print(text["content"])
   chunks = fixed_text_chunk_with_overlap(text["content"], chunk_size=100, chunk_overlap=20)
   print(chunks)


  
  
  
  


