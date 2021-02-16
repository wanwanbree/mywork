##插件
### 用例失败后自动重新运行：pytest-rerunfailures，使用方法：
* 安装插件：pip install pytest-rerunfailures
* pytest test_x.py --reruns=n (失败后重运行的次数)
### 重复运行测试：pytest-repeat，使用方法：
  * 安装插件：pip install pytest-repeat
  pytest test_x.py --count=n (重复运行的次数)
  多线程执行测试任务：pytest-xdist，使用方法：
安装插件：pip install pytest-xdist
pytest test_x.py -n [N, auto] (N：指定并发的进程数，auto：自动检测cpu数量)
为测试设置时间限制：pytest-timeout，使用方法：
安装插件：pip install pytest-timeout
pytest test_x.py --timeout=n (时间限制，单位：秒)
用例失败时立刻显示错误的堆栈回溯信息：pytest-instafail，使用方法：
安装插件：pip install pytest-instafail
pytest test_x.py --instafail
显示色彩和进度条（也能显示错误的堆栈信息）：pytest-sugar，使用方法：
安装插件即可生效：pip install pytest-sugar