## SSDB python链接
```python
import pyssdb
# 链接ssdb服务器
client = pyssdb.Client(host='localhost', port=8888)
```

## SSDB操作之字符串
- set key value 设置键值
- del key  删除键
- get key 获取键
- scan key_start,key_end limit # 查找处于区间[key_start,key_end]之间的键