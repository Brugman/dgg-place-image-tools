import sys
from PIL import Image

# check for args
if len(sys.argv) < 7:
    print(' ')
    print('Incorrect arguments provided.')
    exit()

# get original
image_original = Image.open( sys.argv[1] )

# calc crop args
x_start = int( sys.argv[3] )
y_start = int( sys.argv[4] )
x_end = int( sys.argv[3] ) + int( sys.argv[5] )
y_end = int( sys.argv[4] ) + int( sys.argv[6] )

# crop
image_crop = image_original.crop( ( x_start, y_start, x_end, y_end ) )

# save crop
image_crop.save( sys.argv[2] )
print(' ')
print(f"Cropped image stored as {sys.argv[2]}")

