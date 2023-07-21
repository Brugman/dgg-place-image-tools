# Image Tools for DGG Place

## Installation

- Install Python.
- Install pip.
- Install Pillow.

```sh
pip install Pillow
```

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

### Position image in 4500x3000

Needs an upressed image.
```sh
python position.py input.png output.png X_POS Y_POS
```

### Crop image out of 4500x3000

Keep in mind you want 1 extra blank pixel around the art at all sides.
```sh
python crop.py input.png output.png X_POS Y_POS WIDTH HEIGHT
```

### Merge 2 images

```sh
python merge.py input_1.png input_2.png output.png
```

## Example Workflow

Get art from canvas (dgg-place-template-1.png):
```sh
python crop.py dgg-place-template-1.png chad-large.png 1773 882 483 321
python crop.py dgg-place-template-1.png depresstiny-large.png 3351 2190 360 396
```

Downres large art to small:
```sh
python downres.py chad-large.png chad-small.png
python downres.py depresstiny-large.png depresstiny-small.png
```

This is where you would update the art.

Upres small art to large:
```sh
python upres.py chad-small.png chad-large.png
python upres.py depresstiny-small.png depresstiny-large.png
```

Place large art in mega canvas:
```sh
python position.py chad-large.png canvas-chad.png 1773 882
python position.py depresstiny-large.png canvas-depresstiny.png 3351 2190
```

Merge canvasses:
```sh
python merge.py canvas-chad.png canvas-depresstiny.png dgg-place-template-1-new.png
```

## Disclaimer

I am not a Python dev. I just managed to cobble this together with some help from GPT-4. I take no responsability. Seems solid tho, right?

