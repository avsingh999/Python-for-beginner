# 컬렉션 모듈에는 유용한 데이터 구조가 포함되있습니다.
# https://docs.python.org/3/library/collections.html#module-collections
import collections

# namedtuple() 은 fields라고 이름붙여진 하위클래스의 튜플을 정의합니다.
Person = collections.namedtuple('person',('name','age','height'))
chaz = Person(name='Chaz', age='29', height='180cm')
print(chaz.age)

# 일반튜플처럼 풀릴수 있습니다.
name, age, height = chaz

# defaultdict을 사용하면 사용하면 존재하지 않는 키가 참조될 때 사용할 기본값 또는 타입을 설정할 수 있습니다.
d = collections.defaultdict(int)
d['foo'] += 1
print(d['foo'])

# OrderedDict는 항목을 주문하거나 pop하기 위한 추가 메소드가있는 dict의 서브 클래스입니다.
d = collections.OrderedDict({'apple':'fruit', 'carrot':'vegetable'})
print(d['apple'])
d.move_to_end('apple')
d.popitem()

# ChainMap은 단일 맵핑처럼 작동하기 위해 많은 맵핑을 목록에 저장합니다.
# 매핑이 연속적으로 검색되고 키의 첫 번째 검색 값이 반환됩니다.
baseline = {'music': 'bach', 'art': 'rembrandt'}
adjustments = {'art': 'van gogh', 'opera': 'carmen'}
print(list(collections.ChainMap(adjustments, baseline)))

# adjustments의 값은 ChainMap에 추가된 첫 번째 매핑이기 때문에 반환된다.
print(collections.ChainMap(adjustments, baseline)['art'])

# Counters 객체는 iterable을 통해서 항목을 쉽게 집계 할 수있는 방법을 제공합니다.
# 항목은 키로 저장되고 값으로 계산됩니다
cnt = collections.Counter()
for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
    cnt[word] += 1
print(cnt)
