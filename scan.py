import os
import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin
import subprocess
import urllib.parse
import time
import sys
import concurrent.futures
import logging
import ssl
import socket
import datetime
import random
import string
from urllib.parse import urlparse

from jinja2 import Template

# Function to generate HTML content for pentest results
def generate_pentest_html(url, results):
    # Function to get severity color based on severity level
    def get_severity_color(severity):
        if severity == "High":
            return "text-red-600"
        elif severity == "Medium":
            return "text-yellow-600"
        elif severity == "Low":
            return "text-green-600"
        else:
            return "text-gray-600"

    # HTML structure using Tailwind CSS classes
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Pentest Results - {url}</title>
        <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
        <style>
            /* Additional custom styling can be added here */
        </style>
    </head>
    <body class="bg-gray-100">
        <!-- Top Menu -->
        <nav class="bg-blue-500 p-4">
            <div class="container mx-auto">
                <a href="#" class="text-white font-bold">Home</a>
                <!-- Add more menu items as needed -->
            </div>
        </nav>
        <div class="container mx-auto mt-4">
            <h1 class="text-3xl font-bold mb-4">Pentest Results - {url}</h1>
    """

    # Table to display results
    html_content += """
        <div class="overflow-x-auto">
            <table class="table-auto w-full">
                <thead>
                    <tr>
                        <th class="px-4 py-2">Category</th>
                        <th class="px-4 py-2">Details</th>
                        <th class="px-4 py-2">Severity</th>
                    </tr>
                </thead>
                <tbody>
    """

    # Populate table rows with results
    for category, details in results.items():
        if category != "Hidden Directories" and details:
            for detail, severity in details.items():
                if detail not in ["{}", "[]"]:  # Exclude {} and [] from the output
                    severity_color = get_severity_color(severity)
                    html_content += f"""
                        <tr>
                            <td class="border px-4 py-2">{category}</td>
                            <td class="border px-4 py-2">{detail}</td>
                            <td class="border px-4 py-2 {severity_color}">{severity}</td>
                        </tr>
                    """
    
    # Close table and HTML structure
    html_content += """
                </tbody>
            </table>
        </div>
        </div>
    </body>
    </html>
    """
    return html_content



# Function to sanitize filenames
def sanitize_filename(filename):
    return re.sub(r'[<>:"/\\|?*]', '_', filename)

# Function to write HTML results to a file
def write_html_file(domain, html_content):
    sanitized_domain = sanitize_filename(domain)
    file_name = f"{sanitized_domain}_pentest_results.html"
    with open(file_name, "w") as f:
        f.write(html_content)
    print(f"Pentest results saved to {file_name}")

# Function to get all links from a given URL
def get_links(url):
    print("Getting links...")
    try:
        response = requests.get(url, timeout=60, verify=True)
        response.raise_for_status()  # Raise an error for bad responses
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return []  # Return an empty list if there's an error
    soup = BeautifulSoup(response.content, "html.parser")
    links = []
    for link in soup.find_all("a", href=True):
        links.append(urljoin(url, link["href"]))
    print("Links retrieved.")
    return links

# Function to scan HTML content for vulnerabilities
def scan_html(html_content):
    print("Scanning HTML...")
    vulnerabilities = []
    # Example: Scan for XSS vulnerabilities
    if re.search(r'<script>alert\(.*\)</script>', html_content):
        vulnerabilities.append("XSS vulnerability detected")
    # Scan for outdated HTML attributes or tags
    deprecated_tags = re.findall(r'<(applet|basefont|big|center|dir|font|frame|frameset|isindex|noframes|s|strike|tt|u)>', html_content)
    if deprecated_tags:
        vulnerabilities.append("Deprecated HTML tags detected: {}".format(", ".join(deprecated_tags)))
    # Scan for sensitive data exposure
    if re.search(r'((password|username|credit_card|ssn|social_security_number)\s*[=:]\s*[\'"]?(?P<value>.*?)\b[\'"]?)', html_content, re.IGNORECASE):
        vulnerabilities.append("Sensitive data exposure detected")
    print("HTML scanned.")
    return vulnerabilities

# Function to scan JavaScript content for vulnerabilities
def scan_javascript(js_content):
    print("Scanning JavaScript...")
    vulnerabilities = []
    try:
        # Scan for known JavaScript vulnerabilities
        # Example: Detecting usage of dangerous functions
        dangerous_functions = ['eval', 'document.write', 'innerHTML', 'setTimeout', 'setInterval', 'Function']
        for func in dangerous_functions:
            if re.search(fr'\b{func}\b', js_content):
                vulnerabilities.append(f"Potential usage of dangerous function '{func}' detected")
    except Exception as e:
        vulnerabilities.append(f"Error scanning JavaScript: {e}")
    print("JavaScript scanned.")
    return vulnerabilities

# Function to scan CSS content for vulnerabilities
def scan_css(css_content):
    print("Scanning CSS...")
    vulnerabilities = []
    # Example: Scan for CSS injection vulnerabilities
    if "expression(" in css_content:
        vulnerabilities.append("Potential CSS injection detected")
    # Scan for URL redirection vulnerabilities
    if "url(" in css_content:
        vulnerabilities.append("Potential URL redirection vulnerability detected")
    print("CSS scanned.")
    return vulnerabilities

# Function to scan PHP endpoints for vulnerabilities
def scan_php(url):
    print("Scanning PHP...")
    vulnerabilities = []
    # Example: Check for PHPInfo exposure
    php_info_url = urllib.parse.urljoin(url, 'phpinfo.php')
    response = requests.get(php_info_url, timeout=60)  # Set timeout to 60 seconds
    if 'PHP Version' in response.text:
        vulnerabilities.append("PHPInfo exposure detected")
    # Add more PHP vulnerability checks as needed
    print("PHP scanned.")
    return vulnerabilities

# Function to scan SSL configuration for vulnerabilities
def scan_ssl(url):
    print("Scanning SSL...")
    vulnerabilities = []
    try:
        hostname = url.split('//')[-1].split('/')[0]  # Extract hostname from URL
        context = ssl.create_default_context()
        with socket.create_connection((hostname, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                cert = ssock.getpeercert()
                # Check certificate expiry date
                expiry_date_str = cert['notAfter']
                expiry_date = datetime.datetime.strptime(expiry_date_str, "%b %d %H:%M:%S %Y %Z")
                if expiry_date < datetime.datetime.now():
                    vulnerabilities.append("SSL certificate expired")
    except Exception as e:
        vulnerabilities.append("Error scanning SSL: {}".format(str(e)))
    print("SSL scanned.")
    return vulnerabilities

# Function to scan HTTP headers for vulnerabilities
def scan_headers(url):
    print("Scanning headers...")
    vulnerabilities = []
    try:
        headers = requests.head(url).headers
        # Check for security headers
        if "Content-Security-Policy" not in headers:
            vulnerabilities.append("Content-Security-Policy header missing")
        if "X-XSS-Protection" not in headers:
            vulnerabilities.append("X-XSS-Protection header missing")
        if "X-Content-Type-Options" not in headers:
            vulnerabilities.append("X-Content-Type-Options header missing")
        if "X-Frame-Options" not in headers:
            vulnerabilities.append("X-Frame-Options header missing")
    except Exception as e:
        vulnerabilities.append("Error scanning headers: {}".format(str(e)))
    print("Headers scanned.")
    return vulnerabilities

# Function to scan for file inclusion vulnerabilities
def scan_for_file_inclusion(url):
    print("Scanning for file inclusion...")
    vulnerabilities = []
    try:
        # Example: Check for file inclusion vulnerability
        response = requests.get(url + "?file=../../../../../../../../etc/passwd", timeout=60)  # Set timeout to 60 seconds
        if "root:" in response.text:
            vulnerabilities.append("File inclusion vulnerability detected")
    except Exception as e:
        vulnerabilities.append("Error scanning for file inclusion: {}".format(str(e)))
    print("File inclusion scanned.")
    return vulnerabilities

# Function to scan for command injection vulnerabilities
def scan_for_command_injection(url):
    print("Scanning for command injection...")
    vulnerabilities = []
    try:
        # Example: Check for command injection vulnerability
        response = subprocess.getoutput("ping -c 1 " + url)
        if "64 bytes" in response:
            vulnerabilities.append("Command injection vulnerability detected")
    except Exception as e:
        vulnerabilities.append("Error scanning for command injection: {}".format(str(e)))
    print("Command injection scanned.")
    return vulnerabilities

# Function to find hidden directories on a website
def find_hidden_directories(url):
    print("Finding hidden directories...")
    hidden_dirs = []
    try:
        response = requests.get(url, timeout=60)  # Set timeout to 60 seconds
        if response.status_code == 200:
            parsed_url = urlparse(url)
            base_url = parsed_url.scheme + '://' + parsed_url.netloc
            soup = BeautifulSoup(response.text, 'html.parser')
            for link in soup.find_all('a', href=True):
                href = link['href']
                if href.startswith('/'):
                    hidden_dirs.append(urljoin(base_url, href))
    except Exception as e:
        print("Error finding hidden directories:", e)
    print("Hidden directories found.")
    return hidden_dirs

# Function to scan a link for vulnerabilities
# Function to scan a link for vulnerabilities
def scan_link(link):
    try:
        print(f"Scanning {link}...")
        start_time = time.time()
        response = requests.get(link, timeout=60)
        elapsed_time = time.time() - start_time
        if elapsed_time > 60:
            print(f"Scanning {link} timed out.")
            return link, {"Timeout": ["Scanning timed out"]}

        html_vulnerabilities = scan_html(response.text)
        js_vulnerabilities = scan_javascript(response.text)
        css_vulnerabilities = scan_css(response.text)
        php_vulnerabilities = scan_php(link)
        ssl_vulnerabilities = scan_ssl(link)
        header_vulnerabilities = scan_headers(link)
        file_inclusion_vulnerabilities = scan_for_file_inclusion(link)
        command_injection_vulnerabilities = scan_for_command_injection(link)
        hidden_directories = find_hidden_directories(link)

        # Check if any vulnerabilities were found
        results = {
            "HTML": html_vulnerabilities,
            "JavaScript": js_vulnerabilities,
            "CSS": css_vulnerabilities,
            "PHP": php_vulnerabilities,
            "SSL": ssl_vulnerabilities,
            "Headers": header_vulnerabilities,
            "File Inclusion": file_inclusion_vulnerabilities,
            "Command Injection": command_injection_vulnerabilities,
            "Hidden Directories": hidden_directories
        }
        
        # Remove empty dictionaries from results
        results = {key: value for key, value in results.items() if value}
        
        return link, results
    except requests.exceptions.Timeout:
        print(f"Scanning {link} timed out.")
        return link, {"Timeout": ["Scanning timed out"]}
    except Exception as e:
        print(f"Error scanning {link}: {e}")
        return link, {"Error": [str(e)]}

# Function to search for CVEs related to a given URL
def search_cve(url):
    try:
        cve_response = requests.get(f"https://cve.circl.lu/api/search/{url}")
        if cve_response.status_code == 404:
            print(f"No CVEs found for {url}")
            return None
        cve_response.raise_for_status()  # Raise an exception for other HTTP errors
        cve_results = cve_response.json()
        return cve_results
    except requests.exceptions.RequestException as e:
        print(f"Error searching for CVEs: {e}")
        return None
    except ValueError as ve:
        print(f"Error parsing CVE response: {ve}")
        return None

# Main function to orchestrate the scanning process
def main():
    # Print the warning message in a box
    print("""
╔════════════════════════════════════════════════════════════════════════════════════════════════╗
║                                           WARNING                                              ║
║                                                                                                ║
║  This tool is intended for ethical security testing purposes only. It should only be used on    ║
║  websites that you have explicit permission to scan.                                           ║
║                                                                                                ║
║  Unauthorized scanning of websites may be illegal and unethical. Before proceeding, ensure that  ║
║  you have obtained proper authorization from the website owner or administrator.                ║
║                                                                                                ║
║  Unauthorized scanning can potentially disrupt services, violate privacy laws, and result in    ║
║  legal consequences. By using this tool, you agree to use it responsibly and adhere to all      ║
║  applicable laws and regulations. Failure to do so may result in legal action against you.        ║
║                                                                                                ║
║  Please only use this tool responsibly and on websites you have permission to scan.              ║
║                                                                                                ║
╚════════════════════════════════════════════════════════════════════════════════════════════════╝
    """)
    # Ask for confirmation
    confirmation = input("Do you agree to use this tool responsibly and only on websites you have permission to scan? (yes/no): ")
    if confirmation.lower() != "yes":
        print("You must agree to use this tool responsibly to proceed.")
        return
    # Ask the user for the URL of the website to scan
    url = input("Enter the URL of the website to scan: ")
    try:
        links = get_links(url)
        results = {}
        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
            futures = [executor.submit(scan_link, link) for link in links]
            for future in concurrent.futures.as_completed(futures):
                link, result = future.result()
                results[link] = result
        html_content = generate_pentest_html(url, results)
        write_html_file(url, html_content)
    except KeyboardInterrupt:
        print("\nScan interrupted by user.")
        sys.exit(0)
    except Exception as e:
        print(f"Error during scan: {e}")

if __name__ == "__main__":
    logging.basicConfig(filename='scan.log', level=logging.INFO, format='%(asctime)s %(message)s')
    main()
