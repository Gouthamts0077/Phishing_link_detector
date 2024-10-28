# Phishing_link_detector
Phishing Link Detector 🔍

A Python-based tool to detect and analyze suspicious URLs and identify potential phishing links using pattern recognition and heuristics. This tool is ideal for users looking to add an extra layer of security to their online browsing by quickly checking for phishing indicators in URLs.
Features ✨

    Keyword Analysis: Detects suspicious keywords in URLs that are commonly used in phishing (e.g., "login," "verify," "secure").
    URL Structure Check: Evaluates URL length and the use of special characters.
    Domain Analysis: Identifies suspicious top-level domains (TLDs) frequently associated with phishing.
    Accessibility Validation: Checks if the URL is accessible and monitors for excessive redirects (a common phishing technique).

Setup 🛠️
Prerequisites

    Python 3.6+ is required. You can check your version with:

python3 --version

Requests Library: Install the required library with:

    pip install requests

Installation

    Clone the repository:

git clone https://github.com/your-username/phishing-link-detector.git
cd phishing-link-detector

Ensure dependencies are installed:


    pip install -r requirements.txt

Usage 🚀

Run the script with:


python3 phishing_detector.py

Example:

plaintext

Enter the URL to analyze: http://example-login.freegift.tk

[!] Suspicious keyword found in URL.

[!] URL length is unusually long.

[!] Suspicious Top-Level Domain (TLD) found.

[+] URL is reachable.

[!] Warning: This URL is likely a phishing link.



How It Works 🧠

The tool evaluates the URL using several heuristics:

    Keyword Analysis: Searches for common phishing-related words.
    URL Structure Check: Looks for excessive special characters and lengthy URLs.
    Domain Validation: Flags unusual TLDs associated with free or suspicious domains.
    Reachability Check: Ensures the URL is reachable, identifying multiple redirects as a potential phishing indicator.
