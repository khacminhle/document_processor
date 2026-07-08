from doc_processor.loader import load_document
from doc_processor.metadata import extract_metadata
from doc_processor.chunker import fixed_text_chunk_with_overlap
from doc_processor.config import DEFAULT_CHUNK_SIZE, DEFAULT_OVERLAP
from typing import Any
import time
import logging 

# Initialise logging
logger = logging.getLogger(__name__)

async def chunking_document(file_obj: Any) -> dict: 
  
  # Process start
  start_time = time.perf_counter()
  logger.info(f"Starting document chunking process at {start_time}")  
  
  # Read the file object
  document = await load_document(file_obj)
  logger.info("Document loaded")  

  
  logger.info("Starting metadata extraction process")  
  # Extract metadata 
  metadata = extract_metadata(document["content"])
  logger.info("Metadata extraction process completed")  


  logger.info("Preparing data for chunking algorithms")  
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

  # End time 
  end_time = time.perf_counter()
  duration = end_time - start_time
  logger.info(f"Document chunking process took {duration:.6f} seconds")  
 
  return data


  
  
