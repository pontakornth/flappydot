import tkinter as tk

from gamelib import Sprite, GameApp, Text

CANVAS_WIDTH = 800
CANVAS_HEIGHT = 500

UPDATE_DELAY = 33
GRAVITY = 2.5

STARTING_VELOCITY = -30
JUMPING_VELOCITY = -20


class Dot(Sprite):
    def init_element(self):
        self.vy = STARTING_VELOCITY
        self.is_started = False
        self.is_gameover = False

    def start(self):
        self.is_started = True

    def update(self):
        if self.is_started:
            self.y += self.vy
            self.vy += GRAVITY

    def jump(self):
        self.vy = JUMPING_VELOCITY

    def is_out_of_screen(self):
        return self.y >= CANVAS_HEIGHT

    def game_over(self):
        self.is_gameover = True


class FlappyGame(GameApp):
    def create_sprites(self):
        self.dot = Dot(self, 'images/dot.png', CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2)

        self.elements.append(self.dot)

    def init_game(self):
        self.is_started = False
        self.is_gameover = False
        self.create_sprites()

    def pre_update(self):
        pass

    def post_update(self):
        # Check for lose condition
        # 1. The dot falls of the screen.
        # 2. The dot hits the pillar
        # TODO: Check for the dot hits the pillar
        if self.dot.is_out_of_screen() and not self.is_gameover:
            self.is_gameover = True
            self.dot.game_over()
            # TODO: Make the message appear in the screen.
            print("GAME OVER")

    def on_key_pressed(self, event):
        if event.char == " ":
            if not (self.is_started or self.is_gameover):
                self.is_started = True
                self.dot.start()
            elif not self.is_gameover:
                self.dot.jump()


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Monkey Banana Game")

    # do not allow window resizing
    root.resizable(False, False)
    app = FlappyGame(root, CANVAS_WIDTH, CANVAS_HEIGHT, UPDATE_DELAY)
    app.start()
    root.mainloop()
