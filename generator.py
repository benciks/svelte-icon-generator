import argparse
import os
import sys
import lxml.html as LH

# Parse command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('-i', help='Input folder', required=True, type=str)
parser.add_argument(
    '-o', help='Output folder - defaults to out/ in current directory', type=str, default='out')

args = parser.parse_args()

input_folder = args.i
output_folder = args.o

# Check if input folder exists
if not os.path.exists(input_folder):
    sys.stderr.write('Error: Input folder does not exist')
    exit(1)

# Create output folder if it does not exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Loop through the svg icons
for filename in os.listdir(input_folder):
    icon = os.path.join(input_folder, filename)
    iconName = filename.split('.')[0]

    # Check if the file is a svg file
    if os.path.isfile(icon) and icon.endswith('.svg'):
        svg = open(icon, 'r')
        out = open(os.path.join(output_folder, iconName + '.svelte'), 'w')

        html = LH.fromstring(svg.read())

        for el in html.iter():
            # Add the class attribute to the svg element
            if el.tag == 'svg':
                el.attrib['class'] = '{style}'

                # Check attributes and replace fill and stroke with currentColor
                if 'fill' in el.attrib and el.attrib['fill'] != 'none':
                    el.attrib['fill'] = 'currentColor'

                if 'stroke' in el.attrib and el.attrib['stroke'] != 'none':
                    el.attrib['stroke'] = 'currentColor'

                # Repeat for children such as paths
                for child in el.iter():
                    if 'fill' in child.attrib and child.attrib['fill'] != 'none':
                        child.attrib['fill'] = 'currentColor'

                    if 'stroke' in child.attrib and child.attrib['stroke'] != 'none':
                        child.attrib['stroke'] = 'currentColor'

        # Write the svelte component
        out.write('<script>\n')
        out.write('export let style = "";\n')
        out.write('</script>\n')
        out.write('\n')

        pretty = LH.etree.tostring(html, encoding="unicode", pretty_print=True)
        out.write(pretty)
