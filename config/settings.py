from pathlib import Path
from dotenv import load_dotenv
import os
import sys

BASE_DIR = Path(__file__).resolve().parent.parent
env_path = BASE_DIR / ".env"  # env.dev, env.test, env.prod if needed
load_dotenv(dotenv_path=env_path)
rel_path = os.getenv("PYTHONPATH")
if rel_path:
    sys.path.insert(0, str(BASE_DIR / rel_path))


DATA = BASE_DIR / "data" / "California_Wildfire_Damage.csv"
