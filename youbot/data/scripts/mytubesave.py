import pytube



class YouSave():
    def __init__(self,url):
        self.url = url
        try:
            self.video = pytube.YouTube(url)
            self.api = self.video.vid_info
        except pytube.exceptions.RegexMatchError:
            self.video = None
        self.is_valid = (self.video == None)

    async def get_title(self):
        if self.is_valid:
            return None
        return self.video.title
    
    async def get_author(self):
        if self.is_valid:
            return None
        return self.api["videoDetails"]["author"]

    async def get_imgUrl(self):
        if self.is_valid:
            return None
        return self.api["videoDetails"]["thumbnail"]["thumbnails"][-1]["url"]

    async def get_video(self):        
        if self.is_valid:
            return None

        quality = dict()
        formats = self.api["streamingData"]["adaptiveFormats"]
        for format in formats:
            if "video/mp4;" in format["mimeType"]:
                quality[format["qualityLabel"]] = format["url"]
        return quality
