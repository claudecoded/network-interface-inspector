import os
import sys
import subprocess

# Automatically verify and install dependency if missing
try:
    import netifaces as ni
except ImportError:
    print("[INFO] Dependency 'netifaces' not found. Installing now...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "netifaces"])
    import netifaces as ni

def clear_terminal():
    """Clears the terminal screen based on the host Operating System."""
    os.system('cls' if os.name == 'nt' else 'clear')

def inspect_network_interfaces():
    """Loops through all available network interfaces and extracts their IPv4 addresses safely."""
    clear_terminal()
    
    print("Network Interface Inspector")
    print("=" * 30)
    print("🌐 Network Interfaces\n")
    
    # Retrieve a list of all system interface identifiers
    interfaces = ni.interfaces()
    
    for iface in interfaces:
        print(f"📊 {{{iface}}}")
        
        try:
            # Fetch the addresses associated with the interface
            addresses = ni.ifaddresses(iface)
            
            # Check if an IPv4 configuration (AF_INET) exists for this interface
            if ni.AF_INET in addresses:
                # Extract the primary IP address dictionary
                ipv4_info = addresses[ni.AF_INET][0]
                ip_address = ipv4_info.get("addr")
                
                if ip_address:
                    print(f"   IP : {ip_address}")
            else:
                # Silently skip interfaces with no active IPv4 configuration
                pass
                
        except (ValueError, KeyError, IndexError):
            # Safe boundary catch to prevent crashes on protected or virtual system interfaces
            pass
            
        print("-" * 30)

if __name__ == "__main__":
    inspect_network_interfaces()
