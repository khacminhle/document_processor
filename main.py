from src.doc_processor.loader import load_document
from src.doc_processor.metadata import extract_metadata
from src.doc_processor.chunker import fixed_text_chunk_with_overlap
from pprint import pprint
from src.doc_processor.config import DEFAULT_CHUNK_SIZE, DEFAULT_OVERLAP

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
  chunks = fixed_text_chunk_with_overlap(text=document["content"], 
                                         chunk_size=DEFAULT_CHUNK_SIZE, 
                                         chunk_overlap=DEFAULT_OVERLAP)
  
  data["chunks"] = chunks  

  return data

chunk_data = process_document("data/sample/the_city_that_remembered_rain.md")

test_top_3 = [chunk_data["chunks"][i] for i in range(0, 3)]
pprint(test_top_3)


  