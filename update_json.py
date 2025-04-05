import json
import requests
from datetime import datetime
import re

def fetch_ha_json(channel):
    """Fetch the JSON from Home Assistant for given channel"""
    url = f"https://version.home-assistant.io/{channel}.json"
    response = requests.get(url)
    return response.json()

def fetch_github_releases(repo):
    """Fetch releases from a GitHub repository"""
    url = f"https://api.github.com/repos/ameriDroid/{repo}/releases"
    headers = {
        "Accept": "application/vnd.github.v3+json",
        # Add GitHub token if you have rate limiting issues
        # "Authorization": "token YOUR_GITHUB_TOKEN"
    }
    response = requests.get(url, headers=headers)
    return response.json()

def get_os_versions():
    """Get latest OS versions from GitHub releases"""
    releases = fetch_github_releases("HA-operating-system")
    stable_version = None
    beta_version = None
    dev_version = None
    
    for release in releases:
        version = release["tag_name"].strip("v")
        
        # For stable, get the first non-prerelease
        if not release["prerelease"] and not stable_version:
            stable_version = version
            
        # For beta/dev, get the first prerelease
        if release["prerelease"] and not beta_version:
            beta_version = version
            dev_version = version
            
        if stable_version and beta_version:
            break
            
    return {
        "stable": stable_version,
        "beta": beta_version,
        "dev": dev_version
    }

def get_supervisor_versions():
    """Get latest supervisor versions from GitHub releases"""
    releases = fetch_github_releases("supervisor")
    stable_version = None
    latest_version = None  # This will be used for beta/dev
    
    for release in releases:
        version = release["tag_name"]
        
        # Get the very first version as latest (for beta/dev)
        if not latest_version:
            latest_version = version
        
        # For stable, get the first non-prerelease
        if not release["prerelease"] and not stable_version:
            stable_version = version
            
        if stable_version and latest_version:
            break
            
    return {
        "stable": stable_version,
        "beta": latest_version,  # Use latest version for beta
        "dev": latest_version   # Use latest version for dev
    }

def generate_json(channel):
    """Generate JSON for specified channel"""
    # Fetch base structure from HA
    base_json = fetch_ha_json(channel)
    
    # Get latest versions from GitHub
    os_versions = get_os_versions()
    supervisor_versions = get_supervisor_versions()
    
    os_version = os_versions[channel]
    supervisor_version = supervisor_versions[channel]
    
    # Get Home Assistant version for qemuarm-64
    ha_version = base_json["homeassistant"].get("qemuarm-64", base_json["homeassistant"].get("default"))
    
    # Update the JSON structure
    updated_json = {
        "channel": channel,
        "supervisor": supervisor_version if supervisor_version else base_json["supervisor"],
        "homeassistant": {
            "qemuarm-64": ha_version
        },
        "hassos": {
            "nova": os_version
        },
        "hassos-upgrade": base_json["hassos-upgrade"],
        "ota": "https://github.com/ameriDroid/HA-operating-system/releases/download/{version}/{os_name}_{board}-{version}.raucb",
        "cli": base_json["cli"],
        "dns": base_json["dns"],
        "audio": base_json["audio"],
        "multicast": base_json["multicast"],
        "observer": base_json["observer"],
        "image": {
            "core": "ghcr.io/home-assistant/{machine}-homeassistant",
            "supervisor": "ghcr.io/ameridroid/{arch}-hassio-supervisor",
            "cli": "ghcr.io/home-assistant/{arch}-hassio-cli",
            "audio": "ghcr.io/home-assistant/{arch}-hassio-audio",
            "dns": "ghcr.io/home-assistant/{arch}-hassio-dns",
            "observer": "ghcr.io/home-assistant/{arch}-hassio-observer",
            "multicast": "ghcr.io/home-assistant/{arch}-hassio-multicast"
        },
        "images": {
            "core": "ghcr.io/home-assistant/{machine}-homeassistant",
            "supervisor": "ghcr.io/ameridroid/{arch}-hassio-supervisor",
            "cli": "ghcr.io/home-assistant/{arch}-hassio-cli",
            "audio": "ghcr.io/home-assistant/{arch}-hassio-audio",
            "dns": "ghcr.io/home-assistant/{arch}-hassio-dns",
            "observer": "ghcr.io/home-assistant/{arch}-hassio-observer",
            "multicast": "ghcr.io/home-assistant/{arch}-hassio-multicast"
        }
    }
    
    return updated_json

def save_json(data, channel):
    """Save the JSON data to a file with pretty formatting"""
    filename = f"{channel}.json"
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)

def fetch_apparmor_txt():
    """Fetch the apparmor.txt file from Home Assistant"""
    url = "https://version.home-assistant.io/apparmor.txt"
    response = requests.get(url)
    return response.text

def save_apparmor_files(content):
    """Save the apparmor content to various files"""
    # Save the main apparmor.txt
    with open("apparmor.txt", 'w') as f:
        f.write(content)
    
    # Save channel-specific versions
    for channel in ["stable", "beta", "dev"]:
        with open(f"apparmor_{channel}.txt", 'w') as f:
            f.write(content)

if __name__ == "__main__":
    try:
        # Generate and save JSON files
        for channel in ["stable", "beta", "dev"]:
            json_data = generate_json(channel)
            save_json(json_data, channel)
            print(f"Successfully generated {channel}.json")
        
        # Fetch and save apparmor files
        apparmor_content = fetch_apparmor_txt()
        save_apparmor_files(apparmor_content)
        print("Successfully updated apparmor text files")
    except Exception as e:
        print(f"Error generating files: {str(e)}") 