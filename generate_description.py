import openai
from config import Config

openai.api_key = Config.OPENAI_API_KEY

def generate_property_description(lot_info, structure_type, num_bedrooms, bedroom_features,
                                   num_bathrooms, bathroom_features, kitchen_info, garage_info,
                                   other_features):
    # Your code to generate the property description using OpenAI

    prompt = f"As a realtor, your job is to sell properties, and the first step in doing so is to create a compelling property listing that captures the attention of potential buyers. To design an outstanding property listing, you need to think like a marketer and appeal to your home buyer's needs and desires. Remember, your property listing is your first impression with potential buyers, so make it count. By following these tips, you can create an outstanding property listing that will generate interest, drive traffic, and ultimately lead to a successful sale. Start by highlighting the property's unique features which are included: {lot_info}, {structure_type}, {num_bedrooms} bedrooms, {num_bathrooms} bathrooms, {kitchen_info}, {garage_info}, {other_features}. Now with all this information draft me an amazing property description to sell this home."

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=0.5,
        max_tokens=1024,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    description = response.choices[0].text.strip()
    return description
