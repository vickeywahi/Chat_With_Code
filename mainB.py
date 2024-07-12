#This is a back-up file, with tested code, but less efficient exception handling
import os
import textwrap
from dotenv import load_dotenv
from github import Github
from llama_index.readers.github import GithubRepositoryReader, GithubClient #LlamaDocConfirmed
from llama_index.core import VectorStoreIndex #LlamaDocConfirmed
from llama_index.vector_stores.deeplake import DeepLakeVectorStore
from llama_index.core.storage.storage_context import StorageContext
import re

import signal

def signal_handler(sig, frame):
    print("Exiting, thanks for chatting!")
    exit(0)

# Register the signal handler for SIGINT (Ctrl+C)
signal.signal(signal.SIGINT, signal_handler)

# Load environment variables from .env file
load_dotenv()

# Get GitHub file extensions in scope from .env
file_extensions_str = os.getenv("FILE_EXTENSIONS")
file_extensions = file_extensions_str.split(',')  # Convert to list
DATASET_PATH = os.getenv("DATASET_PATH")

# Function to parse GitHub URL
def parse_github_url(url):
    pattern = r"https://github\.com/([^/]+)/([^/]+)"
    match = re.match(pattern, url)
    return match.groups() if match else (None, None)

# Function to validate owner and repository
def validate_owner_repo(owner, repo):
    return bool(owner) and bool(repo)

# Function to initialize GitHub client
def initialize_github_client():
    github_token = os.getenv("GITHUB_TOKEN")##,verbose) #github_token = os.getenv("GITHUB_TOKEN")
    return GithubClient(github_token)  # Create and return Github instance

# Check for required environment variables
def check_environment_variables():
    required_variables = ["OPENAI_API_KEY", "GITHUB_TOKEN", "ACTIVELOOP_TOKEN", "DATASET_PATH", "FILE_EXTENSIONS"]
    missing_variables = []
    for var in required_variables:
        if not os.getenv(var):
            missing_variables.append(var)
    if missing_variables:
        raise EnvironmentError(
            f"The following environment variables are missing: {', '.join(missing_variables)}"
        )

# Global variable to store documents
#docs = []
branch = "master"  # Set default branch value


def main():
    # Check environment variables before proceeding
    check_environment_variables()
   # global docs
    github_client = initialize_github_client()
    github_url = None  # Initialize github_url outside the loop
    branch = "master"  # Set default branch value

    while True:
        github_url = input("Please enter the GitHub repository URL: ")
        owner, repo = parse_github_url(github_url)

        if owner and repo:
            try:
                loader = GithubRepositoryReader(
                    owner=owner,
                    repo=repo,
                    github_client=github_client, #GithubClient(github_client),
                    filter_file_extensions=(file_extensions, GithubRepositoryReader.FilterType.INCLUDE),
                    verbose=False,
                    concurrent_requests=5, #20
                    use_parser=False, #LlamaDocConfirmed
                )

                print(f"Loading {repo} repository by {owner}")

                # Load repository data, specifying the branch directly
                docs = loader.load_data(branch=branch)#docs = github_repo_reader.load_data(branch=branch)
                print("Documents uploaded:")
                for doc in docs:
                    print(doc.metadata)

                # Create vector store and upload data
                vector_store = DeepLakeVectorStore(
                    dataset_path=DATASET_PATH,
                    overwrite=True,
                    runtime={"tensor_db": True},
                )
                storage_context = StorageContext.from_defaults(vector_store=vector_store)
                index = VectorStoreIndex.from_documents(docs, storage_context=storage_context)
                query_engine = index.as_query_engine()

                print("Uploading to vector store...")

                # Include a simple question to test.
                intro_question = "What is the repository about?"
                print(f"Test question: {intro_question}")
                print("=" * 50)
                answer = query_engine.query(intro_question)

                print(f"Answer: {textwrap.fill(str(answer), 100)} \n")

                while True:
                    user_question = input("Please enter your question (or type 'exit' to quit): ")
                    if user_question.lower() == "exit":
                        print("Exiting, thanks for chatting!")
                        break

                    print(f"Your question: {user_question}")
                    print("=" * 50)

                    answer = query_engine.query(user_question)
                    print(f"Answer: {textwrap.fill(str(answer), 100)} \n")
                break
            except Exception as e:  # catch exception
                print(f"An error occurred while processing the repository: {e}")
                break  # Exit loop after error
                raise  # Re-raise the exception to see the full traceback- added new
        else:
            print("Invalid GitHub URL. Please try again.")
            github_url = None

if __name__ == "__main__":
    main()