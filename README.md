# Image Tools for DGG Place

## Installation

- Install Python.
- Install pip.
- Install Pillow.

```sh
pip install Pillow
```

\
\
\
\
.

## Usage

### Upres image

3x's the image and moves the original pixel over 1 to the right and 1 down, so its centered.
```sh
python upres.py input.png output.png
```

### Downres image

Does the opposite of upres.
```sh
python downres.py input.png output.png
```

### Position image in 6000x3000

The input needs to be an upressed image.
```sh
python position.py input.png output.png X_POS Y_POS
```

### Crop image out of 6000x3000

Keep in mind you want 1 extra blank pixel around the art at all sides.
```sh
python crop.py input.png output.png X_POS Y_POS WIDTH HEIGHT
```

### Merge many images

You can have as many input images as you want.
```sh
python mergemany.py output.png input_1.png input_2.png input_3.png [...]
```

\
\
\
\
.

## Example Workflow

1. Crop art out of the [dgg-place](https://github.com/destinygg/dgg-place) canvas:
```sh
# python crop.py [input] [output] X_POS Y_POS WIDTH HEIGHT
python crop.py dgg-place-template-1.png chad-large.png 3273 882 483 324
python crop.py dgg-place-template-1.png dirlao-large.png 5019 2775 411 225
python crop.py dgg-place-template-1.png dog-large.png 5433 2808 192 192
python crop.py dgg-place-template-1.png pepe-large.png 3168 2799 270 198
python crop.py dgg-place-template-1.png depresstiny-large.png 396 882 315 381
python crop.py dgg-place-template-1.png ua-large.png 1986 957 1287 306
```

2. Downres large art to small:
```sh
# python downres.py [input] [output]
python downres.py chad-large.png chad-small.png
python downres.py dirlao-large.png dirlao-small.png
python downres.py dog-large.png dog-small.png
python downres.py pepe-large.png pepe-small.png
python downres.py depresstiny-large.png depresstiny-small.png
python downres.py ua-large.png ua-small.png
```

3. At this point you can update the small art!

4. Upres small art to large:
```sh
# python upres.py [input] [output]
python upres.py chad-small.png chad-large.png
python upres.py dirlao-small.png dirlao-large.png
python upres.py dog-small.png dog-large.png
python upres.py pepe-small.png pepe-large.png
python upres.py depresstiny-small.png depresstiny-large.png
python upres.py ua-small.png ua-large.png
```

5. Place large art in a 6000x3000 canvas:
```sh
# python position.py [input] [output] X_POS Y_POS
python position.py chad-large.png chad-canvas.png 3273 882
python position.py dirlao-large.png dirlao-canvas.png 5019 2775
python position.py dog-large.png dog-canvas.png 5433 2808
python position.py pepe-large.png pepe-canvas.png 3168 2799
python position.py depresstiny-large.png depresstiny-canvas.png 396 882
python position.py ua-large.png ua-canvas.png 1986 957
```

6. Merge all canvasses:
```sh
# python mergemany.py [output] [input_1] [input_2] [input_3] etc
python mergemany.py dgg-place-template-1-new.png chad-canvas.png dirlao-canvas.png dog-canvas.png pepe-canvas.png depresstiny-canvas.png ua-canvas.png
```

7. Throw `dgg-place-template-1-new.png` on [dgg-place](https://github.com/destinygg/dgg-place) after you rename it.

\
\
\
\
.

## Disclaimer

I am not a Python dev.\
I just managed to cobble this together with some help from GPT-4. I take no responsability.\
Seems solid tho, right?

