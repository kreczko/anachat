from slackbot.bot import respond_to


@respond_to(r'upload_cert')
def upload_cert(message):
    message.reply('uploading your grid certificate...')
    import time
    time.sleep(5)
    message.reply('... just kidding, do not know how to do that (yet)')
