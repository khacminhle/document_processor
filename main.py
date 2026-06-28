# Python import 
import argparse

# import local module
from src.doc_processor.loader import load_document
from src.doc_processor.metadata import extract_metadata
from src.doc_processor.chunker import fixed_text_chunk_with_overlap
from pprint import pprint
from src.doc_processor.config import DEFAULT_CHUNK_SIZE, DEFAULT_OVERLAP
from src.doc_processor.writer import save_json

def process_document() -> dict:
  
  # ------- Args parse for commands line ------- 
  parser = argparse.ArgumentParser(description="A simple text chunking CLI")

  parser.add_argument("path", help="The folder path to output the chunked file")
  args = parser.parse_args()

  # Process document transformation logic
  data = {}

  document = load_document(args.path) # Return dict of content and metadata

  metadata = extract_metadata(document["content"]) # Return dict of title, author and genre
  
  # Extract file data except for content
  file_metadata = {k: v for k, v in document.items() if k != "content"}
  data["metadata"] = file_metadata
  data["metadata"]["author"] = metadata.get("author", "")
  data["metadata"]["genre"] = metadata.get("genre", "")
  
  # Get chunks 
  chunks = fixed_text_chunk_with_overlap(text=document["content"], 
                                         chunk_size=DEFAULT_CHUNK_SIZE, 
                                         chunk_overlap=DEFAULT_OVERLAP)
  
  data["chunks"] = chunks  

  # Build target path 
  output_folder = "data/output/"
  file_name = data["metadata"]["file_name"]
  target_path = output_folder + file_name

  save_json(data=data, target_path=target_path)


if __name__ == "__main__":
  process_document()


  