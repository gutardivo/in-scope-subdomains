import re
import sys

def filter_urls(in_scope_domains, not_in_scope_domains, urls):
    in_scope_pattern = r'^(' + '|'.join(map(re.escape, in_scope_domains)) + r')\..+$'
    not_in_scope_pattern = r'^(' + '|'.join(map(re.escape, not_in_scope_domains)) + r')\..+$'

    in_scope_urls = [url for url in urls if re.match(in_scope_pattern, url)]
    print("In scope URLs:")
    for url in in_scope_urls:
        print(url)

    not_in_scope_urls = [url for url in urls if re.match(not_in_scope_pattern, url)]
    print("\nNot in scope URLs:")
    for url in not_in_scope_urls:
        print(url)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <urls_file>")
        sys.exit(1)

    urls_file = sys.argv[1]

    in_scope_domains = input("Enter in-scope domains (comma-separated, e.g., domain.com, yahoo.com, google.com): ").split(',')
    not_in_scope_domains = input("Enter not in-scope domains (comma-separated, e.g., domain.org, example.com): ").split(',')

    with open(urls_file, 'r') as file:
        urls = file.read().splitlines()

    filter_urls(in_scope_domains, not_in_scope_domains, urls)
