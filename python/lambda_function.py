import os
import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, StickerSendMessage, QuickReply, QuickReplyButton, MessageAction, PostbackAction,
)
LINE_CHANNEL_ACCESS_TOKEN   = os.environ['LINE_CHANNEL_ACCESS_TOKEN']
LINE_CHANNEL_SECRET         = os.environ['LINE_CHANNEL_SECRET']
LINE_BOT_API = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
LINE_HANDLER = WebhookHandler(LINE_CHANNEL_SECRET)

def lambda_handler(event, context):
    logger.info(event)
    signature = event["headers"]["x-line-signature"]
    body = event["body"]

    @LINE_HANDLER.add(MessageEvent, message=TextMessage)
    def on_message(line_event):
        profile = LINE_BOT_API.get_profile(line_event.source.user_id)
        logger.info(profile)

        message = line_event.message.text.lower()
        if message == 'テスト':
            LINE_BOT_API.reply_message(line_event.reply_token,
                TextSendMessage(text=message))
        elif message == '筋肉':
            LINE_BOT_API.reply_message(line_event.reply_token,
                TextSendMessage(text='筋肉'))
        elif message == '筋トレ':
            LINE_BOT_API.reply_message(line_event.reply_token,
                TextSendMessage(text='どこでする？'))
        elif message == 'プロテイン':
            LINE_BOT_API.reply_message(line_event.reply_token, StickerSendMessage(package_id='8515',sticker_id='16581254'))
    
        else:
            LINE_BOT_API.reply_message(line_event.reply_token, StickerSendMessage(package_id='11537',sticker_id='52002744'))
            return


    LINE_HANDLER.handle(body, signature)
    return 0