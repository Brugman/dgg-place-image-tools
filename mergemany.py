import sys
from PIL import Image

# check for args
if len(sys.argv) < 4:
    print(' ')
    print('No input and output arguments provided.')
    exit()

# get image paths
images_path = sys.argv[2:]

# collect image data
images_data = []

for index, item in enumerate( images_path ):
    image_temp = Image.open( item )
    image_temp = image_temp.convert('RGBA')
    images_data.append( image_temp )

# create canvas
image_one = Image.open( sys.argv[2] )
image_final = Image.new( 'RGBA', image_one.size )

# merge images
for index, item in enumerate( images_data ):
    image_final.paste( item, ( 0, 0 ), item )

# save merged image
image_final.save( sys.argv[1] )
print(' ')
print(f"Merged image stored as {sys.argv[1]}")

