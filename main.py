from src.doc_processor.loader import load_document
from src.doc_processor.metadata import extract_metadata
from src.doc_processor.chunker import fixed_text_chunk_with_overlap
from pprint import pprint

def process_document(path) -> dict: 

  data = {}

  document = load_document(path) # Return dict of content and metadata
  metadata = extract_metadata(document["content"]) # Return dict of title, author and genre
  
  # Extract document data
  data["title"] = metadata["title"]
  data["author"] = metadata["author"]

  # Extract file data except for content
  file_metadata = {k: v for k, v in document.items() if k != "content"}
  data.update(file_metadata)

  # Get chunks 
  chunks = fixed_text_chunk_with_overlap(text = document["content"], chunk_size=100, chunk_overlap=20)
  data["chunks"] = chunks  

  return data

