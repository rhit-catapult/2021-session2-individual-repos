Intro to Python
- Variables
    - Hold objects such as words or numbers
    - ex. Cat_Name = "Fluffy"
  
- Strings
  - Strings can be held in variables
  - In the example above, "Fluffy" is a string
  
- Arrays 
  - Actually known as list
  - Also, can be a tuple 
  - However, tuples can be edited
    Stick on array
    self.raindrops.append(new_raindrop)
  
DogBark
- create images - image1 = pygame.image.load("2dogs.JPG")
- font creation - font2 = pygame.font.Font(None, 100)
        caption2 = font2.render("My Turn!", True, WHITE)
        screen.blit(caption2, (100,0))
  
- create sound effects - bark_sound = pygame.mixer.Sound("bark.wav")
- if event.type == pygame.MOUSEBUTTONDOWN:
                bark_sound.play()
  
- Background music
  pygame.mixer.music.load("file name")
  pygame.mixer.music.play(-1)
  pygame.mixer.music.stop()
  
ClickInCircle
- Mouse point reference
- Playing a sound loop
- Displaying text during certain actions

Starter Code for Main
pygame.init()
    screen = pygame.display.set_mode((1000, 600))
    pygame.display.set_caption("Mike's Rainy Day")

Hit boxes Code
hero_hit_box = pygame.Rect(self.x, self.y,
                                  self.image_with_umbrella.get_width(), self.image_with_umbrella.get_height())
        return hero_hit_box.collidepoint(raindrop.x, raindrop.y)

Move
pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_UP]:
            print("You are holding down the up key!")
            eye_y_delta = eye_y_delta - 5
        if pressed_keys[pygame.K_DOWN]:
            print("You are holding down the down key!")
            eye_y_delta = eye_y_delta + 5
        if pressed_keys[pygame.K_RIGHT]:
            print("You are holding down the right key!")
            eye_x_delta = eye_x_delta + 5
        if pressed_keys[pygame.K_LEFT]:
            print("You are holding down the left key!")
            eye_x_delta = eye_x_delta - 5
