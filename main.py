from kivy.app import App
from kivy.uix.videoplayer import VideoPlayer
import os

class KyogaTVApp(App):
    def build(self):
        # Kyoga TV Live Stream
        url = "https://live21.bozztv.com/akamaissh101/ssh101/livetv1995/playlist.m3u8"
        
        # We use the built-in VideoPlayer which is stable on Android
        player = VideoPlayer(
            source=url, 
            state='play', 
            options={'allow_stretch': True}
        )
        return player

if __name__ == "__main__":
    KyogaTVApp().run()
