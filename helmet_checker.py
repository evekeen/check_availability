import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
import time
import random
import argparse

def check_helmet_availability(url):
    # Add randomized user agent to avoid being blocked
    user_agents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
    ]
    
    headers = {
        'User-Agent': random.choice(user_agents),
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Cache-Control': 'max-age=0'
    }
    
    try:
        # Add small delay to mimic human behavior
        time.sleep(random.uniform(1, 3))
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find product name
        product_title = soup.select_one('.product-title h3')
        product_name = product_title.text.strip() if product_title else "Unknown Product"
        
        # Find all size elements
        size_inputs = soup.select('li input[name=product-size]')
        
        available_sizes = []
        unavailable_sizes = []
        
        for size_input in size_inputs:
            size_value = size_input.get('value')
            if size_input.has_attr('disabled'):
                unavailable_sizes.append(size_value)
            else:
                available_sizes.append(size_value)
        
        # Create report
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        report = f"Helmet Availability Report for {product_name} - {now}\n\n"
        
        if available_sizes:
            report += "Available sizes: " + ", ".join(available_sizes) + "\n"
        else:
            report += "No sizes available at the moment.\n"
            
        report += "Unavailable sizes: " + ", ".join(unavailable_sizes) + "\n"
        
        # Include URL for reference
        report += f"\nCheck the product at: {url}"
        
        return report
    except Exception as e:
        return f"Error checking availability: {str(e)}"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Check helmet availability on a product page")
    parser.add_argument("url", help="URL of the product page to check")
    args = parser.parse_args()
    
    report = check_helmet_availability(args.url)
    print(report)
    # send_email(report) 