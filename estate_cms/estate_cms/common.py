from PIL import Image

def pad_image(image, bg_color="#fff", **kwargs):
    """ Pad an image to make it the same aspect ratio of the desired thumbnail.
    """
    print("padding", kwargs)
    img_size = image.size
    des_size = kwargs['size']
    fit = [float(img_size[i])/des_size[i] for i in range(0,2)]

    if fit[0] > fit[1]:
        new_image = Image.new(image.mode,
                              (image.size[0], int(round(des_size[1]*fit[0]))),
                              bg_color)
        top = int((new_image.size[1] - image.size[1])/2)
        left = 0
    elif fit[0] < fit[1]:
        new_image = Image.new(image.mode,
                              (int(round(des_size[0]*fit[1])), image.size[1]),
                              bg_color)
        top = 0
        left = int((new_image.size[0] - image.size[0])/2)
    else:
        return image

    # For transparent
    #mask=Image.new('L', new_image.size, color=0)
    #new_image.putalpha(mask)

    new_image.paste(image, (left, top))
    return new_image
