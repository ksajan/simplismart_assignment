import enum
import os

import dotenv

dotenv.load_dotenv()


# Load the environment variables
class ENV_VARS(enum.Enum):

    LAMMACPP_BASE_URL = os.getenv("LLM_SERVER_BASE_URL")
