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
width, height = 1366, 768
fps = 60
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('game')

main_sound = pygame.mixer.Sound("Feel-Good(chosic.com).mp3")
bg_sound = pygame.mixer.Sound("1 левел.mp3")
main_music, bg_music = True, True
clock = pygame.time.Clock()

def main_meno(): # самое первое окно, стартовое
    start_button = Button(380, 400, 650, 150, "", "play yellow-Photoroom_Nero AI_Photo.png",
                          "play-2-Photoroom_Nero AI_Photo.png", "8af5b2bf5d19c00.mp3")
    quit_button = Button(380, 600, 650, 150, "", "quit yellow-Photoroom_Nero AI_Photo.png",
                         "quit-2-Photoroom_Nero AI_Photo.png", "8af5b2bf5d19c00.mp3")
    options_button = Button(1200, 40, 150, 150, "", "настройки-no-bg-preview (carve,photos)_enhanced.png",
                            "настройки-no-bg-preview (carve,photos)_enhanced.png", "8af5b2bf5d19c00.mp3")
    running = True
    main_sound.play(-1)
    while running:
        screen.fill((0, 0, 0))
        screen.blit(pygame.image.load("фон (2)_Nero AI_Photo (1).jpg"), (0, 0))
        # название игры
        image = pygame.image.load("f-no-bg-preview (carve.photos)_N.png").convert_alpha()
        new_image = pygame.transform.scale(image, (60, 100))
        screen.blit(new_image, (40, 40))
        image = pygame.image.load("L-no-bg-preview (carve,photos)_e.png").convert_alpha()
        new_image = pygame.transform.scale(image, (60, 100))
        screen.blit(new_image, (100, 40))
        image = pygame.image.load("a-fotor-bg-remover-2025021222143.png").convert_alpha()
        new_image = pygame.transform.scale(image, (60, 100))
        screen.blit(new_image, (160, 40))
        image = pygame.image.load("P-no-bg-preview (carve,photos)_e.png").convert_alpha()
        new_image = pygame.transform.scale(image, (60, 100))
        screen.blit(new_image, (220, 40))
        image = pygame.image.load("P-no-bg-preview (carve,photos)_e.png").convert_alpha()
        new_image = pygame.transform.scale(image, (60, 100))
        screen.blit(new_image, (280, 40))
        image = pygame.image.load("Y-no-bg-preview (carve,photos)_e.png").convert_alpha()
        new_image = pygame.transform.scale(image, (60, 100))
        screen.blit(new_image, (340, 40))
        image = pygame.image.load("B-no-bg-preview (carve,photos)_e.png").convert_alpha()
        new_image = pygame.transform.scale(image, (60, 100))
        screen.blit(new_image, (160, 140))
        image = pygame.image.load("u.png").convert_alpha()
        new_image = pygame.transform.scale(image, (60, 100))
        screen.blit(new_image, (220, 140))
        image = pygame.image.load("t.png").convert_alpha()
        new_image = pygame.transform.scale(image, (60, 100))
        screen.blit(new_image, (280, 140))
        image = pygame.image.load("t.png").convert_alpha()
        new_image = pygame.transform.scale(image, (60, 100))
        screen.blit(new_image, (340, 140))
        image = pygame.image.load("e.png").convert_alpha()
        new_image = pygame.transform.scale(image, (60, 100))
        screen.blit(new_image, (400, 140))
        image = pygame.image.load("R-no-bg-preview (carve,photos)_e.png").convert_alpha()
        new_image = pygame.transform.scale(image, (60, 100))
        screen.blit(new_image, (460, 140))
        image = pygame.image.load("f-no-bg-preview (carve.photos)_N.png").convert_alpha()
        new_image = pygame.transform.scale(image, (60, 100))
        screen.blit(new_image, (520, 140))
        image = pygame.image.load("L-no-bg-preview (carve,photos)_e.png").convert_alpha()
        new_image = pygame.transform.scale(image, (60, 100))
        screen.blit(new_image, (580, 140))
        image = pygame.image.load("Y-no-bg-preview (carve,photos)_e.png").convert_alpha()
        new_image = pygame.transform.scale(image, (60, 100))
        screen.blit(new_image, (640, 140))


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
    global main_music, bg_music
    left_button = Button(320, 250, 200, 200, "",
                         "влево-no-bg-preview (carve,photos)_enhanced.png",
                         "влево-no-bg-preview (carve,photos)_enhanced.png",
                         "8af5b2bf5d19c00.mp3")
    music_button = Button(550, 250, 230, 200, "",
                          "музыка-edited-free (carve,photos)_enhanced.png",
                          "музыка-edited-free (carve,photos)_enhanced.png",
                          "8af5b2bf5d19c00.mp3")
    pravila_button = Button(790, 250, 200, 200, "",
                            "правила-no-bg-preview (carve,photos)_enhanced.png",
                            "правила-no-bg-preview (carve,photos)_enhanced.png",
                            "8af5b2bf5d19c00.mp3")

    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(pygame.image.load("фон (2)_Nero AI_Photo (1).jpg"), (-300, 0))
        image = pygame.image.load("под кнопки в настройках.png").convert_alpha()
        new_image = pygame.transform.scale(image, (1000, 600))
        screen.blit(new_image, (200, 50))
        font = pygame.font.SysFont('bookworm', 80)
        text = font.render("Setting", True, (0, 0, 0))
        screen.blit(text, (550, 155))
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

            if event.type == pygame.USEREVENT and event.button == music_button:
                if main_music == True or bg_music == True:
                    main_sound.stop()
                    main_music, bg_music = False, False
                else:
                    main_sound.play()
                    main_music, bg_music = True, True

            left_button.handle_event(event)
            music_button.handle_event(event)
            pravila_button.handle_event(event)
        music_button.check_hover(pygame.mouse.get_pos())
        pravila_button.check_hover(pygame.mouse.get_pos())
        left_button.check_hover(pygame.mouse.get_pos())
        music_button.draw(screen)
        pravila_button.draw(screen)
        left_button.draw(screen)
        pygame.display.flip()


def start_meno(): # меню где уровни
    left_button = Button(100, 530, 180, 180, "",
                         "влево-no-bg-preview (carve,photos)_enhanced.png",
                         "влево-no-bg-preview (carve,photos)_enhanced.png",
                         "8af5b2bf5d19c00.mp3")
    level_1_button = Button(400, 100, 550, 200, "",
                            "level1_Nero AI_Photo-edited-free (carve.photos).png",
                         "level1_Nero AI_Photo-edited-free (carve.photos).png",
                            "8af5b2bf5d19c00.mp3")
    level_2_button = Button(400, 300, 600, 200, "",
                            "level2_Nero AI_Photo-edited-free (carve.photos).png",
                         "level2_Nero AI_Photo-edited-free (carve.photos).png",
                            "8af5b2bf5d19c00.mp3")
    level_3_button = Button(400, 500, 600, 200, "",
                            "level3_Nero AI_Photo-edited-free (carve.photos).png",
                         "level3_Nero AI_Photo-edited-free (carve.photos).png",
                            "8af5b2bf5d19c00.mp3")
    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(pygame.image.load("фон (2)_Nero AI_Photo (1).jpg"), (-300, 0))
        font = pygame.font.SysFont('bookworm', 100)
        text = font.render("Levels", True, (0, 0, 0))
        screen.blit(text, (550, 50))
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

            if event.type == pygame.USEREVENT and event.button == level_2_button:
                level_2()

            if event.type == pygame.USEREVENT and event.button == level_3_button:
                level_3()

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
    if bg_music == True:
        main_sound.stop()
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

def level_2():
    bg_x = 0
    if bg_music == True:
        main_sound.stop()
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

        bg_x -= 2
        if bg_x == -1900:
            bg_x = 0

        pygame.display.flip()

def level_3():
    bg_x = 0
    if bg_music == True:
        main_sound.stop()
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

        bg_x -= 5
        if bg_x == -1900:
            bg_x = 0

        pygame.display.flip()

def dead():
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
        pygame.display.flip()

if __name__ == "__main__":
    main_meno()