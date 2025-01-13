import time
import requests

def download_file(url):
    start_time = time.time()
    response = requests.get(url)
    file_name = url.split("/")[-1]
    with open(file_name, "wb") as file:
        file.write(response.content)
    print(f"Downloaded {file_name} in {time.time() - start_time:.2f} seconds")

def main():
    urls = [
        "https://via.placeholder.com/150",
        "https://via.placeholder.com/300",
        "https://via.placeholder.com/450",
    ]
    
    start_time = time.time()
    for url in urls:
        download_file(url)
    print(f"Total time (single-threaded): {time.time() - start_time:.2f} seconds")

if __name__ == "__main__":
    main()
