from openai_secret_manager import get_secret
import openai

openai.api_key = secrets["api_key"]

models = openai.Model.list()
print(models)
