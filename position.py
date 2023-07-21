import sys
from PIL import Image

# check for args
if len(sys.argv) < 5:
    print(' ')
    print('Incorrect arguments provided.')
    exit()

# get art
image_art = Image.open( sys.argv[1] )

# create canvas
image_canvas = Image.new('RGBA', ( 4500, 3000 ), color=( 0, 0, 0, 0 ) )

# paste art on canvas
image_canvas.paste( image_art, ( int( sys.argv[3] ), int( sys.argv[4] ) ) )

# save canvas
image_canvas.save( sys.argv[2] )
print(' ')
print(f"Positioned image stored as {sys.argv[2]}")

