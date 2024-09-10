from PyQt5.QtWidgets import QApplication, QWidget,QLabel,QPushButton
from os import system
system("cls")


app= QApplication([])

oyna = QWidget()
oyna.setWindowTitle("Asmaul Husna by Fotima")
oyna.setGeometry(700,50,870,950)
oyna.setStyleSheet("""
       background-color: #f2f7ab;           
                   """)

sozLabel = QLabel("<<ASMAUL HUSNA>>",oyna)
sozLabel.move(280,0)
sozLabel.setStyleSheet("""
      font-size: 30px;                 
      color: black;
      font-family: calibri; 
                     
                       """)


info = {
    '1': """ ..........AR-ROHMAN......... 
                     << 55:01 >>
                      الرحمن
    Bu dunyoda barcha mo'minga ham kofirga
    ham birdek ne'mat beradigan Zot...  """,
    '2': """...........AR-ROHIYM............
                    << 114 >>
                    الرحيم
    Oxirat kuni faqat mo'minlargagina rahim,
    shafqat qiladigan rahimli Zot...
    """,
    '3': """..........AL-MALIK........
            << 59:23, 20:114, 23:116 >>
                    الملك
    Barcha mahluqotlarning haqiqiy egasi,
    cheksiz mulku saltanat sohibi bo'lgan Zot...    
    
    """,
    '4': """......AL-QUDDUS......   
            << 59:23,62:1 >>
                القدوس
    Barcha aybu nuqsonlardan,noloyiq
    sifatlardan pok Zot...    
    """,
    '5': """ ..........AS-SALAM......... 
                     << 59:23 >>
                     السلام
    O'ziga hech qanday nuqson yetmaydigan,
    bandalariga salomatlik ato etadigan,
    jannat ahliga salom beradigan Zot...  """,
    '6': """...........MU'MIN............
                    << 59:23 >>
                    المؤمن
   Iymon ato etadigan mo'minlarga omonlik beradigan Zot...
    """,
    '7': """..........AL-MUHAYMIN........
                    << 59:23 >>
                    المهيمن
    Hamma narsani bilib qamrab kuzatib turadigan,
    saqlab qo'riqlaydigan Zot...    
    
    """,
    '8': """......AL-AZIZ......   
         <<3:6, 4:158, 9:40, 48:7,59:23>>
                  العزيز 
    Mag'lub bo'lmaydigan mutloq Aziz Zot...    
    """,
    '9': """......AL-JABBAR ......   
                << 59:23 >>
                الجبار
    Hukmini butun borliqqa o'tkaza oladigan
    utloq hukmron Zot...    
    """,
    '10': """......AL-MUTAKABBIR......   
                <<59:23>>
                المتكبر
    Buyuklik va ulug'lik namoyon etadigan 
    barchadan buyuk Zot...    
    """,
    '11': """......AL-XOLIQ......   
         << 6:102, 13:16, 36:81, 39: 62, 40:62, 59:24>>
                الخالق
    Hamma narsani tayin qilib shunga muvofiq yaratadigan Zot...    
    """,
    '12': """...... AL-BARI'......   
                 << 59:24 >>
                 البارئ
    Mahluqotlarni yo'qdan bor qilib, o'zaro 
    mutanosib va bir-biriga bog'liq holda yaratagigan Zot...    
    """,
    '13': """...... AL-MUSOVVIR......   
                <<59:24 >>
                	المصور
    Har bir narsaga o'ziga xos shakl xususiyat
    beradigan Zot...    
    """,
    
    '14': """......AL-G'OFFAR ......   
         << 20:82, 38:66, 39:5, 40:42, 71:10 >>
                الغفار
    Ko'p marhamat qilib,
    bandalarini gunohlarini o'z fazli ila 
    kechirib yuboruvchi Zot...    
    """,
    '15': """......AL-QOHHAR ......   
         << 12:39, 13:16, 14:48, 38:65, 39:4, 40:16 >>
                    القهار
    Barcha maxluqotlarni qabzasida tutib,
    ularni o'z hukmiga yuritib va qudrati ila
    bo'ysundirib turuvchi Zot...    
    """,
    '16': """......AL-VAHHAB ......   
         << 38:9, 38:35 >>
         الوهاب
    O'z ne'matlarini tekin ato etuvchi Zot...    
    """,
    '17': """......AL-ROZZAQ......   
         << 51:58>>
         الرزاق
    Barcha tirik mavjudot rizqini yetkazib beruvchi Zot...    
    """,
    '18': """......AL-FATTAH ......   
               << 34:26 >>
               الفتاح
    Hukm etuvchi, rahmat hazinalarini ochuvchi Zot...    
    """,
    '19': """......AL-'ALIM ......   
         << 2:158, 3:92, 4:35, 24:41, 33:40 >>
                    العليم
    Biluvchi, dono, ilm sohibi. Bo'lgan va bo'ladigan,
    avvalgi va oxirgi,
    zohir va botin narsalarning barchasini biluvchi Zot...    
    """,
    '20': """...... AL-QOBIZ ......   
         << 2:245 >>
         القابض
    Kimlarningdir rizqini qiyuvchi, ruhlarni qabz etuvchi (oluvchi) Zot...    
    """,
    '21': """......AL-BASIT ......   
         << 2:245 >>
         الباسط   
    Xohlagan bandaning rizqini mo'l, qalbini keng qiluvchi  Zot...    
    """,
    '22': """...... AL-XOFIZ......   
         << 56:3 >>
            الخافض
    Kofirlar martabasini tushiruvchi Zot...    
    """,
    '23': """......AR-ROFI' ......   
         << 58:11, 6:83 >>
       الرافع
    Mo'minlar martabasini ko'taruvchi Zot...    
    """,
    '24': """...... AL-MU'IZZ ......   
         << 3:26 >>
       المعز
    Mo'min va solih bandalarini aziz,kuchli g'olib qiluvchi Zot...    
    """,
    '25': """......AL-MUZILL......   
         << 3:26 >>
       المذل
    Kofir fosiq bandalarini zalil,hor,tuban qiluvchi Zot...    
    """,
    '26': """......AS-SAMI' ......   
         << 2:127, 2:256, 8:17, 49:1 >>
       	السميع
    Maxfiy va oshkora gap va sharpalarni,
    xatto dildan o'tganini ham, eshituvchi Zot...    
    """,
    '27': """......AL-BASIR ......   
         << 4:58, 17:1, 42:11, 42:27 >>
       البصير
    Hamma maxfiy va oshkora narsalarni ko'ruvchi Zot...    
    """,
    '28': """......AL-HAKAM......   
         << 22:69 >>
       الحكم
    Qat'iy hukm etuvchi Zot...    
    """,
    '29': """......AL-ADL ......   
         << al-Kaf'amiyga qarang >>
       العدل
    O'ta adolatli Zot...    
    """,
    '30': """......AL-LATIF ......   
         << 22:63, 31:16, 33:34 >>
       اللطيف
    Bandalariga sezdirmay o'z lutfu ehsonini yetkasizb beruvchi Zot...    
    """,
    '31': """......AL-XOBIR......   
         << 6:18, 17:30, 49:13, 59:18 >>
       الخبير
    Hamma maxfiy va oshkora ishlardan xabardor Zot...    
    """,
    '32': """......AL-HALIM ......   
         << 2:235, 17:44, 22:59, 35:41 >>
       الحليم
    Jazolashga shoshmaydigan, hilm bilan yaxshilik qilib turuvchi Zot...    
    """,
    '33': """...... AL-'AZIM......   
         <<2:255, 42:4, 56:96 >>
       العظيم
    Azamatli va ulug' zot.
    Aql tasavvur qila olmaydigan darajada azamatli va ulug' Zot...    
    """,
    '34': """......AL-G'OFUR ......   
         << 2:173, 8:69, 16:110, 41:32 >>
       الغفور
    Ko'p mag'firat qiluvchi Zot...    
    """,
    '35': """......ASH-SHAKUR ......   
         << 35:30, 35:34, 42:23, 64:17 >>
       الشكور
    O'z amaliga ko'p savob beruvchi Zot...    
    """,
    '36': """......AL-ALIYY ......   
         << 4:34, 31:30, 42:4, 42:51 34:23 >>
       	العلي
    Martabasi oliylikda benihoya Zot...    
    """,
    '37': """......AL-KABIR ......   
         << 13:9, 22:62, 31:30, 34:23 >>
       الكبير
    Hammadan ulug' Zot...    
    """,
    '38': """...... AL-HAFIZ......   
         << 11:57,12:55 >>
       الحفيظ
    Har bir narsani komil muhofaza qiluvchi Zot...    
    """,
    '39': """......AL-MAQIT ......   
         << 4:85  >>
       المقيت
    Barcha moddiy va ruhiy rizqlarni yaratuvchi Zot...    
    """,
    '40': """......AN-HASIB ......   
         << 4:6, 4:86, 33:39 >>
       الحسيب
    Hisob qiluvchi, kifoya qiluvchi Zot...    
    """,
     '41': """...... AL-JALIL......   
         <<  >>
       الجليل
    Sifatlarida ulug'likka ega Zot...    
    """,
    '42': """......AL-KARIM......   
         << 27:40, 82:6 >>
       الكريم
    Saxovatli va karami keng. Birov so'ramasa ham, 
    hech bir evaz olmasdan, narsalarni ato qiluvchi. Qarama-qarshilikdan pok,
    Karamli ishlar va xislatlar sohibi Zot...    
    """,
     '43': """......AR-ROQIB ......   
         << 4:1, 5:117 >>
       الرقيب
    Doimo kuzatib turuvchi.
    Raqiyb - hech bir zararni ham qo'ymay tekshirib turuvchi Zot...    
    """,
    '44': """...... AL-MUJIB ......   
         << 11:61 >>
       المجيب
    Duolarni ijobat qiluvchi Zot...    
    """,
     '45': """......AL-VASI' ......   
         << 2:268, 3:73, 5:54 >>
       الواسع
    Keng va keng qamrovli  Zot...    
    """,
    '46': """......AL-HAKIM ......   
         <<31:27, 46:2, 57:1, 66:2  >>
       الحكيم
    DONO Zot...    
    """,
     '47': """......AL-VADUD......   
         << 11:90, 85:14 >>
       الودود
    Bandalarini sevuvchi Zot...    
    """,
    '48': """......AL-MAJID ......   
         <<11:73 >>
       المجيد
    Eng ulug'vor Zot...    
    """,
     '49': """...... AL-BA'IS......   
         << 22:7 >>
       الباعث
    O'liklarning tiriltiruvchisi Zot...    
    """,
    '50': """......ASH-SHAXID ......   
         <<4:166, 22:17, 41:53, 48:28 >>
       الشهيد
    Har bir narsaga hoziru nozir. Barchaga shohidlik beruvchi Zot...    
    """,
     '51': """......AL-HAQQ ......   
         << 6:62, 22:6, 23:116, 24:25 >>
       الحق
    Ozgarmas sobit zot. Haqni yuzaga chiqaruvchi Zot...    
    """,
    '52': """...... AL-VAKIL......   
         << 3:173, 4:171, 28:28, 73:9 >>
       الوكيل
    Barchaning ishi unga topshirilgan Zot...    
    """,
     '53': """......AL-QOVVIYY ......   
         << 22:74, 42:19, 57:25 >>
       القوى
    Quvvatli Zot...    
    """,
    '54': """......AL-MATIN ......   
         << 51:58 >>
       المتين
    Matonatli  Zot...    
    """,
     '55': """......AL-VALIY ......   
         << 4:45, 7:196, 42:28, 45:19 >>
       الولى
    Himoya qiluvchi do'st, homiy va yordamchi Zot...    
    """,
    '56': """......AL-HAMID ......   
         << 	14:8, 31:12, 31:26, 41:42 >>
       الحميد
    Barcha maqtovlar ila maqtalgan  Zot...    
    """,
     '57': """......AL-MUHSI ......   
         << 72:28, 78:29 >>
       المحصى
    Barcha narsaning hisobini olgan  Zot...    
    """,
    '58': """......AL-MUBDI ......   
         << 10:34, 27:64, 29:19, 85:13 >>
       المبدئ
    Barcha narsalarni avval boshdan bor qilgan Zot...    
    """,
     '59': """......AL-MU'ID ......   
         << 10:34, 27:64, 29:19, 85:13 >>
       المعيد
    Barcha mahluqotlarni hayotgan so'ng o'limga o'limdan
    so'ng hayotga qaytaradigan Zot...    
    """,
    '60': """......AL-MUHYI ......   
         << 7:158, 15:23, 30:50, 57:2 >>
       المحيى
    Hayot bradiganZot...    
    """,
     '61': """...... AL-MUMIT......   
         << 3:156, 7:158, 15:23, 57:2 >>
       المميت
    Ajali yetgan jonzotlarni o'ldiradigan jonini oladigan Zot...    
    """,
    '62': """......AL-HAYY ......   
         << 2:255, 3:2, 20:111, 25:58, 40:65 >>
       الحي
    Azialiy va abadiy barhayot Zot...    
    """,
     '63': """......AL-QOYYUM ......   
         << 2:255, 3:2, 20:111 >>
      القيوم 
    O'z o'zidan qoim bo'lgan va boshqalarni qoim qilgan Zot...    
    """,
    '64': """......AL-VAJID ......   
         << 38:44 >>
       الواجد
    Topuvchi. Xohlagan narsasini topuvchi.
    Bu ishda birov Uni to'sa olmaydi Zot...    
    """,
     '65': """......AL-MAJID ......   
         <<  >>
       الماجد
    Majdu sharaf sohibi bolgan  Zot...    
    """,
    '66': """......AL-VAHID ......   
         <<  >>
       الواحد
     U zot oz zotida ham, sifatlarida ham va ishlarida ham birdir...    
    """,
     '67': """......AL-AHAD ......   
         <<  >>
       الصمد
    Mutloq yagona Zot...    
    """,
    '68': """......AS-SOMAD ......   
         << 112:2 >>
       الصمد
    Hech narsaga muhtoj bo'lmagan behojat,ammo barchani hojati 
    tushadigan hojatbaror Zot...    
    """,
     '69': """...... AL-QODIR......   
         << 6:65, 46:33, 75:40 >>
       	القادر
    Cheksiz qudrat sohibi. 
    U zot har bir narsaga qodirdir. 
    har bir ish unga osondir Zot...    
    """,
    '70': """...... AL-MUQTADIR......   
         << 18:45, 54:42, 6:65>>
       المقتدر
    Juda ham qudratli Zot...    
    """,
    '71': """...... AL-MUQODDIM......   
         <<16:61 >>
      المقدم
    Mo'min va solih bandalarini muqaddam qoyib o'ziga yaqin qiladigan Zot...    
    """,
    '72': """......AL-MU'AXXIR......   
         << 71:4>>
      المؤخر
    Kofir va fosiq bandalarini ortda qoldirib o'zidan uzoq qiladigan Zot...    
    """,
    '73': """......AL-AVVAL ......   
         <<57:3 >>
      الأول
    Barcha narsadan avval bor bo'lgan azaliy  Zot...    
    """,
    '74': """......AL-AXIR ......   
         << 57:3>>
      الأخر
    barcha narsadan keyin o'zi qoladigan abadir  Zot...    
    """,
    '75': """......AZ-ZOHIR ......   
         <<57:3 >>
      الظاهر
    Borligi ochiq ravshan ayon bo'lgan  Zot...    
    """,
    '76': """......AL-BATIN ......   
         <<57:3 >>
      	الباطن
    Sezgi a'zolarimizdan yashirin bo'lgan maxfiy narsalarimizni
    ham biladigan Zot...    
    """,
    '77': """......AL-VALII ......   
         <<13:11 >>
      الوالي
    Har bir narsaga voliy - ega bo'lgan Zot...    
    """,
    '78': """......AL-MUTA'ALI ......   
         <<57:3 >>
      المتعالي
    Nuqsonlardan yuqori turuvchi Zot...    
    """,
    '79': """......AL-BARR ......   
         <<52:28 >>
      البر
    Ulug' yaxshilik qiluvchi Zot...    
    """,
    '80': """......AT-TAVVAB ......   
         <<2:128, 4:64, 49:12, 110:3 >>
      التواب
    Bandalarni tavbaga yo'llovchi 
    va ularning tavbasini ko'plab qabul qiluvchi Zot...    
    """,
    '81': """......AL-MUNTAQIM ......   
         << 32:22, 43:41, 44:16>>
      المنتقم
    Zolim va osiylardan intiqom oluvchi Zot...    
    """,
    '82': """......AL-AFUVV ......   
         <<	4:43, 4:99, 4:149, 22:60, 58:2 >>
      	العفو
    Afv qiluvchi Zot...    
    """,
    '83': """......AR-RO'UF ......   
         <<9:117, 57:9, 59:10 >>
      الرؤوف
    O'ta shafqatli va mehribon Zot...    
    """,
    '84': """......MALIK-UL-MULK ......   
         <<3:26 >>
      	مالك الملك
    Butun mulk va saltanatning egasi bo'lgan Zot...    
    """,
    '85': """......ZUL-JALALI-VAL'IKROM ......   
         <<55:27, 55:78 >>
        ذو الجلال   والإكرام
    Sharaf va kamol egasi. Karam va ikrom egasi bo'lgan Zot...    
    """,
    '86': """......AL-MAQSIT ......   
         <<3:18; al-Kafʿami >>
      المقسط
    O'z adolati ila mazlumlarga nusrat va
    zolimlarga jazo beruvchi.Zot...    
    """,
    '87': """......AL-JAMI' ......   
         <<3:9 >>
        |الجامع
    Jamlovchi. Barcha haqiqatlarni jamlovchi.
    Odamlarni qiyomat kuni jamlovchi. Zot...    
    """,
    '88': """......AL-G'ONI ......   
         <<	39:7, 47:38, 57:24 >>
      الغني
    Behojat. Uning hech kim va hech narsaga hojati tushmaydi. Zot...    
    """,
    '89': """......AL-MUG'NI ......   
         <<9:28 >>
      المغني
    Behojat qiluvchi.
    U zot O'z bandalaridan qay birini xohlasa behojat
    qilib qo'yadi Zot...    
    """,
    '90': """......AL-MANI' ......   
         <<al-Kaf'ami >>
      المانع
    Man qiluvchi Zot...    
    """,
    '91': """......AZ-ZARR ......   
         << 6:17; al-KafʿamI>>
      الضار
    Zarar qiluvchi. Zararli narsalarni ham yaratuvchi Zot...    
    """,
    '92': """...... AN-NAFI'......   
         <<30:37 >>
      النافع
    Manfaat beruvchi Zot...    
    """,
    '93': """......AN-NUR ......   
         << 24:35>>
      النور
    O'z-o'zi ila zohir bo'lgan va o'zgalarni zohir qilgan Zot...    
    """,
    '94': """......AL-HADI' ......   
         <<22:54 >>
      الهادي
    Hidoyatga loyiq bandalarini o'z yo'lida hidoyat qiladigan  Zot...    
    """,
    '95': """......AL-BADI'......   
         <<2:117, 6:101 >>
      البديع
    O'xshashi yo'q narsalarni keltiruvchi Zot...    
    """,
    '96': """......AL-BAQI' ......   
         <<55:27; al-Kafʿami >>
      الباقي
    Boqiy qoluvchi. U doimiy bordir, unga foniylik oriz bo'lmas Zot...    
    """,
    '97': """......AL-VARIS ......   
         <<55:27; al-Kafʿami >>
      الوارث
    Muvjudotlar yo'q bo'lganda ham boqiy qoluvchi zot Zot...    
    """,
    '98': """......AR-ROSHID ......   
         <<2:256,18:17 >>
      الرشيد
    To'g'ri yo'lga irshod qiluvchi. Zot...    
    """,
    '99': """......AS-SOBUR ......   
         <<2:153, 3:200, 103:3 >>
      الصبور
    O'ta sabrli. Osiylarni azoblashga shoshilmaydi Zot...    
    """  
    
}
def bosildi(btn:QPushButton):
    txt = btn.text().lower()
    sozLabel.setText(info[txt])
    sozLabel.adjustSize()
    sozLabel.move((oyna.width() - sozLabel.width())//2,100)
    
bir = QPushButton('<-',oyna)
bir.setGeometry(800,0,50,50)
bir.setStyleSheet("""
      font-size: 25px;
      border-radius: 25px;
      border: 1px solid black;
      background-color: pink;             
                  """)   
    
    
       
a1 = QPushButton("1",oyna)
a1.setGeometry(50,300,60,60)
a1.setStyleSheet("""
  background-color: pink;  
  color: green;
  font-size: 22px;   
                 """)

a2 = QPushButton("2",oyna)
a2.setGeometry(120,300,60,60)
a2.setStyleSheet("""
  background-color: pink;  
  color: green;
  font-size: 22px;   
                 """)

a3 = QPushButton("3",oyna)
a3.setGeometry(190,300,60,60)
a3.setStyleSheet("""
  background-color: pink;  
  color: green;
  font-size: 22px;   
                 """)

a4 = QPushButton("4",oyna)
a4.setGeometry(260,300,60,60)
a4.setStyleSheet("""
  background-color: pink;  
  color: green;
  font-size: 22px;   
                 """)

a5 = QPushButton("5",oyna)
a5.setGeometry(330,300,60,60)
a5.setStyleSheet("""
  background-color: pink;  
  color: green;
  font-size: 22px;   
                 """)

a6 = QPushButton("6",oyna)
a6.setGeometry(400,300,60,60)
a6.setStyleSheet("""
  background-color: pink;  
  color: green;
  font-size: 22px;   
                 """)

a7 = QPushButton("7",oyna)
a7.setGeometry(470,300,60,60)
a7.setStyleSheet("""
  background-color: pink;  
  color: green;
  font-size: 22px;   
                 """)

a8 = QPushButton("8",oyna)
a8.setGeometry(540,300,60,60)
a8.setStyleSheet("""
  background-color: pink;  
  color: green;
  font-size: 22px;   
                 """)

a9 = QPushButton("9",oyna)
a9.setGeometry(610,300,60,60)
a9.setStyleSheet("""
  background-color: pink;  
  color: green;
  font-size: 22px;   
                 """)
a10 = QPushButton("10",oyna)
a10.setGeometry(680,300,60,60)
a10.setStyleSheet("""
  background-color: pink;  
  color: green;
  font-size: 22px;   
                 """)
a11 = QPushButton("11",oyna)
a11.setGeometry(750,300,60,60)
a11.setStyleSheet("""
  background-color: pink;  
  color: green;
  font-size: 22px;   
                 """)

a12 = QPushButton("12",oyna)
a12.setGeometry(50,370,60,60)
a12.setStyleSheet("""
  background-color: pink;  
  color: green;
  font-size: 22px;   
                 """)

a13 = QPushButton("13",oyna)
a13.setGeometry(120,370,60,60)
a13.setStyleSheet("""
  background-color: pink;  
  color: green;
  font-size: 22px;   
                 """)

a14 = QPushButton("14",oyna)
a14.setGeometry(190,370,60,60)
a14.setStyleSheet("""
  background-color: pink;  
  color: green;
  font-size: 22px;   
                 """)

a15 = QPushButton("15",oyna)
a15.setGeometry(260,370,60,60)
a15.setStyleSheet("""
  background-color: pink;  
  color: green;
  font-size: 22px;   
                 """)

a16 = QPushButton("16",oyna)
a16.setGeometry(330,370,60,60)
a16.setStyleSheet("""
  background-color: pink;  
  color: green;
  font-size: 22px;   
                 """)

a17 = QPushButton("17",oyna)
a17.setGeometry(400,370,60,60)
a17.setStyleSheet("""
  background-color: pink;  
  color: green;
  font-size: 22px;   
                 """)

a18 = QPushButton("18",oyna)
a18.setGeometry(470,370,60,60)
a18.setStyleSheet("""
  background-color: pink;  
  color: green;
  font-size: 22px;   
                 """)

a19 = QPushButton("19",oyna)
a19.setGeometry(540,370,60,60)
a19.setStyleSheet("""
  background-color: pink;  
  color: green;
  font-size: 22px;   
                 """)
a20 = QPushButton("20",oyna)
a20.setGeometry(610,370,60,60)
a20.setStyleSheet("""
  background-color: pink;  
  color: green;
  font-size: 22px;   
                 """)
a21 = QPushButton("21",oyna)
a21.setGeometry(680,370,60,60)
a21.setStyleSheet("""
  background-color: pink;  
  color: green;
  font-size: 22px;   
                 """)

a22 = QPushButton("22",oyna)
a22.setGeometry(750,370,60,60)
a22.setStyleSheet("""
  background-color: pink;  
  color: green;
  font-size: 22px;   
                 """)


a23 = QPushButton("23",oyna)
a23.setGeometry(50,440,60,60)
a23.setStyleSheet("""
  background-color: pink;  
  color: green;
  font-size: 22px;   
                 """)

a24 = QPushButton("24",oyna)
a24.setGeometry(120,440,60,60)
a24.setStyleSheet("""
  background-color: pink;  
  color: green;
  font-size: 22px;   
                 """)

a25 = QPushButton("25",oyna)
a25.setGeometry(190,440,60,60)
a25.setStyleSheet("""
  background-color: pink;  
  color: green;
  font-size: 22px;   
                 """)

a26 = QPushButton("26",oyna)
a26.setGeometry(260,440,60,60)
a26.setStyleSheet("""
  background-color: pink;  
  color: green;
  font-size: 22px;   
                 """)

a27 = QPushButton("27",oyna)
a27.setGeometry(330,440,60,60)
a27.setStyleSheet("""
  background-color: pink;  
  color: green;
  font-size: 22px;   
                 """)

a28 = QPushButton("28",oyna)
a28.setGeometry(400,440,60,60)
a28.setStyleSheet("""
  background-color: pink;  
  color: green;
  font-size: 22px;   
                 """)

a29 = QPushButton("29",oyna)
a29.setGeometry(470,440,60,60)
a29.setStyleSheet("""
  background-color: pink;  
  color: green;
  font-size: 22px;   
                 """)

a30 = QPushButton("30",oyna)
a30.setGeometry(540,440,60,60)
a30.setStyleSheet("""
  background-color: pink;  
  color: green;
  font-size: 22px;   
                 """)

a31 = QPushButton("31",oyna)
a31.setGeometry(610,440,60,60)
a31.setStyleSheet("""
  background-color: pink;  
  color: green;
  font-size: 22px;   
                 """)
a32 = QPushButton("32",oyna)
a32.setGeometry(680,440,60,60)
a32.setStyleSheet("""
  background-color: pink;  
  color: green;
  font-size: 22px;   
                 """)
a33 = QPushButton("33",oyna)
a33.setGeometry(750,440,60,60)
a33.setStyleSheet("""
  background-color: pink;  
  color: green;
  font-size: 22px;   
                 """)

a34 = QPushButton("34",oyna)
a34.setGeometry(50,510,60,60)
a34.setStyleSheet("""
  background-color: pink;  
  color: green;
  font-size: 22px;   
                 """)

a35 = QPushButton("35",oyna)
a35.setGeometry(120,510,60,60)
a35.setStyleSheet("""
  background-color: pink;  
  color: green;
  font-size: 22px;   
                 """)

a36 = QPushButton("36",oyna)
a36.setGeometry(190,510,60,60)
a36.setStyleSheet("""
  background-color: pink;  
  color: green;
  font-size: 22px;   
                 """)

a37 = QPushButton("37",oyna)
a37.setGeometry(260,510,60,60)
a37.setStyleSheet("""
  background-color: pink;  
  color: green;
  font-size: 22px;   
                 """)

a37 = QPushButton("37",oyna)
a37.setGeometry(330,510,60,60)
a37.setStyleSheet("""
  background-color: pink;  
  color: green;
  font-size: 22px;   
                 """)
a38 = QPushButton("37",oyna)
a38.setGeometry(330,510,60,60)
a38.setStyleSheet("""
  background-color: pink;  
  color: green;
  font-size: 22px;   
                 """)

a39 = QPushButton("39",oyna)
a39.setGeometry(400,510,60,60)
a39.setStyleSheet("""
  background-color: pink;  
  color: green;
  font-size: 22px;   
                 """)

a40 = QPushButton("40",oyna)
a40.setGeometry(470,510,60,60)
a40.setStyleSheet("""
  background-color: pink;  
  color: green;
  font-size: 22px;   
                 """)

a41 = QPushButton("41",oyna)
a41.setGeometry(540,510,60,60)
a41.setStyleSheet("""
  background-color: pink;  
  color: green;
  font-size: 22px;   
                 """)
a42 = QPushButton("42",oyna)
a42.setGeometry(610,510,60,60)
a42.setStyleSheet("""
  background-color: pink;  
  color: green;
  font-size: 22px;   
                 """)
a43 = QPushButton("43",oyna)
a43.setGeometry(680,510,60,60)
a43.setStyleSheet("""
  background-color: pink;  
  color: green;
  font-size: 22px;   
                 """)

a44 = QPushButton("44",oyna)
a44.setGeometry(750,510,60,60)
a44.setStyleSheet("""
  background-color: pink;  
  color: green;
  font-size: 22px;   
                 """)

a45 = QPushButton("45",oyna)
a45.setGeometry(50,580,60,60)
a45.setStyleSheet("""
  background-color: pink;  
  color: green;
  font-size: 22px;   
                 """)

a46 = QPushButton("46",oyna)
a46.setGeometry(120,580,60,60)
a46.setStyleSheet("""
  background-color: pink;  
  color: green;
  font-size: 22px;   
                 """)

a47 = QPushButton("47",oyna)
a47.setGeometry(190,580,60,60)
a47.setStyleSheet("""
  background-color: pink;  
  color: green;
  font-size: 22px;   
                 """)

a48 = QPushButton("48",oyna)
a48.setGeometry(260,580,60,60)
a48.setStyleSheet("""
  background-color: pink;  
  color: green;
  font-size: 22px;   
                 """)

a49 = QPushButton("49",oyna)
a49.setGeometry(330,580,60,60)
a49.setStyleSheet("""
  background-color: pink;  
  color: green;
  font-size: 22px;   
                 """)

a50 = QPushButton("50",oyna)
a50.setGeometry(400,580,60,60)
a50.setStyleSheet("""
  background-color: pink;  
  color: green;
  font-size: 22px;   
                 """)

a51 = QPushButton("51",oyna)
a51.setGeometry(470,580,60,60)
a51.setStyleSheet("""
  background-color: pink;  
  color: green;
  font-size: 22px;   
                 """)

a52 = QPushButton("52",oyna)
a52.setGeometry(540,580,60,60)
a52.setStyleSheet("""
  background-color: pink;  
  color: green;
  font-size: 22px;   
                 """)

a53 = QPushButton("53",oyna)
a53.setGeometry(610,580,60,60)
a53.setStyleSheet("""
  background-color: pink;  
  color: green;
  font-size: 22px;   
                 """)
a54 = QPushButton("54",oyna)
a54.setGeometry(680,580,60,60)
a54.setStyleSheet("""
  background-color: pink;  
  color: green;
  font-size: 22px;   
                 """)
a55 = QPushButton("55",oyna)
a55.setGeometry(750,580,60,60)
a55.setStyleSheet("""
  background-color: pink;  
  color: green;
  font-size: 22px;   
                 """)

a56 = QPushButton("56",oyna)
a56.setGeometry(50,650,60,60)
a56.setStyleSheet("""
  background-color: pink;  
  color: green;
  font-size: 22px;   
                 """)

a57 = QPushButton("57",oyna)
a57.setGeometry(120,650,60,60)
a57.setStyleSheet("""
  background-color: pink;  
  color: green;
  font-size: 22px;   
                 """)

a58 = QPushButton("58",oyna)
a58.setGeometry(190,650,60,60)
a58.setStyleSheet("""
  background-color: pink;  
  color: green;
  font-size: 22px;   
                 """)

a59 = QPushButton("59",oyna)
a59.setGeometry(260,650,60,60)
a59.setStyleSheet("""
  background-color: pink;  
  color: green;
  font-size: 22px;   
                 """)

a60 = QPushButton("60",oyna)
a60.setGeometry(330,650,60,60)
a60.setStyleSheet("""
  background-color: pink;  
  color: green;
  font-size: 22px;   
                 """)

a61 = QPushButton("61",oyna)
a61.setGeometry(400,650,60,60)
a61.setStyleSheet("""
  background-color: pink;  
  color: green;
  font-size: 22px;   
                 """)

a62 = QPushButton("62",oyna)
a62.setGeometry(470,650,60,60)
a62.setStyleSheet("""
  background-color: pink;  
  color: green;
  font-size: 22px;   
                 """)

a63 = QPushButton("63",oyna)
a63.setGeometry(540,650,60,60)
a63.setStyleSheet("""
  background-color: pink;  
  color: green;
  font-size: 22px;   
                 """)
a64 = QPushButton("64",oyna)
a64.setGeometry(610,650,60,60)
a64.setStyleSheet("""
  background-color: pink;  
  color: green;
  font-size: 22px;   
                 """)
a65 = QPushButton("65",oyna)
a65.setGeometry(680,650,60,60)
a65.setStyleSheet("""
  background-color: pink;  
  color: green;
  font-size: 22px;   
                 """)

a66 = QPushButton("66",oyna)
a66.setGeometry(750,650,60,60)
a66.setStyleSheet("""
  background-color: pink;  
  color: green;
  font-size: 22px;   
                 """)


a67 = QPushButton("67",oyna)
a67.setGeometry(50,720,60,60)
a67.setStyleSheet("""
  background-color: pink;  
  color: green;
  font-size: 22px;   
                 """)

a68 = QPushButton("68",oyna)
a68.setGeometry(120,720,60,60)
a68.setStyleSheet("""
  background-color: pink;  
  color: green;
  font-size: 22px;   
                 """)

a69 = QPushButton("69",oyna)
a69.setGeometry(190,720,60,60)
a69.setStyleSheet("""
  background-color: pink;  
  color: green;
  font-size: 22px;   
                 """)

a70 = QPushButton("70",oyna)
a70.setGeometry(260,720,60,60)
a70.setStyleSheet("""
  background-color: pink;  
  color: green;
  font-size: 22px;   
                 """)

a71 = QPushButton("71",oyna)
a71.setGeometry(330,720,60,60)
a71.setStyleSheet("""
  background-color: pink;  
  color: green;
  font-size: 22px;   
                 """)

a72 = QPushButton("72",oyna)
a72.setGeometry(400,720,60,60)
a72.setStyleSheet("""
  background-color: pink;  
  color: green;
  font-size: 22px;   
                 """)

a73 = QPushButton("73",oyna)
a73.setGeometry(470,720,60,60)
a73.setStyleSheet("""
  background-color: pink;  
  color: green;
  font-size: 22px;   
                 """)

a74 = QPushButton("74",oyna)
a74.setGeometry(540,720,60,60)
a74.setStyleSheet("""
  background-color: pink;  
  color: green;
  font-size: 22px;   
                 """)

a75 = QPushButton("75",oyna)
a75.setGeometry(610,720,60,60)
a75.setStyleSheet("""
  background-color: pink;  
  color: green;
  font-size: 22px;   
                 """)
a76 = QPushButton("76",oyna)
a76.setGeometry(680,720,60,60)
a76.setStyleSheet("""
  background-color: pink;  
  color: green;
  font-size: 22px;   
                 """)
a77 = QPushButton("77",oyna)
a77.setGeometry(750,720,60,60)
a77.setStyleSheet("""
  background-color: pink;  
  color: green;
  font-size: 22px;   
                 """)

a78 = QPushButton("78",oyna)
a78.setGeometry(50,790,60,60)
a78.setStyleSheet("""
  background-color: pink;  
  color: green;
  font-size: 22px;   
                 """)

a79 = QPushButton("79",oyna)
a79.setGeometry(120,790,60,60)
a79.setStyleSheet("""
  background-color: pink;  
  color: green;
  font-size: 22px;   
                 """)

a80 = QPushButton("80",oyna)
a80.setGeometry(190,790,60,60)
a80.setStyleSheet("""
  background-color: pink;  
  color: green;
  font-size: 22px;   
                 """)

a81 = QPushButton("81",oyna)
a81.setGeometry(260,790,60,60)
a81.setStyleSheet("""
  background-color: pink;  
  color: green;
  font-size: 22px;   
                 """)

a82 = QPushButton("82",oyna)
a82.setGeometry(330,790,60,60)
a82.setStyleSheet("""
  background-color: pink;  
  color: green;
  font-size: 22px;   
                 """)

a83 = QPushButton("83",oyna)
a83.setGeometry(400,790,60,60)
a83.setStyleSheet("""
  background-color: pink;  
  color: green;
  font-size: 22px;   
                 """)

a84 = QPushButton("84",oyna)
a84.setGeometry(470,790,60,60)
a84.setStyleSheet("""
  background-color: pink;  
  color: green;
  font-size: 22px;   
                 """)

a85 = QPushButton("85",oyna)
a85.setGeometry(540,790,60,60)
a85.setStyleSheet("""
  background-color: pink;  
  color: green;
  font-size: 22px;   
                 """)
a86 = QPushButton("86",oyna)
a86.setGeometry(610,790,60,60)
a86.setStyleSheet("""
  background-color: pink;  
  color: green;
  font-size: 22px;   
                 """)
a87 = QPushButton("87",oyna)
a87.setGeometry(680,790,60,60)
a87.setStyleSheet("""
  background-color: pink;  
  color: green;
  font-size: 22px;   
                 """)

a88 = QPushButton("88",oyna)
a88.setGeometry(750,790,60,60)
a88.setStyleSheet("""
  background-color: pink;  
  color: green;
  font-size: 22px;   
                 """)

a89 = QPushButton("89",oyna)
a89.setGeometry(50,860,60,60)
a89.setStyleSheet("""
  background-color: pink;  
  color: green;
  font-size: 22px;   
                 """)

a90 = QPushButton("90",oyna)
a90.setGeometry(120,860,60,60)
a90.setStyleSheet("""
  background-color: pink;  
  color: green;
  font-size: 22px;   
                 """)

a91 = QPushButton("91",oyna)
a91.setGeometry(190,860,60,60)
a91.setStyleSheet("""
  background-color: pink;  
  color: green;
  font-size: 22px;   
                 """)

a92 = QPushButton("92",oyna)
a92.setGeometry(260,860,60,60)
a92.setStyleSheet("""
  background-color: pink;  
  color: green;
  font-size: 22px;   
                 """)

a93 = QPushButton("93",oyna)
a93.setGeometry(330,860,60,60)
a93.setStyleSheet("""
  background-color: pink;  
  color: green;
  font-size: 22px;   
                 """)

a94 = QPushButton("94",oyna)
a94.setGeometry(400,860,60,60)
a94.setStyleSheet("""
  background-color: pink;  
  color: green;
  font-size: 22px;   
                 """)

a94 = QPushButton("94",oyna)
a94.setGeometry(470,860,60,60)
a94.setStyleSheet("""
  background-color: pink;  
  color: green;
  font-size: 22px;   
                 """)
a95 = QPushButton("94",oyna)
a95.setGeometry(470,860,60,60)
a95.setStyleSheet("""
  background-color: pink;  
  color: green;
  font-size: 22px;   
                 """)

a96 = QPushButton("96",oyna)
a96.setGeometry(540,860,60,60)
a96.setStyleSheet("""
  background-color: pink;  
  color: green;
  font-size: 22px;   
                 """)
a97 = QPushButton("97",oyna)
a97.setGeometry(610,860,60,60)
a97.setStyleSheet("""
  background-color: pink;  
  color: green;
  font-size: 22px;   
                 """)
a98 = QPushButton("98",oyna)
a98.setGeometry(680,860,60,60)
a98.setStyleSheet("""
  background-color: pink;  
  color: green;
  font-size: 22px;   
                 """)

a99 = QPushButton("99",oyna)
a99.setGeometry(750,860,60,60)
a99.setStyleSheet("""
  background-color: pink;  
  color: green;
  font-size: 22px;   
                 """)

def birbosildi():
    sozLabel.setText(' ')

bir.clicked.connect(birbosildi)
a1.clicked.connect(lambda:bosildi(a1))
a2.clicked.connect(lambda:bosildi(a2))
a3.clicked.connect(lambda:bosildi(a3))
a4.clicked.connect(lambda:bosildi(a4))
a5.clicked.connect(lambda:bosildi(a5))
a6.clicked.connect(lambda:bosildi(a6))
a7.clicked.connect(lambda:bosildi(a7))
a8.clicked.connect(lambda:bosildi(a8))
a9.clicked.connect(lambda:bosildi(a9))
a10.clicked.connect(lambda:bosildi(a10))
a11.clicked.connect(lambda:bosildi(a11))
a12.clicked.connect(lambda:bosildi(a12))
a13.clicked.connect(lambda:bosildi(a13))
a14.clicked.connect(lambda:bosildi(a14))
a15.clicked.connect(lambda:bosildi(a15))
a16.clicked.connect(lambda:bosildi(a16))
a17.clicked.connect(lambda:bosildi(a17))
a18.clicked.connect(lambda:bosildi(a18))
a19.clicked.connect(lambda:bosildi(a19))
a20.clicked.connect(lambda:bosildi(a20))
a21.clicked.connect(lambda:bosildi(a21))
a22.clicked.connect(lambda:bosildi(a22))
a23.clicked.connect(lambda:bosildi(a23))
a24.clicked.connect(lambda:bosildi(a24))
a25.clicked.connect(lambda:bosildi(a25))
a26.clicked.connect(lambda:bosildi(a26))
a27.clicked.connect(lambda:bosildi(a27))
a28.clicked.connect(lambda:bosildi(a28))
a29.clicked.connect(lambda:bosildi(a29))
a30.clicked.connect(lambda:bosildi(a30))
a31.clicked.connect(lambda:bosildi(a31))
a32.clicked.connect(lambda:bosildi(a32))
a33.clicked.connect(lambda:bosildi(a33))
a34.clicked.connect(lambda:bosildi(a34))
a35.clicked.connect(lambda:bosildi(a35))
a36.clicked.connect(lambda:bosildi(a36))
a37.clicked.connect(lambda:bosildi(a37))
a38.clicked.connect(lambda:bosildi(a38))
a99.clicked.connect(lambda:bosildi(a39))
a40.clicked.connect(lambda:bosildi(a40))
a41.clicked.connect(lambda:bosildi(a41))
a42.clicked.connect(lambda:bosildi(a42))
a43.clicked.connect(lambda:bosildi(a43))
a44.clicked.connect(lambda:bosildi(a44))
a45.clicked.connect(lambda:bosildi(a45))
a46.clicked.connect(lambda:bosildi(a46))
a47.clicked.connect(lambda:bosildi(a47))
a48.clicked.connect(lambda:bosildi(a48))
a49.clicked.connect(lambda:bosildi(a49))
a50.clicked.connect(lambda:bosildi(a50))
a51.clicked.connect(lambda:bosildi(a51))
a52.clicked.connect(lambda:bosildi(a52))
a53.clicked.connect(lambda:bosildi(a53))
a54.clicked.connect(lambda:bosildi(a54))
a55.clicked.connect(lambda:bosildi(a55))
a56.clicked.connect(lambda:bosildi(a56))
a57.clicked.connect(lambda:bosildi(a57))
a58.clicked.connect(lambda:bosildi(a58))
a59.clicked.connect(lambda:bosildi(a59))
a60.clicked.connect(lambda:bosildi(a60))
a61.clicked.connect(lambda:bosildi(a61))
a62.clicked.connect(lambda:bosildi(a62))
a63.clicked.connect(lambda:bosildi(a63))
a64.clicked.connect(lambda:bosildi(a64))
a65.clicked.connect(lambda:bosildi(a65))
a66.clicked.connect(lambda:bosildi(a66))
a67.clicked.connect(lambda:bosildi(a67))
a68.clicked.connect(lambda:bosildi(a68))
a69.clicked.connect(lambda:bosildi(a69))
a70.clicked.connect(lambda:bosildi(a70))
a71.clicked.connect(lambda:bosildi(a71))
a72.clicked.connect(lambda:bosildi(a72))
a73.clicked.connect(lambda:bosildi(a73))
a74.clicked.connect(lambda:bosildi(a74))
a75.clicked.connect(lambda:bosildi(a75))
a76.clicked.connect(lambda:bosildi(a76))
a77.clicked.connect(lambda:bosildi(a77))
a78.clicked.connect(lambda:bosildi(a78))
a79.clicked.connect(lambda:bosildi(a79))
a80.clicked.connect(lambda:bosildi(a80))
a81.clicked.connect(lambda:bosildi(a81))
a82.clicked.connect(lambda:bosildi(a82))
a83.clicked.connect(lambda:bosildi(a83))
a84.clicked.connect(lambda:bosildi(a84))
a85.clicked.connect(lambda:bosildi(a85))
a86.clicked.connect(lambda:bosildi(a86))
a87.clicked.connect(lambda:bosildi(a87))
a88.clicked.connect(lambda:bosildi(a88))
a89.clicked.connect(lambda:bosildi(a89))
a90.clicked.connect(lambda:bosildi(a90))
a91.clicked.connect(lambda:bosildi(a91))
a92.clicked.connect(lambda:bosildi(a92))
a93.clicked.connect(lambda:bosildi(a93))
a94.clicked.connect(lambda:bosildi(a94))
a95.clicked.connect(lambda:bosildi(a95))
a96.clicked.connect(lambda:bosildi(a96))
a97.clicked.connect(lambda:bosildi(a97))
a98.clicked.connect(lambda:bosildi(a98))
a99.clicked.connect(lambda:bosildi(a99))










oyna.show()
app.exec_()