::

      ___       __   _______   ________  ___  ___  ________  _________  ________  ___    ___ 
     |\  \     |\  \|\  ___ \ |\   ____\|\  \|\  \|\   __  \|\___   ___\\   __  \|\  \  /  /|
     \ \  \    \ \  \ \   __/|\ \  \___|\ \  \\\  \ \  \|\  \|___ \  \_\ \  \|\  \ \  \/  / /
      \ \  \  __\ \  \ \  \_|/_\ \  \    \ \   __  \ \   __  \   \ \  \ \ \   ____\ \    / / 
       \ \  \|\__\_\  \ \  \_|\ \ \  \____\ \  \ \  \ \  \ \  \   \ \  \ \ \  \___|\/  /  /  
        \ \____________\ \_______\ \_______\ \__\ \__\ \__\ \__\   \ \__\ \ \__\ __/  / /    
         \|____________|\|_______|\|_______|\|__|\|__|\|__|\|__|    \|__|  \|__||\___/ /     
                                                                                \|___|/      

|Build Status| |Build status| |codecov.io| |Scrutinizer Code Quality|
|PyPI| |FOSSA Status|

微信(WeChat) 公众平台第三方 Python SDK。

`【阅读文档】 <http://wechatpy.readthedocs.org/zh_CN/master/>`__
`【快速入门】 <http://wechatpy.readthedocs.org/zh_CN/master/quickstart.html>`__

|Join the chat at https://gitter.im/messense/wechatpy|

功能特性
--------

1. 普通公众平台被动响应和主动调用 API
2. 企业号公众平台被动响应和主动调用 API
3. 微信支付 API

安装
----

从 0.8.0 版本开始，wechatpy 消息加解密同时兼容
`cryptography <https://github.com/pyca/cryptography>`__ 和
`PyCrypto <https://github.com/dlitz/pycrypto>`__, 优先使用 cryptography
库。因而不再强制依赖 PyCrypto 库。可先自行安装 cryptography 或者
PyCrypto 库：

.. code:: bash

    # 安装 cryptography
    pip install cryptography>=0.8.2
    # 或者安装 PyCrypto
    pip install pycrypto>=2.6.1

    Tips: Windows 用户请先安装 PyCrypto 的二进制包后再使用 pip 安装
    wechatpy 。 PyCrypto Windows
    的二进制包可以在\ `这里 <http://www.voidspace.org.uk/python/modules.shtml#pycrypto>`__\ 下载。

推荐使用 pip 进行安装:

.. code:: bash

    pip install wechatpy
    # with cryptography
    pip install wechatpy[cryptography]
    # with pycrypto
    pip install wechatpy[pycrypto]

升级版本：

::

    pip install -U wechatpy

使用示例
--------

使用示例参见 `examples <examples/>`__

贡献代码
--------

请阅读 `贡献代码指南 <.github/CONTRIBUTING.md>`__

问题反馈
--------

我们主要使用 `GitHub
issues <https://github.com/jxtech/wechatpy/issues>`__
进行问题追踪和反馈。

QQ 群：176596300

.. figure:: docs/_static/images/qq-group.png
   :alt: wechatpy QQ 群

   wechatpy QQ 群
License
-------

This work is released under the MIT license. A copy of the license is
provided in the `LICENSE <./LICENSE>`__ file.

|FOSSA Status|

.. |Build Status| image:: https://travis-ci.org/jxtech/wechatpy.svg?branch=master
   :target: https://travis-ci.org/jxtech/wechatpy
.. |Build status| image:: https://ci.appveyor.com/api/projects/status/sluy95tvbe090af1/branch/master?svg=true
   :target: https://ci.appveyor.com/project/messense/wechatpy-den93/branch/master
.. |codecov.io| image:: http://codecov.io/github/jxtech/wechatpy/coverage.svg?branch=master
   :target: http://codecov.io/github/jxtech/wechatpy?branch=master
.. |Scrutinizer Code Quality| image:: https://scrutinizer-ci.com/g/jxtech/wechatpy/badges/quality-score.png?b=master
   :target: https://scrutinizer-ci.com/g/jxtech/wechatpy/?branch=master
.. |PyPI| image:: https://img.shields.io/pypi/v/wechatpy.svg
   :target: https://pypi.python.org/pypi/wechatpy
.. |FOSSA Status| image:: https://app.fossa.io/api/projects/git%2Bgithub.com%2Fjxtech%2Fwechatpy.svg?type=shield
   :target: https://app.fossa.io/projects/git%2Bgithub.com%2Fjxtech%2Fwechatpy?ref=badge_shield
.. |Join the chat at https://gitter.im/messense/wechatpy| image:: https://badges.gitter.im/Join%20Chat.svg
   :target: https://gitter.im/messense/wechatpy?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge
.. |FOSSA Status| image:: https://app.fossa.io/api/projects/git%2Bgithub.com%2Fjxtech%2Fwechatpy.svg?type=large
   :target: https://app.fossa.io/projects/git%2Bgithub.com%2Fjxtech%2Fwechatpy?ref=badge_large


