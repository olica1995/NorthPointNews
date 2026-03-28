from kivy.app import App
from kivy.uix.videoplayer import VideoPlayer

class KyogaTVApp(App):
    def build(self):
        # Your specific Kyoga TV Stream
        url = "https://live21.bozztv.com/akamaissh101/ssh101/livetv1995/playlist.m3u8"
        player = VideoPlayer(source=url, state='play', options={'allow_stretch': True})
        return player

if __name__ == "__main__":
    KyogaTVApp().run()
