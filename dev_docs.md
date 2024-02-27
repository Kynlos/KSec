# Website Security Scanner Developer Documentation

## Introduction
This document serves as a comprehensive guide for developers intending to understand and contribute to the Website Security Scanner Python script. The script is a powerful tool designed to analyze websites for potential vulnerabilities, covering a wide range of security aspects including HTML, JavaScript, CSS, PHP, SSL, HTTP headers, file inclusion, command injection, and hidden directories.

## Implementation Details

### Libraries Used
- **requests**: Utilized for making HTTP requests to the target website.
- **BeautifulSoup**: Employed for parsing HTML content and extracting links.
- **Jinja2**: Used for generating HTML reports with dynamic content.
- **ssl**, **socket**: Used for SSL certificate validation and socket communication.
- **logging**: Implemented for logging scan activities and errors.
- **subprocess**: Utilized for executing external commands (e.g., ping) for command injection scanning.
- **os**, **re**, **urllib.parse**, **time**, **sys**, **concurrent.futures**, **datetime**, **random**, **string**: Standard Python libraries for various functionalities.

### Functions

#### `main()`
- **Purpose**: Entry point of the script, responsible for orchestrating the scanning process.
- **Functionality**:
  - Obtains user input for the target website URL and confirmation for responsible usage.
  - Initiates scans on various aspects of the website.
  - Generates HTML reports summarizing the scan results.

#### `generate_pentest_html(url, results)`
- **Purpose**: Generates an HTML report summarizing the scan results.
- **Inputs**:
  - `url`: URL of the scanned website.
  - `results`: Dictionary containing scan results categorized by vulnerability type.

#### Vulnerability Scanning Functions
- **Purpose**: These functions are responsible for scanning specific aspects of the website for potential vulnerabilities.
- **Functionality**:
  - `scan_html(html_content)`: Scans HTML content for vulnerabilities such as Cross-Site Scripting (XSS), deprecated tags, and sensitive data exposure.
  - `scan_javascript(js_content)`: Scans JavaScript content for potential security risks including usage of dangerous functions.
  - `scan_css(css_content)`: Scans CSS content for vulnerabilities such as CSS injection and URL redirection.
  - `scan_php(url)`: Scans PHP endpoints for vulnerabilities such as PHPInfo exposure.
  - `scan_ssl(url)`: Scans SSL configuration for potential issues like expired certificates.
  - `scan_headers(url)`: Scans HTTP headers for security-related headers.
  - `scan_for_file_inclusion(url)`: Scans for file inclusion vulnerabilities.
  - `scan_for_command_injection(url)`: Scans for command injection vulnerabilities.
  - `find_hidden_directories(url)`: Finds hidden directories within the website structure.
  - `search_cve(url)`: Searches for Common Vulnerabilities and Exposures (CVEs) associated with the provided URL.

#### Utility Functions
- **Purpose**: These functions provide utility operations required for scanning and report generation.
- **Functionality**:
  - `sanitize_filename(filename)`: Sanitizes filenames to prevent invalid characters.
  - `write_html_file(domain, html_content)`: Writes HTML results to a file.
  - `get_links(url)`: Retrieves all links from a given URL.
  - `scan_link(link)`: Initiates scanning of a single link for vulnerabilities.

## Usage
- Ensure Python 3.x is installed on the system.
- Install required dependencies using `pip install -r requirements.txt`.
- Run the script using `python script.py`.
- Follow on-screen instructions to input the URL of the website to be scanned.
- Review the generated HTML report for scan results.

## Testing
- The script should undergo thorough testing on various websites with different configurations to ensure accurate vulnerability detection.
- Unit tests and integration tests should be developed to validate the functionality of individual components and the system as a whole.

## Contributing
- Contributions to the project are encouraged and welcome via pull requests.
- Contributors should adhere to the coding style and guidelines specified in the project repository.

## License
- This project is licensed under the [License Name]. See the LICENSE.md file for detailed information.
# Website Security Scanner Developer Documentation

## Introduction
This document serves as a comprehensive guide for developers intending to understand and contribute to the Website Security Scanner Python script. The script is a powerful tool designed to analyze websites for potential vulnerabilities, covering a wide range of security aspects including HTML, JavaScript, CSS, PHP, SSL, HTTP headers, file inclusion, command injection, and hidden directories.

## Implementation Details

### Libraries Used
- **requests**: Utilized for making HTTP requests to the target website.
- **BeautifulSoup**: Employed for parsing HTML content and extracting links.
- **Jinja2**: Used for generating HTML reports with dynamic content.
- **ssl**, **socket**: Used for SSL certificate validation and socket communication.
- **logging**: Implemented for logging scan activities and errors.
- **subprocess**: Utilized for executing external commands (e.g., ping) for command injection scanning.
- **os**, **re**, **urllib.parse**, **time**, **sys**, **concurrent.futures**, **datetime**, **random**, **string**: Standard Python libraries for various functionalities.

### Functions

#### `main()`
- **Purpose**: Entry point of the script, responsible for orchestrating the scanning process.
- **Functionality**:
  - Obtains user input for the target website URL and confirmation for responsible usage.
  - Initiates scans on various aspects of the website.
  - Generates HTML reports summarizing the scan results.

#### `generate_pentest_html(url, results)`
- **Purpose**: Generates an HTML report summarizing the scan results.
- **Inputs**:
  - `url`: URL of the scanned website.
  - `results`: Dictionary containing scan results categorized by vulnerability type.

#### Vulnerability Scanning Functions
- **Purpose**: These functions are responsible for scanning specific aspects of the website for potential vulnerabilities.
- **Functionality**:
  - `scan_html(html_content)`: Scans HTML content for vulnerabilities such as Cross-Site Scripting (XSS), deprecated tags, and sensitive data exposure.
  - `scan_javascript(js_content)`: Scans JavaScript content for potential security risks including usage of dangerous functions.
  - `scan_css(css_content)`: Scans CSS content for vulnerabilities such as CSS injection and URL redirection.
  - `scan_php(url)`: Scans PHP endpoints for vulnerabilities such as PHPInfo exposure.
  - `scan_ssl(url)`: Scans SSL configuration for potential issues like expired certificates.
  - `scan_headers(url)`: Scans HTTP headers for security-related headers.
  - `scan_for_file_inclusion(url)`: Scans for file inclusion vulnerabilities.
  - `scan_for_command_injection(url)`: Scans for command injection vulnerabilities.
  - `find_hidden_directories(url)`: Finds hidden directories within the website structure.
  - `search_cve(url)`: Searches for Common Vulnerabilities and Exposures (CVEs) associated with the provided URL.

#### Utility Functions
- **Purpose**: These functions provide utility operations required for scanning and report generation.
- **Functionality**:
  - `sanitize_filename(filename)`: Sanitizes filenames to prevent invalid characters.
  - `write_html_file(domain, html_content)`: Writes HTML results to a file.
  - `get_links(url)`: Retrieves all links from a given URL.
  - `scan_link(link)`: Initiates scanning of a single link for vulnerabilities.

## Usage
- Ensure Python 3.x is installed on the system.
- Install required dependencies using `pip install -r requirements.txt`.
- Run the script using `python script.py`.
- Follow on-screen instructions to input the URL of the website to be scanned.
- Review the generated HTML report for scan results.

## Testing
- The script should undergo thorough testing on various websites with different configurations to ensure accurate vulnerability detection.
- Unit tests and integration tests should be developed to validate the functionality of individual components and the system as a whole.

## Contributing
- Contributions to the project are encouraged and welcome via pull requests.
- Contributors should adhere to the coding style and guidelines specified in the project repository.

## License
- This project is licensed under the [License Name]. See the LICENSE.md file for detailed information.
