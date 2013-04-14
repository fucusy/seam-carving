import Image


#representation of image for seam carving
class sc_Image
    def __init__(self, dimensions, pixels): 
    	self.width = pos[0]
    	self.height = pos[1]
    	self.pixels = pixels

    def set_energies():
    	raise NotImplementedError

    # gets the energy of the pixel at a position
    def get_energy (self, pos) :
		if algorithm = 'e1':
			raise NotImplementedError

		elif algorithm = 'e2':
			raise NotImplementedError

		else
			raise Exception("%s is one of the implemented algorithms" %s algorithm)

class Pixel:
    def __init__(self, pos, rgb): 
    	self.pos = pos
    	self.rgb = rgb
    	self.energy = 0

    # get the neighbors of a pixel given an image
    def get_neighbors (self, image):
    	raise NotImplementedError

    # to string function
    def __str__(self):
        return "[%s - %s]" % (str(self.pos), str(self.rgb))

def data_from_image(filepath):
	image = {}
	im = Image.open (filepath)
	width, height = im.size
	for h in range(height):
		for w in range(width):
			image[(w,h)] = Pixel( (w,h), im.getpixel((w,h)) )
	return sc_Image()

def image_from_data (image):
	raise NotImplementedError
