from flask import Flask, render_template
import operator

app = Flask(__name__)

if __name__ == '__main__':
    app.run()


@app.route('/')
def main_page_render():
    return render_template(
        "index.html",
        my_title='Я здесь главная',
        image_url="https://copypast.ru/uploads/posts/1405227712_552412_10150616007542051_578747050_9683411_1186143590_n.jpg"
    )


@app.route('/about/')
def about_page_render():
    return render_template(
        'about.html',
        my_title='About',
        image_url="https://copypast.ru/uploads/posts/1405227712_552412_10150616007542051_578747050_9683411_1186143590_n.jpg",
        content="Жил в деревне мужик и было у него три сына."
                "Раз утром отец возвращается со двора и говорит:"
                "- У нас корову украли."
                "Старший сын: "
                "- Раз кто-то украл, значит вор."
                "Средний сын:"
                "- Раз вор, значит из Марьинки."
                "Младший:"
                "- Раз из Марьинки, значит Ванька Косой."
                "Пошли в Марьинку, поймали Ваньку, дали вухо: "
                "- Верни корову!"
                "- Нет у меня коровы!"
                "Дали еще раз:"
                "- Верни корову!"
                "- Нет у меня коровы! "
                "- Тогда пошли к мировому судье."
                "Приводят Ваньку к судье и говорят:"
                "- Вот он у нас корову украл."
                "- А почему вы решили, что именно он у вас корову украл? "
                "- Ну как!"
                "- Раз кто-то украл, значит вор. "
                "- Раз вор, значит из Марьинки."
                "- Раз из Марьинки, значит Ванька Косой."
                "- Да... Интересная логика."
                "Судья подзывает секретаря, что-то говорит"
                "ему на ухо, секретарь уходит и через"
                "некоторое время возвращается с"
                " закрытой коробкой. "
                "Судья: "
                "- А скажите-ка мне, что в коробке."
                "Отец: "
                "- Коробка квадратная."
                "Старший сын:"
                "- Раз квадратная, значит в ней что-то круглое. "
                "Средний сын:"
                "- Раз круглое, значит оранжевое."
                "Младший: "
                "- Раз оранжевое, значит апельсин."
                "Судья открывает коробку, достает из нее апельсин и говорит:"
                "- Ванька, вор, верни корову"
    )

@app.route('/gallery')
def gallery_page_render():
    return render_template(
        'gallery.html',
        my_title='Галлерея',
        image1_url='https://4.bp.blogspot.com/-E2ln-pAlU4g/TWGQoPkZrtI/AAAAAAAACwE/CqFj1KKEXZE/s1600/BusinessCat2.jpg',
        image2_url='https://a.d-cd.net/fgAAAgGLaOA-960.jpg',
        image3_url='https://i.pinimg.com/originals/fc/fb/ca/fcfbca732fd9f761dcdd93d21f58d7c1.jpg',
        image4_url='https://www.patrasevents.gr/imgsrv/f/full/1792767.jpg'
    )

@app.route('/bye/')
@app.route('/bye/<username>')
def bye_user(username="undefined"):
    if username != "undefined":
        return (f"Пока, {username}!", f"Хорошего вам дня {username}!")[' ' in username]
    else:
        return "Дружок-пирожок, тобой выбран неправильный URL"


@app.route('/<int:x>/<name_operation>/<int:y>')
def calculate(name_operation='undefined', x=0, y=0):
    operation_value = {
        'сумма': lambda x, y: x + y,
        'разность': lambda x, y: x - y,
        'умножение': lambda x, y: x * y,
        'деление': lambda x, y: x / y
    }[name_operation](x, y)
    return f"Результат {name_operation} равен {operation_value}"
