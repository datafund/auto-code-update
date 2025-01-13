from dotenv import load_dotenv
import requests
import argparse
import os

load_dotenv()

figma_token = os.getenv("FIGMA_API_TOKEN")
figma_base_url = "https://api.figma.com/v1"

def figma_request(url: str):
    headers = {
        "X-Figma-Token": f"{figma_token}"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error: Unable to fetch project files (Status Code: {response.status_code})\nResponse: {response.json()}")


def main():
    parser = argparse.ArgumentParser(description="Exports a Figma file into an image")
    parser.add_argument('file_id', type=str, help="ID of file to be exported")
    parser.add_argument('ids', type=str, help="Value of the node-id parameter from the file URL in x:y format")
    
    args = parser.parse_args()
    file_id = args.file_id
    ids = args.ids

    print(file_id, ids)

    image = figma_request(f"{figma_base_url}/images/{file_id}?ids={ids}")

    image_url = image["images"][ids]
    print(image_url)

 
if __name__ == "__main__":
    main()
