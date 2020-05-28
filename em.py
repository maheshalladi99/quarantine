##import sys
##non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
###print(x.translate(non_bmp_map))
##print('This works in IDLE too! \U0001F44D'.translate(non_bmp_map))
##print('This works outside IDLE! \U0001F44D')
for tweet in public_tweets:
    print (tweet.text)
    u=tweet.text
    u=u.encode('unicode-escape').decode('utf-8')
