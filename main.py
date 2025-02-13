import pygame
import sys

class Button: # здесь класс для кнопок
    def __init__(self, x, y, width, height, text, image_path, hover_image_path=None, sound_path=None):
        self.x = x
        self.y = y
        self.width = width
        self.text = text

        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.hover_image = self.image
        if hover_image_path:
            self.hover_image = pygame.image.load(hover_image_path)
            self.hover_image = pygame.transform.scale(self.hover_image, (width, height))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.sound = None
        if sound_path:
            self.sound = pygame.mixer.Sound(sound_path)
        self.is_hovered = False

    def draw(self, screen): # смена картинки у кнопки
        current_image = self.hover_image if self.is_hovered else self.image
        screen.blit(current_image, self.rect.topleft)

        font = pygame.font.Font(None, 36)
        text_surface = font.render(self.text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def check_hover(self, mouse_pos): # координаты
        self.is_hovered = self.rect.collidepoint(mouse_pos)

    def handle_event(self, event): # для музыки во время нажатия на кнопку
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1 and self.is_hovered:
            if self.sound:
                self.sound.play()
            pygame.event.post(pygame.event.Event(pygame.USEREVENT,button=self))

pygame.init()
width, height = 1900, 1000
fps = 60
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('game')

clock = pygame.time.Clock()

def main_meno(): # самое первое окно, стартовое
    start_button = Button(670, 500, 900, 200, "", "play yellow-Photoroom_Nero AI_Photo.png",
                          "play-2-Photoroom_Nero AI_Photo.png", "8af5b2bf5d19c00.mp3")
    quit_button = Button(670, 740, 900, 200, "", "quit yellow-Photoroom_Nero AI_Photo.png",
                         "quit-2-Photoroom_Nero AI_Photo.png", "8af5b2bf5d19c00.mp3")
    options_button = Button(1700, 70, 200, 200, "", "настройки-no-bg-preview (carve,photos)_enhanced.png",
                            "настройки-no-bg-preview (carve,photos)_enhanced.png", "8af5b2bf5d19c00.mp3")
    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(pygame.image.load("фон (2)_Nero AI_Photo (1).jpg"), (0, 0))
        # название игры
        image = pygame.image.load("f-no-bg-preview (carve.photos)_N.png").convert_alpha()
        screen.blit(image, (200, 70))
        image = pygame.image.load("L-no-bg-preview (carve,photos)_e.png").convert_alpha()
        screen.blit(image, (320, 70))
        image = pygame.image.load("a-fotor-bg-remover-2025021222143.png").convert_alpha()
        screen.blit(image, (440, 90))
        image = pygame.image.load("P-no-bg-preview (carve,photos)_e.png").convert_alpha()
        screen.blit(image, (560, 70))
        image = pygame.image.load("P-no-bg-preview (carve,photos)_e.png").convert_alpha()
        screen.blit(image, (680, 70))
        image = pygame.image.load("Y-no-bg-preview (carve,photos)_e.png").convert_alpha()
        screen.blit(image, (800, 70))
        image = pygame.image.load("B-no-bg-preview (carve,photos)_e.png").convert_alpha()
        screen.blit(image, (560, 270))
        image = pygame.image.load("i-no-bg-preview (carve,photos)_e.png").convert_alpha()
        screen.blit(image, (680, 270))
        image = pygame.image.load("R-no-bg-preview (carve,photos)_e.png").convert_alpha()
        screen.blit(image, (800, 270))
        image = pygame.image.load("d-no-bg-preview (carve,photos)_e.png").convert_alpha()
        screen.blit(image, (920, 270))


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.USEREVENT and event.button == start_button: # для вызова меню с уровнями, при нажатии кнопки start
                start_meno()
            if event.type == pygame.USEREVENT and event.button == quit_button: # для завршения работы программы, при нажатии кнопки quit
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.USEREVENT and event.button == options_button: # переносит на настройки
                setting_meno()

            start_button.handle_event(event)
            options_button.handle_event(event)
            quit_button.handle_event(event)

        start_button.check_hover(pygame.mouse.get_pos())
        options_button.check_hover(pygame.mouse.get_pos())
        quit_button.check_hover(pygame.mouse.get_pos())
        start_button.draw(screen)
        options_button.draw(screen)
        quit_button.draw(screen)
        pygame.display.flip()

def setting_meno(): # меню с настройками
    left_button = Button(700, 550, 250, 250, "",
                         "влево-no-bg-preview (carve,photos)_enhanced.png",
                         "влево-no-bg-preview (carve,photos)_enhanced.png",
                         "8af5b2bf5d19c00.mp3")
    music_button = Button(1020, 550, 250, 250, "",
                          "музыка-edited-free (carve,photos)_enhanced.png",
                          "музыка-edited-free (carve,photos)_enhanced.png",
                          "8af5b2bf5d19c00.mp3")
    sound_button = Button(700, 300, 250, 250, "",
                          "звук-no-bg-preview (carve,photos)_enhanced.png",
                          "звук-no-bg-preview (carve,photos)_enhanced.png",
                          "8af5b2bf5d19c00.mp3")
    pravila_button = Button(1020, 300, 250, 250, "",
                            "правила-no-bg-preview (carve,photos)_enhanced.png",
                            "правила-no-bg-preview (carve,photos)_enhanced.png",
                            "8af5b2bf5d19c00.mp3")

    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(pygame.image.load("фон (2)_Nero AI_Photo (1).jpg"), (-300, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

            if event.type == pygame.USEREVENT and event.button == left_button:
                running = False

            left_button.handle_event(event)
            music_button.handle_event(event)
            sound_button.handle_event(event)
            pravila_button.handle_event(event)
        music_button.check_hover(pygame.mouse.get_pos())
        sound_button.check_hover(pygame.mouse.get_pos())
        pravila_button.check_hover(pygame.mouse.get_pos())
        left_button.check_hover(pygame.mouse.get_pos())
        music_button.draw(screen)
        sound_button.draw(screen)
        pravila_button.draw(screen)
        left_button.draw(screen)
        pygame.display.flip()


def start_meno(): # меню где уровни
    left_button = Button(100, 780, 180, 180, "",
                         "влево-no-bg-preview (carve,photos)_enhanced.png",
                         "влево-no-bg-preview (carve,photos)_enhanced.png",
                         "8af5b2bf5d19c00.mp3")
    level_1_button = Button(680, 150, 600, 250, "",
                            "level1_Nero AI_Photo-edited-free (carve.photos).png",
                         "level1_Nero AI_Photo-edited-free (carve.photos).png",
                            "8af5b2bf5d19c00.mp3")
    level_2_button = Button(680, 450, 600, 250, "",
                            "level2_Nero AI_Photo-edited-free (carve.photos).png",
                         "level2_Nero AI_Photo-edited-free (carve.photos).png",
                            "8af5b2bf5d19c00.mp3")
    level_3_button = Button(680, 710, 600, 250, "",
                            "level3_Nero AI_Photo-edited-free (carve.photos).png",
                         "level3_Nero AI_Photo-edited-free (carve.photos).png",
                            "8af5b2bf5d19c00.mp3")
    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(pygame.image.load("фон (2)_Nero AI_Photo (1).jpg"), (-300, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

            if event.type == pygame.USEREVENT and event.button == left_button:
                running = False

            if event.type == pygame.USEREVENT and event.button == level_1_button:
                level_1()

            left_button.handle_event(event)
            level_1_button.handle_event(event)
            level_2_button.handle_event(event)
            level_3_button.handle_event(event)

        left_button.check_hover(pygame.mouse.get_pos())
        left_button.draw(screen)
        level_1_button.check_hover(pygame.mouse.get_pos())
        level_1_button.draw(screen)
        level_2_button.check_hover(pygame.mouse.get_pos())
        level_2_button.draw(screen)
        level_3_button.check_hover(pygame.mouse.get_pos())
        level_3_button.draw(screen)
        pygame.display.flip()

def level_1(): # 1 уровень
    bg_x = 0
    bg_sound = pygame.mixer.Sound("1 левел.mp3")
    bg_sound.play(-1)
    fon = pygame.image.load('фон__enhanced_enhanced (1).png')
    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(fon, (bg_x, 0))
        screen.blit(fon, (bg_x + 1900, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

        bg_x -= 1
        if bg_x == -1900:
            bg_x = 0

        pygame.display.flip()

if __name__ == "__main__":
    main_meno()