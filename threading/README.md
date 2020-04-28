首先调用c.next()启动生成器
然后，一旦生产了东西，通过c.send(n)切换到consumer执行
consumer通过yield拿到消息，处理，又通过yield把结果传回
produce拿到consumer处理的结果，继续生产下一条消息