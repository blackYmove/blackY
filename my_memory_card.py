from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from random import *

class Question():
    def __init__(self, quest, r_ans, que1, que2, que3):
        self.quest = quest
        self.r_ans = r_ans
        self.que1 = que1
        self.que2 = que2
        self.que3 = que3


p = QApplication([])
ok = QWidget()
ok.setGeometry(100,100,400,400)
ok.setWindowTitle('Memory card')
pbut = QPushButton('Ответить')
l_q = QLabel('Какой правильный ответ?')

box1 = QGroupBox('Варианты ответов')

que1 = QRadioButton('1')
que2 = QRadioButton('2')
que3 = QRadioButton('3')
que4 = QRadioButton('4')

a1 = QVBoxLayout()
a2 = QHBoxLayout()
a3 = QHBoxLayout()

a2.addWidget(que1)
a2.addWidget(que2)
a3.addWidget(que3)
a3.addWidget(que4)
a1.addLayout(a2)
a1.addLayout(a3)

box1.setLayout(a1)

l_c = QVBoxLayout()
l_l1 = QHBoxLayout()
l_l2 = QHBoxLayout()
l_l3 = QHBoxLayout()

l_l1.addWidget(l_q, alignment=Qt.AlignCenter)
l_l2.addWidget(box1)
l_l3.addWidget(pbut, alignment=Qt.AlignCenter)

l_c.addLayout(l_l1, stretch=2)
l_c.addLayout(l_l2, stretch=8)
l_c.addLayout(l_l3, stretch=3)
l_c.setSpacing(5)

ok.setLayout(l_c)

box2 = QGroupBox('Результат теста')

l_res = QLabel('прав ты или нет?')
l_cor = QLabel('Правильный ответ')

lay_res = QVBoxLayout()
lay_res.addWidget(l_res, alignment=(Qt.AlignLeft | Qt.AlignTop))
lay_res.addWidget(l_cor, 2, Qt.AlignCenter)
box2.setLayout(lay_res)
l_l2.addWidget(box2)

box2.hide()
RadGr = QButtonGroup()
RadGr.addButton(que1)
RadGr.addButton(que2)
RadGr.addButton(que3)
RadGr.addButton(que4)

def s_tx():
    box1.show()
    box2.hide()
    pbut.setText('Ответить')
    RadGr.setExclusive(False)
    que1.setChecked(False)
    que2.setChecked(False)
    que3.setChecked(False)
    que4.setChecked(False)
    RadGr.setExclusive(True)

ans = [que1, que2, que3, que4]

def s_res():
    box1.hide()
    box2.show()
    pbut.setText('Следующий вопрос')

def ask(q: Question):
    shuffle(ans)
    ans[0].setText(q.r_ans)
    ans[1].setText(q.que1)
    ans[2].setText(q.que2)
    ans[3].setText(q.que3)
    l_q.setText(q.quest)
    l_cor.setText(q.r_ans)
    s_tx()

def ch_ans():
    if ans[0].isChecked():
        l_res.setText('Правильно!')
        ok.score +=1
        print('Статистика\n-Всего вопросов:', ok.total,'\n-Правельных ответов', ok.score)
        print('Рейтинг:',(ok.score/ok.total*100), '%')
    if ans[1].isChecked() or ans[2].isChecked() or ans[3].isChecked():
        l_res.setText('Неверно!')
        print('Рейтинг:',(ok.score/ok.total*100), '%')
    s_res()
ok.c_q = -1

qs = []
qs.append(Question('Какая самая длинная река в России?', 'Лена', 'Енисей', 'Волга', 'Обь'))
qs.append(Question('В каком городе ездит самый быстрый поезд «Маглев»?', 'Шанхай', 'Нью-Йорк', 'Лоднон', 'Москва'))
qs.append(Question('Какой самый высокий водопад в мире?', 'Анхель', 'Виктория', 'Ниагарский', 'Тугела'))
qs.append(Question('Какое озеро самое глубокое на планете Земля?', 'Байкал', 'Мичиган', 'Сан-Мартин', 'Восток'))
qs.append(Question('В какой последовательности расположены цвета на российском флаге?', ' белый, синий, красный', 'красный, белый, синий', 'синий, белый, красный', 'красный, синий, белый'))
qs.append(Question('Сколько в России субъектов Федерации?', '85', '120', '73', '90'))
qs.append(Question('Как называется длина круга?', 'Окружность', 'Диаметр', 'Радиус', 'Площадь'))
qs.append(Question('Сколько ребер у куба?', '12', '3', '6', '8'))
qs.append(Question('Какое число идет после триллиона?', 'Квадриллион', 'Миллиард', 'Квинтиллион', 'Гугол'))
qs.append(Question('Какой формы знак остановки (Движение без остановки запрещено)?', 'Октагон', 'Шестиугольник', 'Трапеция', 'Параллелограмм'))

def n_q():
    ok.total += 1
    print('Статистика\n-Всего вопросов:', ok.total,'\n-Правельных ответов', ok.score)
    c_q1 = randint(0, len(qs) - 1)
    q = qs[c_q1]
    ask(q)

def click_ok():
    if pbut.text() == 'Ответить':
        ch_ans()
    else:
        n_q()

c_q1 = -1
ok.score = 0
ok.total = 0

pbut.clicked.connect(click_ok)
n_q()
ok.show()
p.exec_()