##���
### ����ʧ�ܺ��Զ��������У�pytest-rerunfailures��ʹ�÷�����
* ��װ�����pip install pytest-rerunfailures
* pytest test_x.py --reruns=n (ʧ�ܺ������еĴ���)
### �ظ����в��ԣ�pytest-repeat��ʹ�÷�����
  * ��װ�����pip install pytest-repeat
  pytest test_x.py --count=n (�ظ����еĴ���)
  ���߳�ִ�в�������pytest-xdist��ʹ�÷�����
��װ�����pip install pytest-xdist
pytest test_x.py -n [N, auto] (N��ָ�������Ľ�������auto���Զ����cpu����)
Ϊ��������ʱ�����ƣ�pytest-timeout��ʹ�÷�����
��װ�����pip install pytest-timeout
pytest test_x.py --timeout=n (ʱ�����ƣ���λ����)
����ʧ��ʱ������ʾ����Ķ�ջ������Ϣ��pytest-instafail��ʹ�÷�����
��װ�����pip install pytest-instafail
pytest test_x.py --instafail
��ʾɫ�ʺͽ�������Ҳ����ʾ����Ķ�ջ��Ϣ����pytest-sugar��ʹ�÷�����
��װ���������Ч��pip install pytest-sugar