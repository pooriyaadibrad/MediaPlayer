import pygame
import os

class MusicPlayer:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((300, 200))
        pygame.display.set_caption("Music Player")
        self.clock = pygame.time.Clock()
        self.song_list = []
        self.current_song = 0

    def load_songs(self, folder_path):
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                if file.endswith(".mp3"):
                    self.song_list.append(os.path.join(root, file))

    def play_song(self, song_index):
        pygame.mixer.music.load(self.song_list[song_index])
        pygame.mixer.music.play()

    def next_song(self):
        self.current_song = (self.current_song + 1) % len(self.song_list)
        self.play_song(self.current_song)

    def prev_song(self):
        self.current_song = (self.current_song - 1) % len(self.song_list)
        self.play_song(self.current_song)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if pygame.mixer.music.get_busy():
                            pygame.mixer.music.pause()
                        else:
                            pygame.mixer.music.unpause()
                    if event.key == pygame.K_RIGHT:
                        self.next_song()
                    if event.key == pygame.K_LEFT:
                        self.prev_song()

            self.clock.tick(60)

        pygame.quit()

if __name__ == "__main__":
    player = MusicPlayer()
    player.load_songs("D:\Downloads\Music")
    player.play_song(0)
    player.run()