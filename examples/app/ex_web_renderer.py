from hyo2.abc.app.web_renderer import WebRenderer

wr = WebRenderer(make_app=True)
wr.open("https://www.hydroffice.org")
