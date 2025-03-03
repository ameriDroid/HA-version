# Home Assistant Version JSON Mirror

This repository maintains modified mirrors of Home Assistant's version JSON files, with custom download URLs for the indiedroid Nova's OS artifacts.

## Description

This repository automatically fetches and modifies the following Home Assistant version files:
- `stable.json` from `version.home-assistant.io/stable.json`
- `beta.json` from `version.home-assistant.io/beta.json`

The JSON files are modified to replace:
- `https://os-artifacts.home-assistant.io/` 
- with `https://github.com/ameriDroid/HA-operating-system/releases/download/`


## Usage

The modified JSON files are available at:
- Stable: https://ameridroid.github.io/HA-operating-system/stable.json
- Beta: https://ameridroid.github.io/HA-operating-system/beta.json

## License

This repository only contains modified copies of Home Assistant's version files. All rights belong to their respective owners.

## Contributing

If you find any issues or have suggestions for improvements, please open an issue or submit a pull request. 
