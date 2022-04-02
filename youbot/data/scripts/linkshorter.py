from pyshorteners import Shortener

async def get_shortLink(url):
    exem = Shortener()
    return exem.tinyurl.short(url)