# django-wechat-pay
通过 Django, Django Rest Framework, [wechatpy](https://github.com/jxtech/wechatpy) 实现微信小程序端的支付功能

## 简要指南

### server 端
商户系统先调用该接口在微信支付服务后台生成预支付交易单，返回正确的预支付交易回话标识后再在APP里调起支付

克隆该项目到本地目录
```
cd django-wechat-pay/server/djangoWechat/
pip install -r requirements.txt
python3 manage.py runserver
```

#### 配置支付参数
配置文件路径：
django-wechat-pay/server/djangoWechat/djangoWechat/settings.py

```
# wechat config
WECHAT = {
        'APPID': 'appid',                                           # 小程序ID
        'APPSECRET': 'appsecret',			                        # 小程序SECRET
        'MCH_ID': 'mch_id',                                         # 商户号
        'TOTAL_FEE': '1',                                           # 总金额
        'SPBILL_CREATE_IP': '127.0.0.1',                            # 终端IP
        'NOTIFY_URL': 'http://127.0.0.1:8000/wxpayNotify',          # 通知地址
        'TRADE_TYPE': 'JSAPI',                                      # 交易类型
        'MERCHANT_KEY': 'merchant_key',                             # 商户KEY
        'BODY': '商品描述',                                           # 商品描述
}
```

#### 接口地址
    支付接口：http://127.0.0.1:8000/wxpay/
    通知接口：http://127.0.0.1:8000/wxpayNotify

### client 端
通过微信开发者工具新建项目，将 APPID 替换成你拥有权限的 APPID 进行测试及后续开发…

暂时只提供了基本的支付演示，server 端启动成功的前提下小程序载入编译后会立即调起支付接口，使用当前开发者的微信即可支付。

## 其他
该 demo 只做了简单的支付功能，现金红包、企业付款、订单查询、退款等有空再加上…

## ONE MORE THING...
![wechatpy QQ 群](https://raw.githubusercontent.com/mrhaoji/mrhaoji.github.com/master/IMG_1480.JPG)
   
