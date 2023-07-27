import requests
from bs4 import BeautifulSoup
import concurrent.futures
from urllib.parse import urljoin

def test_csrf_vulnerability(url):
    session = requests.Session()
    response = session.get(url)
    cookies = session.cookies.get_dict()

    # Extract relevant information for the test
    csrf_token = extract_csrf_token(response.text, url)
    target_endpoints = extract_target_endpoints(response.text, url)

    # Craft malicious payload with CSRF token and target endpoint
    payload = {
        'csrf_token': csrf_token,
        'action': 'malicious_action',
        'data': 'malicious_data'
        # Add any additional parameters required by the target endpoint
    }

    # Send POST requests with payload to each target endpoint
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(send_payload_to_endpoint, target_endpoint, payload, cookies) for target_endpoint in target_endpoints]

        # Wait for all futures (requests) to complete
        concurrent.futures.wait(futures)

def extract_csrf_token(html_content, base_url):
    soup = BeautifulSoup(html_content, 'html.parser')
    # Find the CSRF token element in the HTML using appropriate selectors
    csrf_token_element = soup.find('input', {'name': 'csrf_token'})
    if csrf_token_element:
        csrf_token = csrf_token_element['value']
        return csrf_token
    else:
        print(f"CSRF token not found for {base_url}")
        return None

def extract_target_endpoints(html_content, base_url):
    soup = BeautifulSoup(html_content, 'html.parser')
    form_elements = soup.find_all('form')
    target_endpoints = set()

    for form_element in form_elements:
        if form_element.has_attr('action'):
            target_endpoint = form_element['action']
            target_endpoint = urljoin(base_url, target_endpoint)
            target_endpoints.add(target_endpoint)

    if target_endpoints:
        return target_endpoints
    else:
        print(f"No target endpoints found for {base_url}")
        return None

def check_unauthorized_action(response):
    # Implement logic to check if the response indicates a successful unauthorized action
    # This may involve analyzing the response status code, response content, or other indicators

    # Example: Check if the response status code indicates success (e.g., 200 OK)
    if response.status_code == 200:
        # Example: Check if the response content contains a specific string indicating success
        if 'Unauthorized' in response.text:
            return True

    return False

def send_payload_to_endpoint(target_endpoint, payload, cookies):
    session = requests.Session()
    response = session.post(target_endpoint, data=payload, cookies=cookies)

    # Check response for indications of successful unauthorized action
    if check_unauthorized_action(response):
        print(f"CSRF vulnerability detected for endpoint: {target_endpoint}")

        # Generate payload file
        generate_payload_file(payload, target_endpoint)
    else:
        print(f"No CSRF vulnerability detected for endpoint: {target_endpoint}")

def generate_payload_file(payload, target_endpoint):
    with open(f'payload_{target_endpoint.replace("/", "_")}.txt', 'w') as file:
        for key, value in payload.items():
            file.write(f'{key}: {value}\n')

def scan_web_pages(file_path):
    with open(file_path, 'r') as file:
        web_pages = file.read().splitlines()

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(test_csrf_vulnerability, url) for url in web_pages]

        # Wait for all futures (scans) to complete
        concurrent.futures.wait(futures)

# Usage
file_path = input("Enter the path to the text file containing the list of web pages: ")
scan_web_pages(file_path)
