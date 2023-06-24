from reactpy import component, html, run


@component
def App():
    return html.section(
        html.h1("Welcome to Saikumar's ReactPy Application"),
        html.p("This is my first webpage built using ReactPy with starlette"),
    )


run(App)
