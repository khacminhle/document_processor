from doc_processor.writer import save_json_local
import pytest
from pydantic import ValidationError
from pathlib import Path


dirty_data = {
  "chunks":123,
  "document_id":"123_document_id_!"
}

mock_data = {
  
  "metadata": {
    "file_name": "mock_document",
    "file_extension": ".txt",
    "word_count": 43,
    "line_count": 2,
    "author": "Mock Author",
    "genre": "Fantasy"
  },

  "chunks": [
    {
      "chunk_id": 1,
      "text": "The old library appeared only after midnight, when the city clocks stopped and the final train disappeared into the fog.",
      "char_count": 117
    },
    {
      "chunk_id": 2,
      "text": "the final train disappeared into the fog. Inside the library, every book contained a future that had not happened yet.",
      "char_count": 117
    }
  ]
}

# Test save_json_local raise ValidationError when processing
# incorrect data dictionary 

def test_incorrect_data_dict(): 
  with pytest.raises(ValidationError):
    save_json_local(dirty_data, target_path="data/output/", extension=".json")

def test_save_data_to_file(tmp_path):
  # 2. Execute the save function


    first_file = save_json_local(mock_data, target_path=tmp_path, extension=".json")
    second_file = save_json_local(mock_data, target_path=tmp_path, extension=".json")

    assert first_file.exists()
    assert second_file.exists()


    assert first_file.name == f"{tmp_path.name}.json"
    assert second_file.name == f"{tmp_path.name}_copy_1.json"

