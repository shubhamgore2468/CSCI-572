from bs4 import BeautifulSoup
import httpx 
import requests
import json
import random
import time


headers = {
    "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
}

hw1_json = {}


def Search(query):
    links = []
    try:

        delay = random.uniform(10, 50)
        print(f"Sleeping for {delay:.2f} seconds")
        time.sleep(delay)

        url = "https://www.duckduckgo.com/html/?q="+query
        res = requests.get(url, headers=headers)
        res.raise_for_status()  # Raise an error for bad status codes
    except httpx.HTTPStatusError as e:
        print(f"HTTP error occurred: {e}")
        return
    except Exception as e:
        print(f"An error occurred: {e}")
        return

    res_html = res.text
    soup = BeautifulSoup(res_html, "html.parser")
    
    results = soup.find_all(class_="result__url")

    count = 0
    for result in results:
        count += 1
        links.append(result.text.strip())
        if count >=10:
            break
        # print(result)
        # print(result.text)
    # for link in links:
    

    # print(links)
    # print('\n')
    return links


def main():
    queries = []
    

    with open('queries.txt', 'r') as f:
        for line in f:
            queries.append(line.strip())
    
    for query in queries:
        output = []
        print(f"Searching for: {query}")
        print('\n')
        
        output = Search(query)
        if query not in hw1_json:
            hw1_json[query] = []

        hw1_json[query].extend(output)

        # print(hw1_json)

    with open('hw1.json', 'w') as f:
        json.dump(hw1_json, f)
    print('\n')


if __name__ == '__main__' : 
    main()