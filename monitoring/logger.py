import json
import logging
from pathlib import Path
from datetime import datetime, timezone
import hashlib

BASE_DIR = Path(__file__).resolve().parents[1]
LOG_DIR = BASE_DIR / "logs"
LOG_DIR.mkdir(exist_ok=True)

LOG_FILE = LOG_DIR / "predictions.log"

# Logger configuration
logger = logging.getLogger("prediction_logger")
logger.setLevel(logging.INFO)

if not logger.handlers:
    file_handler = logging.FileHandler(LOG_FILE, encoding='utf-8')
    formatter = logging.Formatter('%(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

# Hashing function for input data
def generate_input_hash(input_data: dict) -> str:
    payload_str = json.dumps(input_data, sort_keys=True)
    return hashlib.sha256(payload_str.encode('utf-8')).hexdigest()

# Logging function for predictions
def log_prediction(model_name: str, model_version: str, input_data: dict, prediction: str):
    log_entry = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "model_name": model_name,
        "model_version": model_version,
        "input_data": generate_input_hash(input_data),
        "prediction": prediction
    }
    logger.info(json.dumps(log_entry))