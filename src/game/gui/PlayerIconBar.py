from utils.Util import *


class PlayerIconBar(object):

    def __init__(self, player, is_p1):
        self.player = player
        self.is_player_one = is_p1
        self.num_of_powerups = getNumOfPowerups(player.power)

    def getPlayerIcon(self):
        player_icon_width = 40

        if self.is_player_one:
            if self.player.color == "RED":
                return ICON_BIKES_SHEET.get_image(8 * player_icon_width, 0, 2 * player_icon_width, player_icon_width)
            elif self.player.color == "BLUE":
                return ICON_BIKES_SHEET.get_image(0, 0, 2 * player_icon_width, player_icon_width)
            elif self.player.color == "YELLOW":
                return ICON_BIKES_SHEET.get_image(12 * player_icon_width, 0, 2 * player_icon_width, player_icon_width)
            elif self.player.color == "GREEN":
                return ICON_BIKES_SHEET.get_image(4 * player_icon_width, 0, 2 * player_icon_width, player_icon_width)
        else:
            if self.player.color == "RED":
                return ICON_BIKES_SHEET.get_image(10 * player_icon_width, 0, 2 * player_icon_width, player_icon_width)
            elif self.player.color == "BLUE":
                return ICON_BIKES_SHEET.get_image(2 * player_icon_width, 0, 2 * player_icon_width, player_icon_width)
            elif self.player.color == "YELLOW":
                return ICON_BIKES_SHEET.get_image(14 * player_icon_width, 0, 2 * player_icon_width, player_icon_width)
            elif self.player.color == "GREEN":
                return ICON_BIKES_SHEET.get_image(6 * player_icon_width, 0, 2 * player_icon_width, player_icon_width)

    def getPlayerIconBar(self):
        image = Surface((SCREEN_WIDTH // 2, BORDER_TOP_OFFSET))
        image.fill(BOOSTREDTRAIL)
        image.set_colorkey(BOOSTREDTRAIL)

        if self.is_player_one:
            image.blit(self.getPlayerIcon(), (10, 5))
            image.blit(self.getLives(), (100, 25))
            image.blit(self.getPowerupIcons(), (100, 5))
        else:
            lives = self.getLives()
            powerups = self.getPowerupIcons()

            image.blit(self.getPlayerIcon(), (SCREEN_WIDTH // 2 - 90, 5))
            image.blit(lives, (SCREEN_WIDTH // 2 - 100 - lives.get_width(), 25))
            image.blit(powerups, (SCREEN_WIDTH // 2 - 100 - powerups.get_width(), 5))

        return image

    def getLives(self):
        image = Surface((25 * PLAYER_LIVES - 5, 20))

        image.fill(BOOSTREDTRAIL)
        image.set_colorkey(WHITE)

        if self.is_player_one:
            for i in range(PLAYER_LIVES):
                if i < self.player.lives:
                    image.blit(HEART, (i * (20 + 5), 0))
                else:
                    image.blit(EMPTY_HEART, (i * (20 + 5), 0))
        else:
            for i in range(PLAYER_LIVES):
                if i < self.player.lives:
                    image.blit(HEART, (image.get_width() - 20 - i * (20 + 5), 0))
                else:
                    image.blit(EMPTY_HEART, (image.get_width() - 20 - i * (20 + 5), 0))

        return image

    def getPowerupIcons(self):
        image = Surface((self.num_of_powerups * 14 + 5 * (self.num_of_powerups - 1), 14))
        image.fill(BOOSTREDTRAIL)
        image.set_colorkey(WHITE)

        if self.is_player_one:
            for i in range(self.num_of_powerups):
                if i < self.player.powerups_remaining:
                    image.blit(POWERUP_ICON, (i * (14 + 5), 0))
                else:
                    image.blit(EMPTY_POWERUP_ICON, (i * (14 + 5), 0))
        else:
            for i in range(self.num_of_powerups):
                if i < self.player.powerups_remaining:
                    image.blit(POWERUP_ICON, (image.get_width() - 14 - i * (14 + 5), 0))
                else:
                    image.blit(EMPTY_POWERUP_ICON, (image.get_width() - 14 - i * (14 + 5), 0))

        return image
