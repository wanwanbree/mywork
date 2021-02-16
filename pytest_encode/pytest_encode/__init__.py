# -- coding: utf-8 --
# @ModuleName:__init__.py
# @Author:wanwan
# @Time:2021/2/14 15:27
# -- coding: utf-8 --
# @ModuleName:conftest.py
# @Author:wanwan
# @Time:2021/2/10 14:30
''
from typing import List
import pytest

def pytest_collection_modifyitems(session: "Session",config: "Config",items: List["Item"]
                                  )->None:
    for itme in items:
        itme.name = itme.name.encode('utf-8').decode('unicode-escape')
        itme._nodeid = itme.nodeid.encode('utf-8').decode('unicode-escape')
        if 'add'in itme._nodeid:
            itme.add_marker(pytest.mark.add)