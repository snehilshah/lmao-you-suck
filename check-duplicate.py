import json
from collections import defaultdict


def check_duplicate_images(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)

    url_counts = defaultdict(int)
    duplicates = []

    for device in data.get('devices', []):
        for image in device.get('images', []):
            url = image.get('url')
            url_counts[url] += 1
            if url_counts[url] > 1:
                duplicates.append(url)

    return duplicates


if __name__ == "__main__":
    file_path = 'test.json'
    duplicates = check_duplicate_images(file_path)
    if duplicates:
        print("URLs with more than 2 occurrences found:")
        for url in duplicates:
            print(url)
    else:
        print("No URLs with more than 2 occurrences found.")
