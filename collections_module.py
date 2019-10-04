# The collections module contains some helpful data structures
# https://docs.python.org/3/library/collections.html#module-collections
import collections

# namedtuple() defines a subclass of tuple with named fields
Person = collections.namedtuple('person',('name','age','height'))
chaz = Person(name='Chaz', age='29', height='180cm')
print(chaz.age)

# can be unpacked like regular tuple
name, age, height = chaz

# defaultdict lets you set a default value or type which will be used when a key that doesn't exist is referenced
d = collections.defaultdict(int)
d['foo'] += 1
print(d['foo'])

# OrderedDict is a subclass of dict with additional methods for ordering or popping items
d = collections.OrderedDict({'apple':'fruit', 'carrot':'vegetable'})
print(d['apple'])
d.move_to_end('apple')
d.popitem()

# ChainMap stores a number of mappings in a list to operate like a single mapping
# mappings are searched successively and the first found value for a key is returned
baseline = {'music': 'bach', 'art': 'rembrandt'}
adjustments = {'art': 'van gogh', 'opera': 'carmen'}
print(list(collections.ChainMap(adjustments, baseline)))

# the value from adjustments is returned as it was the first mapping added to the ChainMap
print(collections.ChainMap(adjustments, baseline)['art'])

# Counter objects provide an easy way to tally items from an iterable
# items are stored as keys and counts as values
cnt = collections.Counter()
for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
    cnt[word] += 1
print(cnt)
