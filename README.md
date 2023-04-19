# svelte-icon-generator
A small python script that converts svg icons to svelte components. Resulting components have prop **style** which can be used to assign css classes to them. Styling works the best with tailwind.

## Requirements
- python3

## Install
```
git clone git@github.com:benciks/svelte-icon-generator.git
pip install -r requirements.txt
```

## Usage
```
usage: generator.py [-h] -i I [-o O]
```

Arguments:
- -i INPUT_FOLDER - Folder should contain svg files (Other formats are ignored) - Required
- -o OUTPUT_FOLDER - Default to "out" in current directory

After generating the files, you can copy them over to your project and the use is following:
```html
<script>
import ExampleIcon from '$lib/assets/icons/example.svelte';
</script>

<ExampleIcon style="text-blue-600 h-6 w-6" />
``` 