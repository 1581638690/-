## Redis后台链接
- ./redis-cli -p 6379 -a password  链接Redis，端口可以修改
- 使用python连接redis
```python
# 导入redis
import redis
r = redis.Redis(host='127.0.0.1', port=6379, password='password')
```

## Redis常用命令之LIST操作
- lrange name start end  name为列表名 start为索引开始，end为索引结束
- llen name 查看name中元素数量个数
- lindex name index 获取name中index位置的元素