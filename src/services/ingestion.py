from src.doc_processor.loader import load_document
from src.doc_processor.metadata import extract_metadata
from src.doc_processor.chunker import fixed_text_chunk_with_overlap
from src.doc_processor.config import DEFAULT_CHUNK_SIZE, DEFAULT_OVERLAP

from typing import Any
import json

async def process_document(file_obj: Any) -> dict: 
    
  # Read the file object
  document = await load_document(file_obj)
  
  # Extract metadata 
  metadata = extract_metadata(document["content"])

  # Extract file data except for content
  data = {}  
  file_metadata = {k: v for k, v in document.items() if k != "content"}
  data["metadata"] = file_metadata
  data["metadata"]["author"] = metadata.get("author", "")
  data["metadata"]["genre"] = metadata.get("genre", "")

  # Get chunks 
  chunks = fixed_text_chunk_with_overlap(text=document["content"], 
                                         chunk_size=DEFAULT_CHUNK_SIZE, 
                                         chunk_overlap=DEFAULT_OVERLAP)
  

  data["chunks"] = chunks 

  return data


  
  
