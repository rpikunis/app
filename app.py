from flask import Flask, render_template, jsonify, request
import openai
import os


# Set up Flask app
app = Flask(__name__, static_url_path='/static')


# Set up OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Load prompt from prompts.json file
with open("static/prompts.json", "r") as f:
    prompt = f.read()

# Set up OpenAI completion parameters
model_engine = "text-davinci-002"
max_tokens = 60
temperature = 0.5
n = 1

# Define route for index page
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

# Define route for processing property form data
@app.route("/process_property_form", methods=["POST"])
def process_property_form():
    # Get form data
    lot_info = request.json["lot_info"]
    structure_type = request.json["structure_type"]
    num_bedrooms = request.json["num_bedrooms"]
    bedroom_features = request.json["bedroom_features"]
    num_bathrooms = request.json["num_bathrooms"]
    bathroom_features = request.json["bathroom_features"]
    kitchen_info = request.json["kitchen_info"]
    garage_info = request.json["garage_info"]
    other_features = request.json["other_features"]

    # Generate property description using OpenAI
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt.format(lot_info=lot_info, structure_type=structure_type, num_bedrooms=num_bedrooms, 
                             bedroom_features=bedroom_features, num_bathrooms=num_bathrooms, 
                             bathroom_features=bathroom_features, kitchen_info=kitchen_info, 
                             garage_info=garage_info, other_features=other_features),
        max_tokens=max_tokens,
        temperature=temperature,
        n=n,
    )
    description = completion.choices[0].text.strip()

    # Return property description as JSON response
    return jsonify({"description": description})

if __name__ == "__main__":
    app.run(debug=True)
