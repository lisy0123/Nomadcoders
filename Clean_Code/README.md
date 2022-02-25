# Clean Code

## 목차

>  [0. 추천사 & 들어가면서](https://github.com/lisy0123/Nomadcoders/tree/main/Clean_Code#0-%EC%B6%94%EC%B2%9C%EC%82%AC--%EB%93%A4%EC%96%B4%EA%B0%80%EB%A9%B4%EC%84%9C)
>
>  [1. 깨끗한 코드](https://github.com/lisy0123/Nomadcoders/tree/main/Clean_Code#1-%EA%B9%A8%EB%81%97%ED%95%9C-%EC%BD%94%EB%93%9C)
>
>  [2. 의미있는 이름](https://github.com/lisy0123/Nomadcoders/tree/main/Clean_Code#2-%EC%9D%98%EB%AF%B8%EC%9E%88%EB%8A%94-%EC%9D%B4%EB%A6%84)
>
>  [3. 함수](https://github.com/lisy0123/Nomadcoders/tree/main/Clean_Code#3-%ED%95%A8%EC%88%98)
>
>  [4. 주석]
>
>  [5. 형식 맞추기]
>
>  [6. 객체와 자료 구조]

## 0. 추천사 & 들어가면서

> Day 02 (Feb 19, 2022)

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

> Day 02 (Feb 19, 2022)

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

> Day 03 (Feb 20, 2022)

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

- [헝거리식 표기법](https://itwiki.kr/w/%ED%97%9D%EA%B0%80%EB%A6%AC%EC%95%88_%ED%91%9C%EA%B8%B0%EB%B2%95): 프로그래밍 언어에서 변수 및 함수의 인자 이름 앞에 데이터 타입을 명시하는 코딩 규칙

- 불용어(Noise word): 없어도 의미 전달에 영향이 없는 단어

[:arrow_up: 목차로 돌아가기](https://github.com/lisy0123/Nomadcoders/tree/main/Clean_Code#clean-code)

---

## 3. 함수

> Day 05 (Feb 22, 2022)
>
> Day 06 (Feb 23, 2022)

### :book: 기억하고 싶은 책 내용

- **작게 만들어라!**

  <details>
    <summary> code </summary>
    <div markdown="1">

  ```java
  // 설정(setup) 페이지와 해제(teardown) 페이지를 테스트 페이지에 넣은 후 해당 테스트 페이지를 HTML로 렌더링하는 함수.
  public static String renderPageWithSetupsAndTeardowns(
    PageData pageData, boolean isSuite
  ) throws Exception {
    boolean isTestPage = pageData.hasAttribute("Test");
    if (isTestPage) {
      WikiPage testPage = pageData.getWikiPage();
      StringBuffer newpageContent = new StringBuffer();
      includeSetupPages(testPage, newPageContent, isSuite);
      newPageContent.append(pageData.getContent());
      includeTeardownPages(testPage， newPageContent, isSuite);
      pageData.setContent(newPageContent.toString());
    }
    return pageData.getHtml();
  }
  
  // 다음과 같이 줄일 수 있다.
  public static String renderPageWithSetupsAndTeardowns(
    PageData pageData, boolean isSuite) throws Exception {
    if (isTestPage(pageData))
      includeTeardownPages(pageData, isSuite);
    return pageData.getHtml();
  }
  ```

    </div>
  </details>

  - 블록과 들여쓰기

    if 문/else /while 문 등에 들어가는 블록은 한 줄어야 한다.

    중첩 구조가 생길만큼 함수가 커져서는 안 된다.

    함수에서 들여쓰기 수준이 1, 2단을 넘어서면 안 된다.

- **한 가지만 해라**

  함수는 한 가지를 해야 한다. 그 한 가지를 잘 해야 한다. 그 한 가지만을 해야 한다.

  단순히 다른 표현이 아니라 의미 있는 이름으로 다른 함수를 추출할 수 있다면 그 함수는 여러 작업을 하는 셈이다.

  - 함수 내 섹션

- **함수 당 추상화 수준은 하나로!**

  함수가 확실히 한 가지 작업만 하려면 함수 내 모든 문장의 추상화 수준이 동일해야 한다.

  - 아래 함수에서의 추상화 수준

    `getHtml()`: 상 / `String pagePathName = PathParser.render(pagepath);`: 중 / `.append("\n")`: 하

    <details>
      <summary> code </summary>
      <div markdown="1">

    ```java
    public static String testableHtml(
      PageData pageData,
      boolean includeSuiteSetup
    ) throws Exception {
      Wikipage wikipage = pageData.getWikiPage();
      StringBuffer buffer = new StringBuffer();
      if (pageData.hasAttribute("Test")) {
        if (includeSuiteSetup) {
          WikiPage suiteSetup = PageCrawlerlmpl.getlnheritedPage(
            SuiteResponder.SUITE_SETUP_NAME, wikiPage
          );
          if (suiteSetup != null) {
            wikiPagePath pagePath =
              suiteSetup.getPageCrawler().getFullPath(suiteSetup);
            String pagePathName = PathParser.render(pagePath);
            buffer.append("include -setup .")
              .append(pagePathName)
              .append("\n");
          }
        }
        WikiPage setup =
          PageCrawlerlmpl.getInheritedPage("SetUp", wikiPage);
        if (setup != null) {
          WikiPagePath setupPath =
            wikiPage.getPageCrawler().getFullPath(setup);
          String setupPathName = PathParser.render(setupPath);
          buffer.append("!include -setup .")
            .append(setupPathName)
            .append("\n");
        }
      }
      buffer.append(pageData.getContent());
      if (pageData.hasAttribute("Test")) {
        WikiPage teardown =
          pageCrawlerlmpl.getInheritedPage("TearDown", wikiPage);
        if (teardown != null) {
          WikiPagePath tearDownPath =
            wikiPage.getPageCrawler().getFullPath(teardown);
          String tearDownPathName = PathParser.render(tearDownPath);
          buffer.append("\n")
            .append("!include -teardown .")
            .append(tearDownPathName)
            .append("\n");
        }
        if (includeSuiteSetup) {
          WikiPage suiteTeardown =
            PageCrawlerlmpl.getlnheritedPage(
            	SuiteResponder.SUITE_TEARDOWN_NAME,
            	wikiPage
          );
          if (suiteTeardown != null) {
            Wikipagepath pagePath =
              suiteTeardown.getPageCrawler().getFullPath (suiteTeardown);
            String pagePathName = PathParser.render(pagePath);
            buffer.append("!include -teardown .")
              .append(pagePathName)
              .append("\n");
          }
        }
      }
      pageData.setContent(buffer.toString());
      return pageData.getHtml();                                                                                               }
    ```

      </div>
    </details>

  - 위에서 아래로 코드 읽기: **내려가기 규칙**

    코드는 위에서 아래로 이야기까지 읽혀야 좋다.

    위에서 아래로 프로그램을 읽으면 함수 추상화 수준이 한 번에 한 단계씩 낮아진다.

- **Switch 문**

  다형성을 이용해, 저차원 클래스에 숨기고 절대 반복하지 않는다. 

  <details>
    <summary> code </summary>
    <div markdown="1">


  ```java
  public Money calculatePay(Employee e)
    throws InvalidEmplᄋyeeType {
    switch (e.type) {
      case COMMISSIONED:
        return caleulateCommissionedPay(e);
      case HOURLY:
        return calculateHourlyPay(e);
      case SALARIED:
        return calculateSalariedPay(e);
      default:
        throw new InvalidEmployeeType(e.type);
    }
  }
  ```

    </div>
  </details>

  위 함수 문제점

  1. 함수가 너무 길다.
  2. 한가지 작업만 수행하지 않는다.
  3. SRP 위반: 코드의 변경이유가 여럿이다.
  4. OCP 위반: 새 직업의 유형이 추가 될 때마다 코드 변경 필요.

  개선한 코드는 다음과 같다.

  <details>
    <summary> code </summary>
    <div markdown="1">


  ```java
  public abstract class Employee {
    public abstract boolean isPayday();
    public abstract Money calculatePay();
    public abstract void deliverPay(Money pay);
  }
  
  public interface EmployeeFactory {
    public Employee makeEmployee(EmployeeRecord r) throws InvalidEmployeeType;
  }
  
  public class EmployeeFactorylmpl implements EmployeeFactory {
    public Employee makeEmployee(EmployeeReco rd r) throws InvalidEmployeeType {
      switch (r.type) {
        case COMMISSIONED:
          return new CommissionedEmployee(r);
        case HOURLY:
          return new HourlyEmployee(r);
        case SALARIED:
          ret니rn new SalariedEmployee(r);
        default:
          throw new InvalidEmp 'LoyeeType! r.type);
      }
    }
  }
  ```

    </div>
  </details>

  하지만 위 규칙을 완벽하게 지키기는 어렵다.

- **서술적인 이름을 사용하라!**

  함수가 작고 단순할수록 서술적인 이름을 고르기도 쉬워진다.

  길고 서술적인 이름이 짧고 어려운 이름보다 좋고, 길고 서술적인 주석보다 좋다.

  이름을 붙일 때는 일관성이 있어야 한다.

- **함수 인수**

  함수에서 이상적인 인수 개수는 0개(무항)이고, 3개(삼항) 이상은 가능한 피하는 것이 좋다.

  인수는 개념을 이해하기 어렵게 만든다.

  테스트 관점에서 보면 인수는 더 어렵다. 갖가지 인수 조합으로 함수를 검증하는 테스트 케이스를 작성해야하기 때문이다.

  - 많이 쓰는 단항 형식

    함수에 인수 1개를 넘기는 이유

    1. 인수에 질문을 던지는 경우
    2. 인수를 뭔가로 변환해 결과를 반환하는 경우

    3. 드물게 함수형식의 이벤트까지 존재

    위 세가지의 경우가 아니라면 단항함수는 가급적 피한다.

    ex) `StringBuffer`를 함수의 인수로 넘기는 것을 피한다. 변환함수에서 출력인수를 사용하면 혼란을 일으킨다.

  - 플래그 인수

    함수가 헌꺼번에 여러 가지를 처리한다고 대놓고 공표하는 셈으로 되도록 사용하지 않기.

  - 이항 함수

    인수가 2개인 함수는 인수가 1개인 함수보다 이해하기 어렵다.

    불가피한 상황이 아니라면 위험이 따른다는 사실을 이해하고 가능하면 단항으로 변경해야한다.

  - 삼항 함수

  - 인수 객체

    인수가 2~3개 필요하다면, 그 중 일부를 묶어 하나의 클래스 변수로 선언할 수도 있다.

    <details>
      <summary> code </summary>
      <div markdown="1">


    ```java
    Circle makeCircle(double x, double y, double radius);
    Circle makeCircle(Point center, double radius);
    // x, y를 묶어 하나의 클래스 변수로 넘기려면 결국 이름을 지어야하고, 결국은 개념을 표현하게 된다.
    ```
    
      </div>
    </details>

  - 인수 목록

    때로는 인수가 가변적인 함수도 필요하다. ex) `String.format`

    가변인수를 통해 리스트형 인수를 하나로 취급할 수 있다.

  - 동사와 키워드

    단항 함수는 함수와 인수가 동사/명사 쌍을 이뤄야 한다. ex) `writeField(name)`

    함수 이름에 키워드를 추가하면서 함수 이름에 인수 이름을 넣는다. ex) `assertExpectedEqualsActual(Expected, actual)`

- **부수 효과를 일으키지 마라!**

  부수 효과가 많은 경우, 시간적인 결합이나 순서 종속성을 초래한다.

  <details>
    <summary> code </summary>
    <div markdown="1">


  ```java
  public class UserValidator {
    private Cryptographer cryptographer;
    public boolean checkPassword(String usenName, String password) {
      User user = UserGateway.findByName(userName);
      if (user != User.NULL) {
        String codedPhrase = user.getPhraseEncodedByPassword(); String phrase = cryptographer.decrypt(codedPhrase, password);
        if ("Valinitializeid Password".equals(phrase)) {
          Session.initialize(); return true;
        }
      } return false;
    }
  }
  ```

    </div>
  </details>

  위 함수의 부수효과: `Session.initialize();`

  만약 시간적인 결합이 필요하다면 함수 이름에 분명히 명시한다.

  - 출력 인수

    객체지향 언어에서는 출력 인수를 사용할 필요가 거의 없다. 출력 인수로 사용하라고 설계한 변수 `this`가 있기 때문이다.

    일반적으로 출력 인수는 피해야 한다. 함수에서 상태를 변경해야 한다면 함수가 속한 객체 상태를 변경하는 방식을 택한다.

- **명령과 조희를 분리하라!**

  함수는 객체 상태를 변경하거나, 객체 정보를 반환하거나 둘 중 하나만 해야 한다.

  아래 코드처럼 명령과 조회를 분리해서 혼란을 애초에 뿌리뽑아야 한다.

  <details>
    <summary> code </summary>
    <div markdown="1">

  ```java
  // Bad
  if(set("username", "namget"))....
  
    // Good
  if(attributeExist("username")){
    setAttribute("username", "namget");
  }
  ```

    </div>
  </details>

- **오류 코드보다 예외를 사용하라!**

  명령 함수에서 오류 코드를 반환하는 방식은 명령/조회 분리 규칙을 미묘하게 위반한다. if문에서 명령을 표현식으로 사용하기 쉬운 탓이다.

  오류 코드 대신 예외를 사용해 오류 처리 코드를 원래 코드에서 분리하여 코드를 깔끔하게 만든다.

  <details>
    <summary> code </summary>
    <div markdown="1">

  ```java
  public void delete(Page page) {
    try {
      deletePage(page);
      registry.deleteReference(page.name);
      configKyes.deleteKey(page.name.makeKey());
    } catch (Exception e) {
      logger.log(e.getMessage());
    }
  }
  ```

    </div>
  </details>

  - Try/Catch 블록 뽑아내기

    try/catch는 코드 구조에 혼란을 일으키며 정상 동작과 오류 처리 동작을 뒤섞는다.

    따라서 try/catch 블록을 별도 함수로 뽑아내는것이 좋다.

    <details>
      <summary> code </summary>
      <div markdown="1">

    ```java
    public void delete(Page page) {
      try {
        deletePageAndAllReferences(page);
      } catch (Exception e) {
        logError(e);
      }
    }
    
    private void deletePageAndAllReferences(Page page) throws Exception {
      deletePage(page);
      registry.deleteReference(page.name);
      configKyes.deleteKey(page.name.makeKey());
    }
    
    private void logError(Exception e) {
      logger.log(e.getMessage());
    }
    ```

      </div>
    </details>

  - 오류 처리도 한 가지 작업이다.

    함수는 한 가지 작업만 하고, 오류 처리도 한 가지 작업에 속한다.

  - `Error,java` 의존성 자석

    <details>
      <summary> code </summary>
      <div markdown="1">

    ```java
    public enum Error {
      OK,
      INVALID,
      N0_SUCH,
      LOCKED,
      0UT_0F_RES0URCES,
      WAITING_FOR_EVENT;
    }
    ```

      </div>
    </details>

    위와 같은 클래스는 의존성 자석이다. 다른클래스에서 Error enum을 import하고, Error enum이 변경되면 Error enum을 사용하는 클래스 전부 다시 컴파일하고 배치해야한다.

    오류코드 대신 예외를 사용하면 재컴파일/재배치 없이도 새 예외 클래스를 추가할 수 있다. (OCP를 보여주는 예)

- **반복하지 마라!**

  중복을 없앴더니 모듈 가독성이 크게 높아졌다. 중복은 소프트웨어에서 모든 악의 근원이다. 

  관계형 데이터베이스의 정규 형식, 구조적 프로그래밍, AOP, COP 모두 중복 제거 전략이다.

- **구조적 프로그래밍**

  모든 함수와 함수는 입구와 출구는 하나만 존재한다. 루프 안에서 break, continue를 사용해선 안 되며 goto는 절대로, 절대로 안 된다.

  하지만, 위 규칙은 함수가 아주 클 때만 상당한 이익을 제공한다. 함수를 작게 만든다면 return , break, continue를 여러차례 사용해도 괜찮고, 때로는 단일 입/출구 규칙보다 의도를 표현하기 쉬워진다.

  goto문은 큰 함수에서만 의미가 있으므로, 작은 함수에서는 피해야만 한다.

- **함수를 어떻게 짜죠?**

  서투른 코드를 빠짐없이 테스트하는 단위 테스트 케이스도 만든다.

  다음, 코드를 다듬고, 함수를 만들고, 이름을 바꾸고, 중북을 제거한다. 메서드를 줄익도, 순서를 바꾸며, 때로는 전체클래스를 쪼갠다. 그리고 코드는 항상 단위 테스트를 통과한다.

### 📌 소감 및 생각

코드들을 살펴보면서 저자가 말하고자하는 바들을 잘 알 수 있었다. 특히 이름의 중요성을 많이 느꼈는데, 그 동안 이름을 약어로 많이 썼었는데 반성해야겠다. 그리고 자바는 아직 접한 적 없는 언어인데, 코드를 읽는데 아직까지는 큰 무리가 없어서 다행이었다.

### 🔎 새롭게 배운 개념

- 추상화 수준: 말 그대로 구체적으로 풀어 쓰기보다는 추상적으로 표현되어 있다면 추상화 수준이 높고, 추상화 되어 있지 않고 직접적인 코드는 추상화 수준이 낮다.
- [SRP(Single Responsibility Principle)](https://blog.itcode.dev/posts/2021/08/13/single-responsibility-principle): 단일 책임 원칙, 하나의 객체는 반드시 하나의 동작만의 책임을 갖는다는 원칙.
- [OCP(Open-Closed Principle)](https://blog.itcode.dev/posts/2021/08/14/open-closed-principle): 개방-폐쇄 원칙, 객체의 확장은 개방적으로, 객체의 수정은 폐쇄적으로 대하는 원칙.
- 플래그 인수: 부울값을 넘기게 되면 함수가 여러가지를 처리한다는 의미.
- [AOP(Aspect Oriented Programming)](https://3months.tistory.com/74): 관점 지향 소프트웨어 공학, 또는 상황중심 프로그래밍으로 번역되는 하나의 프로그래밍 방법론으로 객체지향 코드 위에서 이루어지며 객체지향을 보조하는 역할을 한다.
- [COP(Component Oriented Programming)](https://ko.wikipedia.org/wiki/%EC%BB%B4%ED%8F%AC%EB%84%8C%ED%8A%B8_%EA%B8%B0%EB%B0%98_%EC%86%8C%ED%94%84%ED%8A%B8%EC%9B%A8%EC%96%B4_%EA%B3%B5%ED%95%99): 컴포넌트 기반 소프트웨어 공학, 기존의 시스템이나 소프트웨어를 구성하는 컴포넌트를 조립해서 하나의 새로운 응용 프로그램을 만드는 소프트웨어 개발방법론
- 단일 입/출구 규칙(single entry-exit rule): 모든 블록에 입구와 출구는 하나만 존재해야 한다.

[:arrow_up: 목차로 돌아가기](https://github.com/lisy0123/Nomadcoders/tree/main/Clean_Code#clean-code)

---

## 4. 주석

> Day 07 (Feb 24, 2022)
>
> Day 08 (Feb 25, 2022)

### :book: 기억하고 싶은 책 내용

- 주석은 나쁜 코드를 보안하지 못한다. 표현력이 풍부하고 깔끔하며 주석이 거의 없는 코드가 복잡하고 어수선하며 주석이 많이 달린코드보다 훨씬 좋다. 자신이 저지른 난장판을 주석으로 설명하려 애쓰는 대신에 그 난장판을 깨끗히 치우는데 시간을 보내라.
- 코드로 의도를 표현하라.
- **좋은 주석**
  1. 법적인 주석
  2. 정보를 제공하는 주석
  3. 의도를 설명하는 주석
  4. 의미를 명료하게 밝히는 주석
  5. 결과를 경고하는 주석
  6. TODO(앞으로 할 일) 주석
  7. 중요성을 강조하는 주석
  8. 공개 API에서 Javadocs
- **나쁜 주석**
  1. 주절거리는 주석
  2. 같은 이야기를 중복하는 주석
  3. 오해할 여지가 있는 주석
  4. 의무적으로 다는 주석
  5. 이력을 기록하는 주석
  6. 있으나 마나 한 주석 => 함수나 변수로 표현 할 수 있다면 주석을 달지 말라
  7. 위치를 표시하는 주석
  8. 닫는 괄호에 다는 주석
  9. 공로를 돌리거나 저자를 표시하는 주석
  10. 주석으로 처리한 코드
  11. HTML 주석
  12. 전역 정보 (근처에 있는 코드만 주석으로 달 것 => 시스템의 전반적인 정보를 기술하지 마라
  13. 너무 많은 정보
  14. 흥미로운 역사나 정보
  15. 모호한 관계 (코드를 설명하기 위해 주석이 존재하는데 주석에 설명이 필요해선 안된다.)
  16. 함수헤더 (이름을 잘 지은 함수는 주석이 필요하지 않다.)
  17. 비공개 코드에서 Javadocs

### 📌 소감 및 생각

이번 내용은 영어가 주언어가 아닌 사람으로써 저자의 주장에 조금 애매한 감이 있다. 그래도 세계적으로 넓게 보았을 때, 저자의 말에 공감하고 영어 공부를 더 많이 해야겠다는 생각이 들었다.

### 🔎 새롭게 배운 개념

- 쉰들러 리스트
- Javadocs

[:arrow_up: 목차로 돌아가기](https://github.com/lisy0123/Nomadcoders/tree/main/Clean_Code#clean-code)

---

[↩️ Go Back](https://github.com/lisy0123/Nomadcoders)

