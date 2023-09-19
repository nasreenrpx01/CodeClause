import hashlib

# Dictionary to store URL mappings
url_mapping = {}

# Function to generate a short URL
def shorten_url(long_url):
    # Generate a unique hash for the long URL using MD5
    hash_object = hashlib.md5(long_url.encode())
    hash_hex = hash_object.hexdigest()
    
    # Take the first 8 characters of the hash as the short URL
    short_url = hash_hex[:8]
    
    # Store the mapping in the dictionary
    url_mapping[short_url] = long_url
    
    return short_url

# Function to expand a short URL
def expand_url(short_url):
    # Check if the short URL exists in the dictionary
    if short_url in url_mapping:
        return url_mapping[short_url]
    else:
        return "Short URL not found"

# Main program
while True:
    print("URL Shortener Menu:")
    print("1. Shorten URL")
    print("2. Expand Short URL")
    print("3. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        long_url = input("Enter the long URL to shorten: ")
        short_url = shorten_url(long_url)
        print(f"Shortened URL: {short_url}")
    elif choice == '2':
        short_url = input("Enter the short URL to expand: ")
        long_url = expand_url(short_url)
        print(f"Expanded URL: {long_url}")
    elif choice == '3':
        break
    else:
        print("Invalid choice. Please try again.")
