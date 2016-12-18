import itchat
#import spider2
from itchat.content import TEXT
import threading
import time


@itchat.msg_register(itchat.content.TEXT)#, MAP, CARD, NOTE, SHARING])
def text_reply(msg):
    toUserName='filehelper'
    flag='stop'
    if msg['ToUserName']=='filehelper':
      if msg['Text']=='出现':
         flag='menue'
      if msg['Text']=='stop':
         flag='stop'
      while flag!='stop':
           #itchat.send('%s: %s' % ('pi', 'yes my lord'), toUserName)
           itchat.send('please select:\n1.{0}\n2.{1}\n3.{2}'.
                      format('download movies','play music','sth else'),toUserName)
           if msg['Text']==1:
               itchat.send('movie',toUserName)
               flag='stop'
           elif msg['Text']=='2':
               flag='stop'
               itchat.send('music',toUserName)
           elif msg['Text']=='3':
               itchat.send('else',toUserName)
               flag='stop'
           else:
               flag='stop'
def together():#模拟微信登录，并向邮箱发送验证码
  loops=[1,2]
  threads=[]
  nloops=range(len(loops))
  def lp(j,chose):
    if chose==1:
      itchat.auto_login(hotReload=True) #短期内重新登录不需要刷验证码
    else:
      time.sleep(3)

  for i in nloops:
    t=threading.Thread(target=lp,args=(i,loops[i]))
    threads.append(t)

  for i in nloops:
    threads[i].start()

  for i in nloops:
    threads[i].join()

#itchat.auto_login(hotReload=True) #短期内重新登录不需要刷验证码
#
user_info=itchat.search_friends() #获取本用户信息
itchat.run()
itchat.dump_login_status()
