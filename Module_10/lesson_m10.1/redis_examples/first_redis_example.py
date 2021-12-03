import redis
import time


r = redis.StrictRedis(host='localhost', port=6380, db=0)

r.set('test1', 5)

# получаем из переменной test1 значение
print(r.get('test1'))

# уменьшаем значение test1 на 2 (если значение является int)
print(r.decr('test1', 2))  # выдаст 3

# увеличивает значение test1 на 2 (если значение является int)
print(r.incr('test1', 2))  # выдаст 5

# переменная test1 будет удалена через 30 секунд
r.expire('test1', 2)
time.sleep(3)
print(r.get('test1'))
# переменная test1 будет удалена

# сохранить все данные в памяти на диск
r.bgsave()


r.lpush('my_list', 'A')
print(f"my_list: {r.lrange('my_list', 0, -1)}")

# Добавить вторую строку в список справа
r.rpush('my_list', 'B')
print(f"my_list: {r.lrange('my_list', 0, -1)}")

# Вставить третью строку в список справа
r.rpush('my_list', 'C')
print(f"my_list: {r.lrange('my_list', 0, -1)}")

# Удалить из списка 1 экземпляр, значение которого "C"
r.lrem('my_list', 1, 'C')
print(f"my_list: {r.lrange('my_list', 0, -1)}")

# Вставить строку в наш список слева
r.lpush('my_list', 'C')
print(f"my_list: {r.lrange('my_list', 0, -1)}")

# Вытащить первый элемент нашего списка и переместить его в конец
r.rpush('my_list', r.lpop('my_list'))
print(f"my_list: {r.lrange('my_list', 0, -1)}")

# очистить всю выбраную базу
r.flushdb()
