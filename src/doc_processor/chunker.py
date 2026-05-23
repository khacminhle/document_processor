from .loader import load_document
import re
import spacy

chunking_research = "https://www.geeksforgeeks.org/data-analysis/how-to-chunk-text-data-a-comparative-analysis/"

city_that_remembered_rain = "data/sample/the_city_that_remembered_rain.md"
the_library_at_the_edge_of_tomorrow = "data/sample/the_library_at_the_edge_of_tomorrow.txt"
the_lantern_archive_novel = "data/sample/the_lantern_archive_novel.pdf"
empty_novel = "data/sample/empty.txt"
broken_path = "hello"
sample_text = """
# Project Alpha Report

## Executive Summary

Project Alpha is designed to process mixed-format documents and split them into semantically useful chunks. The system should preserve important structure while avoiding chunks that are too large for downstream embedding models.

This paragraph is intentionally a little longer. It contains multiple sentences, related ideas, and enough length to test whether the chunker prefers splitting at paragraph or sentence boundaries before falling back to smaller separators. Ideally, this entire paragraph should remain together unless the configured chunk size forces a split.

## Requirements

The chunker should support:

- Markdown headings
- Paragraph boundaries
- Bullet lists
- Numbered lists
- Code blocks
- Very long sentences
- Short isolated lines

1. First, the document is loaded.
2. Then metadata is extracted.
3. After that, the text is recursively split.
4. Finally, chunks are emitted with source references.
"""


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

  text = (
    "Recursive chunking divides the text hierarchically using a set of separators. "
    "If the initial chunks are too large, the method recursively splits them until "
    "the desired size is achieved. This technique is useful for processing large "
    "texts where simpler chunking methods may fail. Let's see how it works.")
  chunks = recursive_chunk(text, max_size=100)
  print(chunks)
  for i, chunk in enumerate(chunks): 
     print(f"Chunk{i + 1}:\n{chunk}\n")

  

  
  
  
  


