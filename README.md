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

COMING SOON

## Examples

Get art (chad) from canvas (dgg-place-template-1.png):
```sh
python crop.py dgg-place-template-1.png dgg-large.png 1773 882 483 321
```

Downres large art to small:
```sh
python downres.py dgg-large.png dgg-small.png
```

Upres small art to large:
```sh
python upres.py dgg-small.png dgg-large.png
```

Place large art in canvas:
```sh
python position.py dgg-large.png dgg-place-template-1-new.png 1773 882
```

## Disclaimer

I am not a Python dev. I just managed to cobble this together with some help from GPT-4. I take no responsability. Seems solid tho, right?

