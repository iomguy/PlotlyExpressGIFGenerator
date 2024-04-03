import plotly.express as px
import pandas as pd
import numpy as np

import gif_animation_plotly


r = np.random.RandomState(42)

# sample data
df = pd.DataFrame(
    {
        "step": np.repeat(np.arange(0, 8), 10),
        "x": np.tile(np.linspace(0, 9, 10), 8),
        "y": r.uniform(0, 5, 80),
    }
)

# plotly animated figure
fig = px.bar(df, x="x", y="y", animation_frame="step")

gif_animation_plotly.generate_gif(figure=fig, filename="example.gif")