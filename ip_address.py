import os


def get_ip_address(url):
    command = "host " + url
    process = os.popen(command)
    results = str(process.read()) # extracting domain name
    marker = results.find ('has address') + 12
    return results[marker:].splitlines()[0]

print(get_ip_address('christopherboedicker.com'))