# If SQLite hasn't been installed, install it 
# Common file descriptor 
# 0: stdin
# 1: stdout
# 2: stderr

# Check if sqlite3 has been installed
# stderror goes to >/dev/null
if command -v sqlite3 >/dev/null 2>&1; then 
  echo "sqlite3 is installed"
else
  echo "sqlite3 is not installed"
fi  

# Some syntax 
# -f -> regular file exists
# -d -> directory exists
# -e -> anything exists (file, directory, symlink)

# Check if the database has already been created 
# CONSTANT
DB_FILE="document_processor.db"
DOCUMENT_CORPUS_TABLE="document_corpus"

if [ -f "$DB_FILE" ]; then
  echo "DB File exists"
else
  echo "DB File doesn't exist, creating db file"

  # SELECT 1 tells SQLite to do a tiny piece of work
  # If we don't do this, SQLITE3 stuck in 
  # interactive mode
  if sqlite3 "$DB_FILE" "SELECT 1;" >/dev/null; then 
    echo "Created $DB_FILE"
  else
    echo "Failed to create $DB_FILE"
    exit 1
  fi  
fi

# Check and create table 
if sqlite3 "$DB_FILE" \
  "SELECT EXISTS (
    SELECT 1
    FROM sqlite_master
    WHERE type = 'table'
      and name = '$DOCUMENT_CORPUS_TABLE'
  );" | grep -q "^1$"; then 
  echo "Document corpus table already exists"
else
  echo "Corpus table does not exist, creating table"

  if sqlite3 "$DB_FILE" "
    CREATE TABLE IF NOT EXISTS $DOCUMENT_CORPUS_TABLE (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    full_text TEXT NOT NULL,
    author TEXT, 
    genre TEXT,
    word_count INT, 
    line_count INT,    
    content_hash TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );" >/dev/null; then
    echo "$DOCUMENT_CORPUS_TABLE table created";

  else
    echo "Failed to create $DOCUMENT_CORPUS_TABLE table"
    exit 1
  fi  
fi








