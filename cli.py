import argparse
import asyncio

from src.doc_processor.loader import load_document
from src.doc_processor.metadata import extract_metadata
from src.doc_processor.chunker import fixed_text_chunk_with_overlap
from src.doc_processor.config import DEFAULT_CHUNK_SIZE, DEFAULT_OVERLAP
from src.doc_processor.writer import save_json_local

async def process_document(path: str) -> dict:
  data = {}

  document = await load_document(path)
  metadata = extract_metadata(document["content"])

  file_metadata = {k: v for k, v in document.items() if k != "content"}
  data["metadata"] = file_metadata
  data["metadata"]["author"] = metadata.get("author", "")
  data["metadata"]["genre"] = metadata.get("genre", "")

  chunks = fixed_text_chunk_with_overlap(
    text=document["content"],
    chunk_size=DEFAULT_CHUNK_SIZE,
    chunk_overlap=DEFAULT_OVERLAP,
  )
  data["chunks"] = chunks

  output_folder = "data/output/"
  file_name = data["metadata"]["file_name"]
  target_path = output_folder + file_name

  saved_file_path = save_json_local(data=data, target_path=target_path)
  return saved_file_path


def main() -> None:
  parser = argparse.ArgumentParser(description="A simple text chunking CLI")
  parser.add_argument("path", help="Path to the file")
  args = parser.parse_args()
  cli_result = asyncio.run(process_document(args.path))
  print(cli_result)


if __name__ == "__main__":
  main()


  
