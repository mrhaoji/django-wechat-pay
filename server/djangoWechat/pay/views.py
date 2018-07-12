from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import HttpResponse, JsonResponse
import requests
import json
from django.conf import settings
from wechatpy.pay import WeChatPay

def get_user_info(js_code):
    """
    使用 临时登录凭证code 获取 session_key 和 openid 等
    支付部分仅需 openid，如需其他用户信息请按微信官方开发文档自行解密
    """
    req_params = {
        'appid': settings.WECHAT['APPID'],
        'secret': settings.WECHAT['APPSECRET'],
        'js_code': js_code,
        'grant_type': 'authorization_code',
    }
    user_info = requests.get('https://api.weixin.qq.com/sns/jscode2session', 
                              params=req_params, timeout=3, verify=False)
    return user_info.json()

@api_view(['GET', 'POST'])
def wxpay(request):
    """
    通过小程序前端 wx.login() 接口获取临时登录凭证 code
    将 code 作为参数传入，调用 get_user_info() 方法获取 openid
    """
    code = request.GET.get("code", None)
    openid = get_user_info(code)['openid']
    
    pay = WeChatPay(settings.WECHAT['APPID'], settings.WECHAT['MERCHANT_KEY'], settings.WECHAT['MCH_ID'])
    order = pay.order.create(
        trade_type = settings.WECHAT['TRADE_TYPE'],     # 交易类型，小程序取值：JSAPI
        body = settings.WECHAT['BODY'],                 # 商品描述，商品简单描述
        total_fee = settings.WECHAT['TOTAL_FEE'],       # 标价金额，订单总金额，单位为分
        notify_url = settings.WECHAT['NOTIFY_URL'],     # 通知地址，异步接收微信支付结果通知的回调地址，通知url必须为外网可访问的url，不能携带参数。
        user_id = openid                                # 用户标识，trade_type=JSAPI，此参数必传，用户在商户appid下的唯一标识。
    )
    wxpay_params = pay.jsapi.get_jsapi_params(order['prepay_id'])
    
    return HttpResponse(json.dumps(wxpay_params))

@api_view(['GET', 'POST'])
def wxpayNotify(request):
    _xml = request.body
    #拿到微信发送的xml请求 即微信支付后的回调内容
    xml = str(_xml, encoding="utf-8")
    print("xml", xml)
    return_dict = {}
    tree = et.fromstring(xml)
    #xml 解析
    return_code = tree.find("return_code").text
    try:
        if return_code == 'FAIL':
            # 官方发出错误
            return_dict['message'] = '支付失败'
            #return Response(return_dict, status=status.HTTP_400_BAD_REQUEST)
        elif return_code == 'SUCCESS':
        #拿到自己这次支付的 out_trade_no 
            _out_trade_no = tree.find("out_trade_no").text
                #这里省略了 拿到订单号后的操作 看自己的业务需求
    except Exception as e:
        pass
    finally:
        return HttpResponse(return_dict, status=status.HTTP_200_OK)