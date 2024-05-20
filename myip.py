import subprocess

# Function to check if the requests library is installed
def check_requests_installed():
    try:
        import requests
        return True
    except ImportError:
        return False

# Function to install the requests library using pip
def install_requests():
    subprocess.check_call(['pip', 'install', 'requests'])

# Function to get public IP address
def get_public_ip():
    try:
        import requests
        response = requests.get('https://httpbin.org/ip')
        data = response.json()
        public_ip = data['origin']
        return public_ip
    except Exception as e:
        print("Error fetching public IP:", e)
        return None

# Function to print IP address with highlighting
def print_highlighted_ip(ip_address):
    print("\033[91m{}\033[0m".format(ip_address))  # ANSI escape code for red color

if __name__ == "__main__":
    if not check_requests_installed():
        print("Requests library not found. Installing...")
        install_requests()
    
    public_ip = get_public_ip()
    if public_ip:
        print("Your public IP address is: ", end="")
        print_highlighted_ip(public_ip)
