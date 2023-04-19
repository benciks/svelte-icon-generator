# svelte-icon-generator
A small python script that converts svg icons to svelte components that export prop **style** which can be used to assign classes to them. Tailwind is recommended but in no way required.

## Requirements
- python3

## Install
```
source venv/bin/activate
pip install -r requirements.txt
```

## Usage
```
usage: generator.py [-h] -i I [-o O]
```

Arguments:
- -i INPUT_FOLDER = Input folder containing svg files (Other formats are ignored) - Required
- -o OUTPUT_FOLDER = Output folder - default to "out" in current directory