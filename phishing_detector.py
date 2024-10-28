import re
import requests

# Sample keywords commonly found in phishing URLs
PHISHING_KEYWORDS = [
    "login", "signin", "verify", "account", "update", "secure", "banking",
    "free", "gift", "prize", "win", "alert", "confirm", "support"
]

# Suspicious TLDs often used in phishing
SUSPICIOUS_TLDS = [".tk", ".ml", ".ga", ".cf", ".gq"]

def check_suspicious_patterns(url):
    """
    Analyze URL for suspicious patterns commonly found in phishing sites.
    """
    suspicious_count = 0
    
    # Check for keywords
    if any(keyword in url.lower() for keyword in PHISHING_KEYWORDS):
        print("[!] Suspicious keyword found in URL.")
        suspicious_count += 1
    
    # Check for long URL length
    if len(url) > 75:
        print("[!] URL length is unusually long.")
        suspicious_count += 1
    
    # Check for multiple special characters
    if len(re.findall(r"[._\-@]", url)) > 4:
        print("[!] Excessive special characters in URL.")
        suspicious_count += 1

    # Check if TLD is suspicious
    if any(url.endswith(tld) for tld in SUSPICIOUS_TLDS):
        print("[!] Suspicious Top-Level Domain (TLD) found.")
        suspicious_count += 1

    return suspicious_count

def validate_url(url):
    """
    Validate if URL is reachable and possibly legitimate.
    """
    try:
        response = requests.get(url, timeout=5)
        # Check if URL redirects too many times (a phishing pattern)
        if len(response.history) > 3:
            print("[!] Excessive redirects detected.")
            return False
        if response.status_code == 200:
            print("[+] URL is reachable.")
            return True
        else:
            print(f"[!] URL returned status code: {response.status_code}")
            return False
    except requests.RequestException as e:
        print(f"[!] Error reaching the URL: {e}")
        return False

def identify_phishing_link(url):
    """
    Identify if a URL is potentially a phishing link.
    """
    print(f"\nAnalyzing URL: {url}")
    
    # Step 1: Check for suspicious patterns
    suspicious_count = check_suspicious_patterns(url)
    
    # Step 2: Validate URL accessibility
    if not validate_url(url):
        print("[!] URL is likely phishing.")
        return

    # Final check
    if suspicious_count >= 2:
        print("[!] Warning: This URL is likely a phishing link.")
    else:
        print("[+] This URL appears to be safe.")

def main():
    print("Welcome to the Phishing Link Detection Tool!")
    url = input("Enter the URL to analyze: ")
    identify_phishing_link(url)

if __name__ == "__main__":
    main()

