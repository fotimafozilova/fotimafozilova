from PyQt5. QtWidgets import QApplication, QWidget, QLabel,QPushButton,QRadioButton, QCheckBox, QMessageBox,QButtonGroup
import os
os.system("cls")
count = 0
jamlash = 0
TESTS = [
    {
        'id': 1,
        'question': "Islomda birinchi shahid bo'lgan ayol sahobiya kim edi?",
        'answers': {
            'A':" Omina bintu Vahb ",
            'B':" Somayya bintu Xayyat ",
            'C':" Safiyya bintu Abdulmuttalib",
        },
        'right_ans':['B']
    },
    {
        'id': 2,
        'question': "Payg'ambarimiz(s.a.v) sut onalari kim bo'lgan?",
        'answers': {
            'A':" Atoqa bintu Abdulmuttalib ",
            'B':" Omina bintu Vahb ",
            'C':" Halima binti Abu Zuayb as-Sa'diya",
        },
        'right_ans':['C']
    },
    {
        'id': 3,
        'question': "Muhammad(s.a.v)ning birinchi vafot etgan qizlari?",
        'answers': {
            'A':" Ruqayya bintu Muhammad(s.a.v) ",
            'B':" Ummu Kulsum bintu Muhammad(s.a.v) ",
            'C':" Fotima bintu Muhammad(s.a.v)",
        },
        'right_ans':['A']
    },
    {
        'id': 4,
        'question': "Uch Marta jannat bashorotini olgan sahoba kim?",
        'answers': {
            'A':" Abdulloh ibn Amr ",
            'B':" Said ibn Zayd  ",
            'C':" Tolha ibn Ubaydulloh",
        },
        'right_ans':['A']
    },
    {
        'id': 5,
        'question': "Rosululloh(s.a.v)ning o'g'illarini soni nechta?",
        'answers': {
            'A':" 4 ",
            'B':" 3 ",
            'C':" 2",
        },
        'right_ans':['B']
    },
    {
        'id': 6,
        'question': "Onalari sabab Rosululloh bilan ko'risha olmagan kishi ?",
        'answers': {
            'A':" Sa'd ibn Abuvaqqos ",
            'B':" Abu Ubayda in Jarroh ",
            'C':" Uvayis Qaraniy",
        },
        'right_ans':['C']
    },
    {
        'id': 7,
        'question': "Juma so'zining ma'nosi qanday?",
        'answers': {
            'A':" Jamlash ",
            'B':" Umug'lash ",
            'C':" Mag'firat Qilish",
        },
        'right_ans':['A']
    },
    {
        'id':8,
        'question': "Qalamda birinchi bo'lb qaysi payg'ambar yozgan?",
        'answers': {
            'A':" Sulaymon(alayhissalom) ",
            'B':" Nuh(alayhissalom) ",
            'C':" Idris(alayhissalom)",
        },
        'right_ans':['C']
    },
    {
        'id':9,
        'question': "Rosululloh(s.a.v)ning birinchi muazzini kim edi?",
        'answers': {
            'A':" Abu Bakr Siddiq(r.a.) ",
            'B':" Bilol ibn Roboh(r.a.) ",
            'C':" Anas ibn Molik(r.a.)",
        },
        'right_ans':['B']
    },
    {
        'id':10,
        'question': "Qiyomatkun ogoh surini qaysi fairishta chaladi?",
        'answers': {
            'A':" Mikoil alayhissalom ",
            'B':" Jabroil alayhissalom ",
            'C':" Isrofil alayhissalom ",
        },
        'right_ans':['C']
    },
     {
        'id':11,
        'question': "Payg'ambar(s.a.v) kimni yuziga tuproq soching degan?",
        'answers': {
            'A':" Maddohlarning ",
            'B':" Yolg'onchilarning ",
            'C':" G'iybatchilarning ",
        },
        'right_ans':['A']
    },
      {
        'id':12,
        'question': "Islomning beshinchi arkoni qaysi?",
        'answers': {
            'A':" Zakot",
            'B':" Haj ",
            'C':" Ro'za ",
        },
        'right_ans':['B']
    },
     {
        'id':13,
        'question': "Ibrohim alayhissalomning otalarini ismi ?",
        'answers': {
            'A':" Ozor",
            'B':" Abu Jahl ",
            'C':" Shuayb(a.s) ",
        },
        'right_ans':['A']
    },
     {
        'id':14,
        'question': "Quyosh ufqqa botayotganda qaysi namoz o'qiladi?",
        'answers': {
            'A':" Shom namozi ",
            'B':" Asr namozining qazosi ",
            'C':" To'g'ri javob yo'q ",
        },
        'right_ans':['C']
    },
     {
        'id':15,
        'question': "Haj amalining uch eng asosiy sharti ?",
        'answers': {
            'A':" Arofatdagi tura, Tavof, Ihrom kiyish ",
            'B':" Tavof,Sa'y, Muzdalifadagi tura, ",
            'C':" Boshni qirqish, qisqartirish,Tavof ",
        },
        'right_ans':['A']
    },    
]
class Window(QWidget):
    son_index = 0
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Test by Fotima")
        self.setFixedSize(1000,500)
        self.lastlabel = QLabel(self)
        self.lastlabel.move(200,200)
        self.lastlabel.hide()
        self.savollabel = QLabel("Question",self)
        self.savollabel.setStyleSheet("font-size:26px;font-weight:bold;color:purple;")
        self.savollabel.move(10,10)
        
        self.a_variant = QRadioButton("A",self)
        self.a_variant.setStyleSheet("font-size: 26px; color:darkred;")
        self.a_variant.move(50,60)
        
        self.b_variant = QRadioButton("B",self)
        self.b_variant.setStyleSheet("font-size: 26px; color:darkred;")
        self.b_variant.move(50,100)
        
        self.c_variant = QRadioButton("C",self)
        self.c_variant.setStyleSheet("font-size: 26px; color:darkred;")
        self.c_variant.move(50,140)
        
        self.javoblar = QButtonGroup()
        self.javoblar.addButton(self.a_variant)
        self.javoblar.addButton(self.b_variant)
        self.javoblar.addButton(self.c_variant)
        
        self.nextBtn = QPushButton("keyingi", self)
        self.nextBtn.setStyleSheet("font-size: 22px;")
        self.nextBtn.move(800, 400)

        self.buttondiqoshish()

        self.nextBtn.clicked.connect(self.nextFunction)
        self.show()
        
    def buttondiqoshish(self):
        question = TESTS[self.son_index]
        
        self.savollabel.setText(question['question'])
        self.a_variant.setText(question['answers']['A'])
        self.b_variant.setText(question['answers']['B'])
        self.c_variant.setText(question['answers']['C'])
        

        self.a_variant.adjustSize()
        self.b_variant.adjustSize()
        self.c_variant.adjustSize()
        
    def clearbuttons(self):
        self.javoblar.setExclusive(False)  
        for button in self.javoblar.buttons():
            button.setChecked(False)
        self.javoblar.setExclusive(True) 
        
    def nextFunction(self):
        global count
        
        selected_button = self.javoblar.checkedButton()
        javoblartext = []
        if selected_button:
            for i in range(len(TESTS[self.son_index]["right_ans"])):
                javoblartext.append(TESTS[self.son_index]["answers"][TESTS[self.son_index]["right_ans"][i]])
            if selected_button.text() in javoblartext:
                count += 1               
        self.clearbuttons()
        self.son_index += 1
        
        if self.son_index >= len(TESTS):
            self.a_variant.close()
            self.b_variant.close()
            self.c_variant.close()
            self.savollabel.clear()
            self.nextBtn.close()
            self.lastlabel.setText(f"Siz {count} ta to'g'ri javob topdingiz :)")
            self.lastlabel.setStyleSheet("font-size: 28px;color: purple")
            self.lastlabel.show()
            print(f"{count}")
           
        else:
            self.buttondiqoshish()    
            
app = QApplication([])
oyna = Window()
app.exec()