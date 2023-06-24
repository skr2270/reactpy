from fastapi import FastAPI
from reactpy import component, html
from reactpy.backend.fastapi import configure


@component
def Photo():
    return html.section(
        html.h1("Saikumar's About Featured Image"),
        html.p(html.b("SKR"), " stands for:"),
        html.ul(html.li("S: Sai"), html.li("K: Kumar"), html.li("R: Rayavarapu")),
        html.img(
            {
                "src": "https://cdn.hashnode.com/res/hashnode/image/upload/v1606381729046/WRX4JmNNV.jpeg?w=500&h=500&fit=crop&crop=faces&auto=compress,format&format=webp",
                "style": {"height": "50%"},
                "alt": "Saikumar's About Image",
            }
        ),
    )


app = FastAPI()
configure(app, Photo)
