from flask import Flask

app = Flask(__name__)

@app.route('/')

def hello_world():
    s='''
    <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Розовый магазин</title>
            <link rel="stylesheet" href="styles.css">
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
        </head>
        <body>
            <header>
                <img src="logo.png" class="header_block">
                <h1 class="header_block">Розовый магазин</h1>
                <a href="about_us.html" class="header_block">О нас</a>
                <a href="catalog.html" class="header_block">Каталог</a>
                <a href="start_page.html" class="header_block">Главное меню</a>
            </header>
            <div>
                <br><h1 style="text-align: center; font-size: 100px">Каталог</h1>
            </div>
                <br><br>
            <div class="item_card">
                <a href="pen.html" style="font-size: 45px">Футболка 1</a><br>
                <img src="Картинка1.png" width="250px">
            </div>

            <div class="item_card">
                <a style="font-size: 45px">Ручка 1</a><br>
                <img src="Картинка2.png" width="250px">
            </div>

            <div class="item_card">
                <a style="font-size: 30px">Игровая мышь 1</a><br>
                <img src="Картинка3.png" width="250px">
            </div>
            <br><br><br><br>

        </body>
        <footer>
            ArsPro_13      Арсений Проводов          Vintbolt13@gmail.com
        </footer>
    </html> 
    '''
    return s

if __name__ == '__main__':
    app.run(debug=True)