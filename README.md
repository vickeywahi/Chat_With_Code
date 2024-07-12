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

### Create a Virtual Environment:
Bash
pyenv virtualenv 3.10.13 repo-ai

### Activate the Environment:
Bash
pyenv activate repo-ai

### Install Dependencies:
Bash
pip install -r requirements.txt

### Set up Your Environment Variables:
Create a .env file in your project directory.

### Fill it with the following values (replace placeholders with your actual credentials):
GITHUB_TOKEN=your_github_personal_access_token
OPENAI_API_KEY=your_openai_api_key
ACTIVELOOP_TOKEN=your_activeloop_token
DATASET_PATH="hub://your_org_name/your_deep_lake_dataset_name"  

### main.py() is working, but a number of enhanceents could be made in due course

Type your natural language questions about your codebase.
<img width="1036" alt="Screenshot 2024-07-12 at 10 08 25" src="https://github.com/user-attachments/assets/485759a8-9ff7-4bbc-98ff-24a3b0d610e8">


