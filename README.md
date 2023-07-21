# Image Tools for DGG Place

## Installation

- Install Python.
- Install pip.

```sh
pip install Pillow
```

## Usage

### Upres image

```sh
python upres.py input.png output.png
```

### Downres image

```sh
python downres.py input.png output.png
```

### Position image in 4500x3000

```sh
python position.py input.png output.png X_POS Y_POS
```

### Crop image out of 4500x3000

```sh
python crop.py input.png output.png X_POS Y_POS WIDTH HEIGHT
```

## Examples

Get art from canvas (dgg-place-template-1.png):

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

