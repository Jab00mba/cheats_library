import sqlite3
import sys
import os
from PIL import Image
from PIL.ImageQt import ImageQt

from PyQt5.QtGui import QPixmap, QMovie, QColor
from PyQt5.QtCore import Qt, QTimer, QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QGraphicsDropShadowEffect
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from UI import Foundation
from PyQt5 import QtWidgets, QtGui, QtCore
from splash2 import Splash_window

counter = 0


class LoadingScreen(QMainWindow, Splash_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.main_win = QMainWindow()
        self.ui = Splash_window()
        self.ui.setupUi(self.main_win)
        self.initUI()
        self.setWindowTitle('Cheat library')

        # этот таймер вызывает каждые 35 миллисекнд функцию которая изменяет шкалу загрузки нашего приложения
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        self.timer.start(50)

    def initUI(self):
        # ставит гифку не лейбл
        self.movie = QMovie("database/splash_images/mr_true_splash2.gif")
        self.label.setMovie(self.movie)
        self.setFixedSize(750, 460)
        # убираем кнопки навигации и т.д. чтобы была чисто гифка
        self.setWindowFlags(Qt.WindowStaysOnTopHint | QtCore.Qt.FramelessWindowHint)
        # здесь мы добавляем эффект тени сзади нашего окна загрузки
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.dropShadowFrame.setGraphicsEffect(self.shadow)

        self.player = QMediaPlayer()
        self.playAudio()

        # этот таймер ждет 5500 миллисекунд и вызывает функцию закрывающую окно
        timer = QTimer(self)
        self.startAnimation()
        timer.singleShot(7000, self.stopAnimation)
        self.show()
        # создаем переменную класса чтобы запустить основную программу после окна загрузки
        self.mainwindow = CheatLibrary()

    def playAudio(self):
        fullFilepath = os.path.join(os.getcwd(), 'database/audio/loading_music.mp3')
        url = QUrl.fromLocalFile(fullFilepath)
        content = QMediaContent(url)
        self.player.setMedia(content)
        self.player.play()

    def stopAudio(self):
        self.player.stop()

    def progress(self):
        global counter
        # устанавлиеваем значение шкалы загрузки так чтобы достигнув 100 программа прекращала увеличение шкалы
        self.progressBar.setValue(counter)
        if counter > 100:
            self.timer.stop()
        counter += 1

    def startAnimation(self):
        # запускает гифку
        self.movie.start()

    def stopAnimation(self):
        # закрывает окно загрузки и открывает основуню программу
        self.movie.stop()
        self.stopAudio()
        self.close()
        self.mainwindow.show()


class CheatLibrary(QMainWindow, Foundation):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.main_win = QMainWindow()
        self.ui = Foundation()
        self.ui.setupUi(self.main_win)
        self.ui.stackedWidget.setCurrentWidget(self.ui.main_page)
        # назначаем функции для каждой кнопки
        self.ui.home_button.clicked.connect(self.home)
        self.ui.weapon_button.clicked.connect(self.show_weapon_page)
        self.ui.spawn_button.clicked.connect(self.show_spawn_page)
        self.ui.world_button.clicked.connect(self.show_world_page)
        self.ui.gameplay_button.clicked.connect(self.show_gameplay_page)
        self.ui.search_button.clicked.connect(self.search)
        self.setWindowTitle('Cheat library')
        self.cheat_pages_dict = {}  # словарь со всеми виджетами в которых содержится описание каждого чита
        self.cheat_buttons_list = []  # список со всеми Qpushbutton которые генерировались с помощью цикла
        # каждая кнопка является ссылкой к соответствующиму виджету
        self.spawn_buttons()  # создает кнопки которые добавляет в соответствующий список
        for btn in self.cheat_buttons_list:
            btn.clicked.connect(self.cheat_page_opener)  # этот цикл открывает виджет с описанием чита
            # если нажата соответствующая кнопка

    def search(self):
        # здесь я реализовал поиск читов
        # создаем новый виджет на котором будут результаты поиска
        self.ui.answers_page = QtWidgets.QWidget()
        self.ui.answers_page.setObjectName('search_page')
        self.ui.stackedWidget.addWidget(self.ui.answers_page)

        search_cheat_buttons_list = []  # в этом списке будут найденные кнопки
        answers = []
        # эти 3 переменные отвечают за расстояние между кнопками и их количество чтобы кнопки не выходили за рамки
        # и не накладывались друг на друга
        movementy, movementx, value_of_buttons = 30, 10, 0
        # получает введенный запрос
        request = self.ui.search_label.text()
        # проверяем есть ли среди имеющихся pushbutton соответствующий запросу
        for button in self.cheat_buttons_list:
            if request in button.objectName():
                # если есть, то добавляем его название в список ответов
                answers.append(button.objectName())
        # если запрос был пустой то программа выведет ошибку о том что не было ничего найдено
        if request == '' or request == ' ':
            self.notFoundPageCreate(request)
        # если запрос соответствует одному из имеющихся pushbutton то выполняем слеудющее
        elif len(answers):
            # для каждого из найденных ответов на запрос
            for answer in answers:
                # создаем отдельный виджет
                self.pages_creator(answer)
                self.cheat_pages_dict[answer] = self.ui.page
                # и добавляем туда найденный pushbutton
                self.buttons_creater(answer.upper(), self.ui.answers_page, movementx, movementy)
                # если такой же запрос был ранее то чтобы избежать дубликатов не добавляем его в список кнопок
                if self.button in search_cheat_buttons_list:
                    continue
                # а если дубликата нет то добавляем
                search_cheat_buttons_list.append(self.button)
                movementy += 50  # меняет координаты чтобы следующая кнопка не была на одном месте что и прежняя
                value_of_buttons += 1
                if value_of_buttons == 11:  # этот блок сдвигает столбец с кнопками чтобы они равномерно распределились
                    movementy = 30
                    movementx += 150
                    value_of_buttons = 0
        # если среди имеющихся pushbutton нет совпадений, то проверяем есть ли совпадения в описаниях читов
        elif len(answers) == 0:
            capreq = request.capitalize()
            # добавляем все читы которые подходят по описанию чита в список
            with sqlite3.connect('database/cheats.db') as db:
                sql = db.cursor()
                cheats = sql.execute(f"""SELECT cheat FROM cheats WHERE description LIKE '%{capreq}%'
                OR description LIKE '%{request}%'""").fetchall()
                # ищем данный чит в списке всех pushbutton'ов и добавляем в список
                for cheat in cheats:
                    for button in self.cheat_buttons_list:
                        if cheat[0].lower() in button.objectName():
                            answers.append(button.objectName())
                # если не было найдено совпадений по описанию чита то выводим виджет с ошибкой
                if len(answers) == 0:
                    self.notFoundPageCreate(request)
            # если найдены совпадения то как и в прошлый раз создаем виджет на котором выведены все совпавшие pushbutton
            for answer in answers:
                self.pages_creator(answer)
                self.cheat_pages_dict[answer] = self.ui.page
                self.buttons_creater(answer.upper(), self.ui.answers_page, movementx, movementy)
                if self.button in search_cheat_buttons_list:
                    continue
                search_cheat_buttons_list.append(self.button)
                movementy += 50  # меняет координаты чтобы следующая кнопка не была на одном месте что и прежняя
                value_of_buttons += 1
                if value_of_buttons == 11:  # этот блок сдвигает столбец с кнопками чтобы они равномерно распределились
                    movementy = 30
                    movementx += 150
                    value_of_buttons = 0
        # выводим виджет с ответами на запрос
        self.ui.stackedWidget.setCurrentWidget(self.ui.answers_page)
        # и проверяем не выбранн ли один из запросов
        for btn in search_cheat_buttons_list:
            btn.clicked.connect(self.cheat_page_opener)

    def notFoundPageCreate(self, name):
        # виджет с сообщением об ошибке
        self.label = QtWidgets.QLabel(self.ui.answers_page)
        self.label.setGeometry(QtCore.QRect(160, 20, 1000, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setFamily("Montserrat")
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setText(f"im sorry, cheats with name '{name}' not found")
        self.imageLabel = QtWidgets.QLabel(self.ui.answers_page)
        self.imageLabel.setGeometry(QtCore.QRect(150, 90, 828, 584))
        self.imageLabel.setObjectName("imageLabel")
        self.current_img = Image.open('database/images/errorfile.jpg')
        self.current_img = self.current_img.resize((828, 584))
        self.a = ImageQt(self.current_img)
        self.pixmap = QPixmap.fromImage(self.a)
        self.imageLabel.setPixmap(self.pixmap)

    def cheat_page_opener(self):
        # эта функция создает страницу с описанием выбранного чита
        with sqlite3.connect('database/cheats.db') as db:
            sql = db.cursor()
            desc = sql.execute(
                f"""SELECT description FROM cheats WHERE cheat = '{self.sender().objectName().upper()}'""").fetchall()
            desc = desc[0][0]  # выводит описание выбранного чита из датабазы и сохраняет в списке
            # т.к. вывелся список с 1 кортежом то я сделал из него строку
        # для каждой страницы чита нужно добавить описание
        for i in self.cheat_pages_dict:
            # проверяет является ли данный виджет принадлежащий выбранному читу
            if self.cheat_pages_dict[i].objectName() == self.sender().objectName():
                self.label = QtWidgets.QLabel(self.cheat_pages_dict[i])  # создает заголовок с читом
                self.label.setGeometry(QtCore.QRect(160, 20, 350, 50))
                font = QtGui.QFont()
                font.setPointSize(20)
                font.setFamily("Montserrat")
                font.setBold(True)
                font.setWeight(75)
                self.label.setFont(font)
                self.label.setText(self.sender().objectName().upper())

                self.textBrowser = QtWidgets.QTextBrowser(
                    self.cheat_pages_dict[i])  # создает textbrowser в котором описание чита
                self.textBrowser.setGeometry(QtCore.QRect(160, 89, 500, 136))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setFamily("Noto Sans")
                font.setBold(False)
                font.setWeight(40)
                self.textBrowser.setFont(font)
                # добавляет описание чита
                self.textBrowser.setText(desc)
                # а также соответствующую картинку
                self.imageLabel = QtWidgets.QLabel(self.cheat_pages_dict[i])
                self.imageLabel.setGeometry(QtCore.QRect(680, 90, 240, 135))
                self.imageLabel.setText('')
                self.imageLabel.setObjectName("imageLabel")
                # в случае отсутствия выводит шаблонную картинку
                try:
                    self.current_img = Image.open('database/images/' + str(self.sender().objectName()).upper() + '.jpg')
                except FileNotFoundError:  # чтобы программа не вылетела в случае отсутствия картинки
                    self.current_img = Image.open('database/images/errorfile.jpg')
                self.current_img = self.current_img.resize((240, 135))
                self.a = ImageQt(self.current_img)
                self.pixmap = QPixmap.fromImage(self.a)
                self.imageLabel.setPixmap(self.pixmap)
                # выводит выбранный виджет
                self.ui.stackedWidget.setCurrentWidget(self.cheat_pages_dict[i])

    def pages_creator(self, name):
        # создает виджет
        self.ui.page = QtWidgets.QWidget()
        self.ui.page.setObjectName(name)
        self.ui.stackedWidget.addWidget(self.ui.page)

    def buttons_creater(self, code, page, movementx, movementy):
        # созадет pushbutton
        self.button = QPushButton(code, page)
        self.button.setObjectName(code.lower())
        self.button.resize(140, 40)
        self.button.move(movementx, movementy)

    def categories(self):
        # добавляет отсортированные по категориям списки с читами
        categories = []
        with sqlite3.connect('database/cheats.db') as db:
            sql = db.cursor()
            for i in ['weapon', 'gameplay', 'world', 'spawn']:
                codes = sql.execute(f"""SELECT cheat FROM cheats WHERE category = '{i}'""").fetchall()
                categories.append(codes)
        return categories

    def spawn_buttons(self):
        # функуця создает основные pushbutton которые выводят читы соответствующей категории
        # создаем 4 виджета на которых будут по категориям распределены читы
        pages = [self.ui.weapon_page, self.ui.gameplay_page, self.ui.world_page, self.ui.spawn_page]
        code_indx = 0
        for page in pages:
            movementy, movementx, value_of_buttons = 30, 10, 0  # это значения координат кнопок и их кол-во
            # начиная с первой категории выводим читы в виде кнопок на соответствующий виджет
            codes = self.categories()[code_indx]
            # каждый чит необходимой категории добавляется на виджет и на каждый чит создается виджет на который потом
            # добавим описание
            for code in codes:
                code = code[0]
                # создает виджет с названием чита чтобы в последующем сравнить его с читом и добавить нужное описание
                self.pages_creator(code.lower())
                page2 = self.ui.page
                # добавляем этот в иджет в словарь всех виджетов
                self.cheat_pages_dict[code.lower()] = page2
                # создаем кнопку чита при нажатии которая выведет свое описание
                self.buttons_creater(code, page, movementx, movementy)
                butn = self.button
                # и добавляем в список всех кнопок для реализации поиска в последующем
                self.cheat_buttons_list.append(butn)
                movementy += 50  # меняет координаты чтобы следующая кнопка не была на одном месте что и прежняя
                value_of_buttons += 1
                if value_of_buttons == 11:  # этот блок сдвигает столбец с кнопками чтобы они равномерно распределились
                    movementy = 30
                    movementx += 150
                    value_of_buttons = 0
            code_indx += 1

    def show(self):
        self.main_win.show()

    def home(self):  # эта функция выводит главную страницу программы
        self.ui.stackedWidget.setCurrentWidget(self.ui.main_page)

    def show_weapon_page(self):
        # эта функция выводит виджет выбранной категории на которой все отсортированые по категории читы
        self.ui.stackedWidget.setCurrentWidget(self.ui.weapon_page)

    def show_spawn_page(self):
        # эта функция выводит виджет выбранной категории на которой все отсортированые по категории читы
        self.ui.stackedWidget.setCurrentWidget(self.ui.spawn_page)

    def show_gameplay_page(self):
        # эта функция выводит виджет выбранной категории на которой все отсортированые по категории читы
        self.ui.stackedWidget.setCurrentWidget(self.ui.gameplay_page)

    def show_world_page(self):
        # эта функция выводит виджет выбранной категории на которой все отсортированые по категории читы
        self.ui.stackedWidget.setCurrentWidget(self.ui.world_page)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = LoadingScreen()
    ex.show()
    sys.exit(app.exec_())
