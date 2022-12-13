import pygame as pg
import sys
import random


def check_bound(obj_rct, scr_rct):
    #第一引数：こうかとんrectまたは爆弾rect
    #代に引数：スクリーンrect
    # 範囲内：+1, 範囲外：-1
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right:
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        tate = -1
    return yoko, tate

def game_over():
    #ゲームオーバー時に画像を出力する処理
    clock = pg.time.Clock()
    pg.display.set_caption("こうかとん、死す。")
    scrn_sfc = pg.display.set_mode((1600, 900))
    scrn_rct = scrn_sfc.get_rect()
    img_sfc = pg.image.load("fig/game_over.jpg")
    img_sfc = pg.transform.scale(img_sfc, (1600, 900))
    img_rct = img_sfc.get_rect()
    scrn_sfc.blit(img_sfc, img_rct)
    pg.display.update()
    clock.tick(0.3)

def main():
    clock = pg.time.Clock()
    # 1
    pg.display.set_caption("逃げろ！こうかとん")
    scrn_sfc = pg.display.set_mode((1600, 900))
    scrn_rct = scrn_sfc.get_rect()
    pgbg_sfc = pg.image.load("fig/pg_bg.jpg")
    pgbg_rct = pgbg_sfc.get_rect()

    # 3
    tori_sfc = pg.image.load("fig/2.png")
    tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0)
    tori_rct = tori_sfc.get_rect()
    tori_rct.center = 900, 400
    scrn_sfc.blit(tori_sfc, tori_rct)

    # 5
    bomb_sfc = pg.Surface((60, 60))
    bomb_sfc.set_colorkey((0, 0, 0))
    #爆弾の大きさを30に変更
    pg.draw.circle(bomb_sfc, (255, 0, 0), (30, 30), 30)
    bomb_rct = bomb_sfc.get_rect()
    bomb_rct.centerx = random.randint(0, scrn_rct.width)
    bomb_rct.centery = random.randint(0, scrn_rct.height)
    scrn_sfc.blit(bomb_sfc, bomb_rct)

    # 10個のコインを設置。
    coin1_sfc = pg.Surface((80, 80))
    coin1_sfc.set_colorkey((0, 0, 0))
    #コインの大きさを40に指定
    pg.draw.circle(coin1_sfc, (255, 255, 0), (40, 40), 40)
    coin1_rct = coin1_sfc.get_rect()
    coin1_rct.centerx = random.randint(0, scrn_rct.width)
    coin1_rct.centery = random.randint(0, scrn_rct.height)
    scrn_sfc.blit(coin1_sfc, coin1_rct)

    coin2_sfc = pg.Surface((80, 80))
    coin2_sfc.set_colorkey((0, 0, 0))
    #コインの大きさを40に指定
    pg.draw.circle(coin2_sfc, (255, 255, 0), (40, 40), 40)
    coin2_rct = coin2_sfc.get_rect()
    coin2_rct.centerx = random.randint(0, scrn_rct.width)
    coin2_rct.centery = random.randint(0, scrn_rct.height)
    scrn_sfc.blit(coin2_sfc, coin2_rct)

    coin3_sfc = pg.Surface((80, 80))
    coin3_sfc.set_colorkey((0, 0, 0))
    #コインの大きさを40に指定
    pg.draw.circle(coin3_sfc, (255, 255, 0), (40, 40), 40)
    coin3_rct = coin3_sfc.get_rect()
    coin3_rct.centerx = random.randint(0, scrn_rct.width)
    coin3_rct.centery = random.randint(0, scrn_rct.height)
    scrn_sfc.blit(coin3_sfc, coin3_rct)

    coin4_sfc = pg.Surface((80, 80))
    coin4_sfc.set_colorkey((0, 0, 0))
    #コインの大きさを40に指定
    pg.draw.circle(coin4_sfc, (255, 255, 0), (40, 40), 40)
    coin4_rct = coin4_sfc.get_rect()
    coin4_rct.centerx = random.randint(0, scrn_rct.width)
    coin4_rct.centery = random.randint(0, scrn_rct.height)
    scrn_sfc.blit(coin4_sfc, coin4_rct)

    coin5_sfc = pg.Surface((80, 80))
    coin5_sfc.set_colorkey((0, 0, 0))
    #コインの大きさを40に指定
    pg.draw.circle(coin5_sfc, (255, 255, 0), (40, 40), 40)
    coin5_rct = coin5_sfc.get_rect()
    coin5_rct.centerx = random.randint(0, scrn_rct.width)
    coin5_rct.centery = random.randint(0, scrn_rct.height)
    scrn_sfc.blit(coin5_sfc, coin5_rct)

    coin6_sfc = pg.Surface((80, 80))
    coin6_sfc.set_colorkey((0, 0, 0))
    #コインの大きさを40に指定
    pg.draw.circle(coin6_sfc, (255, 255, 0), (40, 40), 40)
    coin6_rct = coin6_sfc.get_rect()
    coin6_rct.centerx = random.randint(0, scrn_rct.width)
    coin6_rct.centery = random.randint(0, scrn_rct.height)
    scrn_sfc.blit(coin6_sfc, coin6_rct)

    coin7_sfc = pg.Surface((80, 80))
    coin7_sfc.set_colorkey((0, 0, 0))
    #コインの大きさを40に指定
    pg.draw.circle(coin7_sfc, (255, 255, 0), (40, 40), 40)
    coin7_rct = coin7_sfc.get_rect()
    coin7_rct.centerx = random.randint(0, scrn_rct.width)
    coin7_rct.centery = random.randint(0, scrn_rct.height)
    scrn_sfc.blit(coin7_sfc, coin7_rct)

    coin8_sfc = pg.Surface((80, 80))
    coin8_sfc.set_colorkey((0, 0, 0))
    #コインの大きさを40に指定
    pg.draw.circle(coin8_sfc, (255, 255, 0), (40, 40), 40)
    coin8_rct = coin8_sfc.get_rect()
    coin8_rct.centerx = random.randint(0, scrn_rct.width)
    coin8_rct.centery = random.randint(0, scrn_rct.height)
    scrn_sfc.blit(coin8_sfc, coin8_rct)

    coin9_sfc = pg.Surface((80, 80))
    coin9_sfc.set_colorkey((0, 0, 0))
    #コインの大きさを40に指定
    pg.draw.circle(coin9_sfc, (255, 255, 0), (40, 40), 40)
    coin9_rct = coin9_sfc.get_rect()
    coin9_rct.centerx = random.randint(0, scrn_rct.width)
    coin9_rct.centery = random.randint(0, scrn_rct.height)
    scrn_sfc.blit(coin9_sfc, coin9_rct)

    coin10_sfc = pg.Surface((80, 80))
    coin10_sfc.set_colorkey((0, 0, 0))
    #コインの大きさを40に指定
    pg.draw.circle(coin10_sfc, (255, 255, 0), (40, 40), 40)
    coin10_rct = coin10_sfc.get_rect()
    coin10_rct.centerx = random.randint(0, scrn_rct.width)
    coin10_rct.centery = random.randint(0, scrn_rct.height)
    scrn_sfc.blit(coin10_sfc, coin10_rct)

    #爆弾の側を1.5に変更
    vx, vy = +1.5, +1.5
    
    # コインを取ったかどうかを判定するためのflag
    coin1_flag, coin2_flag, coin3_flag, coin4_flag, coin5_flag, coin6_flag, coin7_flag, coin8_flag, coin9_flag, coin10_flag = True, True, True, True, True, True, True, True, True, True

    
    # 2
    while True:
        scrn_sfc.blit(pgbg_sfc, pgbg_rct)

        for event in pg.event.get():
            if event.type == pg.QUIT: #×ボタンのクリック
                return

        key_dct = pg.key.get_pressed() #辞書型
        # 4
        if key_dct[pg.K_UP]:
            tori_rct.centery -= 1
        if key_dct[pg.K_DOWN]:
            tori_rct.centery += 1
        if key_dct[pg.K_LEFT]:
            tori_rct.centerx -= 1
        if key_dct[pg.K_RIGHT]:
            tori_rct.centerx += 1
        if check_bound(tori_rct, scrn_rct) != (+1, +1):
            if key_dct[pg.K_UP]:
                tori_rct.centery += 1
            if key_dct[pg.K_DOWN]:
                tori_rct.centery -= 1
            if key_dct[pg.K_LEFT]:
                tori_rct.centerx += 1
            if key_dct[pg.K_RIGHT]:
                tori_rct.centerx -= 1
        scrn_sfc.blit(tori_sfc, tori_rct) #これで新しい座標を貼り付け

        # 6
        bomb_rct.move_ip(vx, vy)
        scrn_sfc.blit(bomb_sfc, bomb_rct)
        if coin1_flag == True:
            scrn_sfc.blit(coin1_sfc, coin1_rct)
        if coin2_flag == True:
            scrn_sfc.blit(coin2_sfc, coin2_rct)
        if coin3_flag == True:
            scrn_sfc.blit(coin3_sfc, coin3_rct)
        if coin4_flag == True:
            scrn_sfc.blit(coin4_sfc, coin4_rct)
        if coin5_flag == True:
            scrn_sfc.blit(coin5_sfc, coin5_rct)
        if coin6_flag == True:
            scrn_sfc.blit(coin6_sfc, coin6_rct)
        if coin7_flag == True:
            scrn_sfc.blit(coin7_sfc, coin7_rct)
        if coin8_flag == True:
            scrn_sfc.blit(coin8_sfc, coin8_rct)
        if coin9_flag == True:
            scrn_sfc.blit(coin9_sfc, coin9_rct)
        if coin10_flag == True:
            scrn_sfc.blit(coin10_sfc, coin10_rct)
        yoko, tate = check_bound(bomb_rct, scrn_rct)
        vx *= yoko
        vy *= tate
        # bomb_rct.move_ip(vx, vy)
        # scrn_sfc.blit(bomb_sfc, bomb_rct)
        
        # 8
        if tori_rct.colliderect(bomb_rct):
            clock.tick(1)
            game_over()
            return
        
        # コインに接触したらflagをFalseにして、表示されないようにする
        if tori_rct.colliderect(coin1_rct):
            coin1_flag = False
        if tori_rct.colliderect(coin2_rct):
            coin2_flag = False
        if tori_rct.colliderect(coin3_rct):
            coin3_flag = False
        if tori_rct.colliderect(coin4_rct):
            coin4_flag = False
        if tori_rct.colliderect(coin5_rct):
            coin5_flag = False
        if tori_rct.colliderect(coin6_rct):
            coin6_flag = False
        if tori_rct.colliderect(coin7_rct):
            coin7_flag = False
        if tori_rct.colliderect(coin8_rct):
            coin8_flag = False
        if tori_rct.colliderect(coin9_rct):
            coin9_flag = False
        if tori_rct.colliderect(coin10_rct):
            coin10_flag = False

        # 全てのコインに接触したら終了
        if (coin1_flag == False) and (coin2_flag == False) and (coin3_flag == False) and (coin4_flag == False) and (coin5_flag == False) and (coin6_flag == False) and (coin7_flag == False) and (coin8_flag == False) and (coin9_flag == False) and (coin10_flag == False):
            clock.tick(1)
            return

        pg.display.update()
        clock.tick(1000)

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()