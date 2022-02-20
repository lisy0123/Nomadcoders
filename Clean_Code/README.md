# Clean Code

## 목차

>  [0. 추천사 & 들어가면서](https://github.com/lisy0123/Nomadcoders/tree/main/Clean_Code#0-%EC%B6%94%EC%B2%9C%EC%82%AC--%EB%93%A4%EC%96%B4%EA%B0%80%EB%A9%B4%EC%84%9C)
>
>  [1. 깨끗한 코드](https://github.com/lisy0123/Nomadcoders/tree/main/Clean_Code#1-%EA%B9%A8%EB%81%97%ED%95%9C-%EC%BD%94%EB%93%9C)
>
>  [2. 의미있는 이름](https://github.com/lisy0123/Nomadcoders/tree/main/Clean_Code#2-%EC%9D%98%EB%AF%B8%EC%9E%88%EB%8A%94-%EC%9D%B4%EB%A6%84)
>
>  [3. 함수]
>
>  [4. 주석]
>
>  [5. 형식 맞추기]
>
>  [6. 객체와 자료 구조]

## 0. 추천사 & 들어가면서

### :book: 기억하고 싶은 책 내용

- 사소한 곳에서 발휘하는 정직은 사소하지 않다: 단순히 사소한 것에 집중할 뿐 아니라 사소한 것에 정직해야 한다는 의미
- 신은 세세함에 깃들어 있다. - 루트비히 미스 반 데어 로에, 건축가
- 5S 원칙: 정리(Seiri, 정렬), 정돈(Seiton, 체계화), 청소(Seiso, 광내기), 청결(Seiketsu, 표준화), 생활화(Shutsuke, 규율)
- 작은 것에도 충실한 사람이 큰 것에도 충실하다.
- 품질은 하늘에서 뚝 떨어진 위대한 방법론이 아니라 사심 없이 기울이는 무수한 관심에서 얻어진다.
- 장인 정신: 이론 + 실전

### 📌 소감 및 생각

클린코드는 코드를 짤 때마다 항상 따라오는 말이다. 42SV를 다니면서 그 중요성을 처음 알았고, 팀플을 하면서 클린코드의 중요성을 다시 한 번 느낄 수 있었다. 내 코드는 얼마나 꺠끗한지 되돌아보면서 내 코드 작성 습관을 다듬는데 좋은 지침서가 되어줄 것 같다.

### 🔎 새롭게 배운 개념

- [애자일](http://www.incodom.kr/%EC%95%A0%EC%9E%90%EC%9D%BC_%EB%B0%A9%EB%B2%95%EB%A1%A0): 개인별 또는 팀 간에 고객과 협업하고 빠른 개발을 수행(고객과 협업)
- [린(Lean)](http://www.incodom.kr/%EB%A6%B0_%EC%86%8C%ED%94%84%ED%8A%B8%EC%9B%A8%EC%96%B4_%EA%B0%9C%EB%B0%9C%EB%B0%A9%EB%B2%95%EB%A1%A0): 고객 관점에서 전체 프로세스상에서 낭비를 제거하여 고객 가치를 높이는 것에 우선순위(전적으로 고객 관점)

[:arrow_up: 목차로 돌아가기](https://github.com/lisy0123/Nomadcoders/tree/main/Clean_Code#clean-code)

---

## 1. 깨끗한 코드

### :book: 기억하고 싶은 책 내용

- 코드는 요구사항을 표현하는 언어라는 사실을 명심한다.
- 좋은 코드를 사수하는 일은 바로 우리 프로그래머들의 책임이다.
- 깨끗한 코드를 작성하는 프로그래머는 빈 캔퍼스를 우아한 작품으로 바꿔가는 화가와 같다.
- 나쁜 코드는 나쁜 코드를 유혹한다.
- 꺠끗한 코드는 세세한 사항까지 꼼꼼하게 처리하는 코드이다.
- 깨끗한 코드는 한가지에 집중한다.
- 아우리 코드가 우아해도, 아무리 가독성이 높아도, 테스트 케이스가 없으면 깨끗하지 않다.
- 깨끗한 코드는 주의 깊게 작성한 코드다.
- 중복 줄이기, 표현력 높이기, 초반부터 간단한 추상화 고려하기

### 📌 소감 및 생각

나쁜 코드를 클린 코드를 바꾸는 법에 대해 알려준다는 말이 가장 눈에 띄었다. 42SV에서 만든 코드 작성 습관과 책의 내용과 비교하면서 습관을 다듬어 나가고, 나쁜 코드를 고치는 연습을 해야겠다. 그리고 초반뿐만 아니라 꾸준히 클린 코드를 유지해야 한다는 말도 명심하자.

### 🔎 새롭게 배운 개념

- [킬러 앱](https://ko.wikipedia.org/wiki/%ED%82%AC%EB%9F%AC_%EC%95%A0%ED%94%8C%EB%A6%AC%EC%BC%80%EC%9D%B4%EC%85%98): 인기와 수요가 높은 응용 프로그램 제품

- 르발랑의 법칙: 나중은 절대 돌아지 않는다는 법칙
- SRP(Single Responsibility Principle): 클래스에는 한 가지, 단 한 가지 변경 이유만 존재해야 한다.
- OCP(Open CLosed Principle): 클래스는 확장에 열려 있어야 하며 변경에 닫혀 있어야 한다.
- LSP(Liskov Substitution Principle): 상속받은 클래스는 기초 클래스를 대체할 수 있어야 한다.
- DIP(Dependency Inversion Principle): 추상화에 의존해야 하며, 구체화에 의존하면 안 된다.
- ISP(Interface Sepgregation Principle): 클라이언트에 밀접하게 작게 쪼개진 인터페이스를 유지한다.

[:arrow_up: 목차로 돌아가기](https://github.com/lisy0123/Nomadcoders/tree/main/Clean_Code#clean-code)

---

## 2. 의미있는 이름

### :book: 기억하고 싶은 책 내용

- **의도를 분명히 밝혀라**

  변수의 존재 이유는? 수행 기능은? 사용 방법은? 따로 주석이 필요하다면 의도를 분명히 드러내지 못했다는 말이다.

  <details>
    <summary> code </summary>
    <div markdown="1">

  ```java
  // Bad
  public List<int[]> getThem() {
    List<int[]> list1 = new ArrayList<int[]>();
    for (int[] x : theList)
      if (x[0] == 4)
        list1.add(x);
    return list1;
  }
  
  // Good
  public List<Cell> getFlaggedCells() {
    List<Cell> flaggedCells = new ArrayList<Cell>();
    for (Cell cell : gameBoard)
      if (cell.isFlagged())
        flaggedCells.add(cell);
    return flaggedCells;
  }
  ```

    </div>
  </details>

- **그릇된 정보를 피하라**

  일관성이 떨어지는 표기법은 그릇된 정보다.

  약어를 지양하자.

- **의미 있게 구분하라**

  읽는 사람이 차이를 알도록 이름을 지어라.

  <details>
    <summary> code </summary>
    <div markdown="1">

  ```java
  // Bad
  public state void copyChars(char a1[], char a2[])
    
  // Good
  public state void copyChars(char source, char destination)
  ```

    </div>
  </details>

- **발음하기 쉬운 이름을 사용하라**

  <details>
    <summary> code </summary>
    <div markdown="1">

  ```java
  // Bad
  Date genymdhms;
    
  // Good
  Date generationTimestamp;
  ```

    </div>
  </details>

- **검색하기 쉬운 이름을 사용하라**

  이름 길이는 범위 크기에 비례해야 한다.

  <details>
    <summary> code </summary>
    <div markdown="1">

  ```java
  // Bad
  for (int i = 0; i < 10; i++) {
    s += i * 5;
  }
    
  // Good
  int maxIndex = 10;
  const int MULTIPLICATION_CONDITION = 5;
  int sum = 0;
  
  for (int i = 0; i < maxIndex; i++) {
    sum += i * MULTIPLICATION_CONDITION;
  }
  ```

    </div>
  </details>

- **인코딩을 피하라**

  헝거리식 표기법을 지양하자.

  멤버 변수임을 명시하기 위해 "m_" 접두어 사용하는 것을 지양하고, 클래스와 함수는 접두어가 필요없을 정도로 작게 구현한다.

  <details>
    <summary> code </summary>
    <div markdown="1">

  ```java
  // Bad
  String m_dsc;
  public interface IShapeFactory;
  public class ShapeFactory;
  
  // Good
  String description;
  public interface ShapeFactory;
  public class ShapeFactoryImp;
  public class CShapeFactory;
  ```

    </div>
  </details>

- **자신의 기억력을 자랑하지 마라**

  전문가 프로그래머는 자신의 능력을 좋은 방향으로 사용해 남들이 이해하는 코드를 내놓는다.

- **클래스 & 객체 이름: 명사, 명사구**

  `Customer, WikiPage, AddressParser`

- **메서드 이름: 동사, 동사구**

  접근자, 변경자, 조건자는 Javabean 표준에 따라 get, set, is 붙이기.

  <details>
    <summary> code </summary>
    <div markdown="1">

  ```java
  string name = employee.getName();
  customer.setName("mike");
  if (paycheck.isPosted())...
  
  // Bad
  Complex fulcrumPoint = new Complex(10.0)
  
  // Good
  Complex fulcrumPoint = Complex.FromRealNumber(10.0)
  ```

    </div>
  </details>

- **기발한 이름은 피하라**

  의도를 분명하고 솔직하게 표현하라.

- **한 개념에 한 단어를 사용하라**

  메서드 이름은 독자적이고 일관적이어야 한다.

- **말장난을 하지 마라**

  한 개념에 한 단어를 사용하되, 일관성을 고려한다.

- **해법 영역, 문제 영역에서 가져온 이름을 사용하라**

  - **해법 영역 (Solution Domain)**

    개발자라면 당연히 알고 있을 전산용어, 알고리즘 이름, 패턴 이름, 수학 용어 등은 사용하자. `JobQueue`, `AccountVisitor(Visitor pattern)` 등

  - **문제 영역 (Problem Domain)**

    실제 도메인의 전문가에게 의미를 물어 파악할 수 있도록 문제 영역에서 이름을 가져오자.

- **의미 있는 맥락을 추가하라**

  <details>
    <summary> code </summary>
    <div markdown="1">

  ```java
  // Bad
  private static void printGuessStatistics(char candidate, int count) {
    String number;
    String verb;
    String pluralModifier;
  
    if (count == 0) {
      number = "no";
      verb = "are";
      pluralModifier = "s";
    } else if (count == 1) {
      number = "1";
      verb = "is";
      pluralModifier = "";
    } else {
      number = Integer.toString(count);
      verb = "are";
      pluralModifier = "s";
    }
    
    String guessMessage = String.format("There %s %s %s%s", verb, number, candidate, pluralModifier);
    System.out.println(guessMessage);
  }
  
  // Good
  public class GuessStatisticsMeeage {
    String number;
    String verb;
    String pluralModifier;
  
    public String make(char candidate, int count) {
      createPluralDependentMessage(count);
      return String.format("There %s %s %s%s", verb, number, candidate, pluralModifier);
    }
  
    private void createPluralDependentMessage(int count) {
      if (count == 0) {
        thereAreNoLetters();
      } else if (count == 1) {
        thereIsOneLetter();
      } else {
        thereManyLetters(count);
      }
    }
  
    private void thereManyLetters(int count) {
      number = Integer.toString(count);
      verb = "are";
      pluralModifier = "s";
    }
  
    private void thereIsOneLetter() {
      number = "1";
      verb = "is";
      pluralModifier = "";
    }
  
    private void thereAreNoLetters() {
      number = "no";
      verb = "are";
      pluralModifier = "s";
    }
  }
  ```

    </div>
  </details>

- **불필요한 맥락을 없애라**

### 📌 소감 및 생각

코드가 길어지면 길어질수록 각 변수나 함수들의 이름들은 다채로워진다. 한끗 차이인 이름을 가지고 고민한 적도, 이미 존재하는 함수명 때문에 골머리를 앓은 적도 있었다. 개인적으로 이름이 긴 것을 싫어하다보니 약어를 자주 사용했었는데 앞으로는 지양해야겠다. 그 중에서 발음하기 쉬운 이름은 생각도 안 해봤는데 새롭게 알아간다. 영어가 주언어가 아니다보니 발음까지는 크게 신경쓰지 않았던 것 같다.

### 🔎 새롭게 배운 개념

- 불용어(Noise word): 없어도 의미 전달에 영향이 없는 단어

[:arrow_up: 목차로 돌아가기](https://github.com/lisy0123/Nomadcoders/tree/main/Clean_Code#clean-code)

---

[↩️ Go Back](https://github.com/lisy0123/Nomadcoders)

