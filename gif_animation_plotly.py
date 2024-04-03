import plotly.express as px
import io
import PIL


def generate_gif(figure, filename, duration=500):
    '''
    generate ...
    '''    
    # generate images for each 'animation step' of the plotly figure
    frames = []
    for s, fr in enumerate(figure.frames):
        # set main traces to appropriate traces within plotly frame
        figure.update(data=fr.data)
        # move slider to correct place
        figure.layout.sliders[0].update(active=s)
        # generate image of current state
        frames.append(PIL.Image.open(io.BytesIO(figure.to_image(format="png"))))
        
    # create animated GIF
    frames[0].save(
            filename,
            save_all=True,
            append_images=frames[1:],
            optimize=True,
            duration=duration,
            loop=0,
        )