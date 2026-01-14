### 소스 코드 (LeetCode/Medium/0739-daily-temperatures/0739-daily-temperatures.py)

```python
class Solution:

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
# 1. 리스트는 앞부분 삽입, 제거는 한칸씩 밀으니 n임-> 큐에넣고, 하나씩 pop하면서 찾아가야하나
    # 아주 맨 끝에 답이 있을수있는경우 시간 초과(최악의 상황을 가정하지 못해서 놓친 포인트)
# 2. 중복제거해서, 정렬해 target이후보다 큰값들중 제일 작은 인덱스를 찾아보는 형식으로 가야겠다
    # 찾은후 삭제연산을 진행해도, 초반시점에서 정렬한 값보다 큰값에 대한 모든 인덱스를 일일히 살펴봐야하므로  N^2의 시간초과가 난다.
# 3. 스택을 활용하자 매순간 모든 데이터를 조사하는게 아니라 한번의 순회로 여러개를 처리하자.
    # 스택의 top에 마지막 날짜가 오도록 담아두고, 리스트를 순회해, 리스트의 요소가 높다면 반복적으로 pop과 함께 날짜 차이 계산
    #마지막 날이나 100도인 날이 본인의 답이 필요 없다고 해서 루프를 건너뛰어 버리면 그 날만 기다리던 과거의 데이터들을 구출해 줄 기회조차 사라짐
        answer = [0] * len(temperatures)
        notFindYet= deque()
        for i,current in enumerate(temperatures):
            while notFindYet and current>temperatures[notFindYet[-1]]:
                index= notFindYet.pop()
                answer[index]=i-index
            notFindYet.append(i)
        return answer
```


## [1단계] Python 알고리즘 분석 및 Java 변환

### 1. ⚔️ 접근 방식 및 복잡도 분석

- **팩트 체크:** `deque`를 스택으로 활용해 현재 온도보다 높은 온도가 나올 때까지 인덱스를 보관하는 방식은 아주 훌륭합니다. 이 방식은 각 원소가 스택에 한 번 들어갔다 한 번 나오기 때문에 **시간 복잡도 $O(N)$**으로 최적화된 풀이입니다. (브루트 포스 $O(N^2)$를 피한 점 칭찬합니다.)
- **개선점:** 사실 Python의 `list`는 내부적으로 동적 배열이라 스택(LIFO)으로 쓸 때는 `deque`보다 아주 미세하게 빠를 수 있습니다. 하지만 `deque`를 선택한 것 자체가 자료구조의 의도를 명확히 한 것이라 나쁘지 않습니다.

### 2. 🐍 Pythonic 클린 코드

- **Pythonic:** `notFindYet`이라는 변수명은 자바 스타일(camelCase)입니다. 파이썬에서는 `stack` 혹은 `pending_indices` 처럼 **snake_case**를 권장합니다.
- **Convention:** `while`문 안에서 `notFindYet[-1]`을 조회할 때, `deque`보다는 일반 `list`를 사용하는 것이 파이썬 커뮤니티에서는 더 일반적인 'Stack' 구현 방식입니다.

### 3. ☕ 실무용 모범 답안 (Modern Java 17+)

실무 스타일의 Java로 변환해 보겠습니다. Java에서는 `Stack` 클래스 대신 성능이 더 우수한 `ArrayDeque`를 사용합니다.

```Java
import java.util.ArrayDeque;
import java.util.Deque;

public class TemperatureService {
    /**
     * @param temperatures 일일 온도 배열
     * @return 다음 더 따뜻한 날까지의 대기 일수 배열
     */
    public int[] calculateWaitDays(int[] temperatures) {
        int n = temperatures.length;
        int[] answer = new int[n];
        //Java에서는 Stack 클래스보다 ArrayDeque가 훨씬 빠르고 권장됩니다.(LIFO 구조)
        Deque<Integer> stack = new ArrayDeque<>();
        for (int i = 0; i < n; i++) {
            int currentTemp = temperatures[i];
            // 스택이 비어있지 않고, 현재 온도가 스택 Top의 온도보다 높을 때까지 반복
            while (!stack.isEmpty() && currentTemp > temperatures[stack.peek()]) {
                int prevIndex = stack.pop();
                answer[prevIndex] = i - prevIndex;
            }
            stack.push(i);
        }
        return answer;
    }
}
```

> **💡 Java Point:**
>
> 1. **ArrayDeque:** Python의 `deque`와 유사하지만, Java의 `Stack` 클래스는 Thread-safe 성질 때문에 무겁습니다. 실무에선 `Deque` 인터페이스의 구현체인 `ArrayDeque`를 사용하세요.
>     
> 2. **Primitive Array:** 알고리즘 연산에서는 `List<Integer>`보다 `int[]`를 사용하는 것이 메모리 오버헤드를 줄이는 실무적인 선택입니다.

### 4. 🧠 CS 기본기 검증 (Interview Prep)

**Q1. Stack과 Queue의 차이점을 설명하고, 이 문제에서 Stack을 선택한 이유를 말씀해 주세요.**

- **A:** Stack은 LIFO(Last-In-First-Out) 구조이고, Queue는 FIFO(First-In-First-Out) 구조입니다. 이 문제에서는 **'가장 최근에 확인한 온도'**부터 차례대로 현재 온도와 비교해야 하므로, 마지막에 들어온 데이터를 먼저 꺼내는 Stack이 적합합니다.
 
**Q2. ArrayDeque와 LinkedList의 차이는 무엇이며, 왜 이 상황에서 ArrayDeque가 유리한가요?**

- **A:** `ArrayDeque`는 내부적으로 배열을 사용하여 인덱스 접근이 빠르고 캐시 지역성(Locality)이 좋습니다. 반면 `LinkedList`는 각 노드가 포인터로 연결되어 메모리 할당 오버헤드가 크고 성능이 떨어질 수 있습니다. 스택으로만 사용할 때는 `ArrayDeque`가 메모리 효율과 속도 면에서 압도적입니다.

---

**사수:** "자, 로직은 완벽하네. 근데 이게 만약 우리 회사의 **'실시간 전국 센서 온도 모니터링 시스템'**의 일부라고 생각하면 어떨까? 이 코드를 그대로 서버에 올리면 금방 문제가 생길 텐데…"

현업에 오신 걸 환영합니다. 코딩 테스트는 **'한 번의 실행(Process)'**으로 결과가 나오면 끝이지만, 실무는 **'수많은 요청이 24시간 흐르는 상태(Stream)'**입니다.

## [2단계] 🚨 신입 사원 업무 시뮬레이션 (Real World Engineering)

### 1. 🏢 업무 배경 파악 (Scenario Definition)

- **기능 요건:** **"스마트 팩토리 온도 이탈 알림 시스템"**
- **상세:** 수천 개의 센서에서 1초마다 온도 데이터를 보냅니다. 특정 시점의 온도보다 **더 높은 온도가 감지되는 순간**, "이전 저온 구간이 총 몇 초간 지속되었는지"를 계산해 대시보드에 뿌려주고 로그를 남겨야 합니다.

### 2. 💡 사수의 귓속말 (Gap Analysis: Algo vs Eng)

> **[Case D: 메모리 내 자료구조 사용 시] → 데이터 증발 및 정합성 파괴**
>
> "신입님, 지금 로직에서 `stack(notFindYet)`에 데이터를 쌓아두셨죠? 알고리즘 풀 땐 `answer` 배열에 쓱쓱 채우면 그만이지만, 이건 **실무 서버**입니다. 만약 센서 데이터 10만 개가 들어와서 '더 높은 온도'를 기다리며 스택에 머물고 있는데, **서버가 배포되거나 갑자기 재부팅되면 어떻게 될까요?**
>
> 메모리에 있던 `stack` 데이터는 **싹 다 날아갑니다.** 어떤 센서가 대기 중이었는지, 그전 온도가 몇이었는지 영원히 알 수 없게 되죠. 실무에선 이런 '상태(State)'를 서버 메모리에 두는 건 아주 위험한 발상입니다."

---
### 3. 🛠️ 기술적 의사결정 (Architecture & Stack)

이 문제를 해결하려면 서버가 꺼져도 안전하고, 여러 서버가 공유할 수 있는 **[옵션 2 - Caching Layer 위임]** 전략을 써야 합니다. **Redis**를 활용해 인메모리 스택을 외부로 분리하겠습니다.

**[Redis 기반 설계]**

- **Data Structure:** `Redis List` (Stack처럼 활용)
- **Key:** `sensor:pending:indices`
- Logic:
	1. 새로운 온도가 들어오면 Redis의 최상단(LINDEX) 데이터와 비교.
    1. 조건 만족 시 LPOP으로 꺼내고 결과 저장.
```Java
// Redis를 활용한 상태 유지 로직 (의사 코드)
public void processTemperature(String sensorId, double currentTemp) {
    String stackKey = "sensor:stack:" + sensorId;
    // 1. 스택의 Top 확인 (가장 최근 대기 데이터)
    String topData = redisTemplate.opsForList().index(stackKey, -1); 
    while (topData != null && currentTemp > parseTemp(topData)) {
        // 2. 조건 만족 시 Pop 하고 비즈니스 로직 처리
        String popped = redisTemplate.opsForList().rightPop(stackKey);
        long duration = calculateDuration(popped, currentTime);
        saveToDatabase(sensorId, duration); // 결과를 DB에 영구 저장
        // 다음 데이터 확인
        topData = redisTemplate.opsForList().index(stackKey, -1);
    }
    // 3. 현재 온도를 스택에 Push (다음 고온을 기다림)
    redisTemplate.opsForList().rightPush(stackKey, serialize(currentTemp, currentTime));
}
```

- opsForList(): List(순서가 있는 목록) 조작할때 `RedisTemplate`의 메서드
---

### 4. 🧪 촘촘한 예외 처리 (Production Readiness)

- **Redis 장애 대응:** Redis 연결이 끊기면 시스템 전체가 마비됩니다. 이럴 땐 **Local Cache(Caffeine)**에 임시 저장하거나, **Kafka** 같은 메시지 큐를 앞에 두어 재처리(Retry) 메커니즘을 갖춰야 합니다.
- **무한 대기 데이터:** 온도가 계속 떨어지기만 하면 Redis Stack에 데이터가 무한히 쌓입니다. **TTL(Time To Live)**을 설정하거나, 일정 기간이 지난 데이터는 '상승 없음'으로 간주하고 강제 종료하는 스케줄러가 필요합니다.

---

### 📝 퇴근 전 'Todo 리스트' (Dev Process)

1. **설계:** * Redis Key 컨벤션 확립 (`sensor:{id}:temp_stack`)
    
    - 결과 저장을 위한 `temperature_history` 테이블 인덱스 설계 (`sensor_id`, `created_at`)
        
2. **구현:** * Spring Data Redis를 활용한 `StackRepository` 구현
    
    - 온도 비교 로직 내 동시성 제어(분산 락 고려) 적용
        
3. **검증:** * 서버 강제 종료 후 다시 켰을 때 데이터가 이어서 처리되는지 확인
    
    - 초당 5,000건 이상의 트래픽에서 Redis 지연 시간(Latency) 측정

### [실무형 구현] Redis Stack & 분산 락 적용 코드

#### 1. 의존성 설정 (build.gradle)

실무에서는 Redis 순정 클라이언트보다 **Redisson**을 많이 써. 분산 락(Lock) 기능을 아주 편하게 제공하거든.

```Gradle
dependencies {
    implementation 'org.springframework.boot:spring-boot-starter-data-redis'
    implementation 'org.redisson:redisson-spring-boot-starter:3.23.1'
}
```

#### 2. 데이터 모델 (Record)

Java 16+부터 지원하는 `record`를 써서 불변 데이터를 정의하자.

```Java
public record TemperatureReading(double temperature, long timestamp) {}
```

#### 3. 온도 처리 서비스 (Core Logic)

여기가 핵심이야. **Redisson**을 활용해 특정 센서 ID별로 락을 걸고, Redis를 스택으로 사용해.

```Java
@Service
@RequiredArgsConstructor
@Slf4j
public class TemperatureService {
    private final RedissonClient redissonClient;
    private final StringRedisTemplate redisTemplate; // Redis 명령 실행기
    private final TemperatureRepository temperatureRepository; // DB 저장용
    private static final String STACK_KEY_PREFIX = "sensor:stack:";
    private static final String LOCK_KEY_PREFIX = "lock:sensor:";
    public void processSensorData(String sensorId, TemperatureReading current) {
        String lockKey = LOCK_KEY_PREFIX + sensorId;
        String stackKey = STACK_KEY_PREFIX + sensorId;
        // 1. 분산 락 획득 (최대 5초 대기, 10초 후 자동 해제)
        RLock lock = redissonClient.getLock(lockKey);
        try {
            if (lock.tryLock(5, 10, TimeUnit.SECONDS)) {
                // 2. Redis Stack에서 확인 (가장 최근 대기 데이터)
                while (true) {
                    // Python의 stack[-1]과 동일 (Redis의 오른쪽 끝 데이터 조회)
                    String topJson = redisTemplate.opsForList().index(stackKey, -1);
                    if (topJson == null) break;
                    TemperatureReading prev = deserialize(topJson);
                    
                    // 현재 온도가 더 높다면? (알고리즘 조건 만족)
                    if (current.temperature() > prev.temperature()) {
                        redisTemplate.opsForList().rightPop(stackKey); // Pop
                        saveResultToDb(sensorId, prev, current); // 결과 기록
                    } else {
                        break;
                    }
                }
                // 3. 현재 온도를 다음 상승 시점을 위해 Push
                redisTemplate.opsForList().rightPush(stackKey, serialize(current));
            }
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
            log.error("락 획득 중 인터럽트 발생", e);
        } finally {
            // 4. 반드시 락 해제
            if (lock.isHeldByCurrentThread()) {
                lock.unlock();
            }
        }
    }
    private void saveResultToDb(String sensorId, TemperatureReading prev, TemperatureReading current) {
        long duration = current.timestamp() - prev.timestamp();
        // 실제 DB(JPA 등)에 저장하는 로직
        log.info("센서 {} : {}초 만에 온도 상승 감지!", sensorId, duration);
    }
}
```

---

### 💡 사수의 추가 코멘트 (Code Review)

1. 왜 분산 락(RLock)을 썼을까?
	서버가 3대라고 해보자. 센서 A의 데이터가 거의 동시에 2번 들어왔을 때, 서버 1과 서버 2가 동시에 Redis Stack을 읽으면 같은 데이터를 두 번 Pop 하거나, 정합성이 깨질 수 있어. redissonClient.getLock(sensorId)는 해당 센서에 대해 한 번에 하나의 서버만 작업하도록 보장해 주지.
2. Serialization(직렬화)의 중요성
	Python은 객체를 대충 담아도 되지만, Java는 Redis에 저장할 때 String이나 Byte로 변환해야 해. 보통 Jackson 라이브러리를 써서 JSON으로 변환해 저장하는 게 나중에 디버깅(Redis-cli로 확인)하기 편해.
3. DB 인덱스 설계의 이유
	temperature_history 테이블에 (sensor_id, created_at) 복합 인덱스를 걸라고 한 건, 나중에 특정 센서의 시간대별 온도 변화 통계를 뽑을 때 쿼리 성능을 $O(N)$에서 $O(\log N)$으로 줄이기 위해서야.
