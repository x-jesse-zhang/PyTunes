import os
import pyglet
# Disable error checking for increased performance
pyglet.options['debug_gl'] = False
from pyglet import gl

VERSION = '5.9'

import kytten
from background import Background

dialog = kytten.Dialog(
        kytten.TitleFrame("Kytten Demo",
            kytten.VerticalLayout([
                kytten.Label("Select dialog to show"),
                kytten.Menu(options=["Document", "Form", "Scrollable"],
                            on_select=on_select),
            ]),
        ),
        window=window, batch=batch, group=fg_group,
        anchor=kytten.ANCHOR_TOP_LEFT,
        theme=theme)