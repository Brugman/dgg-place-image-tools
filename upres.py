import sys
from PIL import Image

# check for args
if len(sys.argv) < 3:
    print(' ')
    print('No input and output arguments provided.')
    exit()

# get old
image_old = Image.open( sys.argv[1] )
# get size of old
image_old_w, image_old_h = image_old.size

# calc size of new
image_new_w = int( round( image_old_w * 3 ) )
image_new_h = int( round( image_old_h * 3 ) )
# create new
image_new = Image.new('RGBA', ( image_new_w, image_new_h ), color=( 0, 0, 0, 0 ) )

# loop over old pixels
for x_old in range( image_old_w ):
    for y_old in range( image_old_h ):
        # get color
        color = image_old.getpixel( ( x_old, y_old ) )
        # print(f"pixel at {x_old} x {y_old} is color {color}")
        # calc new coords
        x_new = ( ( x_old + 1 ) * 3 ) - 1 - 1
        y_new = ( ( y_old + 1 ) * 3 ) - 1 - 1
        # put pixel
        image_new.putpixel( ( x_new, y_new ), color )

# save new
image_new.save( sys.argv[2] )
print(' ')
print(f"Upressed image stored as {sys.argv[2]}")

