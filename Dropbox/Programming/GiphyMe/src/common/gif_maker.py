from PIL import Image, ImageDraw
import tempfile as tp
import imageio
import os
from src.config import Config


def iter_frames(im):
    try:
        i= 0
        while 1:
            im.seek(i)
            imframe = im.copy()
            if i == 0:
                palette = imframe.getpalette()
            else:
                imframe.putpalette(palette)
            yield imframe
            i += 1
    except EOFError:
        pass


## Expand gifs into frames with temp folder
def expand_gif(input_filename):
    im = Image.open(input_filename)
    test_folder = tp.mkdtemp()
    gif_images = []
    for i, frame in enumerate(iter_frames(im)):
        frame.save(test_folder + '/gifs%d.png' % i, **frame.info)
        gif_images.append('gifs%d.png' % i)
    print os.listdir(test_folder)
    print test_folder
    return gif_images, test_folder


## Create images from
def create_gif(gif_images, output_filename):
    images = []
    for filename in gif_images:
        images.append(imageio.imread(filename))
    imageio.mimsave(Config.UPLOAD_FOLDER + output_filename, images)

def test_gif():
    folder = "/Users/mattujet/Desktop/GiphyMe/giphyme/Dropbox/Programming/GiphyMe/src/"
    listing = os.listdir(folder)
    images = []
    for filename in listing:
        filename = "/Users/mattujet/Desktop/GiphyMe/giphyme/Dropbox/Programming/GiphyMe/src/"+filename
        images.append(imageio.imread(filename))
    imageio.mimsave('new_giphyme.gif',images)
    return 200




def print_images():
    folder = "/Users/mattujet/Desktop/GiphyMe/giphyme/Dropbox/Programming/GiphyMe/src/"
    listing = os.listdir(folder)
    os.remove("/Users/mattujet/Desktop/GiphyMe/giphyme/Dropbox/Programming/GiphyMe/src/.DS_Store")
    for filename in listing:
        print filename

## Expand gifs into frames old method with no temp folders
# def expand_gif_old(input_filename):
#     im = Image.open(input_filename)
#     gif_images = []
#     for i, frame in enumerate(iter_frames(im)):
#         frame.save('gifs%d.png' % i, **frame.info)
#         gif_images.append('gifs%d.png' % i)
#     return gif_images

# test = expand_gif('new.gifs')
# create_gif(test,'new_1.gifs')