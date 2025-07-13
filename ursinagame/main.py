from ursina import *

if __name__ == '__main__':
    app = Ursina()

window.borderless = False
window.color = color.black
window.fullscreen = False
window.title = 'Ursina Game - Playground'

# Load the sprite sheet using Sprite and Animation

# Assuming you have exported the .tmx spritesheet as a .png and have a .json or .txt animation definition.
# For this example, let's assume the spritesheet is 'PyLab/tiled/sprites/male_character/Base_boy.png'
# and each direction is a row: 0=down, 1=left, 2=right, 3=up, each with 3 frames.

directions = {
    'none': -1,
    'down': 0,
    'left': 1,
    'right': 2,
    'up': 3
}

current_direction = 'down'

#player_graphics = SpriteSheetAnimation('Unarmed_Walk_full', tileset_size=(6,4), fps=6, animations={
#    'idle' : ((0,0), (0,0)),        # makes an animation from (0,0) to (0,0), a single frame
#    'walk_up' : ((0,0), (3,0)),     # makes an animation from (0,0) to (3,0), the bottom row
#    'walk_right' : ((0,1), (3,1)),
#    'walk_left' : ((0,2), (3,2)),
#    'walk_down' : ((0,3), (3,3)),
#    }
#)

player = SpriteSheetAnimation('Unarmed_Walk_full', tileset_size=(6,4), fps=6, animations={
        'walk_down':   ((0,3),(5,3)),
        'walk_left':   ((0,2),(5,2)),
        'walk_right':  ((0,1),(5,1)),
        'walk_up':     ((0,0),(5,0)),
        'idle_down':   ((2,3),(2,3)),
        'idle_left':   ((2,2),(2,2)),
        'idle_right':  ((2,1),(2,1)),
        'idle_up':     ((2,0),(2,0)),
    })


'''
def input(key):
    if key == 'up arrow':
        red_square.play_animation('walk_up')
    elif key == 'down arrow':
        red_square.play_animation('walk_down')
    elif key == 'right arrow':
        red_square.play_animation('walk_right')
    elif key == 'left arrow':
        red_square.play_animation('walk_left')
'''

#player = Entity(model='quad', texture='Unarmed_Walk_full', position=(0,0,0), scale=(1,1,1))

#player = Entity(model='quad', texture='Unarmed_Walk_full', position=(0,0,0), scale=(1,1,1), animation=player_graphics)
#player_graphics.parent = player

speed = 1

def update():
    direction = None
    move = Vec3(0,0,0)
    global current_direction

    if held_keys['up arrow']:
        move.y += 1
        direction = 'up'
    elif held_keys['down arrow']:
        move.y -= 1
        direction = 'down'
    if held_keys['left arrow']:
        move.x -= 1
        direction = 'left'
    elif held_keys['right arrow']:
        move.x += 1
        direction = 'right'

    if move != Vec3(0,0,0):
        move = move.normalized() * time.dt * speed
        player.position += move
        if direction != current_direction:
            player.play_animation(f'walk_{direction}')
            current_direction = direction
    else:
        player.play_animation(f'idle_{current_direction}')

if __name__ == '__main__':
    app.run()