# About

## Overview
The Website Security Scanner is a sophisticated Python script meticulously designed to empower security professionals, developers, and website administrators with robust capabilities for identifying and mitigating potential vulnerabilities within web applications. This tool serves as an essential asset in the arsenal of security practitioners, offering an automated and comprehensive approach to security testing.

## Purpose
In today's digital landscape, web applications are continuously exposed to evolving threats, ranging from common vulnerabilities like Cross-Site Scripting (XSS) to complex security risks such as command injection and SSL misconfigurations. The primary purpose of the Website Security Scanner is to provide a proactive defense mechanism against these threats by facilitating systematic vulnerability assessment and detection. By automating the scanning process, the script aims to streamline security assessments, accelerate vulnerability identification, and ultimately enhance the resilience of web applications against potential cyber attacks.

## Features
### Comprehensive Scanning Capabilities
- **HTML Vulnerability Scanning:** Detects XSS vulnerabilities, deprecated HTML tags, and potential exposure of sensitive data within HTML content.
- **JavaScript Vulnerability Scanning:** Analyzes JavaScript code for potential security risks, including the usage of dangerous functions.
- **CSS Vulnerability Scanning:** Identifies CSS injection vulnerabilities and URL redirection risks within CSS files.
- **PHP Endpoint Scanning:** Checks for PHPInfo exposure and other PHP-related vulnerabilities.
- **SSL Configuration Scanning:** Evaluates SSL certificate expiration, SSL/TLS configurations, and potential security weaknesses.
- **HTTP Header Scanning:** Assess security-related HTTP headers to ensure proper security controls are in place.
- **File Inclusion and Command Injection Scanning:** Detects file inclusion vulnerabilities and potential command injection points.
- **Hidden Directory Detection:** Identifies hidden directories within the website structure, enhancing reconnaissance capabilities.

### CVE Search Functionality
- Enables users to search for Common Vulnerabilities and Exposures (CVEs) associated with a given website, providing insights into known vulnerabilities and potential risks.

### HTML Report Generation
- Generates comprehensive HTML reports summarizing the scan results, facilitating in-depth analysis and reporting of security findings.
- Reports are structured and well-organized, providing clear visibility into identified vulnerabilities and their severity levels.

### User-Friendly Interface
- Features a simple command-line interface, making it accessible to users of all skill levels.
- Offers intuitive prompts and instructions, guiding users through the scanning process seamlessly.

## Scan Types

### HTML Vulnerability Scanning
HTML vulnerability scanning involves analyzing the HTML content of the website to identify potential security risks. This includes detecting XSS vulnerabilities, deprecated HTML tags, and instances of sensitive data exposure within the HTML code.

### JavaScript Vulnerability Scanning
JavaScript vulnerability scanning focuses on assessing the JavaScript code used within the website for security risks. This includes analyzing for the usage of dangerous functions and potential vulnerabilities within the JavaScript implementation.

### CSS Vulnerability Scanning
CSS vulnerability scanning aims to identify security issues within the Cascading Style Sheets (CSS) used in the website. This includes detecting CSS injection vulnerabilities and potential risks related to URL redirection within CSS files.

### PHP Endpoint Scanning
PHP endpoint scanning involves checking for vulnerabilities related to PHP endpoints within the website. This includes detecting PHPInfo exposure and other potential PHP-related security risks.

### SSL Configuration Scanning
SSL configuration scanning evaluates the Secure Sockets Layer (SSL) configuration of the website for potential security weaknesses. This includes assessing SSL certificate expiration, SSL/TLS configurations, and other SSL-related risks.

### HTTP Header Scanning
HTTP header scanning assesses the HTTP headers sent by the website to ensure proper security controls are in place. This includes checking for security-related headers such as Content-Security-Policy, X-XSS-Protection, X-Content-Type-Options, and X-Frame-Options.

### File Inclusion and Command Injection Scanning
File inclusion and command injection scanning involves detecting vulnerabilities related to file inclusion and command injection within the website. This includes identifying potential points of exploitation and assessing the risk associated with these vulnerabilities.

### Hidden Directory Detection
Hidden directory detection aims to identify hidden directories within the website structure. This enhances reconnaissance capabilities and helps in discovering potential security risks.

## License
The Website Security Scanner is licensed under the MIT License, providing users with the freedom to use, modify, and distribute the software in accordance with the terms of the license. Refer to the LICENSE.md file for detailed licensing information.
