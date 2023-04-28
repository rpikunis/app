import json
import random
from flask import Flask, jsonify, request, render_template

from generate_description import generate_description

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate_description", methods=["POST"])
def get_description():
    # Read prompts from file
    with open('/Users/Richie/Desktop/app/prompts.json', 'r') as f:
        prompts = json.load(f)


    # Select random prompt
    prompt_obj = random.choice(prompts)
    prompt = prompt_obj["prompt"]

    # Fill prompt with input values
    for variable in prompt_obj["variables"]:
        name = variable["name"]
        default = variable["default"]
        value = request.form.get(name, default)
        prompt = prompt.replace(f"{{{name}}}", str(value))

    print(f"Generated prompt: {prompt}")

    # Generate description using prompt
    description = generate_description(prompt)

    print(f"Generated description: {description}")

    # Return description as JSON
    return jsonify(description=description)

if __name__ == "__main__":
    app.run()
