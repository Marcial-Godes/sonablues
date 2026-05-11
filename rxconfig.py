import reflex as rx

from reflex_base.plugins.sitemap import SitemapPlugin


config = rx.Config(
    app_name="sonablues",

    plugins=[
        rx.plugins.RadixThemesPlugin(),
        SitemapPlugin(),
    ],
)