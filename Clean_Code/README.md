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
>  [4. 주석](https://github.com/lisy0123/Nomadcoders/tree/main/Clean_Code#4-%EC%A3%BC%EC%84%9D)
>
>  [5. 형식 맞추기](https://github.com/lisy0123/Nomadcoders/tree/main/Clean_Code#5-%ED%98%95%EC%8B%9D-%EB%A7%9E%EC%B6%94%EA%B8%B0)
>
>  [6. 객체와 자료 구조](https://github.com/lisy0123/Nomadcoders/tree/main/Clean_Code#6%EA%B0%9D%EC%B2%B4%EC%99%80-%EC%9E%90%EB%A3%8C-%EA%B5%AC%EC%A1%B0)
>
>  [7. 오류처리](https://github.com/lisy0123/Nomadcoders/tree/main/Clean_Code#7-%EC%98%A4%EB%A5%98%EC%B2%98%EB%A6%AC)
>
>  [8. 경계](https://github.com/lisy0123/Nomadcoders/tree/main/Clean_Code#8-%EA%B2%BD%EA%B3%84)
>
>  [9. 단위 테스트](https://github.com/lisy0123/Nomadcoders/tree/main/Clean_Code#9-%EB%8B%A8%EC%9C%84-%ED%85%8C%EC%8A%A4%ED%8A%B8)
>
>  [10. 클래스](https://github.com/lisy0123/Nomadcoders/tree/main/Clean_Code#10-%ED%81%B4%EB%9E%98%EC%8A%A4)
>
>  ...
>
>  [Missions]

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

  - **블록과 들여쓰기**

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

  - **위에서 아래로 코드 읽기: 내려가기 규칙**

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
  
  **위 함수 문제점**
  
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

  - **많이 쓰는 단항 형식**

    함수에 인수 1개를 넘기는 이유

    1. 인수에 질문을 던지는 경우
    2. 인수를 뭔가로 변환해 결과를 반환하는 경우

    3. 드물게 함수형식의 이벤트까지 존재

    위 세가지의 경우가 아니라면 단항함수는 가급적 피한다.

    ex) `StringBuffer`를 함수의 인수로 넘기는 것을 피한다. 변환함수에서 출력인수를 사용하면 혼란을 일으킨다.

  - **플래그 인수**

    함수가 헌꺼번에 여러 가지를 처리한다고 대놓고 공표하는 셈으로 되도록 사용하지 않기.

  - **이항 함수**

    인수가 2개인 함수는 인수가 1개인 함수보다 이해하기 어렵다.

    불가피한 상황이 아니라면 위험이 따른다는 사실을 이해하고 가능하면 단항으로 변경해야한다.

  - **삼항 함수**

  - **인수 객체**

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

  - **인수 목록**

    때로는 인수가 가변적인 함수도 필요하다. ex) `String.format`

    가변인수를 통해 리스트형 인수를 하나로 취급할 수 있다.

  - **동사와 키워드**

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

  - **출력 인수**

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

  - **Try/Catch 블록 뽑아내기**

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

- 나쁜 코드에 주석을 달지 마라. 새로 짜라. - 브라이언 W. 커니헨,  P.J.플라우거

- 잘 달린 주석은 그 어떤 정보보다 유용하다. 경솔하고 근거 없는 주석은 코드를 이해하기 어렵게 만든다. 오래되고 조잡한 주석은 거짓과 잘못된 정보를 퍼뜨려 해악을 미친다.

- **주석은 나쁜 코드를 보완하지 못한다**

  표현력이 풍부하고 깔끔하며 주석이 거의 없는 코드가, 복잡하고 어수선하며 주석이 많이 달린 코드보다 훨씬 좋다. 

  자신이 저지른 난장판을 주석으로 설명하려 애쓰는 대신에 그 난장판을 깨끗히 치우는데 시간을 보내라.

- **코드로 의도를 표현하라!**

  <details>
    <summary> code </summary>
    <div markdown="1">
  
  ```java
  // Bad
  // 직원에게 복지 혜택을 받을 자격이 있는지 검사한다.
  if ((employee.flags & HOURLY_FLAG) &&
     (employee.age > 65))
  
  // Good
  if (employee.isEligibleForFullBenefits())
  ```
  
    </div>
  </details>

- **좋은 주석**

  정말로 좋은 주석은, 주석을 달지 않을 방법을 찾아낸 주석이다!

  1. **법적인 주석**

     법적인 이유로 특정 주석을 넣으라고 명시하는 경우

     각 소스 파일 첫머리에 주석으로 들어가는 저작권 정보와 소유권 정보

     <details>
       <summary> code </summary>
       <div markdown="1">

     ```java
     // Copyright (C) 2003, 2004, 2005 by Object Montor, Inc. All right reserved.
     // GNU General Public License
     ```

       </div>
     </details>

  2. **정보를 제공하는 주석**

     기본적인 정보를 주석으로 제공하면 편리

     <details>
       <summary> code </summary>
       <div markdown="1">

     ```java
     // 테스트 중인 Responder 인스턴스를 반환
     protected abstract Responder responderInstance();
     
     // 물론 주석도 함수 이름에 정보를 담아 responderBeingTested로 바꾸면 다음과 같이 없앨 수 있다.
     
     // Better
     // kk:mm:ss EEE, MMM dd, yyyy 형식이다.
     Pattern timeMatcher = Pattern.compile("\\d*:\\d*\\d* \\w*, \\w*, \\d*, \\d*");
     ```

       </div>
     </details>

  3. **의도를 설명하는 주석**

     코드를 짜면서 개발자의 결정에 깔린 의도를 설명하는 주석

     <details>
       <summary> code </summary>
       <div markdown="1">

     ```java
     // 스레드를 대량 생성하는 방법으로 어떻게든 경쟁 조건을 만들려 시도한다.
     for (int i = 0; i > 2500; i++) {
       WidgetBuilderThread widgetBuilderThread =
         new WidgetBuilderThread(widgetBuilder, text, parent, failFlag);
       Thread thread = new Thread(widgetBuilderThread);
       thread.start();
     }
     ```

       </div>
     </details>

  4. **의미를 명료하게 밝히는 주석**

     인수나 반환값이 표준 라이브러리나 변경하지 못하는 코드에 속할 때, 의미를 명료하게 밝히는 주석이 유용

     주석이 올바른지 검증하기 어렵다. 이는 의미를 명료히 밝히는 주석이 필요한 이유인 경우, 주석이 위험한 이유이기도 하다.

     주석을 달때는 더 나은 방법이 없는지를 고민하고 정확히 달도록 주의해야한다.

  5. **결과를 경고하는 주석**

     다른 프로그래머에게 결과를 경고 할 목적으로 주석 사용

     <details>
       <summary> code </summary>
       <div markdown="1">

     ```java
     // 여유 시간이 충분하지 않다면 실행하지 마십시오.
     public void _testWithReallyBigFile() {
       ...
     }
     
     public static SimpleDateFormat makeStandardHttpDateFormat() {
       // SimpleDateFormat은 스레드에 안전하지 못하므로, 각 인스턴스를 독립적으로 생성해야한다.
       SimpleDateFormat df = new SimpleDateFormat(".......");
       return df;
     }
     ```

       </div>
     </details>

  6. **TODO(앞으로 할 일) 주석**

     프로그래머가 필요하다 여기지만 당장 구현하기 어려운 업무를 기술하는 주석

     주기적으로 TODO 주석을 점검해 없애도 괜찮은 주석을 없애라.

     <details>
       <summary> code </summary>
       <div markdown="1">

     ```java
     //TODO-MdM 현재 필요하지 않다.
     protected VersionInfo makeVersion() throws Exception {
       return null;
     }
     ```

       </div>
     </details>

  7. **중요성을 강조하는 주석**

     대수롭지 않다고 여겨질 뭔가의 중요성을 강조하기 위해서도 사용

     <details>
       <summary> code </summary>
       <div markdown="1">

     ```java
     String ListItemContent = match.group(3).trim();
     //여기서 trim은 정말 중요하다.trim 함수는 문자열에서 시작 공백을 제거한다
     //문자열에 시작 공백이 잇으면 다른 문자열로 인식되기 때문이다.
     new ListItemWidget(this, listItemContent, this.level + 1);
     return buildList(text.substring(match.end()));
     ```

       </div>
     </details>

  8. **공개 API에서 Javadocs**

     설명이 잘 된 공개 API는 참으로 유용하고 만족스럽다.

     공개 API를 구현한다면 반드시 훌륭한 Javadocs를 작성한다.

     하지만 여느 주석과 마찬가지로 Javadocs 역시 독자를 오도하거나, 잘못 위치하거나, 그릇된 정보를 전달할 가능성이 존재한다.

- **나쁜 주석**

  1. **주절거리는 주석**

     <details>
       <summary> code </summary>
       <div markdown="1">

     ```java
     public void loadProperties() {
       try {
         String propertiesPath = propertiesLocation + "/" + PROPERTIES_FILE;
         FileInputStream propertiesStream = new FileInputStream(propertiesPath);
         loadedProperties.load(propertiesStream);
       } catch (IOException e) {
         // 속성 파일이 없다면 기본값을 모두 메모리로 읽어 들였다는 의미다.
       }
     }
     ```

       </div>
     </details>

     이해가 안 되어 다른 모듈까지 뒤져야 하는 주석은 독자와 제대로 소통하지 못하는 주석이다.

  2. **같은 이야기를 중복하는 주석**

     코드의 내용을 그대로 중복하는 주석. 전혀 필요없는 코드이다.

     <details>
       <summary> code </summary>
       <div markdown="1">

     ```java
     // this.closed가 true일 때 반환되는 유틸리티 메서드다.
     // 타임아웃에 도달하면 예외를 던진다.
     public synchronized void waitForClose(final long timeoutMillis) throws Exception {
       if (!closed) {
         wait(timeoutMillis);
         if (!closed) {
           throw new Exception("MockResponseSender could not be closed");
         }
       }
     }
     ```

       </div>
     </details>

  3. **오해할 여지가 있는 주석**

     실제 코드가 동작하는 것과 살짝 다른 정보로 주석이 달려있을 경우

  4. **의무적으로 다는 주석**

     모든 함수에 Javadocs를 달거나 모든 변수에 주석을 달아야 한다는 규칙은 코드를 복잡하게 만들고 잘못된 정보를 제공할 여지만 만든다.

     <details>
       <summary> code </summary>
       <div markdown="1">
     
     ```java
     /**
      * @param title CD 제목
      * @param author CD 저자
      * @param tracks CD 트랙 숫자
      * @param durationInMinutes CD 길이(단위: 분)
      */
     public void addCD(String title, String author, int tracks, int durationInMinutes) {
       CD cd = new CD();
       cd.title = title;
       cd.author = author;
       cd.tracks = tracks;
       cd.duration = durationInMinutes;
       cdList.add(cd);
     }
     ```
     
       </div>
     </details>
  
  5. **이력을 기록하는 주석**
  
     모듈에 가한 변경을 모두 기록하는 일종의 일지 혹은 로그
  
     소스 코드 관리 시스템이 없는 시절에는 유용했으나 지금은 혼란만 가중되므로 완전히 제거하는 것이 좋다.
  
     <details>
       <summary> code </summary>
       <div markdown="1">
     
     ```java
     * 변경 이력 (11-Oct-2001부터)
     * ------------------------------------------------
     * 11-Oct-2001 : 클래스를 다시 정리하고 새로운 패키지인
     * 05-Nov-2001: getDescription() 메소드 추가
     * ...
     ```
     
       </div>
     </details>
  
  6. **있으나 마나 한 주석**
  
     너무 당연한 사실을 언급하며 새로운 정보를 제공하지 못하는 주석
  
     <details>
       <summary> code </summary>
       <div markdown="1">
     
     ```java
     /*
      * 기본 생성자
      */
     protected AnnualDateRule() {
     }
     ```
     
       </div>
     </details>
  
  7. **무서운 잡음**
  
     수행하는 목적 없이 작성된 주석
  
     <details>
       <summary> code </summary>
       <div markdown="1">
     
     ```java
     /** The name. */
     private String name;
     
     /** The version. */
     private String version;
     ```
     
       </div>
     </details>
  
  8. **함수나 변수로 표현할 수 있다면 주석을 달지 마라**
  
     주석이 필요하지 않도록 코드를 개선하는 편이 더 좋다.
  
     <details>
       <summary> code </summary>
       <div markdown="1">
     
     ```java
     // Bad
     // 전역 목록 <smodule>에 속하는 모듈이 우리가 속한 하위 시스템에 의존하는가?
     if (smodule.getDependSubsystems().contains(subSysMod.getSubSystem()))
     
     // Good
     ArrayList moduleDependees = smodule.getDependSubsystems();
     String ourSubSystem = subSysMod.getSubSystem();
     if (moduleDependees.contains(ourSubSystem))
     ```
     
       </div>
     </details>
  
  9. **위치를 표시하는 주석**
  
     소스 파일에서 특정 위치를 표시하기 위해 주석 사용
  
     <details>
       <summary> code </summary>
       <div markdown="1">
     
     ```java
     // Actions /////////////////////////////////////////////
     ```
     
       </div>
     </details>
  
     너무 자주 사용하지 않는다면 눈에 띄며 주의를 환기한다. 그러므로 반드시 필요할 때만, 아주 드물게 사용하는 편이 좋다.
  
  10. **닫는 괄호에 다는 주석**
  
      중첩이 심하고 장황한 함수라면 의미가 있을지도 모르지만 작고 캡슐화면 함수에는 잡음일 뿐이다.
  
      그러므로 닫는 괄호에 주석을 달아야겠다는 생각이 든다면 대신에 함수를 줄이려 시도하자.
  
  11. **공로를 돌리거나 저자를 표시하는 주석**
  
      소스 코드 관리 시스템은 누가 언제 무엇을 추가했는지 귀신처럼 기억하므로, 저자 이름으로 코드를 오염시킬 필요가 없다.
  
  12. **주석으로 처리한 코드**
  
      주석으로 처리한 코드는 이유가 있어서 남겨놨을거라고, 중요하니까 지우면 안 된다고 생각하기 때문에 쓸모없는 코드임에도 지워지지 않기도 한다.
  
      소스코드 관리 시스템이 코드를 기억해주기 때문에 주석으로 처리할 필요 없이 삭제하는 것이 좋다.
  
  13. **HTML 주석**
  
      주석을 뽑아 웹 페이지에 올릴 거라면 주석에 HTML 태그를 삽입해야 하는 책임은 프로그래머가 아니라 도구가 져야한다.
  
      <details>
        <summary> code </summary>
        <div markdown="1">
      
      ```html
      /*
      <p/>
      <pre>
      용법 :
       ........
       </pre>
       */
      ```
      
        </div>
      </details>
  
  14. **전역 정보**
  
      주석을 달아야 한다면 근처에 있는 코드만 기술하라. 코드 일부에 주석을 달면서 시스템의 전반적인 정보를 기술하지 마라.
  
      <details>
        <summary> code </summary>
        <div markdown="1">
  
      ```java
      /**
       * 적합성 테스트가 동작하는 포트: 기본값은 <b>8082</b>.
       *
       * @param fitnessePort
       */
      public void setFitnessePort(int fitnessePort) {
        this.fitnewssePort = fitnessePort;
      }
      ```
  
        </div>
      </details>
  
  15. **너무 많은 정보**
  
      흥미로운 역사나 관련 없는 정보를 장황하게 늘어놓지 마라.
  
  16. **모호한 관계**
  
      주석과 주석이 설명하는 코드는 둘 사이 관계가 명백해야 한다.
  
      주석을 다는 목적은 코드만으로 설명이 부족해서다. 주석 자체가 다시 설명을 요구해서는 안된다.
  
  17. **함수헤더**
  
      짧고 한 가지만 수행하며 이름을 잘 붙인 함수가 주석으로 헤더를 추가한 함수보다 휠씬 좋다.
  
  18. **비공개 코드에서 Javadocs**
  
      공개 API는 Javadocs가 유용하지만 공개하지 않을 경우에는 쓸모가 없다.
  
      유용하지 않을 뿐만 아니라 Javadocs 주석이 요구하는 형식으로 인해 코드만 보기 싫고 산만해질 뿐이다.

### 📌 소감 및 생각

여러가지 많이 얻어갈 수 있는 단원이었다. 코드를 주석 처리하지 말고, 의무적으로 주석을 달지 말아야겠다. 특히 같은 이야기를 중복하는 주석에서 가장 많이 찔렸는데, 앞으로 개선해야겠다. 주석에 대해서는 크게 생각한 적이 없었는데, 앞으로는 주석도 신경써야겠다.

### 🔎 새롭게 배운 개념

- 쉰들러 리스트: 스티븐 스필버그 감독, 주인공 쉰들러가 유대인들을 안전한 곳으로 피신시키기 위해서 작성했다는 아홉 개의 명단이다.

[:arrow_up: 목차로 돌아가기](https://github.com/lisy0123/Nomadcoders/tree/main/Clean_Code#clean-code)

---

## 5. 형식 맞추기

> Day 11 (Feb 28, 2022)

### :book: 기억하고 싶은 책 내용

- **형식을 맞추는 목적**
- **적절한 행 길이를 유지하라**
  - **신문 기사처럼 작성하라**
  - **개념은 빈 행으로 분리하라**
  - **세로 밀집도**
  - **수직 거리**
  - **세로 순서**
- **가로 형식 맞추기**
  - **가로 공백과 밀집도**
  - **가로 정렬**
  - **들여쓰기**
  - **가짜 범위**
- **팀 규칙**
- **밥 아저씨의 형식 규칙**

### 📌 소감 및 생각

포맷팅을 지원해주는 툴을 이용하기 전에 스스로 형식을 맞추는 것이 중요하다고 생각한다. 형식이라는 기본적인 것에서 코드의 깔끔함이 나오는 것이라고 생각한다. 이번 챕터는 어느 정도 유의하고 중요하다고 생각하는 점이 있어 공감이 많이 갔다.

### 🔎 새롭게 배운 개념

- 

[:arrow_up: 목차로 돌아가기](https://github.com/lisy0123/Nomadcoders/tree/main/Clean_Code#clean-code)

---

## 6.객체와 자료 구조

> Day 12 (March 1, 2022)

### :book: 기억하고 싶은 책 내용

- **자료 추상화**
- **자료/객체 비대칭**
- **디미터 법칙**
  - **기차 충돌**
  - **잡종 구조**
  - **구조체 감추기**
- **자료 전달 객체**
  - **활성 레코드**
- **결론**

### 📌 소감 및 생각

개념을 정리하고 배우는 시간이었다. 클린 코드를 짜는 방법뿐만 아니라 기초 지식들을 확실하게 알고 넘어갈 수 있어서 좋았다. 

### 🔎 새롭게 배운 개념

- 

[:arrow_up: 목차로 돌아가기](https://github.com/lisy0123/Nomadcoders/tree/main/Clean_Code#clean-code)

---

## 7. 오류처리

> Day 14 (March 3, 2022)
>
> Day 15 (March 4, 2022)

### :book: 기억하고 싶은 책 내용

- 

### 📌 소감 및 생각



### 🔎 새롭게 배운 개념

- 

[:arrow_up: 목차로 돌아가기](https://github.com/lisy0123/Nomadcoders/tree/main/Clean_Code#clean-code)

---

## 8. 경계

> Day 16 (March 6, 2022)
>

### :book: 기억하고 싶은 책 내용

- 

### 📌 소감 및 생각



### 🔎 새롭게 배운 개념

- 

[:arrow_up: 목차로 돌아가기](https://github.com/lisy0123/Nomadcoders/tree/main/Clean_Code#clean-code)

---

## 9. 단위 테스트

> Day 17 (March 7, 2022)

### :book: 기억하고 싶은 책 내용

- 

### 📌 소감 및 생각



### 🔎 새롭게 배운 개념

- 

[:arrow_up: 목차로 돌아가기](https://github.com/lisy0123/Nomadcoders/tree/main/Clean_Code#clean-code)

---

## 10. 클래스

> Day 19 (March 9, 2022)
>
> Day 20 (March 10, 2022)

### :book: 기억하고 싶은 책 내용

- 

### 📌 소감 및 생각



### 🔎 새롭게 배운 개념

- 

[:arrow_up: 목차로 돌아가기](https://github.com/lisy0123/Nomadcoders/tree/main/Clean_Code#clean-code)

---

## Missions

|                           Mission                            | Topics                                                       |
| :----------------------------------------------------------: | ------------------------------------------------------------ |
| [Mission 01](https://github.com/lisy0123/Nomadcoders/blob/main/Clean_Code/mission01.md) | `Pick Top 3 Best TIL`                                        |
| [Mission 02](https://github.com/lisy0123/Nomadcoders/blob/main/Clean_Code/mission02.md) | `1. Use searchable names`<br />`2. Use meaningful and pronounceable variable names`<br />`3. Don't add unneeded context` |

[:arrow_up: 목차로 돌아가기](https://github.com/lisy0123/Nomadcoders/tree/main/Clean_Code#clean-code)

---

[↩️ Go Back](https://github.com/lisy0123/Nomadcoders)

