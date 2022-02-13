import pygame
import easygui
from Button import Button
from Client import Client
from Massage import Massage


class ClientGUI:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.WIDHT = 500
        self.HIGHT = 500
        self.screen = pygame.display.set_mode((self.WIDHT, self.HIGHT), depth=32)
        self.clock = pygame.time.Clock()
        self.Font = pygame.font.SysFont('ariel', 20)
        self.button_login = Button(pygame.Rect((8, 8), (70, 30)), "Log in", (255, 255, 128))
        self.button_getlist = Button(pygame.Rect((370, 8), (70, 30)), "get list", (255, 255, 128))
        self.button_send = Button(pygame.Rect((370, 50), (100, 30)), "send massage", (255, 255, 128))
        self.display()

    def display(self):
        enter = False
        while True:
            for eve in pygame.event.get():
                if eve.type == pygame.QUIT:
                    pygame.quit()
                    exit(0)
                if eve.type == pygame.MOUSEBUTTONDOWN:
                    if self.button_login.rect.collidepoint(eve.pos):
                        self.button_login.pressed()
                    if self.button_getlist.rect.collidepoint(eve.pos):
                        self.button_getlist.pressed()
                    if self.button_send.rect.collidepoint(eve.pos):
                        self.button_send.pressed()
            pygame.draw.rect(self.screen, self.button_login.color, self.button_login.rect)
            if self.button_login.is_pressed:
                if not enter:
                    name = easygui.enterbox('enter your user name:', 'Log in')
                    server = easygui.enterbox('enter your server name:', 'Log in')
                    client = Client(name, server)
                    enter = True
                self.button_login.text = "Log out"
                pygame.draw.rect(self.screen, self.button_getlist.color, self.button_getlist.rect)
                button_getlist_text = self.Font.render(self.button_getlist.text, True, (0, 0, 0))
                self.screen.blit(button_getlist_text, (self.button_getlist.rect.x + 10, self.button_getlist.rect.y + 5))
                pygame.draw.rect(self.screen, self.button_send.color, self.button_send.rect)
                button_send_text = self.Font.render(self.button_send.text, True, (0, 0, 0))
                self.screen.blit(button_send_text, (self.button_send.rect.x, self.button_send.rect.y + 5))
                if self.button_getlist.is_pressed:
                    list1 = client.get_list()
                    easygui.msgbox(list1, "users list")
                if self.button_send.is_pressed:
                    dest = easygui.enterbox("enter your massage destination:", "send massage")
                    text = easygui.enterbox("enter your massage:", "send massage")
                    client.send_message(text, dest)
            else:
                enter = False
                self.button_login.text = "Log in"
            button_login_text = self.Font.render(self.button_login.text, True, (0, 0, 0))
            self.screen.blit(button_login_text, (self.button_login.rect.x + 10, self.button_login.rect.y+5))
            pygame.display.update()
            self.screen.fill(pygame.Color(255, 250, 250))
            pygame.display.set_caption("Client")
            self.clock.tick(60)