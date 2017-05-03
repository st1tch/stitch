from PIL import Image, ImageDraw

draw_text = open('test','r').read().split('\n')[:-1]
size = 20
image = Image.new('RGB', (((len(draw_text[0]) * size), len(draw_text) * size)))
draw = ImageDraw.Draw(image)

for i in range(0, len(draw_text)):
    for j in range(0, len(draw_text[0])):
        pos = ((j * size, i * size), (j * size + size, i * size + size))
        draw.rectangle(pos, 'black' if draw_text[i][j] == 'X' else 'white')

image.save('qrcode.png')
'''
....X.....
..XXXXXX..
..........
'''
