from pathlib import Path
import asyncio
import re
import spacy
import logging 
from doc_processor.loader import load_document

# Initialise logging
logger = logging.getLogger(__name__)
nlp = spacy.load('en_core_web_sm') # Load sentences splitting model

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
  
  # Raise exception if chunk overlap is bigger than chunk size 
  if chunk_size < 0 or chunk_overlap < 0: 
     raise ValueError(f"Chunk size and chunk overlap must be greater than 0")
  if not isinstance(chunk_size, int) or not isinstance(chunk_overlap, int): 
     raise TypeError(f"Incorrect input type for chunk size and chunk overlap")
  

  # Split words
  logger.info(f"Splitting content: {text[:30]}..")
  word_splits = word_splitter(text)
  text_chunks = []
  counter = 0 # Use this for chunk id
  
  # Start chunking process
  logger.info("Starting chunking process")
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

  total_chunks = len(text_chunks) #Calculate total number of chunked text
  logger.info(f"Chunked {total_chunks}")
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
    clean_text = text.replace("\n\n", " ").replace("\n", " ")

    chunked_text = []
    # Load SpaCy's English model
    
    # Process the text
    doc = nlp(clean_text)

    # Extract sentences
    chunked_text = [sentence for sentence in doc.sents]
    return chunked_text

def split_text_with_overlap(text: str, chunk_size: int, overlap: int):

   def word_splitter(text: str): 
      text_chunks = re.split(r'\s+', text)
      return text_chunks 
   
   chunk_text = [] 
   text_splits = word_splitter(text)

   for i in range(0, len(text_splits), chunk_size):
     chunk = text_splits[max(i - overlap, 0): chunk_size + i]
     chunk_text.append(" ".join(chunk))

   return chunk_text
      


def recursive_chunk_retired(text: str, max_size:int, level=0) -> str:
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
         current_chunk = recursive_chunk_retired(chunk, max_size, level)
         final_chunks.extend(current_chunk)
      else:
         final_chunks.append(chunk)

    return final_chunks



async def main() -> None:
   doc_file_path = "data/sample/short_story_testing.md"
   text = await load_document(doc_file_path)
   
   
   # chunks = fixed_text_chunk_with_overlap(text["content"], chunk_size=100, chunk_overlap=20)
   # chunks = split_sentences_spacy(text["content"])
   chunks = split_text_with_overlap(text["content"], chunk_size=20, overlap=5)
   print(chunks[0])
   
   
if __name__ == "__main__":
   asyncio.run(main())


  
  
  
  

