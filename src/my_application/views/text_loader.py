import  pygame

def draw_text(text, font, text_color, x_coords, y_coords):
    img = font.render(text, True, text_color)
    screen.blit(img, (x_coords,y_coords))