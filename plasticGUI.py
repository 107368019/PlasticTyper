import plastic
import sys
import os
from PyQt6.QtWidgets import QStyleFactory,QTabWidget,QApplication, QWidget, QCalendarWidget,QCheckBox,QMessageBox, QPushButton,QLabel,QLineEdit, QVBoxLayout ,QGridLayout,QComboBox
from PyQt6.QtCore import Qt 
from PyQt6.QtGui import QPalette, QTextCharFormat,QIcon

class MyApp(QWidget):
    def btnClicked(self):
        sender = self.sender()  
        text = sender.text() 
        
        self.data['mode']= text


        # self.close()

        plastic.doAutoTyping(self.data)

    def userComboActivated(self, text):
        self.data['user']= text

    def practiceTimeComboActivated(self, index):
        
        self.data['practiceTime']= index


    def __init__(self):
        super().__init__()
        self.window_width, self.window_height = 250, 50
        self.setMinimumSize(self.window_width, self.window_height)
        self.setWindowTitle('Typing Master')
        self.setWindowIcon(QIcon('maple.jpg'))
        self.setStyleSheet('''
            QWidget {
                font-size: 20px;
            }
        ''')        

        self.data = {'user':'建威','mode':'開始測驗','practiceTime':'0'}
        

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        userLayout = QGridLayout()


        userCombo = QComboBox()
        userCombo.setProperty('id','user')
        userCombo.addItem("建威")
        userCombo.addItem("宇翔")
        userCombo.addItem("美樺")

        # 创建标签用于显示选择的选项
        comboLabel = QLabel('<font size="2"> User : </font>')

        # 连接下拉列表的信号与槽
        userCombo.textActivated.connect(self.userComboActivated)

        userLayout.addWidget(comboLabel, 3, 0)
        userLayout.addWidget(userCombo, 3, 1)

        self.layout.addLayout(userLayout)




        # 创建 QTabWidget
        tab_widget = QTabWidget()

        # 创建第一个标签页
        tab1 = QWidget()
        tab1.layout = QGridLayout()
        testBtn = QPushButton("開始測驗")
        tab1.layout.addWidget(QLabel(),0 ,0 )
        tab1.layout.addWidget(testBtn,0 ,1 )
        testBtn.clicked.connect(self.btnClicked)
        tab1.setLayout(tab1.layout)

        # 创建第二个标签页
        tab2 = QWidget()
        tab2.layout = QGridLayout()
        tab2.layout.addWidget(QLabel("練習時間") , 0, 0)

        pracitceCombo = QComboBox()    
        
        pracitceCombo.setProperty('id','practiceTime')
        pracitceCombo.addItem("1分鐘")
        pracitceCombo.addItem("5分鐘")
        pracitceCombo.addItem("10分鐘")
        pracitceCombo.activated.connect(self.practiceTimeComboActivated) 
        tab2.layout.addWidget(pracitceCombo , 0, 1)


        practiceBtn = QPushButton("開始練習")
        practiceBtn.clicked.connect(self.btnClicked)
        tab2.layout.addWidget(practiceBtn , 1, 1)
        tab2.setLayout(tab2.layout)

        # 将标签页添加到 QTabWidget
        tab_widget.addTab(tab1, "測驗")
        tab_widget.addTab(tab2, "練習")


        self.layout.addWidget(tab_widget)

        autor_label = QLabel('<font size="1"> Autor :  Ted </font>')
        version_label = QLabel('<font size="1"> Version : 1.0 </font>')
        
        self.layout.addWidget(autor_label)
        self.layout.addWidget(version_label)


        



        
if __name__ == '__main__':

    app = QApplication([])
    app.setStyle('Fusion')
    # app.setStyle('Macintosh')


    myApp = MyApp()
    
    myApp.show()
    
    app.exec()
    # try:
    #     sys.exit(app.exec())
    # except SystemExit:
    #     print('Closing Window...')