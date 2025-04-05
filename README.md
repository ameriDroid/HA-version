# Home Assistant Version JSON Files

This repository maintains version information JSON files and AppArmor profiles for Home Assistant components, customized for ameriDroid's builds. The files are automatically updated every 6 hours and published to GitHub Pages.

## JSON Files

The following JSON files are available:

- **Stable**: [`https://ameridroid.github.io/HA-version/stable.json`](https://ameridroid.github.io/HA-version/stable.json)
- **Beta**: [`https://ameridroid.github.io/HA-version/beta.json`](https://ameridroid.github.io/HA-version/beta.json)
- **Dev**: [`https://ameridroid.github.io/HA-version/dev.json`](https://ameridroid.github.io/HA-version/dev.json)

## AppArmor Profiles

The following AppArmor profiles are available:

- **Main**: [`https://ameridroid.github.io/HA-version/apparmor.txt`](https://ameridroid.github.io/HA-version/apparmor.txt)
- **Stable**: [`https://ameridroid.github.io/HA-version/apparmor_stable.txt`](https://ameridroid.github.io/HA-version/apparmor_stable.txt)
- **Beta**: [`https://ameridroid.github.io/HA-version/apparmor_beta.txt`](https://ameridroid.github.io/HA-version/apparmor_beta.txt)
- **Dev**: [`https://ameridroid.github.io/HA-version/apparmor_dev.txt`](https://ameridroid.github.io/HA-version/apparmor_dev.txt)

## Version Sources

- **Home Assistant**: Versions are sourced from the official Home Assistant version JSONs
- **Supervisor**: Latest releases from [ameriDroid/supervisor](https://github.com/ameriDroid/supervisor)
- **Operating System**: Latest releases from [ameriDroid/HA-operating-system](https://github.com/ameriDroid/HA-operating-system)
- **AppArmor Profiles**: Sourced from the official Home Assistant AppArmor profiles

## Automatic Updates

The files are automatically updated every 6 hours via GitHub Actions. The workflow:

1. Fetches the latest versions from all sources
2. Generates new JSON files
3. Updates AppArmor profile files
4. Publishes them to the gh-pages branch
5. Makes them available via GitHub Pages

## Development

To update the files locally:

1. Install Python dependencies:
```bash
pip install requests
```

2. Run the update script:
```bash
python update_json.py
```
