import time
import requests
import threading

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
    threads = []
    for url in urls:
        thread = threading.Thread(target=download_file, args=(url,))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()
    print(f"Total time (multithreaded): {time.time() - start_time:.2f} seconds")

if __name__ == "__main__":
    main()
