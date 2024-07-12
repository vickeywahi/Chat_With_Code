# Chat_With_Code

## Project Description

Learn how to effortlessly index GitHub repositories into Deep Lake and interact with your code through natural language queries. This guide will walk you through the steps of creating a powerful tool to search, explore, and understand your codebase.

## Features

- Seamlessly index your GitHub repositories using LlamaIndex.
- Store and manage code embeddings efficiently in Activeloop Deep Lake.
- Interact with your code using natural language queries.
- Retrieve relevant code snippets and explanations.
- (Optional) Enhance the experience with text-to-speech and audio recording features using ElevenLabs.

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/vickeywahi/Chat_With_Code
   cd Chat_With_Code
Use code with caution.
content_copy
Create a Virtual Environment:

Bash
python3 -m venv repo-ai
Use code with caution.
content_copy
Activate the Environment:

Bash
source repo-ai/bin/activate  # macOS/Linux
.\repo-ai\Scripts\activate    # Windows
Use code with caution.
content_copy
Install Dependencies:

Bash
pip install -r requirements.txt
Use code with caution.
content_copy
Set up Your Environment Variables:

Create a .env file in your project directory.

Fill it with the following values (replace placeholders with your actual credentials):

GITHUB_TOKEN=your_github_personal_access_token
OPENAI_API_KEY=your_openai_api_key
ACTIVELOOP_TOKEN=your_activeloop_token
DATASET_PATH="hub://your_org_name/your_deep_lake_dataset_name"  
Usage
Index Your Repository:

Run the indexing script (e.g., python index.py) to process your code and store it in Deep Lake.
Start the Chat Interface:

Run the main application (e.g., streamlit run app.py).
Type your natural language questions about your codebase.
