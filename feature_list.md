# Website Security Scanner

## Introduction
This Python script serves as a website security scanner, designed to analyze websites for potential vulnerabilities. It utilizes various techniques to assess the security posture of a given web application or site, including scanning for HTML, JavaScript, CSS, PHP, SSL, HTTP headers, file inclusion, command injection vulnerabilities, and hidden directories. Additionally, it can search for Common Vulnerabilities and Exposures (CVEs) associated with the provided URL.

**Disclaimer:** This tool is intended for ethical security testing purposes only. It should only be used on websites that you have explicit permission to scan. Unauthorized scanning of websites may be illegal and unethical, leading to legal consequences. By using this tool, you agree to use it responsibly and adhere to all applicable laws and regulations.

## Features

### HTML Vulnerability Scanning
- Detection of potential Cross-Site Scripting (XSS) vulnerabilities.
- Identification of deprecated HTML tags.
- Recognition of sensitive data exposure within HTML content.

### JavaScript Vulnerability Scanning
- Detection of potentially dangerous JavaScript functions.
- Analysis of JavaScript code for security risks.

### CSS Vulnerability Scanning
- Identification of potential CSS injection vulnerabilities.
- Detection of URL redirection vulnerabilities within CSS files.

### PHP Endpoint Scanning
- Detection of PHPInfo exposure.
- Additional PHP vulnerability checks can be added as needed.

### SSL Configuration Scanning
- Assessment of SSL certificate expiration.
- Verification of SSL/TLS configurations.

### HTTP Header Scanning
- Evaluation of security-related HTTP headers, including Content-Security-Policy, X-XSS-Protection, X-Content-Type-Options, and X-Frame-Options.

### File Inclusion Vulnerability Scanning
- Detection of file inclusion vulnerabilities.
- Evaluation of file inclusion risks.

### Command Injection Vulnerability Scanning
- Detection of command injection vulnerabilities.
- Analysis of potential command injection points.

### Hidden Directory Detection
- Identification of hidden directories within the website structure.
- Enumeration of hidden paths and directories.

### CVE Search
- Search for CVEs associated with the provided URL.
- Retrieve information on known vulnerabilities related to the website.

### HTML Report Generation
- Generation of an HTML report summarizing the scan results.
- Report includes detailed findings categorized by vulnerability type.

## Usage
1. Run the script and agree to the terms of use.
2. Input the URL of the website to be scanned.
3. The script will analyze the website for vulnerabilities.
4. Upon completion, an HTML report containing the scan results will be generated.

## Dependencies
- Python 3.x
- Requests
- BeautifulSoup
- Jinja2