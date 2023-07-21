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
image_new_w = int( round( image_old_w / 3 ) )
image_new_h = int( round( image_old_h / 3 ) )
# create new
image_new = Image.new('RGBA', ( image_new_w, image_new_h ), color=( 0, 0, 0, 0 ) )

# loop over new pixels
for x_new in range( image_new_w ):
    for y_new in range( image_new_h ):
        # calc old coords
        x_old = ( ( x_new + 1 ) * 3 ) - 1 - 1
        y_old = ( ( y_new + 1 ) * 3 ) - 1 - 1
        # get color
        color = image_old.getpixel( ( x_old, y_old ) )
        # print(f"pixel at {x_old} x {y_old} is color {color}")
        # put pixel
        image_new.putpixel( ( x_new, y_new ), color )

# save new
image_new.save( sys.argv[2] )
print(' ')
print(f"Downressed image stored as {sys.argv[2]}")

