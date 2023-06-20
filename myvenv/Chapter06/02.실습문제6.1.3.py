# 실습문제 6.1.3
# 로또 번호 추출기

import random

def getRandomNumber():
    number = random.randint(1, 45)

    return number

lotto = []
for i in range(6):
    num = getRandomNumber()
    if num not in lotto:
        lotto.append(num)

print(sorted(lotto))

### 다른 방법
lotto_num = []
count = 0

while True:
    if count == 6:
        break

    random_number = getRandomNumber()
    if random_number not in lotto_num:
        lotto_num.append(random_number)
        count += 1

