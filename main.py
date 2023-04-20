def z1():
    from PIL import Image
    file = "otkritka.jpg"
    image = Image.open(file)
    image.show()
    image = image.crop((310, 200, 640, 480))
    image.save('cropped_otkritka.jpg')
    image.show()

def z2():
    from PIL import Image
    a = {"Новый год": "ny.jpg", "23 февраля": "23f.jpg", "8 марта": "8m.jpg", "1 мая": "1m.jpg", "9 мая": "9m.jpg", "День рождения": "dr.jpg"}
    f = str(input("Введите праздник: "))
    file = a[f]
    image = Image.open(file)
    image.show()


def z3():
    from PIL import Image, ImageDraw, ImageFont
    name = str(input("Введите имя: "))
    image = Image.open("9m.jpg")
    font = ImageFont.truetype("arial.ttf", 65)
    drawer = ImageDraw.Draw(image)
    drawer.text((550, 70), name + ", поздравляю!", font=font, fill='red', stroke_width=2, stroke_fill="black")
    image.save('modified.png')
    image.show()

z3()