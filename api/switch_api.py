import uvicorn
import sys
import os

def run_api():
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

def stop_api():
    os._exit(0)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python switch_api.py [run|stop]")
        sys.exit(1)
    
    command = sys.argv[1]
    if command == "run":
        run_api()
    elif command == "stop":
        stop_api()
    else:
        print("Invalid command. Use 'run' or 'stop'.")
        sys.exit(1)