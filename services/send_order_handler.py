import datetime
from whatsapp_api_client_python import API
from utils.logging import logger
from dotenv import load_dotenv
import os
import pytz
import json


def handle_new_order(request):
    order_data = request.get_json()
    logger.debug('Data received:\n' + json.dumps(order_data, indent=4))




def handle_send_order_by_whatsapp(new_order):
        # send the order using green-api
        # idInstance and apiTokenInstance from https://console.green-api.com/
        greenAPI = API.GreenAPI(
                os.getenv('GREENAPI_IDINSTANCE'), os.getenv('GREENAPI_APITOKENINSTANCE')
        )

        #load_dotenv()
        dst_phone_no =  "972" + os.getenv('DST_PHONE_NO')[1:] + "@c.us"

        # current timestamp
        timestamp_now = datetime.datetime.now(tz=pytz.timezone('Israel')).strftime('%d/%m/%Y %H:%M')
        
        # message first part
        hebrew_message = (timestamp_now
        + "\n\nשם הלקוח: {name}\nטלפון: {phoneNo}\nכתובת: {address}\n\n".format(
                name=new_order.customerName, phoneNo=new_order.phoneNo, address=new_order.address
                ))

        # concat each candleItem to first message part
        for candleItem in new_order.candleItems:
                hebrew_message = hebrew_message + "שם הנר: {candleName}\nכמות: {quantity}\nצבע: {color}\nריח: {smell}\nתיאור: {description}\nמחיר ליחידה: {price}\n\n".format(
                candleName=candleItem.candleName, quantity=candleItem.quantity, color=candleItem.color, smell=candleItem.smell, description=candleItem.description, price=candleItem.price
                )

        response = greenAPI.sending.sendMessage(dst_phone_no, hebrew_message)

        print(response.data)
        if response.code == 200:
                success_msg = "order sent successfully!"
                logger.debug(success_msg)
                return success_msg
        else:
                fail_msg = "failed to send order by whatsapp!"
                logger.debug(fail_msg)
                logger.debug(response.data)
                logger.debug(response.error)
                return fail_msg


        
        # english text for testing
        # message first part
        # message = (timestamp_now
        # + "\n\nClient name: {name}\nPhone: {phoneNo}\nAddress: {address}\n\n".format(
        #         name=new_order.customerName, phoneNo=new_order.phoneNo, address=new_order.address
        #         ))

        # # concat each candleItem to first message part
        # for candleItem in new_order.candleItems:
        #         message = message + "Candle name: {candleName}\nQuantity: {quantity}\nPrice: {price}\n\n".format(
        #         candleName=candleItem.candleName, quantity=candleItem.quantity, price=candleItem.price
        #         )