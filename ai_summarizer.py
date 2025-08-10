import os          # For interacting with the operating system (e.g., getting environment variables)
import openai      # OpenAI Python client library to interact with GPT models
import argparse    # For parsing command-line arguments

# Function to summarize a text file using an OpenAI Chat model
def summarize_file(input_path, model="gpt-3.5-turbo"):
    # Open the file in read mode, using UTF-8 encoding to handle most characters
    with open(input_path, 'r', encoding='utf-8') as f:
        text = f.read()  # Read the entire file content into a single string

    # Set the OpenAI API key from the environment variable "OPENAI_API_KEY"
    # You must export this key before running the script
    openai.api_key = os.getenv("OPENAI_API_KEY")

    # Send the request to the OpenAI API to summarize the text
    resp = openai.ChatCompletion.create(
        model=model,  # Which GPT model to use (default: gpt-3.5-turbo)
        messages=[
            # System role defines the assistant's general behavior
            {"role": "system", "content": "You are a helpful assistant."},
            # User role contains the actual task for GPT
            {"role": "user", "content": f"Summarize this text:\n\n{text}"}
        ]
    )

    # Extract the summary text from the API response and remove extra spacesS
    return resp.choices[0].message.content.strip()

# This block runs only if the file is executed directly (not imported as a module)
if __name__ == "__main__":
    # Create a command-line argument parser
    p = argparse.ArgumentParser()
    # Required argument: path to the text file that needs summarizing
    p.add_argument("--input", required=True, help="path to your file")
    # Optional argument: which GPT model to use
    p.add_argument("--model", default="gpt-3.5-turbo", help="Model OpenAI")
    # Parse the provided command-line arguments
    args = p.parse_args()

    # Call the summarization function with the given file path and model
    summary = summarize_file(args.input, args.model)

    # Print the resulting summary to the console
    print("📄 Summary:\n", summary)
