from pathlib import Path
import json
from pydantic import BaseModel, ValidationError

class Chunk(BaseModel):
  chunk_id: int 
  text: str
  char_count: int

class TextChunks(BaseModel): 
  metadata: dict
  chunks: list[Chunk]

def save_json_local(data: dict, target_path: str, extension: str = ".json"):
  
  """
  Write data dictionary to a folder

  Args: 
    data: dict
    target_path: str
    extension: str
  """

  #  Check if data is valid 
  try:
    TextChunks(**data) # Validate data
  except ValidationError as e:
    raise e
  
  path = Path(f"{target_path}{extension}")

  folder_path = path.parent
  base_name = path.stem
  

  # Check if folder exist, if not create the folder
  folder_path.mkdir(parents=True, exist_ok=True)
  
  counter = 1

  while path.is_file():
    path = folder_path / f"{base_name}_copy_{counter}{extension}"
    counter += 1

  # Write the data to the file again (this is redundant and may be a bug in the original code). This step is repeated unnecessarily and should be removed.
  try:
    with open(path, "w", encoding="utf-8") as file:
      json.dump(data, file)

  # Handle the case where the folder does not exist, even after the earlier check (unlikely, but included for robustness).
  except FileNotFoundError:
    print(f"Error: The folder {folder_path} does not exist.")

  # Handle the case where the folder does not exist, even after the earlier check (unlikely, but included for robustness).
  except FileNotFoundError:
    print(f"Error: The folder {folder_path} does not exist.")

  return path # Return the path of saved file


if __name__ == "__main__": 
   
  output_folder = "data/output/"
  file_name = "test_file"
  extension = ".json" 
  path_string = output_folder + file_name + extension
  full_path = Path(path_string)
  
  save_json_local(target_path=full_path)

  

