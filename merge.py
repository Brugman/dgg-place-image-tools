import sys
from PIL import Image

# check for args
if len(sys.argv) < 4:
    print(' ')
    print('No input and output arguments provided.')
    exit()

# get art
image_one = Image.open( sys.argv[1] )
image_two = Image.open( sys.argv[2] )

# make sure its rgba
image_one = image_one.convert('RGBA')
image_two = image_two.convert('RGBA')

# create canvas
image_merged = Image.new( 'RGBA', image_one.size )

# merge images
image_merged.paste( image_one, ( 0, 0 ) )
image_merged.paste( image_two, ( 0, 0 ), image_two )

# save merged image
image_merged.save( sys.argv[3] )
print(' ')
print(f"Merged image stored as {sys.argv[2]}")

