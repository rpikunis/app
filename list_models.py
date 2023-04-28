from openai_secret_manager import get_secret
import openai

# Get your OpenAI API key
secrets = get_secret("openai")
openai.api_key = secrets["api_key"]

# List your OpenAI models
models = openai.Model.list()
print(models)
