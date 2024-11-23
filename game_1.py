import pygame
pygame.init()

# Create the game window
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Two Agents Game")

# Agent 1 variables
x1 = 50
y1 = 50
width1 = 40
height1 = 50
vel1 = 5

# Agent 2 variables
x2 = 200
y2 = 200
width2 = 40
height2 = 50
vel2 = 5

# Main game loop
run = True
while run:
    pygame.time.delay(100)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Get the state of all keys
    keys = pygame.key.get_pressed()

    # Control Agent 1 with arrow keys
    if keys[pygame.K_LEFT]:
        x1 -= vel1
    if keys[pygame.K_RIGHT]:
        x1 += vel1
    if keys[pygame.K_UP]:
        y1 -= vel1
    if keys[pygame.K_DOWN]:
        y1 += vel1

    # Control Agent 2 with WASD keys
    if keys[pygame.K_a]:  # Move left
        x2 -= vel2
    if keys[pygame.K_d]:  # Move right
        x2 += vel2
    if keys[pygame.K_w]:  # Move up
        y2 -= vel2
    if keys[pygame.K_s]:  # Move down
        y2 += vel2

    # Clear the window and redraw
    win.fill((0, 0, 0))  # Fill with black color
    pygame.draw.rect(win, (255, 0, 0), (x1, y1, width1, height1))  # Agent 1 (Red)
    pygame.draw.rect(win, (0, 0, 255), (x2, y2, width2, height2))  # Agent 2 (Blue)
    pygame.display.update()

pygame.quit()
