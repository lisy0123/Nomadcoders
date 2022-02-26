# Mission 02

> Day 09 (Feb 26, 2022)
>
> Day 10 (Feb 27, 2022)

## :one: mission 01

```java
// BAD 더러운 코드 😣
// Hint❕ : 검색하기 쉬운 이름을 사용하세요.
// blastOFF는 로켓 발사를 의미. 86400000은 하루의 밀리초 (milliseconds) 의미. 

// What the heck is 86400000 for?
setTimeout(blastOff, 86400000);

// GOOD 😎
// 위 코드를 깨끗하게 다시 작성해 주세요.

const MILLISECONDS_PER_DAY = 60 * 60 * 24 * 1000;
setTimeout(blastOff, MILLISECONDS_PER_DAY);

// 어떻게 고쳤는지, 사례에서 무엇을 배워야 하는지 설명해주세요.

// 검색 가능한 이름으로 고치기.
// 대문자로 상수 선언.
// 숫자의 의미를 알 수 있게 정의.
```

---

## :two: mission 02

```java
// BAD 더러운 코드 😣
// Hint❕ : 의미있는 이름을 사용해주세요.

const yyyymmdstr = moment().format("YYYY/MM/DD");

// GOOD 😎
// 위 코드를 깨끗하게 다시 작성해 주세요.

const currentDate - moment().format("YYYY/MM/DD");

// 어떻게 고쳤는지, 사례에서 무엇을 배워야 하는지 설명해주세요.

// 의미있고 발음하기 쉬운 변수 이름 사용
```

---

## :three: mission 03

```java
// BAD 더러운 코드 😣
// Hint❕ : 불필요하게 반복하지 마세요.

const Car = {
  carMake: "Honda",
  carModel: "Accord",
  carColor: "Blue"
};

function paintCar(car, color) {
  car.carColor = color;
}

// GOOD 😎
// 위 코드를 깨끗하게 다시 작성해 주세요.

const Car = {
  make: "Honda",
  model: "Accord",
  color: "Blue"
};

function paintCar(car, color) {
  car.color = color;
}

// 어떻게 고쳤는지, 사례에서 무엇을 배워야 하는지 설명해주세요.

// 클래스/개체 이름을 통해 알 수 있는 경우, 불필요한 반복 제거.
```

