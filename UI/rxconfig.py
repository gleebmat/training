import reflex as rx

config = rx.Config(
    app_name="training",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)