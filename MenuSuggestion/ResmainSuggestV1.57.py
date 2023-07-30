import random
manu = {'rice':{
'boil':{'pig':["ข้าวหมูแดง","ข้าวขาหมู","ข้าวต้มหมู","ข้าวพะแนงหมู"],"chicken":["ข้าวมันไก่","ข้าวน่องไก่ตุ๋น","ข้าวมัสมั่นไก่","ข้าวพะแนงไก่"],'duck':["ข้าวหน้าเป็ด","โจ๊กเป็ดเห็ดหอม"]},
'puff':{'pig':["ข้าวผัดหมู","ข้าวกะเพราหมู","ข้าวกะเพราหมูสับ","ข้าวกะเพราหมูป่า","ข้าวกะเพราหมูยอ","ข้าวกะเพราหมูกรอบ","ข้าวผัดพริกแกงหมู","ข้าวผัดคะน้าหมูกรอบ","ข้าวผัดผงกะหรี่หมู"],'chicken':["ข้าวผัดไก่","ข้าวกะเพราไก่","ข้าวกะเพราเครื่องในไก่","ข้าวสเต๊กไก่ผัด","ข้าวผัดพริกแกงไก่","ข้าวผัดไก่ขิง","ข้าวผัดผงกะหรี่ไก่"],
'sea':["ข้าวผัดทะเล","ข้าวผัดกุ้ง","ข้าวผัดปู","ข้าวกะเพราทะเล","ข้าวกะเพรากุ้ง","ข้าวกะเพราปลาหมึก","ข้าวพริกแกงทะเล"]},
'fry':{'chicken':["ข้าวมันไก่ทอด","ข้าวไก่ทอดกระเทียม","ข้าวไก่ทอด","ข้าวเขียวหวานไก่ทอด","ข้าวไก่กรอบ","ข้าวไก่ทอดน้ำปลา"]},
'deep':{'chicken':["ข้าวหมกไก่","ข้าวหมกน่องไก่"]},
'grill':{'pig':["ข้าวคอหมูย่าง","ข้าวยำคอหมูย่าง"],'chicken':["ข้าวยำไก่ย่าง","ข้าวไก่ย่าง"]},
'steam':{'chicken':["ข้าวไก่นึ่ง"]}}
,
'noodle':{
'boil':{'pig':["สุกี้หมู","ก๋วยเตี๋ยวหมู","ก๋วยเตี๋ยวน้ำตกหมู","บะหมี่เกี๊ยวหมูแดง","บะหมี่ขาหมู","เย็นตาโฟหมู","ราดหน้าหมู"],
'chicken':["ราดหน้าไก่","สุกี้ไก่"],'sea':["ราดหน้าทะเล","เย็นตาโฟทะเล","สุกี้ทะเล"],'duck':["บะหมี่เป็ด"]},
'puff':{'pig':["ผัดไทยหมู","ผัดซีอิ๊วหมู","ผัดซีอิ๊วเบค่อน","สปาเก็ตตี้ขี้เมาหมู"],'chicken':["ผัดไทยไก่","ผัดซีอิ๊วไก่"],'sea':["ผัดไทยปลาหมึก","ผัดไทยกุ้ง","ผัดซีอิ๊วทะเล","สปาเก็ตตี้ขี้เมาทะเล"]}
}}

def typesuggest(decis):
    while True:
        print("กรุณาเลือกประเภทอาหารที่คุณต้องการ")
        print("ข้าว (Rice)\nเส้น (Noodle)")
        matterial = input(":") ##รับค่าmatterial จากผู้ใช้
        matterial = matterial.lower() ##เปลี่ยนmatterial เป็นตัวเล็ก 
        if matterial != "rice" and matterial != "noodle": ##ตรวจเช็คmatterial ไม่เท่ากับ rice,noodle 
            print("กรุณากรอกข้อมูลใหม่")
            typesuggest(decis) ##เรียกใช้ฟังก์ชั่น การเลือกเมนูโดยใช้ประเภทอาหาร
            break
        if matterial == "rice" or matterial == "noodle": ##ตรวจเช็ค matterial เท่ากับ rice,noodle
            print("เลือกวิธีปรุงอาหาร") ## บอกผู้ใช้ว่าสามารถเลือกวิธีการปรุงอาหารได้
            if matterial =="rice": ## ถ้าmatterial เป็น rice
                for i in manu['rice'].keys(): ##ให้ i loop ใน manu['rice'].keys()
                    print("-",i) ##แสดงค่า i ที่วิ่งใน manu['rice'].keys()
                print("อาหารประเภท",matterial)
            elif matterial =="noodle":
                for i in manu['noodle'].keys():
                    print("-",i)
                print("อาหารประเภท",matterial)
        process = input(":") ##รับค่าprocess จากผู้ใช้
        process = process.lower() ##เปลี่ยนprocess เป็นตัวเล็ก 
        if process not in manu['rice'].keys() and process not in manu['noodle'].keys(): ##ตรวจเช็ค process ไม่อยู่ในmanu['rice'].keys() และ manu['noodle'].keys()
            print("กรุณากรอกข้อมูลให้ถูกต้อง")
            print("ต้องการกลับไปเริ่มใหม่(R)")
            print("ต้องการแสดงผลข้อมูลทันที(N)")
            way = input(":")
            way = way.upper()
            if way == "R": ##ถ้า wayที่ผู้ใช้ป้อนเข้ามา คือ R จะเรียกใช้ฟังก์ชั่น การเลือกเมนูโดยใช้ประเภทอาหาร
                typesuggest(decis)
                break
            elif way == "N": ##ถ้า way คือ N
                suggest = []
                for i in manu[matterial]: ##ให้ i loop ใน manu[matterial]
                    for n in manu[matterial][i]: ##ให้ n loop ใน manu[matterial][i]
                        for p in manu[matterial][i][n]: ##ให้ p loop ใน manu[matterial][i][n]
                            suggest.append(p) ##ทุกค่า p จะถูกเก็บไว้ใน suggest
                print("อาหารที่เราแนะนำคุณคือ:"," ,".join(suggest))
                break
            else:
                break
        elif process in manu['rice'].keys() or process in manu['noodle'].keys(): ##ตรวจเช็ค process ว่าอยู่ใน manu['rice'].keys()  หรือ อยู่ใน manu['noodle'].keys() รึเปล่า
            print("เลือกเนื้อสัตว์") ##บอกผู้ใช้ว่าสามารถเลือกเนื้อสัตว์ได้
            if matterial == "rice" or process in manu['rice'].keys(): ##ตรวจเช็คmatterial คือ rice หรือ process อยู่ใน manu['rice].keys() 
                for i in manu[matterial][process].keys(): ##ให้ i loop ใน manu[matterial][process].keys()
                    print("-",i) ##แสดงค่า ทุก i ที่วิ่งใน manu[matterial][process].keys()
            print("อาหารประเภท",matterial)
            print("วิธีในการทำอาหาร",process)
            meat = input(":") ##รับค่า meat จากผู้ใช้
            meat = meat.lower()
        if meat not in manu[matterial][process].keys(): ##ตรวจเช็คค่า meat ไม่อยู่ใน manu[matterial][process].keys()
            print("กรุณากรอกข้อมูลให้ถูกต้อง")
            print("ต้องการกลับไปเริ่มใหม่(R)")
            print("ต้องการแสดงผลข้อมูลทันที(N)")
            way = input(":")
            way = way.upper()
            if way == "R": ##ถ้าค่า way คือ R เรียกใช้ฟังก์ชั่น เลือกเมนูโดยใช้ประเภทอาหาร
                typesuggest(decis)
                break
            elif way == "N": 
                suggest = []
                for i in manu[matterial][process].values(): ##ให้ i loop ในmanu[matterial][process].values()
                    for n in i:
                        suggest.append(n) ##เก็บทุกค่า n ที่วิ่งใน i ไว้ใน suggest
                print("อาหารที่เราแนะนำคุณคือ:"," ,".join(suggest))
                break
            else:
                break
        if matterial in manu.keys() and process in manu[matterial].keys() and meat in manu[matterial][process]:
            ##ถ้า matterial อยู่ใน manu.keys() และ process อยู่ใน manu[matterial].keys()และ meat อยู่ใน manu[matterial][process]
            print("=================")
            print("อาหารประเภท",matterial)
            print("วิธีในการทำอาหาร",process)
            print("เนื้อสัตว์",meat)
            print("=================")
            print("อาหารที่เราแนะนำคุณคือ:"," ,".join(manu[matterial][process][meat])) ##แสดงผลรายการอาหารตามตัวเลือกที่ผู้ใช้งานเลือก
            break
        

def randomsuggest(decis):
    while True:
        ranmatterial = list() ##สร้างลิสเปล่าเพื่อรอรับค่า
        ranprocess = list()
        ranmeat = list()
        for i in manu.keys(): ##ให้ i loop ใน manu.keys()
            ranmatterial.append(i) ##ให้ทุกค่า i เก็บไว้ใน ranmatterial
            afterranmat = random.choice(ranmatterial) ##นำ ranmatterial ที่เก็บค่า i แล้ว มาสุ่มแล้วเก็บไว้ใน afterranmat
        for i in manu[afterranmat].keys(): ##ให้ i loop ใน manu[afterranmat].keys()
            ranprocess.append(i) ##ทุกค่า i ที่วิ่งในmanu[afterranmat].keys() เก็บไว้ใน ranprocess
            afterranprocess = random.choice(ranprocess) ##นำ ranprocess ที่เก็บค่า i แล้ว มาสุ่มแล้วเก็บไว้ใน afterranprocess
        for i in manu[afterranmat][afterranprocess].keys(): ##ให้ i loop ใน manu[afterranmat][afterranprocess].keys()
            ranmeat.append(i) ##ทุกค่า i ที่วิ่งในmanu[afterranmat][afterranprocess].keys() เก็บไว้ใน ranmeat
            afterranmeat = random.choice(ranmeat) ##นำ ranmeat ที่เก็บค่า i แล้ว มาสุ่มแล้วเก็บไว้ใน afterranmeat
        final = random.choice(manu[afterranmat][afterranprocess][afterranmeat]) ##สุ่มเมนูจาก manu[afterranmat][afterranprocess][afterranmeat]แล้วเก็บไว้ใน final
        print(final) ##แสดงเมนูอาหารที่ถูกสุ่ม
        print("=================")
        print("กด N เพื่อทำการสุ่มต่อ")
        ranway = input(":")
        ranway = ranway.upper()
        if ranway == "N":
            pass
        else:
            break
        
def addmanu(addjustmanu):
    while True:
        print('Welcome to "What’s for lunch?" ')
        print("เลือกประเภทอาหารที่คุณต้องการเพิ่มเมนูอาหาร")
        print("ข้าว (Rice) \nเส้น (Noodle)")
        addmatterial = input(":") ##รับค่า addmatterial จากผู้ใช้
        addmatterial = addmatterial.lower() ##แปลง matterial เป็นตัวพิมพ์เล็ก
        if addmatterial in manu.keys(): ##เช็ค addmatterial อยู่ใน manu.keys()
            print("Select your Process") 
        if addmatterial in manu.keys():
            for i in manu[addmatterial].keys(): ##ให้ i loop ใน manu[addmatterial].keys()
                print("-",i) ##แสดงผลทุกค่า i ที่วิ่งใน manu[addmatterial].keys()
            print("อาหารประเภท",addmatterial)
        elif addmatterial not in manu.keys(): ##ถ้าaddmatterial ไม่อยู่ในmanu.keys()
            print("กรุณากรอกข้อมูลให้ถูกต้อง")
            addmanu(adjustmanu) ##เรียกใช้ฟังก์ชั่นเพิ่มเมนู
            break
        addprocess = input(":") ##รับค่า addprocess จากผู้ใช้
        addprocess = addprocess.lower() ##แปลง addprocess เป็นตัวพิมพ์เล็ก
        if addprocess in manu[addmatterial].keys(): ## เช็ค addprocess อยู่ใน manu[addmatterial].keys()
            print("กรุณาเลือกเนื้อ (select Meat)") 
            if addmatterial == 'rice': 
                for i in manu['rice'][addprocess].keys(): ##ให้ i loop ใน manu['rice'][addprocess].keys()
                    print("-",i) ##แสดงทุกค่า i ที่วิ่งใน manu['rice'][addprocess].keys()
            elif addmatterial == 'noodle':
                for i in manu['noodle'][addprocess].keys():
                    print("-",i)
            print("อาหารประเภท",addmatterial)
            print("วิธีในการทำเมนูอาหาร",addprocess)
            addmeat= input(":") ##รับค่า addmeat จากผู้ใช้
            addmeat = addmeat.lower() ##แปลง addmeat เป็นตัวพิมพ์เล็ก
        elif addprocess not in manu[addmatterial].keys(): ##เช็ค addprocess ไม่อยู่ใน manu[addmatterial].keys()
            print("กรุณาใส่ข้อมูลให้ถูกต้อง")
            addmanu(adjustmanu) ##เรียกใช้ฟังก์ชั่นเพิ่มเมนู
            break
        if addmeat not in manu[addmatterial][addprocess].keys(): ##เช็ค addmeat ไม่อยู่ใน manu[addmatterial][addprocess].keys()
            print("กรุณาใส่ขอมูลให้ถูกต้อง")
            addmanu(adjustmanu) ##เรียกใช้ฟังก์ชั่นเพิ่มเมนู
            break
        elif addmeat in manu[addmatterial][addprocess].keys(): ##เช็ค addmeat อยู่ใน manu[addmatterial][addprocess].keys() หรือไม่
            print("กรุณาเพิ่มเมนูอาหาร")
            newmanu = input(":") ##รับค่าเมนู newmanu จากผู้ใช้
            manu[addmatterial][addprocess][addmeat].append(newmanu) ##นำ newmanu เพิ่มลงในdictionary ตามประเภทที่ผู้ใช้งานเลือก
            break

while True:
    autho_inside = True
    allmanu = []
    print('Welcome to "What’s for lunch?"')
    print("กรุณาเลือกสถานะผู้ใช้งาน")
    print("1.เจ้าของร้าน (A)")
    print("2.ลูกค้าทั่วไป (C)")
    print("3.จบการทำงาน (L)")
    custo_addmin = input(":") ##รับค่า custo_addmin จากผู้ใช้
    custo_addmin = custo_addmin.upper() ##แปลง custo_addmin เป็นพิมพ์ใหญ่
    if custo_addmin == "3" or custo_addmin == "L": ##ตรวจสอบcusto_addmin เป็น3 หรือ เป็น L
        autho_inside = False ##เปลี่ยน cuto_addmin เป็น False
        break
    elif autho_inside == True:
        while True:
            if custo_addmin == "2" or custo_addmin == "C" or custo_addmin == "CUSTOMER": ##ตรวจสอบ custo_addmin เป็น 2 หรือ C หรือ CUSTOMER
                print('Welcome to "What’s for lunch?"')
                print("กรุณาเลือกตัวเลือก")
                print("1.เลือกประเภทอาหาร (T)")
                print("2.แสดงรายการเมนูอาหารทั้งหมด (E)")
                print("3.สุ่มเมนูอาหาร (R)")
                print("4.กลับสู่หน้าหลัก (L)")
                decis = input(":")
                decis = decis.upper()
                if decis =="T" or decis == "1": ##ตรวจเช็ค decis เป็น T หรือ 1 หรือไม่
                    typesuggest(decis) ##เรียกใช้ฟังก์ชั่น โดยใช้ประเภทอาหาร
                    break
                elif decis =="E" or decis == "2": ##ตรวจเช็ค decis เป็น E หรือ 2 หรือไม่
                    for i in manu.keys(): ##ให้ i loop ใน manu.keys()
                        for n in manu[i].keys(): ##ให้ n loop ใน manu[i].keys()
                            for p in manu[i][n]: ##ให้ p loop ใน manu[i][n]
                                for h in manu[i][n][p]: ##ให้ h loop ใน manu[i][n][p]
                                    allmanu.append(h) ##นำทุก h เพิ่มลงใน allmanu
                    print("รายการเมนูอาหารทั้งหมด",allmanu) ##แสดงผลรายการอาหารทั้งหมด
                    break
                elif decis == "R" or decis == "3": ##ตรวจเช็ค decis เป็น R หรือ 3 หรือไม่
                    randomsuggest(decis)
                elif decis == "4" or decis == "L": ##ตรวจเช็ค decis เป็น L หรือ 4 หรือไม่
                    break
                else:
                    print("กรุณากรอกข้อมูลใหม่")
            elif custo_addmin == "1" or custo_addmin == "A" or custo_addmin == "ADDMIN": ##ตรวจเช็ค custo_addmin เป็น 1 หรือ A หรือ ADDMIN หรือไม่
                adjustmanu = custo_addmin 
                addmanu(adjustmanu) ##เรียกใช้ฟังก์ชั่นเพิ่มเมนูอาหาร
                break
            else:
                print("กรุณากรอกข้อมูลให้ถูกต้อง")
                break
