#我的第一次作业

##git上传
* 绑定git
* 创建仓库
* 上传文件
##pytest

#fixture
* userfixture是由内到外执行
* 使用装饰器userfixture调用时拿不到调用函数的返回值，建议使用传函数形式调用
* outouse = true 默认所有用例调用
* fixture 可以内调用另一个fixture
* yield 在方法后执行；相当于return
  yield 需要返回的参数名
  结束代码
  yield之前代码显示执行并返回yield后的参数
  等测试代码执行完成后再执行yield的后面的代码
* scope 定义作用域
  scope=seasion 整个执行文件内执行一次
##conftest文件
* 数据共享文件，名字固定不能修改
* 可存放fixture,hook函数
* 就近生效（多个文件夹同时存在，按就近原则生效）



