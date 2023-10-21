# AUTOMATIC RECYCLING SEPARATION
## : 딥러닝 모델을 이용해 유리&플라스틱&캔 구별하기
(4조_왓더분리_deeplearning_project)
---

## Content
01. Situation
02. Solution
03. How
04. Roadmap
05. Step By Step
06. Let's see
07. Estimation

---

## 01. Situation

### The Way of the Garbage
- Information 01
: 우리가 버린 쓰레기는 크게 소각장 , 매립지 , 재활용 선별장으로 가게 된다 .
- Information 02
: 소각되는 비율은 29.92%(13,730 톤 ), 매립은 14.78%(6,782 톤 ) 그리고 재활용은 54.66% (25,086 톤 ) 를 차지한다 .
- Information 03
: 서울시 기준 1 인당 하루 플라스틱 배출량은 2016년과 대비해 2020 년에 2 배 넘게 증가하는 등 쓰레기 배출량은 해마다 증가하고있다 .
- Information 04
: 코로나 이전에 공공 재활용 선별장의 시설 용량이 충분했더라도 현재는 폐기물이 너무 많아져서 대부 분의 지자체가 감당하기 어려운 상황

### 재활용품 선별장의 실태
- After Covid19 #1
  : 코로나19의 시대가 지나고 배달음식과 쓰레기 배출량은 늘었지만, 재활용품이 분리되는 비율은 줄었습니다.
- Global boiling #2
  : 그만큼 지구와 동물,식물 그리고 사람들에게 쓰레기로 인한 피해는 늘고있습니다. 결국에 이 플라스틱들은 지구온난화의 원인이 되고 있습니다.
- Reducing people #3
  : 인구가 줄어들고 있습니다. 이는 인공지능이 필수불가결하게 사용되는 시대가 될 것을 의미합니다.
  ‘나머지 선별인원 11명 모두가 외국인 노동자였다.’ _기사일부 발췌

### 재활용품에 대해
- 01 무엇을 분류하나요?
  - 플라스틱류 - PET, PE, PP
  - 고철류 - 철캔, 고철, 알루미늄캔
  - 병류 - 공병(소주,맥주병), 백색병, 갈색병, 녹색병
  - 종이류 - 파지, 우유팩
  - 기타 - 비닐류
- 02 어떤 순서로 하나요?
  - 저장된 폐기물을 컨베이어 벨트로 이송 후, 컨베이어 벨트 위의 폐기물을 직접 골라냄.
  - 대형 잔재물 제거 > 재활용품 크기별 선별 > 1차 선별 > 품목별로 크게 선별 > 자력선별기 > 비철금속 선별기 > 2차 수선별실 > 광학 선별기 > 압축 및 잔재물 처리
- 03 왜 실용화되지 않죠?
  - 우리나라에 맞는 모델이 없어 직접 만들어야하기에 더딘것으로 보이며, 전반적으로 점점 상용화되는 추세이다.
    
---

## 02. Solution
- our system: 딥러닝 모델을 이용해 유리&플라스틱&캔 구별하기
- 저희 시스템은 일반적으로 재활용센터의 과정(시나리오)을 기반으로 아래와 같은 차이점을 갖고 있습니다.

- 01. '구간마다 멈추는 벨트'를 갖고 있습니다.
- 02. 크게 'Can&Plastic&Glass'을 가지고 테스트합니다.
- 03. 보통 '집는 방식'을 사용하나, 이번에는 '미는 방식'을 사용하였습니다.

---

## 03. How
![Screenshot from 2023-10-21 18-06-23](https://github.com/addinedu-amr-3rd/Robot-repo-1/assets/140477578/0db8e90d-97f9-4149-8f33-10b3ac4e1300)

---

## 04. Roadmap
![Screenshot from 2023-10-21 18-08-21](https://github.com/addinedu-amr-3rd/Robot-repo-1/assets/140477578/b16cec88-14a8-450e-8010-2e27b9457e98)

---

## 05. Step By Step
![Screenshot from 2023-10-21 18-09-07](https://github.com/addinedu-amr-3rd/Robot-repo-1/assets/140477578/f4f2e336-8918-4269-b212-767586926271)
![Screenshot from 2023-10-21 18-10-06](https://github.com/addinedu-amr-3rd/Robot-repo-1/assets/140477578/168c0def-9095-41e0-ae91-80a20b3d3542)
![Screenshot from 2023-10-21 18-10-15](https://github.com/addinedu-amr-3rd/Robot-repo-1/assets/140477578/2c9daa46-5811-4596-b770-7eab25daf3c4)

---

## 06. Let's see
https://github.com/addinedu-amr-3rd/Robot-repo-1/assets/140477578/163eb364-0a1f-4b45-a099-df01d72ff0fb

---

## 07. Estimation

---
