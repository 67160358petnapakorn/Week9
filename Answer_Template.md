# รายงานแลป OLTP OLAP และ Pivot

ชื่อ:เพชรนภากร พลนิกร รหัส:67160358 กลุ่ม:1

## 1 OLTP
โค้ด/ผลรันสองรอบ/คำอธิบายสถานะและ ETL
ใช้การแก้ไขข้อมูลแบบมีเงื่อนไข เพื่อป้องกันการแก้ไขซ้ำ โดยเปลี่ยนสถานะของ O1004 จาก PENDING เป็น PAID

ผลรันครั้งที่ 1:

Before: [('O1004', 'PENDING')]
After: [('O1004', 'PAID')]

ผลรันครั้งที่ 2:

Before: [('O1004', 'PAID')]
After: [('O1004', 'PAID')]

การรันครั้งที่ 2 ไม่มีการเปลี่ยนแปลง เพราะเงื่อนไขกำหนดให้สถานะเดิมต้องเป็น PENDING

## 2 Grain และ Star Schema
แผนภาพ/PK/FK/Dimensions/Measures/Hierarchy/ผล q01
1 แถวใน sales แทนรายการขายสินค้า 1 รายการภายใน Order

Dimension ที่ใช้

Date
Product
Store/Province

Measures

quantity
unit_price
amount

Hierarchy

Date → Year → Month → Day
Product → Category
Location → Region → Province

## 3 OLAP
ผล q02–q07 และ q12 พร้อมคำอธิบาย Operation และ WHERE/HAVING
q02 — ยอดขายรายเดือน
2026-08    490
2026-09    900

เดือนกันยายนมียอดขายสูงกว่าเดือนสิงหาคม

q03 — ยอดขายตามเดือนและจังหวัด
2026-08  Bangkok    310
2026-08  Chonburi   180
2026-09  Bangkok    540
2026-09  Chonburi   360

q04 — ยอดขายรายวัน
2026-08-08    180
2026-08-09    150
2026-08-10    160
2026-09-09    360
2026-09-10    300
2026-09-11    240 

q05 — ยอดขายเดือนกันยายนตามจังหวัด
Bangkok     540
Chonburi    360

q06 — ยอดขาย Drink เดือนกันยายน
Bangkok     300
Chonburi    200

q07 — จังหวัดที่มียอดขายมากกว่า 500
Bangkok     850
Chonburi    540

q08 — สรุปตามสินค้า
Tea       Quantity = 15    Revenue = 750
Cookie    Quantity = 8     Revenue = 640
## 4 Pivot
ผล q08/P1/P2/Drink และก่อนหลังแก้ mean พร้อมผล assert
P1 — Province × Month
             2026-08   2026-09    All
Bangkok         310       540      850
Chonburi        180       360      540
All             490       900     1390
P2 — September Category × Province
          Bangkok   Chonburi
Drink        300       200
Snack        240       160
P3 — ตรวจ Grand Total
Pivot Grand Total: 1390
DataFrame Total: 1390
PASS

แสดงว่า Pivot มี Grand Total ตรงกับยอดรวมของข้อมูล

P4 — Export

สร้างไฟล์ CSV สำเร็จแล้ว:

pivot_p1_province_month.csv
pivot_p2_september_category_province.csv
## 5 ตรวจความถูกต้อง
ผล q09–q11 ชนิด Measure และคำอธิบาย AOV กับ JOIN
q09
Total Revenue       = 1390
Mean Line Amount    = 173.75
Line Count          = 8

SUM(amount) เป็น Measure ที่สามารถรวมค่าได้ ส่วน AVG(amount) เป็นค่าเฉลี่ย ไม่ควรนำค่าเฉลี่ยของแต่ละกลุ่มมาบวกกัน

q10
Order Count     = 6
Total Revenue   = 1390
AOV             = 231

AOV คือยอดขายเฉลี่ยต่อ Order

1390 ÷ 6 ≈ 231.67

แต่ SQLite แสดง 231 เนื่องจากการหารจำนวนเต็ม

q11
Line Count      = 8
Order Count     = 6
Total Revenue   = 1390

จำนวนรายการขายมี 8 รายการ แต่เป็น Order ที่ไม่ซ้ำกัน 6 Order
## 6 สรุป
ข้อค้นพบ 2 ข้อ ข้อจำกัด 1 ข้อ และการใช้ AI (ถ้ามี)
ข้อค้นพบ

เดือนกันยายนมียอดขายสูงกว่าเดือนสิงหาคม โดยมียอดขาย 900 จากทั้งหมด 1,390
Bangkok มียอดขายสูงที่สุด 850 และสูงกว่า Chonburi ที่มียอดขาย 540

ข้อจำกัด
ข้อมูลมีจำนวนรายการไม่มาก จึงอาจยังไม่เพียงพอสำหรับการวิเคราะห์แนวโน้มในระยะยาว

การใช้ AI
ใช้ AI ช่วยอธิบายแนวคิด SQL, OLTP, OLAP และ Pivot รวมถึงช่วยตรวจสอบผลลัพธ์ของคำสั่งที่เขียนขึ้น