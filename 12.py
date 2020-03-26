# -*- coding: utf-8 -*- 
import KIA
from KIA import *
from akad.ttypes import *
from thrift.unverting import *
from thrift.TMultiplexedProcessor import *
from thrift.TSerialization import *
from thrift.TRecursive import *
from thrift import transport, protocol, server
from multiprocessing import Pool, Process
from humanfriendly import format_timespan, format_size, format_number, format_length
from time import sleep
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib.request, urllib.parse, urllib.error, urllib.parse
from datetime import timedelta, date
from datetime import datetime
from gtts import gTTS
import html5lib,shutil
import wikipedia,goslate
import ffmpy
from bs4 import BeautifulSoup
from googletrans import Translator
import youtube_dl
#SEMOGA BERMANFAAT,,,TEGUH S..
#=============
cl = LineClient("06555mai@gmail.com","mai06555mai")
cl.log("Auth Token : " + str(cl.authToken))
channel = LineChannel(cl)
cl.log("Channel Access Token : " + str(channel.channelAccessToken))

ki = LineClient("kqm46169@zzrgg.com","mai06555mai")
ki.log("Auth Token : " + str(ki.authToken))
channel1 = LineChannel(ki)
ki.log("Channel Access Token : " + str(channel1.channelAccessToken))

kk = LineClient("aoj83430@bcaoo.com","mai06555mai")
kk.log("Auth Token : " + str(kk.authToken))
channel2 = LineChannel(kk)
kk.log("Channel Access Token : " + str(channel2.channelAccessToken))

kc = LineClient("rxa09671@eoopy.com","mai06555mai")
kc.log("Auth Token : " + str(kc.authToken))
channel3 = LineChannel(kc)
kc.log("Channel Access Token : " + str(channel3.channelAccessToken))


km = LineClient("zii43214@eoopy.com","mai06555mai")
km.log("Auth Token : " + str(km.authToken))
channel4 = LineChannel(km)
km.log("Channel Access Token : " + str(channel4.channelAccessToken))


kb = LineClient("fjr17555@zzrgg.com","mai06555mai")
kb.log("Auth Token : " + str(kb.authToken))
channel5 = LineChannel(kb)
kb.log("Channel Access Token : " + str(channel5.channelAccessToken))


kn = LineClient("oiu99345@bcaoo.com","mai06555mai")
kn.log("Auth Token : " + str(kn.authToken))
channel6 = LineChannel(kn)
kn.log("Channel Access Token : " + str(channel6.channelAccessToken))


ko = LineClient("bzf97835@bcaoo.com","mai06555mai")
ko.log("Auth Token : " + str(ko.authToken))
channel7 = LineChannel(ko)
ko.log("Channel Access Token : " + str(channel7.channelAccessToken))


kw = LineClient("rye61111@bcaoo.com","mai06555mai")
kw.log("Auth Token : " + str(kw.authToken))
channel8 = LineChannel(kw)
kw.log("Channel Access Token : " + str(channel8.channelAccessToken))


ke = LineClient("piu45560@bcaoo.com","mai06555mai")
ke.log("Auth Token : " + str(ke.authToken))
channel9 = LineChannel(ke)
ke.log("Channel Access Token : " + str(channel9.channelAccessToken))

ky = LineClient("ctc88352@bcaoo.com","mai06555mai")
ky.log("Auth Token : " + str(ky.authToken))
channel10 = LineChannel(ky)
ky.log("Channel Access Token : " + str(channel10.channelAccessToken))


sw = LineClient("vgc03839@zzrgg.com","mai06555mai")
sw.log("Auth Token : " + str(sw.authToken))
channel11 = LineChannel(sw)
sw.log("Channel Access Token : " + str(channel11.channelAccessToken))


print("---LOGIN SUCCES---\n mai")

poll = LinePoll(cl)
call = cl
creator = ["uc66e45201d1612eb4ce7b3a86bac4685"]
owner = ["uc66e45201d1612eb4ce7b3a86bac4685"]
admin = ["uc66e45201d1612eb4ce7b3a86bac4685"]
staff = ["uc66e45201d1612eb4ce7b3a86bac4685"]
mid = cl.getProfile().mid
Amid = ki.getProfile().mid
Bmid = kk.getProfile().mid
Cmid = kc.getProfile().mid
Dmid = km.getProfile().mid
Emid = kb.getProfile().mid
Fmid = kn.getProfile().mid
Gmid = ko.getProfile().mid
Hmid = kw.getProfile().mid
Imid = ke.getProfile().mid
Jmid = ky.getProfile().mid
Zmid = sw.getProfile().mid
KAC = [ki,kk,kc,km,kb,kn,ko,kw,ke,ky]
ABC = [ki,kk,kc,km,kb,kn,ko,kw,ke,ky,sw]
Bots = [mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid,Zmid]
Ghost = [sw]
Dpk = admin + staff

protectqr = []
protectkick = []
protectjoin = []
protectinvite = []
protectcancel = []
protectantijs = []
ghost = []
welcome = []

responsename1 = ki.getProfile().displayName
responsename2 = kk.getProfile().displayName
responsename3 = kc.getProfile().displayName
responsename4 = km.getProfile().displayName
responsename5 = kb.getProfile().displayName
responsename6 = kn.getProfile().displayName
responsename7 = ko.getProfile().displayName
responsename8 = kw.getProfile().displayName
responsename9 = ke.getProfile().displayName
responsename10 = ky.getProfile().displayName

settings = {
    "Picture":False,
    "group":{},
    "groupPicture":False,
    "changePicture":False,
    "autoJoinTicket":True,
    "userAgent": [
        "Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
        "Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0"
    ]
}

wait = {
    "limit": 5,
    "owner":{},
    "admin":{},
    "addadmin":False,
    "delladmin":False,
    "staff":{},
    "addstaff":False,
    "dellstaff":False,
    "bots":{},
    "addbots":False,
    "dellbots":False,
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "Talkblacklist":{},
    "Talkwblacklist":False,
    "Talkdblacklist":False,
    "talkban":True,
    "contact":False,
    'autoJoin':True,
    'autoBlock':False,
    'autoAdd':True,
    'autoRead':False,
    'autoLeave':False,
    'autoLeave1':False,
    "detectMention":False,
    "Mentionkick":False,
    "welcomeOn":False,
    "sticker":False,
    "selfbot":True,
    "protectantijsOn":True,
    "ghostOn":True,
    "mention":"╰☆ Massage Reader Cought☆╮ 😊",
    "Respontag":"╚»★★«╝",
    "welcome":"wєlcσmє",
    "comment":"ไลค์ให้แล้วนะ",
    "message":"ออโต้บล็อค กรุนารอผมมาปลดบล็อค",
}

read = {
    "readPoint":{},
    "readMember":{},
    "readTime":{},
    "ROM":{},
}

cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

with open('creator.json', 'r') as fp:
    creator = json.load(fp)
with open('owner.json', 'r') as fp:
    owner = json.load(fp)

Setbot = codecs.open("setting.json","r","utf-8")
Setmain = json.load(Setbot)

mulai = time.time()

tz = pytz.timezone("Asia/Jakarta")
timeNow = datetime.now(tz=tz)

def restart_program(): 
    python = sys.executable
    os.execl(python, python, * sys.argv)

def restartBot():
    python = sys.executable
    os.execl(python, python, *sys.argv)

def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)

def runtime(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)

def mentionMembers(to, mid):
    try:
        arrData = ""
        textx = "⁑ℓιѕт⁑「{}」\n\n \n1. ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def siderMembers(to, mid):
    try:
        arrData = ""
        textx = "Hallo ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["mention"]
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def welcomeMembers(to, mid):
    try:
        arrData = ""
        textx = "Hallo  ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = cl.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["welcome"]+"\nNama grup : "+str(ginfo.name)
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMention(to, mid, firstmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x \n"
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        today = datetime.today()
        future = datetime(2018,3,1)
        hari = (str(future - today))
        comma = hari.find(",")
        hari = hari[:comma]
        teman = cl.getAllContactIds()
        gid = cl.getGroupIdsJoined()
        tz = pytz.timezone("Asia/Jakarta")
        timeNow = datetime.now(tz=tz)
        eltime = time.time() - mulai
        bot = runtime(eltime)
        text += mention+"◐ Jam : "+datetime.strftime(timeNow,'%H:%M:%S')+" Wib\n◐ Group : "+str(len(gid))+"\n◐ Teman : "+str(len(teman))+"\n◐ Expired : In "+hari+"\n◐ Version : MAI\n◐ Tanggal : "+datetime.strftime(timeNow,'%Y-%m-%d')+"\n◐ Runtime : \n • "+bot
        cl.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def command(text):
    pesan = text.lower()
    if pesan.startswith(Setmain["keyCommand"]):
        cmd = pesan.replace(Setmain["keyCommand"],"")
    else:
        cmd = "command"
    return cmd

def help():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage = "▬▬▬▬*****▬▬▬▬\n" + \
                  "╔═[ คำสั่งรวม ]\n"+\
                  "║☈ " + key + "H\n" + \
                  "║☈ " + key + "Hb\n" + \
                  "║☈ " + key + "Hg\n" + \
                  "║☈ " + key + "ดึงคิก\n" + \
                  "║☈ " + key + "b\n" + \
                  "║☈ " + key + "in\n" + \
                  "║☈ " + key + "out\n" + \
                  "║☈ " + key + "ผีมา\n" + \
                  "║☈ " + key + "ผีออก\n" + \
                  "║☈ " + key + "Ginfo\n" + \
                  "║☈ " + key + "เปิดลิ้ง\n" + \
                  "║☈ " + key + "ปิดลิ้ง\n" + \
                  "║☈ " + key + "ลิ้ง\n" + \
                  "║☈ " + key + "รายชื่อกลุ่ม\n" + \
                  "╠══[ protect ]\n" + \
                  "║🛡☈ " + key + "Notag「on/off」\n" + \
                  "║🛡☈ " + key + "Allpro「on/off」\n" + \
                  "║🛡☈ " + key + "Protecturl「on/off」\n" + \
                  "║🛡☈ " + key + "Protectjoin「on/off」\n" + \
                  "║🛡☈ " + key + "Protectkick「on/off」\n" + \
                  "║🛡☈ " + key + "Protectinvite「on/off」\n" + \
                  "║🛡☈ " + key + "Protectcancel「on/off」\n" + \
                  "║🛡☈ " + key + "js「on/off」\n" + \
                  "║🛡☈ " + key + "ผี「on/off」\n" + \
                  "╠══[ Set kicker ]\n" + \
                  "║☈ " + key + "Gk「@」\n" + \
                  "║☈ " + key + "Bk「@」\n" + \
                  "║☈ " + key + "/mai *คำสั่งบินกลุ่ม\n" + \
                  "╠══[ Set user ]\n" + \
                  "║☈ " + key + "Invite「on/off」\n" + \
                  "║☈ " + key + "Unsend「on/off」\n" + \
                  "║☈ " + key + "Timeline「on/off」\n" + \
                  "║☈ " + key + "Contact「on/off」\n" + \
                  "║☈ " + key + "join「on/off」\n" + \
                  "║☈ " + key + "Autoadd「on/off」\n" + \
                  "║☈ " + key + "Welcome「on/off」\n" + \
                  "║☈ " + key + "Autoleave「on/off」\n" + \
                  "║☈ " + key + "มุดลิ้ง「on/off」\n" + \
                  "╠══[ Set Admin ]\n" + \
                  "║☈ " + key + "บอทแอด「@」\n" + \
                  "║☈ " + key + "บอทลบ「@」\n" + \
                  "║☈ " + key + "ตั้งสตาฟ「@」\n" + \
                  "║☈ " + key + "ลบสตาฟ「@」\n" + \
                  "║☈ " + key + "ตั้งแอดมิน「@」\n" + \
                  "║☈ " + key + "ลบแอดมิน「@」\n" + \
                  "║☈ " + key + "Refresh\n" + \
                  "║☈ " + key + "รายชื่อบอท\n" + \
                  "║☈ " + key + "รายชื่อแอดมิน\n" + \
                  "║☈ " + key + "set2\n" + \
                  "╚═[ SELFBOT ]\n" + \
                  "▬▬▬▬*****▬▬▬▬\n" + \
                  "\nคำสั่งรวม\n"
    return helpMessage

def helpbot():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage1 = "▬▬▬▬*****▬▬▬▬\n" + \
                  "╔═[ Help blacklist ]\n"+\
                  "║☈ " + key + "Bc\n" + \
                  "║☈ " + key + "Ban:on\n" + \
                  "║☈ " + key + "Unban:on\n" + \
                  "║☈ " + key + "Ban「@」\n" + \
                  "║☈ " + key + "Unban「@」\n" + \
                  "║☈ " + key + "ดำ「@」\n" + \
                  "║☈ " + key + "ขาว「@」\n" + \
                  "║☈ " + key + "Talkban:on\n" + \
                  "║☈ " + key + "Untalkban:on\n" + \
                  "║☈ " + key + "รายชื่อดำ\n" + \
                  "║☈ " + key + "Talkbanlist\n" + \
                  "║☈ " + key + "Cb\n" + \
                  "║☈ " + key + "Refresh\n" + \
                  "╠══[ Help bot ]\n" + \
                  "║☈ " + key + "A1\n" + \
                  "║☈ " + key + "A2\n" + \
                  "║☈ " + key + "A3\n" + \
                  "║☈ " + key + "A4\n" + \
                  "║☈ " + key + "A5\n" + \
                  "║☈ " + key + "A6\n" + \
                  "║☈ " + key + "A7\n" + \
                  "║☈ " + key + "A8\n" + \
                  "║☈ " + key + "A9\n" + \
                  "║☈ " + key + "A10\n" + \
                  "╠══[ Help update ]\n" + \
                  "║☈ " + key + "Up\n" + \
                  "║☈ " + key + "1up\n" + \
                  "║☈ " + key + "2up\n" + \
                  "║☈ " + key + "3up\n" + \
                  "║☈ " + key + "4up\n" + \
                  "║☈ " + key + "5up\n" + \
                  "║☈ " + key + "6up\n" + \
                  "║☈ " + key + "7up\n" + \
                  "║☈ " + key + "8up\n" + \
                  "║☈ " + key + "9up\n" + \
                  "║☈ " + key + "10up\n" + \
                  "║☈ " + key + "gup\n" + \
                  "║☈ " + key + "ชื่อ:「Name」\n" + \
                  "║☈ " + key + "ชื่อ1:「Name」\n" + \
                  "║☈ " + key + "ชื่อ2:「Name」\n" + \
                  "║☈ " + key + "ชื่อ3:「Name」\n" + \
                  "║☈ " + key + "ชื่อ4:「Name」\n" + \
                  "║☈ " + key + "ชื่อ5:「Name」\n" + \
                  "║☈ " + key + "ชื่อ6:「Name」\n" + \
                  "║☈ " + key + "ชื่อ7:「Name」\n" + \
                  "║☈ " + key + "ชื่อ8:「Name」\n" + \
                  "║☈ " + key + "ชื่อ9:「Name」\n" + \
                  "║☈ " + key + "ชื่อ10:「Name」\n" + \
                  "║☈ " + key + "ชื่อผี:「Name」\n" + \
                  "╠══[ Cek Seting ]\n" + \
                  "║☈ " + key + "Cek sider\n" + \
                  "║☈ " + key + "Cek spam\n" + \
                  "║☈ " + key + "Cek pesan \n" + \
                  "║☈ " + key + "Cek respon \n" + \
                  "║☈ " + key + "Cek leave\n" + \
                  "║☈ " + key + "Cek welcome\n" + \
                  "║☈ " + key + "Set sider:「Text」\n" + \
                  "║☈ " + key + "Set spam:「Text」\n" + \
                  "║☈ " + key + "Set pesan:「Text」\n" + \
                  "║☈ " + key + "Set respon:「Text」\n" + \
                  "║☈ " + key + "Set leave:「Text」\n" + \
                  "║☈ " + key + "Set welcome:「Text」\n" + \
                  "║☈ " + key + "Gif:「Mid korban」「Jumlah」\n" + \
                  "║☈ " + key + "Spam:「Mid korban」「Jumlah」\n" + \
                  "╚═[ SELFBOT]\n" + \
                  "▬▬▬▬ஜ۩۞۩ஜ▬▬▬▬\n" + \
                  "\nคำสั่งบอท\n"
    return helpMessage1

def helpgroup():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage2 = "▬▬▬▬****▬▬▬▬\n" + \
                  "╔═[ Help Group ]\n"+\
                  "║☈ " + key + "มี\n" + \
                  "║☈ " + key + "มิด「@」\n" + \
                  "║☈ " + key + "ตัส「@」\n" + \
                  "║☈ " + key + "Gk「@」\n" + \
                  "║☈ " + key + "Bk「@」\n" + \
                  "║☈ " + key + "in\n" + \
                  "║☈ " + key + "out\n" + \
                  "║☈ " + key + "Set2\n" + \
                  "║☈ " + key + "About\n" + \
                  "║☈ " + key + "รี\n" + \
                  "║☈ " + key + "b\n" + \
                  "║☈ " + key + "Creator\n" + \
                  "║☈ " + key + "Spb\n" + \
                  "║☈ " + key + "ปิดบอท10/เปิดบอท10\n" + \
                  "║☈ " + key + "ดึง[vm\n" + \
                  "║☈ " + key + "Respon\n" + \
                  "║☈ " + key + "join\n" + \
                  "║☈ " + key + "bye\n" + \
                  "║☈ " + key + "ผีมา\n" + \
                  "║☈ " + key + "ผีออก\n" + \
                  "╚[ SELFbot]\n" + \
                  "▬▬▬▬*****▬▬▬▬\n" + \
                  "\nคำสั่งกลุ่ม\n"
    return helpMessage2

def bot(op):
    global time
    global ast
    global groupParam
    try:
        if op.type == 0:
            return
        
        if op.type == 11:
            if op.param1 in protectqr:
                wait["blacklist"][op.param2] = True
                try:
                    if cl.getGroup(op.param1).preventedJoinByTicket == False:
                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                            cl.reissueGroupTicket(op.param1)
                            X = cl.getGroup(op.param1)
                            X.preventedJoinByTicket = True
                            Ticket = cl.reissueGroupTicket(op.param1)
                            sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                            sw.kickoutFromGroup(op.param1,[op.param2])
                            sw.leaveGroup(op.param1)
                            cl.updateGroup(X)
                except:
                    try:
                        if ki.getGroup(op.param1).preventedJoinByTicket == False:
                            if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                ki.reissueGroupTicket(op.param1)
                                X = ki.getGroup(op.param1)
                                X.preventedJoinByTicket = True
                                Ticket = ki.reissueGroupTicket(op.param1)
                                sx.acceptGroupInvitationByTicket(op.param1,Ticket)
                                sw.kickoutFromGroup(op.param1,[op.param2])
                                sw.leaveGroup(op.param1)
                                ki.updateGroup(X)
                    except:
                        try:
                            if kk.getGroup(op.param1).preventedJoinByTicket == False:
                                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                    kk.reissueGroupTicket(op.param1)
                                    X = kk.getGroup(op.param1)
                                    X.preventedJoinByTicket = True
                                    Ticket = kk.reissueGroupTicket(op.param1)
                                    sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    sw.kickoutFromGroup(op.param1,[op.param2])
                                    sw.leaveGroup(op.param1)
                                    kk.updateGroup(X)
                        except:
                            try:
                                if kc.getGroup(op.param1).preventedJoinByTicket == False:
                                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                        kc.reissueGroupTicket(op.param1)
                                        X = kc.getGroup(op.param1)
                                        X.preventedJoinByTicket = True
                                        Ticket = kc.reissueGroupTicket(op.param1)
                                        sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        sw.kickoutFromGroup(op.param1,[op.param2])
                                        sw.leaveGroup(op.param1)
                                        kc.updateGroup(X)
                            except:
                                try:
                                    if km.getGroup(op.param1).preventedJoinByTicket == False:
                                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                            km.reissueGroupTicket(op.param1)
                                            X = km.getGroup(op.param1)
                                            X.preventedJoinByTicket = True
                                            Ticket = km.reissueGroupTicket(op.param1)
                                            sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            sw.kickoutFromGroup(op.param1,[op.param2])
                                            km.updateGroup(X)
                                except:
                                    try:
                                        if kb.getGroup(op.param1).preventedJoinByTicket == False:
                                            if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                                kb.reissueGroupTicket(op.param1)
                                                X = kb.getGroup(op.param1)
                                                X.preventedJoinByTicket = True
                                                Ticket = kb.reissueGroupTicket(op.param1)
                                                sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                sw.kickoutFromGroup(op.param1,[op.param2])
                                                kb.updateGroup(X)
                                    except:
                                        try:
                                            if kn.getGroup(op.param1).preventedJoinByTicket == False:
                                                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                                    kb.reissueGroupTicket(op.param1)
                                                    X = kb.getGroup(op.param1)
                                                    X.preventedJoinByTicket = True
                                                    Ticket = kb.reissueGroupTicket(op.param1)
                                                    sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                    sw.kickoutFromGroup(op.param1,[op.param2])
                                                    kn.updateGroup(X)
                                        except:
                                            pass
        if op.type == 13:
            if mid in op.param3:
                if wait["autoLeave"] == False:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                        cl.leaveGroup(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)

        if op.type == 13:
            if mid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
            if Amid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        ki.acceptGroupInvitation(op.param1)
                        ginfo = ki.getGroup(op.param1)
                        ki.leaveGroup(op.param1)
                    else:
                        ki.acceptGroupInvitation(op.param1)
                        ginfo = ki.getGroup(op.param1)
            if Bmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kk.acceptGroupInvitation(op.param1)
                        ginfo = kk.getGroup(op.param1)
                        kk.leaveGroup(op.param1)
                    else:
                        kk.acceptGroupInvitation(op.param1)
                        ginfo = kk.getGroup(op.param1)
            if Cmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kc.acceptGroupInvitation(op.param1)
                        ginfo = kc.getGroup(op.param1)
                        kc.leaveGroup(op.param1)
                    else:
                        kc.acceptGroupInvitation(op.param1)
                        ginfo = kc.getGroup(op.param1)
            if Dmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        km.acceptGroupInvitation(op.param1)
                        ginfo = km.getGroup(op.param1)
                        km.leaveGroup(op.param1)
                    else:
                        kb.acceptGroupInvitation(op.param1)
                        ginfo = km.getGroup(op.param1)
            if Emid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kb.acceptGroupInvitation(op.param1)
                        ginfo = kb.getGroup(op.param1)
                        kb.leaveGroup(op.param1)
                    else:
                        kb.acceptGroupInvitation(op.param1)
                        ginfo = kb.getGroup(op.param1)
            if Fmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kn.acceptGroupInvitation(op.param1)
                        ginfo = kn.getGroup(op.param1)
                        kn.leaveGroup(op.param1)
                    else:
                        kn.acceptGroupInvitation(op.param1)
                        ginfo = kn.getGroup(op.param1)
            if Gmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        ko.acceptGroupInvitation(op.param1)
                        ginfo = ko.getGroup(op.param1)
                        ko.leaveGroup(op.param1)
                    else:
                        ko.acceptGroupInvitation(op.param1)
                        ginfo = ko.getGroup(op.param1)
            if Hmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kw.acceptGroupInvitation(op.param1)
                        ginfo = kw.getGroup(op.param1)
                        kw.leaveGroup(op.param1)
                    else:
                        kw.acceptGroupInvitation(op.param1)
                        ginfo = kw.getGroup(op.param1)
            if Imid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        ke.acceptGroupInvitation(op.param1)
                        ginfo = ke.getGroup(op.param1)
                        ke.leaveGroup(op.param1)
                    else:
                        ke.acceptGroupInvitation(op.param1)
                        ginfo = ke.getGroup(op.param1)
            if Jmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        ky.acceptGroupInvitation(op.param1)
                        ginfo = ky.getGroup(op.param1)
                        ky.leaveGroup(op.param1)
                    else:
                        ky.acceptGroupInvitation(op.param1)
                        ginfo = ky.getGroup(op.param1)
#____________________________________________________________________
        if op.type == 13:
            if op.param1 in protectinvite:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    try:
                        group = cl.getGroup(op.param1)
                        gMembMids = [contact.mid for contact in group.invitee]
                        for _mid in gMembMids:
                            random.choice(ABC).cancelGroupInvitation(op.param1,[_mid])
                    except:
                        try:
                            group = ki.getGroup(op.param1)
                            gMembMids = [contact.mid for contact in group.invitee]
                            for _mid in gMembMids:
                                random.choice(ABC).cancelGroupInvitation(op.param1,[_mid])
                        except:
                            try:
                                group = kk.getGroup(op.param1)
                                gMembMids = [contact.mid for contact in group.invitee]
                                for _mid in gMembMids:
                                    random.choice(ABC).cancelGroupInvitation(op.param1,[_mid])
                            except:
                                try:
                                    group = kc.getGroup(op.param1)
                                    gMembMids = [contact.mid for contact in group.invitee]
                                    for _mid in gMembMids:
                                        random.choice(ABC).cancelGroupInvitation(op.param1,[_mid])
                                except:
                                    try:
                                        group = km.getGroup(op.param1)
                                        gMembMids = [contact.mid for contact in group.invitee]
                                        for _mid in gMembMids:
                                            random.choice(ABC).cancelGroupInvitation(op.param1,[_mid])
                                    except:
                                        try:
                                            group = kb.getGroup(op.param1)
                                            gMembMids = [contact.mid for contact in group.invitee]
                                            for _mid in gMembMids:
                                                random.choice(ABC).cancelGroupInvitation(op.param1,[_mid])
                                        except:
                                            try:
                                                group = kn.getGroup(op.param1)
                                                gMembMids = [contact.mid for contact in group.invitee]
                                                for _mid in gMembMids:
                                                    random.choice(ABC).cancelGroupInvitation(op.param1,[_mid])
                                            except:
                                                try:
                                                    group = ko.getGroup(op.param1)
                                                    gMembMids = [contact.mid for contact in group.invitee]
                                                    for _mid in gMembMids:
                                                        random.choice(ABC).cancelGroupInvitation(op.param1,[_mid])
                                                except:
                                                    try:
                                                        group = kw.getGroup(op.param1)
                                                        gMembMids = [contact.mid for contact in group.invitee]
                                                        for _mid in gMembMids:
                                                            random.choice(ABC).cancelGroupInvitation(op.param1,[_mid])
                                                    except:
                                                        try:
                                                            group = ke.getGroup(op.param1)
                                                            gMembMids = [contact.mid for contact in group.invitee]
                                                            for _mid in gMembMids:
                                                                random.choice(ABC).cancelGroupInvitation(op.param1,[_mid])
                                                        except:
                                                            try:
                                                                group = ky.getGroup(op.param1)
                                                                gMembMids = [contact.mid for contact in group.invitee]
                                                                for _mid in gMembMids:
                                                                    random.choice(ABC).cancelGroupInvitation(op.param1,[_mid])
                                                            except:
                                                                pass
        if op.type == 13:
            if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                wait["blacklist"][op.param2] = True
                try:
                    if op.param3 not in wait["blacklist"]:
                        ki.cancelGroupInvitation(op.param1,[op.param3])
                        ki.kickoutFromGroup(op.param1, [op.param2])
                except:
                        try:
                            if op.param3 not in wait["blacklist"]:
                                kk.cancelGroupInvitation(op.param1,[op.param3])
                                kk.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                if op.param3 not in wait["blacklist"]:
                                    kc.cancelGroupInvitation(op.param1,[op.param3])
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    if op.param3 not in wait["blacklist"]:
                                        km.cancelGroupInvitation(op.param1,[op.param3])
                                        km.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        if op.param3 not in wait["blacklist"]:
                                            kb.cancelGroupInvitation(op.param1,[op.param3])
                                            kb.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            if op.param3 not in wait["blacklist"]:
                                                ko.cancelGroupInvitation(op.param1,[op.param3])
                                                ko.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            try:
                                                if op.param3 not in wait["blacklist"]:
                                                    kn.cancelGroupInvitation(op.param1,[op.param3])
                                                    kn.kickoutFromGroup(op.param1,[op.param2])
                                            except:
                                                try:
                                                    if op.param3 not in wait["blacklist"]:
                                                        kw.cancelGroupInvitation(op.param1,[op.param3])
                                                        kw.kickoutFromGroup(op.param1,[op.param2])
                                                except:
                                                    try:
                                                        if op.param3 not in wait["blacklist"]:
                                                            ke.cancelGroupInvitation(op.param1,[op.param3])
                                                            ke.kickoutFromGroup(op.param1,[op.param2])
                                                    except:
                                                        try:
                                                            if op.param3 not in wait["blacklist"]:
                                                                ky.cancelGroupInvitation(op.param1,[op.param3])
                                                                ky.kickoutFromGroup(op.param1,[op.param2])
                                                        except:
                                                            pass
                return
                                                            
        if op.type == 13:
            if op.param3 in wait["blacklist"]:
                    try:
                        random.choice(ABC).cancelGroupInvitation(op.param1,[op.param3])
                    except:
                        pass

        if op.type == 17:
            if op.param2 in wait["blacklist"]:
                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
            else:
                pass

        if op.type == 17:
            if op.param1 in welcome:
                if op.param2 in Bots:
                    pass
                ginfo = cl.getGroup(op.param1)
                contact = cl.getContact(op.param2).picturePath
                image = 'http://dl.profile.line.naver.jp'+contact
                welcomeMembers(op.param1, [op.param2])
                cl.sendImageWithURL(op.param1, image)

        if op.type == 17:
            if op.param1 in protectjoin:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                else:
                    pass

        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    if (wait["message"] in [" "," ","\n",None]):
                        pass
                    else:
                        cl.sendText(op.param1, wait["message"])

        if op.type == 5:
            print ("[ 5 ] SELFBOT")
            if wait["autoBlock"] == False:
                cl.sendText(op.param1, wait["message"])
                cl.sendContact(op.param1, "uc66e45201d1612eb4ce7b3a86bac4685")
                cl.blockContact(op.param1)

        if op.type == 19:
            if op.param1 in protectkick:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                else:
                    pass

        if op.type == 19:
            try:
                if op.param1 in ghost:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        G = cl.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(op.param1)
                        sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                        sw.kickoutFromGroup(op.param1,[op.param2])
                        sw.leaveGroup(op.param1)
                        X = cl.getGroup(op.param1)
                        X.preventedJoinByTicket = True
                        cl.updateGroup(X)
            except:
                pass             
                
        if op.type == 19:
            try:
                if op.param1 in protectantijs:
                  if op.param3 in mid:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        sw.acceptGroupInvitation(op.param1)
                        G = sw.getGroup(op.param1)
                        G.prevenJoinByTicket = False
                        sw.updateGroup(G)
                        Ticket = sw.reissueGroupTicket(op.param1)
                        random.choice(KAC).acceptGroupInvitationByTicket(op.param1,Ticket)
                        sw.kickoutFromGroup(op.param1,[op.param2])
                        G.prevenJoinByTicket = True
                        sw.updateGroup(G)
                        wait["blacklist"][op.param2] = True
                        sw.leaveGroup(op.param1)
                        cl.inviteIntoGroup(op.param1,[Zmid])
                        cl.inviteIntoGroup(op.param1,[admin])
                    else:
                       pass
                        
                if op.param3 in Zmid:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.findAndAddContactsByMid(op.param3)
                        cl.inviteIntoGroup(op.param1,[Zmid])
                        cl.sendMessage(op.param1,"=AntiJS Invited=")
                    else:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.findAndAddContactsByMid(op.param3)
                        cl.inviteIntoGroup(op.param1,[Zmid])
                        cl.sendMessage(op.param1,"Pro Tect Js")
                        
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    if op.param3 in admin:
                        if op.param1 in protectantijs:
                            wait["blacklist"][op.param2] = True
                            cl.kickoutFromGroup(op.param1,[op.param2])
                            cl.findAndAddContactsByMid(op.param3)
                            cl.inviteIntoGroup(op.param1,[op.param3])
                            cl.sendMessage(op.param1,"=Admin Invited=")
                else:
                    pass
            except:
                pass
  
        if op.type == 32:
            if op.param1 in protectcancel:
              if op.param3 in Bots:    
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in wait["blacklist"]:
                            random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                            random.choice(ABC).inviteIntoGroup(op.param1,[Zmid])
                    except:
                        try:
                            if op.param3 not in wait["blacklist"]:
                                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                random.choice(ABC).inviteIntoGroup(op.param1,[Zmid])
                        except:
                            try:
                                if op.param3 not in wait["blacklist"]:
                                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                    random.choice(ABC).inviteIntoGroup(op.param1,[Zmid])
                            except:
                                try:
                                    if op.param3 not in wait["blacklist"]:
                                        random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                        random.choice(ABC).inviteIntoGroup(op.param1,[Zmid])
                                except:
                                    try:
                                        if op.param3 not in wait["blacklist"]:
                                            random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                            random.choice(ABC).inviteIntoGroup(op.param1,[Zmid])
                                    except:
                                        try:
                                            if op.param3 not in wait["blacklist"]:
                                                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                                random.choice(ABC).inviteIntoGroup(op.param1,[Zmid])
                                        except:
                                            try:
                                                if op.param3 not in wait["blacklist"]:
                                                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                                    random.choice(ABC).inviteIntoGroup(op.param1,[Zmid])
                                            except:
                                                try:
                                                    if op.param3 not in wait["blacklist"]:
                                                        random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                                        random.choice(ABC).inviteIntoGroup(op.param1,[Zmid])
                                                except:
                                                    try:
                                                        if op.param3 not in wait["blacklist"]:
                                                            random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                                            random.choice(ABC).inviteIntoGroup(op.param1,[Zmid])
                                                    except:
                                                        pass

#--------------------------------------------------------

        if op.type == 19:
            if mid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        ki.kickoutFromGroup(op.param1,[op.param2])
                        time.sleep(0.008) 
                        ki.inviteIntoGroup(op.param1,[op.param3])
                        cl.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kk.kickoutFromGroup(op.param1,[op.param2])
                            time.sleep(0.008) 
                            kk.inviteIntoGroup(op.param1,[op.param3])
                            cl.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kc.kickoutFromGroup(op.param1,[op.param2])
                                time.sleep(0.008) 
                                kc.inviteIntoGroup(op.param1,[op.param3])
                                cl.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    km.kickoutFromGroup(op.param1,[op.param2])
                                    time.sleep(0.008) 
                                    km.inviteIntoGroup(op.param1,[op.param3])
                                    cl.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        kb.kickoutFromGroup(op.param1,[op.param2])
                                        time.sleep(0.008) 
                                        kb.inviteIntoGroup(op.param1,[op.param3])
                                        cl.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            kn.kickoutFromGroup(op.param1,[op.param2])
                                            time.sleep(0.008) 
                                            kn.inviteIntoGroup(op.param1,[op.param3])
                                            cl.acceptGroupInvitation(op.param1)
                                        except:
                                            try:
                                                ko.kickoutFromGroup(op.param1,[op.param2])
                                                time.sleep(0.008) 
                                                ko.inviteIntoGroup(op.param1,[op.param3])
                                                cl.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    kw.kickoutFromGroup(op.param1,[op.param2])
                                                    time.sleep(0.008) 
                                                    kw.inviteIntoGroup(op.param1,[op.param3])
                                                    cl.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        ke.kickoutFromGroup(op.param1,[op.param2])
                                                        time.sleep(0.008) 
                                                        ke.inviteIntoGroup(op.param1,[op.param3])
                                                        cl.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            G = random.choice(ABC).getGroup(op.param1)
                                                            G.preventedJoinByTicket = False
                                                            random.choice(ABC).updateGroup(G)
                                                            Ticket = random.choice(ABC).reissueGroupTicket(op.param1)
                                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            km.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kn.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kw.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            ky.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            G = random.choice(ABC).getGroup(op.param1)
                                                            G.preventedJoinByTicket = True
                                                            random.choice(ABC).updateGroup(G)
                                                            Ticket = random.choice(ABC).reissueGroupTicket(op.param1)
                                                        except:
                                                            try:
                                                                ky.kickoutFromGroup(op.param1,[op.param2])
                                                                time.sleep(0.008) 
                                                                ky.inviteIntoGroup(op.param1,[op.param3])
                                                                cl.acceptGroupInvitation(op.param1)
                                                            except:
                                                                try:
                                                                    ki.kickoutFromGroup(op.param1,[op.param2])
                                                                    time.sleep(0.008) 
                                                                    ki.inviteIntoGroup(op.param1,[op.param3])
                                                                    cl.acceptGroupInvitation(op.param1)
                                                                except:
                                                                    try:
                                                                        kk.kickoutFromGroup(op.param1,[op.param2])
                                                                        time.sleep(0.008) 
                                                                        kk.inviteIntoGroup(op.param1,[op.param3])
                                                                        cl.acceptGroupInvitation(op.param1)
                                                                    except:
                                                                        try:
                                                                            kc.kickoutFromGroup(op.param1,[op.param2])
                                                                            time.sleep(0.008) 
                                                                            kc.inviteIntoGroup(op.param1,[op.param3])
                                                                            cl.acceptGroupInvitation(op.param1)
                                                                        except:
                                                                            try:
                                                                                km.kickoutFromGroup(op.param1,[op.param2])
                                                                                time.sleep(0.008) 
                                                                                km.inviteIntoGroup(op.param1,[op.param3])
                                                                                cl.acceptGroupInvitation(op.param1)
                                                                            except:
                                                                                try:
                                                                                    kb.kickoutFromGroup(op.param1,[op.param2])
                                                                                    time.sleep(0.008) 
                                                                                    kb.inviteIntoGroup(op.param1,[op.param3])
                                                                                    cl.acceptGroupInvitation(op.param1)
                                                                                except:
                                                                                    try:
                                                                                        kn.kickoutFromGroup(op.param1,[op.param2])
                                                                                        time.sleep(0.008) 
                                                                                        kn.inviteIntoGroup(op.param1,[op.param3])
                                                                                        cl.acceptGroupInvitation(op.param1)
                                                                                    except:
                                                                                        try:
                                                                                            ko.kickoutFromGroup(op.param1,[op.param2])
                                                                                            time.sleep(0.008) 
                                                                                            ko.inviteIntoGroup(op.param1,[op.param3])
                                                                                            cl.acceptGroupInvitation(op.param1)
                                                                                        except:
                                                                                            try:
                                                                                                kw.kickoutFromGroup(op.param1,[op.param2])
                                                                                                time.sleep(0.008) 
                                                                                                kw.inviteIntoGroup(op.param1,[op.param3])
                                                                                                cl.acceptGroupInvitation(op.param1)
                                                                                            except:
                                                                                                pass
                return
        if op.type == 19:
            if Amid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kk.kickoutFromGroup(op.param1,[op.param2])
                        time.sleep(0.008) 
                        kk.inviteIntoGroup(op.param1,[op.param3])
                        ki.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kc.kickoutFromGroup(op.param1,[op.param2])
                            time.sleep(0.008) 
                            kc.inviteIntoGroup(op.param1,[op.param3])
                            ki.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                km.kickoutFromGroup(op.param1,[op.param2])
                                time.sleep(0.008) 
                                km.inviteIntoGroup(op.param1,[op.param3])
                                ki.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    kb.kickoutFromGroup(op.param1,[op.param2])
                                    time.sleep(0.008) 
                                    kb.inviteIntoGroup(op.param1,[op.param3])
                                    ki.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        kn.kickoutFromGroup(op.param1,[op.param2])
                                        time.sleep(0.008) 
                                        kn.inviteIntoGroup(op.param1,[op.param3])
                                        ki.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            ko.kickoutFromGroup(op.param1,[op.param2])
                                            time.sleep(0.008) 
                                            ko.inviteIntoGroup(op.param1,[op.param3])
                                            ki.acceptGroupInvitation(op.param1)
                                        except:
                                            try:
                                                kw.kickoutFromGroup(op.param1,[op.param2])
                                                time.sleep(0.008) 
                                                kw.inviteIntoGroup(op.param1,[op.param3])
                                                ki.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    ke.kickoutFromGroup(op.param1,[op.param2])
                                                    time.sleep(0.008) 
                                                    ke.inviteIntoGroup(op.param1,[op.param3])
                                                    ki.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        ky.kickoutFromGroup(op.param1,[op.param2])
                                                        time.sleep(0.008) 
                                                        ky.inviteIntoGroup(op.param1,[op.param3])
                                                        ki.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            G = random.choice(ABC).getGroup(op.param1)
                                                            G.preventedJoinByTicket = False
                                                            random.choice(ABC).updateGroup(G)
                                                            Ticket = random.choice(ABC).reissueGroupTicket(op.param1)
                                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            km.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kn.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kw.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            ky.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            G = random.choice(ABC).getGroup(op.param1)
                                                            G.preventedJoinByTicket = True
                                                            random.choice(ABC).updateGroup(G)
                                                            Ticket = random.choice(ABC).reissueGroupTicket(op.param1)
                                                        except:
                                                            try:
                                                                kk.kickoutFromGroup(op.param1,[op.param2])
                                                                time.sleep(0.008) 
                                                                kk.inviteIntoGroup(op.param1,[op.param3])
                                                                ki.acceptGroupInvitation(op.param1)
                                                            except:
                                                                try:
                                                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                                                    time.sleep(0.008) 
                                                                    kc.inviteIntoGroup(op.param1,[op.param3])
                                                                    ki.acceptGroupInvitation(op.param1)
                                                                except:
                                                                    try:
                                                                        km.kickoutFromGroup(op.param1,[op.param2])
                                                                        time.sleep(0.008) 
                                                                        km.inviteIntoGroup(op.param1,[op.param3])
                                                                        ki.acceptGroupInvitation(op.param1)
                                                                    except:
                                                                        try:
                                                                            kb.kickoutFromGroup(op.param1,[op.param2])
                                                                            time.sleep(0.008) 
                                                                            kb.inviteIntoGroup(op.param1,[op.param3])
                                                                            ki.acceptGroupInvitation(op.param1)
                                                                        except:
                                                                            try:
                                                                                kn.kickoutFromGroup(op.param1,[op.param2])
                                                                                time.sleep(0.008) 
                                                                                kn.inviteIntoGroup(op.param1,[op.param3])
                                                                                ki.acceptGroupInvitation(op.param1)
                                                                            except:
                                                                                try:
                                                                                    ko.kickoutFromGroup(op.param1,[op.param2])
                                                                                    time.sleep(0.008) 
                                                                                    ko.inviteIntoGroup(op.param1,[op.param3])
                                                                                    ki.acceptGroupInvitation(op.param1)
                                                                                except:
                                                                                    try:
                                                                                        kw.kickoutFromGroup(op.param1,[op.param2])
                                                                                        time.sleep(0.008) 
                                                                                        kw.inviteIntoGroup(op.param1,[op.param3])
                                                                                        ki.acceptGroupInvitation(op.param1)
                                                                                    except:
                                                                                        try:
                                                                                            ke.kickoutFromGroup(op.param1,[op.param2])
                                                                                            time.sleep(0.008) 
                                                                                            ke.inviteIntoGroup(op.param1,[op.param3])
                                                                                            ki.acceptGroupInvitation(op.param1)
                                                                                        except:
                                                                                            try:
                                                                                                ky.kickoutFromGroup(op.param1,[op.param2])
                                                                                                time.sleep(0.008) 
                                                                                                ky.inviteIntoGroup(op.param1,[op.param3])
                                                                                                ki.acceptGroupInvitation(op.param1)
                                                                                            except:
                                                                                                pass
                return
        if op.type == 19:
            if Bmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kc.kickoutFromGroup(op.param1,[op.param2])
                        time.sleep(0.008) 
                        kc.inviteIntoGroup(op.param1,[op.param3])
                        kk.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            km.kickoutFromGroup(op.param1,[op.param2])
                            time.sleep(0.008) 
                            km.inviteIntoGroup(op.param1,[op.param3])
                            kk.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kb.kickoutFromGroup(op.param1,[op.param2])
                                time.sleep(0.008) 
                                kb.inviteIntoGroup(op.param1,[op.param3])
                                kk.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    kn.kickoutFromGroup(op.param1,[op.param2])
                                    time.sleep(0.008) 
                                    kn.inviteIntoGroup(op.param1,[op.param3])
                                    kk.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        ko.kickoutFromGroup(op.param1,[op.param2])
                                        time.sleep(0.008) 
                                        ko.inviteIntoGroup(op.param1,[op.param3])
                                        kk.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            kw.kickoutFromGroup(op.param1,[op.param2])
                                            time.sleep(0.008) 
                                            kw.inviteIntoGroup(op.param1,[op.param3])
                                            kk.acceptGroupInvitation(op.param1)
                                        except:
                                            try:
                                                ke.kickoutFromGroup(op.param1,[op.param2])
                                                time.sleep(0.008) 
                                                ke.inviteIntoGroup(op.param1,[op.param3])
                                                kk.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    ky.kickoutFromGroup(op.param1,[op.param2])
                                                    time.sleep(0.008) 
                                                    ky.inviteIntoGroup(op.param1,[op.param3])
                                                    kk.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        ki.kickoutFromGroup(op.param1,[op.param2])
                                                        time.sleep(0.008) 
                                                        ki.inviteIntoGroup(op.param1,[op.param3])
                                                        kk.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            G = random.choice(ABC).getGroup(op.param1)
                                                            G.preventedJoinByTicket = False
                                                            random.choice(ABC).updateGroup(G)
                                                            Ticket = random.choice(ABC).reissueGroupTicket(op.param1)
                                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            km.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kn.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kw.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            ky.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            G = random.choice(ABC).getGroup(op.param1)
                                                            G.preventedJoinByTicket = True
                                                            random.choice(ABC).updateGroup(G)
                                                            Ticket = random.choice(ABC).reissueGroupTicket(op.param1)
                                                        except:
                                                            try:
                                                                kc.kickoutFromGroup(op.param1,[op.param2])
                                                                time.sleep(0.008) 
                                                                kc.inviteIntoGroup(op.param1,[op.param3])
                                                                kk.acceptGroupInvitation(op.param1)
                                                            except:
                                                                try:
                                                                    km.kickoutFromGroup(op.param1,[op.param2])
                                                                    time.sleep(0.008) 
                                                                    km.inviteIntoGroup(op.param1,[op.param3])
                                                                    kk.acceptGroupInvitation(op.param1)
                                                                except:
                                                                    try:
                                                                        kb.kickoutFromGroup(op.param1,[op.param2])
                                                                        time.sleep(0.008) 
                                                                        kb.inviteIntoGroup(op.param1,[op.param3])
                                                                        kk.acceptGroupInvitation(op.param1)
                                                                    except:
                                                                        try:
                                                                            kn.kickoutFromGroup(op.param1,[op.param2])
                                                                            time.sleep(0.008) 
                                                                            kn.inviteIntoGroup(op.param1,[op.param3])
                                                                            kk.acceptGroupInvitation(op.param1)
                                                                        except:
                                                                            try:
                                                                                ko.kickoutFromGroup(op.param1,[op.param2])
                                                                                time.sleep(0.008) 
                                                                                ko.inviteIntoGroup(op.param1,[op.param3])
                                                                                kk.acceptGroupInvitation(op.param1)
                                                                            except:
                                                                                try:
                                                                                    kw.kickoutFromGroup(op.param1,[op.param2])
                                                                                    time.sleep(0.008) 
                                                                                    kw.inviteIntoGroup(op.param1,[op.param3])
                                                                                    kk.acceptGroupInvitation(op.param1)
                                                                                except:
                                                                                    try:
                                                                                        ke.kickoutFromGroup(op.param1,[op.param2])
                                                                                        time.sleep(0.008) 
                                                                                        ke.inviteIntoGroup(op.param1,[op.param3])
                                                                                        kk.acceptGroupInvitation(op.param1)
                                                                                    except:
                                                                                        try:
                                                                                            ky.kickoutFromGroup(op.param1,[op.param2])
                                                                                            time.sleep(0.008) 
                                                                                            ky.inviteIntoGroup(op.param1,[op.param3])
                                                                                            kk.acceptGroupInvitation(op.param1)
                                                                                        except:
                                                                                            try:
                                                                                                ki.kickoutFromGroup(op.param1,[op.param2])
                                                                                                time.sleep(0.008) 
                                                                                                ki.inviteIntoGroup(op.param1,[op.param3])
                                                                                                kk.acceptGroupInvitation(op.param1)
                                                                                            except:
                                                                                                pass
                return
        if op.type == 19:
            if Cmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        km.kickoutFromGroup(op.param1,[op.param2])
                        time.sleep(0.008) 
                        km.inviteIntoGroup(op.param1,[op.param3])
                        kc.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kb.kickoutFromGroup(op.param1,[op.param2])
                            time.sleep(0.008) 
                            kb.inviteIntoGroup(op.param1,[op.param3])
                            kc.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kn.kickoutFromGroup(op.param1,[op.param2])
                                time.sleep(0.008) 
                                kn.inviteIntoGroup(op.param1,[op.param3])
                                kc.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    ko.kickoutFromGroup(op.param1,[op.param2])
                                    time.sleep(0.008) 
                                    ko.inviteIntoGroup(op.param1,[op.param3])
                                    kc.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        kw.kickoutFromGroup(op.param1,[op.param2])
                                        time.sleep(0.008) 
                                        kw.inviteIntoGroup(op.param1,[op.param3])
                                        kc.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            ke.kickoutFromGroup(op.param1,[op.param2])
                                            time.sleep(0.008) 
                                            ke.inviteIntoGroup(op.param1,[op.param3])
                                            kc.acceptGroupInvitation(op.param1)
                                        except:
                                            try:
                                                ky.kickoutFromGroup(op.param1,[op.param2])
                                                time.sleep(0.008) 
                                                ky.inviteIntoGroup(op.param1,[op.param3])
                                                kc.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    ki.kickoutFromGroup(op.param1,[op.param2])
                                                    time.sleep(0.008) 
                                                    ki.inviteIntoGroup(op.param1,[op.param3])
                                                    kc.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        kk.kickoutFromGroup(op.param1,[op.param2])
                                                        time.sleep(0.008) 
                                                        kk.inviteIntoGroup(op.param1,[op.param3])
                                                        kc.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            G = random.choice(ABC).getGroup(op.param1)
                                                            G.preventedJoinByTicket = False
                                                            random.choice(ABC).updateGroup(G)
                                                            Ticket = random.choice(ABC).reissueGroupTicket(op.param1)
                                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            km.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kn.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kw.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            ky.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            G = random.choice(ABC).getGroup(op.param1)
                                                            G.preventedJoinByTicket = True
                                                            random.choice(ABC).updateGroup(G)
                                                            Ticket = random.choice(ABC).reissueGroupTicket(op.param1)
                                                        except:
                                                            try:
                                                                km.kickoutFromGroup(op.param1,[op.param2])
                                                                time.sleep(0.008) 
                                                                km.inviteIntoGroup(op.param1,[op.param3])
                                                                kc.acceptGroupInvitation(op.param1)
                                                            except:
                                                                try:
                                                                    kb.kickoutFromGroup(op.param1,[op.param2])
                                                                    time.sleep(0.008) 
                                                                    kb.inviteIntoGroup(op.param1,[op.param3])
                                                                    kc.acceptGroupInvitation(op.param1)
                                                                except:
                                                                    try:
                                                                        kn.kickoutFromGroup(op.param1,[op.param2])
                                                                        time.sleep(0.008) 
                                                                        kn.inviteIntoGroup(op.param1,[op.param3])
                                                                        kc.acceptGroupInvitation(op.param1)
                                                                    except:
                                                                        try:
                                                                            ko.kickoutFromGroup(op.param1,[op.param2])
                                                                            time.sleep(0.008) 
                                                                            ko.inviteIntoGroup(op.param1,[op.param3])
                                                                            kc.acceptGroupInvitation(op.param1)
                                                                        except:
                                                                            try:
                                                                                kw.kickoutFromGroup(op.param1,[op.param2])
                                                                                time.sleep(0.008) 
                                                                                kw.inviteIntoGroup(op.param1,[op.param3])
                                                                                kc.acceptGroupInvitation(op.param1)
                                                                            except:
                                                                                try:
                                                                                    ke.kickoutFromGroup(op.param1,[op.param2])
                                                                                    time.sleep(0.008) 
                                                                                    ke.inviteIntoGroup(op.param1,[op.param3])
                                                                                    kc.acceptGroupInvitation(op.param1)
                                                                                except:
                                                                                    try:
                                                                                        ky.kickoutFromGroup(op.param1,[op.param2])
                                                                                        time.sleep(0.008) 
                                                                                        ky.inviteIntoGroup(op.param1,[op.param3])
                                                                                        kc.acceptGroupInvitation(op.param1)
                                                                                    except:
                                                                                        try:
                                                                                            ki.kickoutFromGroup(op.param1,[op.param2])
                                                                                            time.sleep(0.008) 
                                                                                            ki.inviteIntoGroup(op.param1,[op.param3])
                                                                                            kc.acceptGroupInvitation(op.param1)
                                                                                        except:
                                                                                            try:
                                                                                                kk.kickoutFromGroup(op.param1,[op.param2])
                                                                                                time.sleep(0.008) 
                                                                                                kk.inviteIntoGroup(op.param1,[op.param3])
                                                                                                kc.acceptGroupInvitation(op.param1)
                                                                                            except:
                                                                                                pass
                return
        if op.type == 19:
            if Dmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kb.kickoutFromGroup(op.param1,[op.param2])
                        time.sleep(0.008) 
                        kb.inviteIntoGroup(op.param1,[op.param3])
                        km.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kn.kickoutFromGroup(op.param1,[op.param2])
                            time.sleep(0.008) 
                            kn.inviteIntoGroup(op.param1,[op.param3])
                            km.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                ko.kickoutFromGroup(op.param1,[op.param2])
                                time.sleep(0.008) 
                                ko.inviteIntoGroup(op.param1,[op.param3])
                                km.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    kw.kickoutFromGroup(op.param1,[op.param2])
                                    time.sleep(0.008) 
                                    kw.inviteIntoGroup(op.param1,[op.param3])
                                    km.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        ke.kickoutFromGroup(op.param1,[op.param2])
                                        time.sleep(0.008) 
                                        ke.inviteIntoGroup(op.param1,[op.param3])
                                        km.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            ky.kickoutFromGroup(op.param1,[op.param2])
                                            time.sleep(0.008) 
                                            ky.inviteIntoGroup(op.param1,[op.param3])
                                            km.acceptGroupInvitation(op.param1)
                                        except:
                                            try:
                                                ki.kickoutFromGroup(op.param1,[op.param2])
                                                time.sleep(0.008) 
                                                ki.inviteIntoGroup(op.param1,[op.param3])
                                                km.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    kk.kickoutFromGroup(op.param1,[op.param2])
                                                    time.sleep(0.008) 
                                                    kk.inviteIntoGroup(op.param1,[op.param3])
                                                    km.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        kc.kickoutFromGroup(op.param1,[op.param2])
                                                        time.sleep(0.008) 
                                                        kc.inviteIntoGroup(op.param1,[op.param3])
                                                        km.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            G = random.choice(ABC).getGroup(op.param1)
                                                            G.preventedJoinByTicket = False
                                                            random.choice(ABC).updateGroup(G)
                                                            Ticket = random.choice(ABC).reissueGroupTicket(op.param1)
                                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            km.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kn.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kw.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            ky.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            G = random.choice(ABC).getGroup(op.param1)
                                                            G.preventedJoinByTicket = True
                                                            random.choice(ABC).updateGroup(G)
                                                            Ticket = random.choice(ABC).reissueGroupTicket(op.param1)
                                                        except:
                                                            try:
                                                                kb.kickoutFromGroup(op.param1,[op.param2])
                                                                time.sleep(0.008) 
                                                                kb.inviteIntoGroup(op.param1,[op.param3])
                                                                km.acceptGroupInvitation(op.param1)
                                                            except:
                                                                try:
                                                                    kn.kickoutFromGroup(op.param1,[op.param2])
                                                                    time.sleep(0.008) 
                                                                    kn.inviteIntoGroup(op.param1,[op.param3])
                                                                    km.acceptGroupInvitation(op.param1)
                                                                except:
                                                                    try:
                                                                        ko.kickoutFromGroup(op.param1,[op.param2])
                                                                        time.sleep(0.008) 
                                                                        ko.inviteIntoGroup(op.param1,[op.param3])
                                                                        km.acceptGroupInvitation(op.param1)
                                                                    except:
                                                                        try:
                                                                            kw.kickoutFromGroup(op.param1,[op.param2])
                                                                            time.sleep(0.008) 
                                                                            kw.inviteIntoGroup(op.param1,[op.param3])
                                                                            km.acceptGroupInvitation(op.param1)
                                                                        except:
                                                                            try:
                                                                                ke.kickoutFromGroup(op.param1,[op.param2])
                                                                                time.sleep(0.008) 
                                                                                ke.inviteIntoGroup(op.param1,[op.param3])
                                                                                km.acceptGroupInvitation(op.param1)
                                                                            except:
                                                                                try:
                                                                                    ky.kickoutFromGroup(op.param1,[op.param2])
                                                                                    time.sleep(0.008) 
                                                                                    ky.inviteIntoGroup(op.param1,[op.param3])
                                                                                    km.acceptGroupInvitation(op.param1)
                                                                                except:
                                                                                    try:
                                                                                        ki.kickoutFromGroup(op.param1,[op.param2])
                                                                                        time.sleep(0.008) 
                                                                                        ki.inviteIntoGroup(op.param1,[op.param3])
                                                                                        km.acceptGroupInvitation(op.param1)
                                                                                    except:
                                                                                        try:
                                                                                            kk.kickoutFromGroup(op.param1,[op.param2])
                                                                                            time.sleep(0.008) 
                                                                                            kk.inviteIntoGroup(op.param1,[op.param3])
                                                                                            km.acceptGroupInvitation(op.param1)
                                                                                        except:
                                                                                            try:
                                                                                                kc.kickoutFromGroup(op.param1,[op.param2])
                                                                                                time.sleep(0.008) 
                                                                                                kc.inviteIntoGroup(op.param1,[op.param3])
                                                                                                km.acceptGroupInvitation(op.param1)
                                                                                            except:
                                                                                                pass
                return
        if op.type == 19:
            if Emid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kn.kickoutFromGroup(op.param1,[op.param2])
                        time.sleep(0.008) 
                        kn.inviteIntoGroup(op.param1,[op.param3])
                        kb.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            ko.kickoutFromGroup(op.param1,[op.param2])
                            time.sleep(0.008) 
                            ko.inviteIntoGroup(op.param1,[op.param3])
                            kb.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kw.kickoutFromGroup(op.param1,[op.param2])
                                time.sleep(0.008) 
                                kw.inviteIntoGroup(op.param1,[op.param3])
                                kb.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    ke.kickoutFromGroup(op.param1,[op.param2])
                                    time.sleep(0.008) 
                                    ke.inviteIntoGroup(op.param1,[op.param3])
                                    kb.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        ky.kickoutFromGroup(op.param1,[op.param2])
                                        time.sleep(0.008) 
                                        ky.inviteIntoGroup(op.param1,[op.param3])
                                        kb.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            ki.kickoutFromGroup(op.param1,[op.param2])
                                            time.sleep(0.008) 
                                            ki.inviteIntoGroup(op.param1,[op.param3])
                                            kb.acceptGroupInvitation(op.param1)
                                        except:
                                            try:
                                                kk.kickoutFromGroup(op.param1,[op.param2])
                                                time.sleep(0.008) 
                                                kk.inviteIntoGroup(op.param1,[op.param3])
                                                kb.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                                    time.sleep(0.008) 
                                                    kc.inviteIntoGroup(op.param1,[op.param3])
                                                    kb.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        km.kickoutFromGroup(op.param1,[op.param2])
                                                        time.sleep(0.008) 
                                                        km.inviteIntoGroup(op.param1,[op.param3])
                                                        kb.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            G = random.choice(ABC).getGroup(op.param1)
                                                            G.preventedJoinByTicket = False
                                                            random.choice(ABC).updateGroup(G)
                                                            Ticket = random.choice(ABC).reissueGroupTicket(op.param1)
                                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            km.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kn.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kw.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            ky.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            G = random.choice(ABC).getGroup(op.param1)
                                                            G.preventedJoinByTicket = True
                                                            random.choice(ABC).updateGroup(G)
                                                            Ticket = random.choice(ABC).reissueGroupTicket(op.param1)
                                                        except:
                                                            try:
                                                                kn.kickoutFromGroup(op.param1,[op.param2])
                                                                time.sleep(0.008) 
                                                                kn.inviteIntoGroup(op.param1,[op.param3])
                                                                kb.acceptGroupInvitation(op.param1)
                                                            except:
                                                                try:
                                                                    ko.kickoutFromGroup(op.param1,[op.param2])
                                                                    time.sleep(0.008)
                                                                    ko.inviteIntoGroup(op.param1,[op.param3])
                                                                    kb.acceptGroupInvitation(op.param1)
                                                                except:
                                                                    try:
                                                                        kw.kickoutFromGroup(op.param1,[op.param2])
                                                                        time.sleep(0.008) 
                                                                        kw.inviteIntoGroup(op.param1,[op.param3])
                                                                        kb.acceptGroupInvitation(op.param1)
                                                                    except:
                                                                        try:
                                                                            ke.kickoutFromGroup(op.param1,[op.param2])
                                                                            time.sleep(0.008) 
                                                                            ke.inviteIntoGroup(op.param1,[op.param3])
                                                                            kb.acceptGroupInvitation(op.param1)
                                                                        except:
                                                                            try:
                                                                                ky.kickoutFromGroup(op.param1,[op.param2])
                                                                                time.sleep(0.008) 
                                                                                ky.inviteIntoGroup(op.param1,[op.param3])
                                                                                kb.acceptGroupInvitation(op.param1)
                                                                            except:
                                                                                try:
                                                                                    ki.kickoutFromGroup(op.param1,[op.param2])
                                                                                    time.sleep(0.008) 
                                                                                    ki.inviteIntoGroup(op.param1,[op.param3])
                                                                                    kb.acceptGroupInvitation(op.param1)
                                                                                except:
                                                                                    try:
                                                                                        kk.kickoutFromGroup(op.param1,[op.param2])
                                                                                        time.sleep(0.008) 
                                                                                        kk.inviteIntoGroup(op.param1,[op.param3])
                                                                                        kb.acceptGroupInvitation(op.param1)
                                                                                    except:
                                                                                        try:
                                                                                            kc.kickoutFromGroup(op.param1,[op.param2])
                                                                                            time.sleep(0.008) 
                                                                                            kc.inviteIntoGroup(op.param1,[op.param3])
                                                                                            kb.acceptGroupInvitation(op.param1)
                                                                                        except:
                                                                                            try:
                                                                                                km.kickoutFromGroup(op.param1,[op.param2])
                                                                                                time.sleep(0.008) 
                                                                                                km.inviteIntoGroup(op.param1,[op.param3])
                                                                                                kb.acceptGroupInvitation(op.param1)
                                                                                            except:
                                                                                                pass
                return
        if op.type == 19:
            if Fmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        ko.kickoutFromGroup(op.param1,[op.param2])
                        time.sleep(0.008) 
                        ko.inviteIntoGroup(op.param1,[op.param3])
                        kn.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kw.kickoutFromGroup(op.param1,[op.param2])
                            time.sleep(0.008) 
                            kw.inviteIntoGroup(op.param1,[op.param3])
                            kn.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                ke.kickoutFromGroup(op.param1,[op.param2])
                                time.sleep(0.008) 
                                ke.inviteIntoGroup(op.param1,[op.param3])
                                kn.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    ky.kickoutFromGroup(op.param1,[op.param2])
                                    time.sleep(0.008) 
                                    ky.inviteIntoGroup(op.param1,[op.param3])
                                    kn.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        ki.kickoutFromGroup(op.param1,[op.param2])
                                        time.sleep(0.008) 
                                        ki.inviteIntoGroup(op.param1,[op.param3])
                                        kn.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            kk.kickoutFromGroup(op.param1,[op.param2])
                                            time.sleep(0.008) 
                                            kk.inviteIntoGroup(op.param1,[op.param3])
                                            kn.acceptGroupInvitation(op.param1)
                                        except:
                                            try:
                                                kc.kickoutFromGroup(op.param1,[op.param2])
                                                time.sleep(0.008) 
                                                kc.inviteIntoGroup(op.param1,[op.param3])
                                                kn.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    km.kickoutFromGroup(op.param1,[op.param2])
                                                    time.sleep(0.008) 
                                                    km.inviteIntoGroup(op.param1,[op.param3])
                                                    kn.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        kb.kickoutFromGroup(op.param1,[op.param2])
                                                        time.sleep(0.008) 
                                                        kb.inviteIntoGroup(op.param1,[op.param3])
                                                        kn.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            G = random.choice(ABC).getGroup(op.param1)
                                                            G.preventedJoinByTicket = False
                                                            random.choice(ABC).updateGroup(G)
                                                            Ticket = random.choice(ABC).reissueGroupTicket(op.param1)
                                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            km.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kn.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kw.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            ky.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            G = random.choice(ABC).getGroup(op.param1)
                                                            G.preventedJoinByTicket = True
                                                            random.choice(ABC).updateGroup(G)
                                                            Ticket = random.choice(ABC).reissueGroupTicket(op.param1)
                                                        except:
                                                            try:
                                                                ko.kickoutFromGroup(op.param1,[op.param2])
                                                                time.sleep(0.008) 
                                                                ko.inviteIntoGroup(op.param1,[op.param3])
                                                                kn.acceptGroupInvitation(op.param1)
                                                            except:
                                                                try:
                                                                    kw.kickoutFromGroup(op.param1,[op.param2])
                                                                    time.sleep(0.008) 
                                                                    kw.inviteIntoGroup(op.param1,[op.param3])
                                                                    kn.acceptGroupInvitation(op.param1)
                                                                except:
                                                                    try:
                                                                        ke.kickoutFromGroup(op.param1,[op.param2])
                                                                        time.sleep(0.008) 
                                                                        ke.inviteIntoGroup(op.param1,[op.param3])
                                                                        kn.acceptGroupInvitation(op.param1)
                                                                    except:
                                                                        try:
                                                                            ky.kickoutFromGroup(op.param1,[op.param2])
                                                                            time.sleep(0.008) 
                                                                            ky.inviteIntoGroup(op.param1,[op.param3])
                                                                            kn.acceptGroupInvitation(op.param1)
                                                                        except:
                                                                            try:
                                                                                ki.kickoutFromGroup(op.param1,[op.param2])
                                                                                time.sleep(0.008) 
                                                                                ki.inviteIntoGroup(op.param1,[op.param3])
                                                                                kn.acceptGroupInvitation(op.param1)
                                                                            except:
                                                                                try:
                                                                                    kk.kickoutFromGroup(op.param1,[op.param2])
                                                                                    time.sleep(0.008) 
                                                                                    kk.inviteIntoGroup(op.param1,[op.param3])
                                                                                    kn.acceptGroupInvitation(op.param1)
                                                                                except:
                                                                                    try:
                                                                                        kc.kickoutFromGroup(op.param1,[op.param2])
                                                                                        time.sleep(0.008) 
                                                                                        kc.inviteIntoGroup(op.param1,[op.param3])
                                                                                        kn.acceptGroupInvitation(op.param1)
                                                                                    except:
                                                                                        try:
                                                                                            km.kickoutFromGroup(op.param1,[op.param2])
                                                                                            time.sleep(0.008) 
                                                                                            km.inviteIntoGroup(op.param1,[op.param3])
                                                                                            kn.acceptGroupInvitation(op.param1)
                                                                                        except:
                                                                                            try:
                                                                                                kb.kickoutFromGroup(op.param1,[op.param2])
                                                                                                time.sleep(0.008) 
                                                                                                kb.inviteIntoGroup(op.param1,[op.param3])
                                                                                                kn.acceptGroupInvitation(op.param1)
                                                                                            except:
                                                                                                pass
                return
        if op.type == 19:
            if Gmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kw.kickoutFromGroup(op.param1,[op.param2])
                        time.sleep(0.008) 
                        kw.inviteIntoGroup(op.param1,[op.param3])
                        ko.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            ke.kickoutFromGroup(op.param1,[op.param2])
                            time.sleep(0.008) 
                            ke.inviteIntoGroup(op.param1,[op.param3])
                            ko.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                ky.kickoutFromGroup(op.param1,[op.param2])
                                time.sleep(0.008) 
                                ky.inviteIntoGroup(op.param1,[op.param3])
                                ko.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    ki.kickoutFromGroup(op.param1,[op.param2])
                                    time.sleep(0.008) 
                                    ki.inviteIntoGroup(op.param1,[op.param3])
                                    ko.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        kk.kickoutFromGroup(op.param1,[op.param2])
                                        time.sleep(0.008) 
                                        kk.inviteIntoGroup(op.param1,[op.param3])
                                        ko.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            kc.kickoutFromGroup(op.param1,[op.param2])
                                            time.sleep(0.008) 
                                            kc.inviteIntoGroup(op.param1,[op.param3])
                                            ko.acceptGroupInvitation(op.param1)
                                        except:
                                            try:
                                                km.kickoutFromGroup(op.param1,[op.param2])
                                                time.sleep(0.008) 
                                                km.inviteIntoGroup(op.param1,[op.param3])
                                                ko.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    kb.kickoutFromGroup(op.param1,[op.param2])
                                                    time.sleep(0.008) 
                                                    kb.inviteIntoGroup(op.param1,[op.param3])
                                                    ko.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        kn.kickoutFromGroup(op.param1,[op.param2])
                                                        time.sleep(0.008) 
                                                        kn.inviteIntoGroup(op.param1,[op.param3])
                                                        ko.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            G = random.choice(ABC).getGroup(op.param1)
                                                            G.preventedJoinByTicket = False
                                                            random.choice(ABC).updateGroup(G)
                                                            Ticket = random.choice(ABC).reissueGroupTicket(op.param1)
                                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            km.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kn.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kw.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            ky.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            G = random.choice(ABC).getGroup(op.param1)
                                                            G.preventedJoinByTicket = True
                                                            random.choice(ABC).updateGroup(G)
                                                            Ticket = random.choice(ABC).reissueGroupTicket(op.param1)
                                                        except:
                                                            try:
                                                                kw.kickoutFromGroup(op.param1,[op.param2])
                                                                time.sleep(0.008) 
                                                                kw.inviteIntoGroup(op.param1,[op.param3])
                                                                ko.acceptGroupInvitation(op.param1)
                                                            except:
                                                                try:
                                                                    ke.kickoutFromGroup(op.param1,[op.param2])
                                                                    time.sleep(0.008) 
                                                                    ke.inviteIntoGroup(op.param1,[op.param3])
                                                                    ko.acceptGroupInvitation(op.param1)
                                                                except:
                                                                    try:
                                                                        ky.kickoutFromGroup(op.param1,[op.param2])
                                                                        time.sleep(0.008) 
                                                                        ky.inviteIntoGroup(op.param1,[op.param3])
                                                                        ko.acceptGroupInvitation(op.param1)
                                                                    except:
                                                                        try:
                                                                            ki.kickoutFromGroup(op.param1,[op.param2])
                                                                            time.sleep(0.008) 
                                                                            ki.inviteIntoGroup(op.param1,[op.param3])
                                                                            ko.acceptGroupInvitation(op.param1)
                                                                        except:
                                                                            try:
                                                                                kk.kickoutFromGroup(op.param1,[op.param2])
                                                                                time.sleep(0.008) 
                                                                                kk.inviteIntoGroup(op.param1,[op.param3])
                                                                                ko.acceptGroupInvitation(op.param1)
                                                                            except:
                                                                                try:
                                                                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                                                                    time.sleep(0.008) 
                                                                                    kc.inviteIntoGroup(op.param1,[op.param3])
                                                                                    ko.acceptGroupInvitation(op.param1)
                                                                                except:
                                                                                    try:
                                                                                        km.kickoutFromGroup(op.param1,[op.param2])
                                                                                        time.sleep(0.008) 
                                                                                        km.inviteIntoGroup(op.param1,[op.param3])
                                                                                        ko.acceptGroupInvitation(op.param1)
                                                                                    except:
                                                                                        try:
                                                                                            kb.kickoutFromGroup(op.param1,[op.param2])
                                                                                            time.sleep(0.008) 
                                                                                            kb.inviteIntoGroup(op.param1,[op.param3])
                                                                                            ko.acceptGroupInvitation(op.param1)
                                                                                        except:
                                                                                            try:
                                                                                                kn.kickoutFromGroup(op.param1,[op.param2])
                                                                                                time.sleep(0.008) 
                                                                                                kn.inviteIntoGroup(op.param1,[op.param3])
                                                                                                ko.acceptGroupInvitation(op.param1)
                                                                                            except:
                                                                                                pass
                return
        if op.type == 19:
            if Hmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        ke.kickoutFromGroup(op.param1,[op.param2])
                        time.sleep(0.008) 
                        ke.inviteIntoGroup(op.param1,[op.param3])
                        kw.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            ky.kickoutFromGroup(op.param1,[op.param2])
                            time.sleep(0.008) 
                            ky.inviteIntoGroup(op.param1,[op.param3])
                            kw.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                ki.kickoutFromGroup(op.param1,[op.param2])
                                time.sleep(0.008) 
                                ki.inviteIntoGroup(op.param1,[op.param3])
                                kw.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    kk.kickoutFromGroup(op.param1,[op.param2])
                                    time.sleep(0.008) 
                                    kk.inviteIntoGroup(op.param1,[op.param3])
                                    kw.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        kc.kickoutFromGroup(op.param1,[op.param2])
                                        time.sleep(0.008) 
                                        kc.inviteIntoGroup(op.param1,[op.param3])
                                        kw.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            km.kickoutFromGroup(op.param1,[op.param2])
                                            time.sleep(0.008) 
                                            km.inviteIntoGroup(op.param1,[op.param3])
                                            kw.acceptGroupInvitation(op.param1)
                                        except:
                                            try:
                                                kb.kickoutFromGroup(op.param1,[op.param2])
                                                time.sleep(0.008) 
                                                kb.inviteIntoGroup(op.param1,[op.param3])
                                                kw.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    kn.kickoutFromGroup(op.param1,[op.param2])
                                                    time.sleep(0.008) 
                                                    kn.inviteIntoGroup(op.param1,[op.param3])
                                                    kw.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        ko.kickoutFromGroup(op.param1,[op.param2])
                                                        time.sleep(0.008) 
                                                        ko.inviteIntoGroup(op.param1,[op.param3])
                                                        kw.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            G = random.choice(ABC).getGroup(op.param1)
                                                            G.preventedJoinByTicket = False
                                                            random.choice(ABC).updateGroup(G)
                                                            Ticket = random.choice(ABC).reissueGroupTicket(op.param1)
                                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            km.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kn.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kw.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            ky.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            G = random.choice(ABC).getGroup(op.param1)
                                                            G.preventedJoinByTicket = True
                                                            random.choice(ABC).updateGroup(G)
                                                            Ticket = random.choice(ABC).reissueGroupTicket(op.param1)
                                                        except:
                                                            try:
                                                                ke.kickoutFromGroup(op.param1,[op.param2])
                                                                time.sleep(0.008) 
                                                                ke.inviteIntoGroup(op.param1,[op.param3])
                                                                kw.acceptGroupInvitation(op.param1)
                                                            except:
                                                                try:
                                                                    ky.kickoutFromGroup(op.param1,[op.param2])
                                                                    time.sleep(0.008) 
                                                                    ky.inviteIntoGroup(op.param1,[op.param3])
                                                                    kw.acceptGroupInvitation(op.param1)
                                                                except:
                                                                    try:
                                                                        ki.kickoutFromGroup(op.param1,[op.param2])
                                                                        time.sleep(0.008) 
                                                                        ki.inviteIntoGroup(op.param1,[op.param3])
                                                                        kw.acceptGroupInvitation(op.param1)
                                                                    except:
                                                                        try:
                                                                            kk.kickoutFromGroup(op.param1,[op.param2])
                                                                            time.sleep(0.008) 
                                                                            kk.inviteIntoGroup(op.param1,[op.param3])
                                                                            kw.acceptGroupInvitation(op.param1)
                                                                        except:
                                                                            try:
                                                                                kc.kickoutFromGroup(op.param1,[op.param2])
                                                                                time.sleep(0.008) 
                                                                                kc.inviteIntoGroup(op.param1,[op.param3])
                                                                                kw.acceptGroupInvitation(op.param1)
                                                                            except:
                                                                                try:
                                                                                    km.kickoutFromGroup(op.param1,[op.param2])
                                                                                    time.sleep(0.008) 
                                                                                    km.inviteIntoGroup(op.param1,[op.param3])
                                                                                    kw.acceptGroupInvitation(op.param1)
                                                                                except:
                                                                                    try:
                                                                                        kb.kickoutFromGroup(op.param1,[op.param2])
                                                                                        time.sleep(0.008) 
                                                                                        kb.inviteIntoGroup(op.param1,[op.param3])
                                                                                        kw.acceptGroupInvitation(op.param1)
                                                                                    except:
                                                                                        try:
                                                                                            kn.kickoutFromGroup(op.param1,[op.param2])
                                                                                            time.sleep(0.008) 
                                                                                            kn.inviteIntoGroup(op.param1,[op.param3])
                                                                                            kw.acceptGroupInvitation(op.param1)
                                                                                        except:
                                                                                            try:
                                                                                                ko.kickoutFromGroup(op.param1,[op.param2])
                                                                                                time.sleep(0.008) 
                                                                                                ko.inviteIntoGroup(op.param1,[op.param3])
                                                                                                kw.acceptGroupInvitation(op.param1)
                                                                                            except:
                                                                                                pass
                return
        if op.type == 19:
            if Imid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        ky.kickoutFromGroup(op.param1,[op.param2])
                        time.sleep(0.008) 
                        ky.inviteIntoGroup(op.param1,[op.param3])
                        ke.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                            time.sleep(0.008) 
                            ki.inviteIntoGroup(op.param1,[op.param3])
                            ke.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                                time.sleep(0.008) 
                                kk.inviteIntoGroup(op.param1,[op.param3])
                                ke.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    time.sleep(0.008) 
                                    kc.inviteIntoGroup(op.param1,[op.param3])
                                    ke.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        km.kickoutFromGroup(op.param1,[op.param2])
                                        time.sleep(0.008) 
                                        km.inviteIntoGroup(op.param1,[op.param3])
                                        ke.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            kb.kickoutFromGroup(op.param1,[op.param2])
                                            time.sleep(0.008) 
                                            kb.inviteIntoGroup(op.param1,[op.param3])
                                            ke.acceptGroupInvitation(op.param1)
                                        except:
                                            try:
                                                kn.kickoutFromGroup(op.param1,[op.param2])
                                                time.sleep(0.008) 
                                                kn.inviteIntoGroup(op.param1,[op.param3])
                                                ke.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    ko.kickoutFromGroup(op.param1,[op.param2])
                                                    time.sleep(0.008) 
                                                    ko.inviteIntoGroup(op.param1,[op.param3])
                                                    ke.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        kw.kickoutFromGroup(op.param1,[op.param2])
                                                        time.sleep(0.008) 
                                                        kw.inviteIntoGroup(op.param1,[op.param3])
                                                        ke.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            G = random.choice(ABC).getGroup(op.param1)
                                                            G.preventedJoinByTicket = False
                                                            random.choice(ABC).updateGroup(G)
                                                            Ticket = random.choice(ABC).reissueGroupTicket(op.param1)
                                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            km.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kn.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kw.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            ky.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            G = random.choice(ABC).getGroup(op.param1)
                                                            G.preventedJoinByTicket = True
                                                            random.choice(ABC).updateGroup(G)
                                                            Ticket = random.choice(ABC).reissueGroupTicket(op.param1)
                                                        except:
                                                            try:
                                                                ky.kickoutFromGroup(op.param1,[op.param2])
                                                                time.sleep(0.008) 
                                                                ky.inviteIntoGroup(op.param1,[op.param3])
                                                                ke.acceptGroupInvitation(op.param1)
                                                            except:
                                                                try:
                                                                    ki.kickoutFromGroup(op.param1,[op.param2])
                                                                    time.sleep(0.008) 
                                                                    ki.inviteIntoGroup(op.param1,[op.param3])
                                                                    ke.acceptGroupInvitation(op.param1)
                                                                except:
                                                                    try:
                                                                        kk.kickoutFromGroup(op.param1,[op.param2])
                                                                        time.sleep(0.008) 
                                                                        kk.inviteIntoGroup(op.param1,[op.param3])
                                                                        ke.acceptGroupInvitation(op.param1)
                                                                    except:
                                                                        try:
                                                                            kc.kickoutFromGroup(op.param1,[op.param2])
                                                                            time.sleep(0.008) 
                                                                            kc.inviteIntoGroup(op.param1,[op.param3])
                                                                            ke.acceptGroupInvitation(op.param1)
                                                                        except:
                                                                            try:
                                                                                km.kickoutFromGroup(op.param1,[op.param2])
                                                                                time.sleep(0.008) 
                                                                                km.inviteIntoGroup(op.param1,[op.param3])
                                                                                ke.acceptGroupInvitation(op.param1)
                                                                            except:
                                                                                try:
                                                                                    kb.kickoutFromGroup(op.param1,[op.param2])
                                                                                    time.sleep(0.008) 
                                                                                    kb.inviteIntoGroup(op.param1,[op.param3])
                                                                                    ke.acceptGroupInvitation(op.param1)
                                                                                except:
                                                                                    try:
                                                                                        kn.kickoutFromGroup(op.param1,[op.param2])
                                                                                        time.sleep(0.008) 
                                                                                        kn.inviteIntoGroup(op.param1,[op.param3])
                                                                                        ke.acceptGroupInvitation(op.param1)
                                                                                    except:
                                                                                        try:
                                                                                            ko.kickoutFromGroup(op.param1,[op.param2])
                                                                                            time.sleep(0.008) 
                                                                                            ko.inviteIntoGroup(op.param1,[op.param3])
                                                                                            ke.acceptGroupInvitation(op.param1)
                                                                                        except:
                                                                                            try:
                                                                                                kw.kickoutFromGroup(op.param1,[op.param2])
                                                                                                time.sleep(0.008) 
                                                                                                kw.inviteIntoGroup(op.param1,[op.param3])
                                                                                                ke.acceptGroupInvitation(op.param1)
                                                                                            except:
                                                                                                pass
                return
        if op.type == 19:
            if Jmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        ke.kickoutFromGroup(op.param1,[op.param2])
                        time.sleep(0.008)
                        ke.inviteIntoGroup(op.param1,[op.param3])
                        ky.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                            time.sleep(0.008)
                            ki.inviteIntoGroup(op.param1,[op.param3])
                            ky.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                                time.sleep(0.008)
                                kk.inviteIntoGroup(op.param1,[op.param3])
                                ky.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    time.sleep(0.008)
                                    kc.inviteIntoGroup(op.param1,[op.param3])
                                    ky.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        km.kickoutFromGroup(op.param1,[op.param2])
                                        time.sleep(0.008)
                                        km.inviteIntoGroup(op.param1,[op.param3])
                                        ky.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            kb.kickoutFromGroup(op.param1,[op.param2])
                                            time.sleep(0.008)
                                            kb.inviteIntoGroup(op.param1,[op.param3])
                                            ky.acceptGroupInvitation(op.param1)
                                        except:
                                            try:
                                                kn.kickoutFromGroup(op.param1,[op.param2])
                                                time.sleep(0.008)
                                                kn.inviteIntoGroup(op.param1,[op.param3])
                                                ky.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    ko.kickoutFromGroup(op.param1,[op.param2])
                                                    time.sleep(0.008)
                                                    ko.inviteIntoGroup(op.param1,[op.param3])
                                                    ky.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        kw.kickoutFromGroup(op.param1,[op.param2])
                                                        time.sleep(0.008)
                                                        kw.inviteIntoGroup(op.param1,[op.param3])
                                                        ky.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            G = random.choice(ABC).getGroup(op.param1)
                                                            G.preventedJoinByTicket = False
                                                            random.choice(ABC).updateGroup(G)
                                                            Ticket = random.choice(ABC).reissueGroupTicket(op.param1)
                                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            km.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kn.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kw.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            ky.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            G = random.choice(ABC).getGroup(op.param1)
                                                            G.preventedJoinByTicket = True
                                                            random.choice(ABC).updateGroup(G)
                                                            Ticket = random.choice(ABC).reissueGroupTicket(op.param1)
                                                        except:
                                                            try:
                                                                ke.kickoutFromGroup(op.param1,[op.param2])
                                                                time.sleep(0.008)
                                                                ke.inviteIntoGroup(op.param1,[op.param3])
                                                                ky.acceptGroupInvitation(op.param1)
                                                            except:
                                                                try:
                                                                    ki.kickoutFromGroup(op.param1,[op.param2])
                                                                    time.sleep(0.008)
                                                                    ki.inviteIntoGroup(op.param1,[op.param3])
                                                                    ky.acceptGroupInvitation(op.param1)
                                                                except:
                                                                    try:
                                                                        kk.kickoutFromGroup(op.param1,[op.param2])
                                                                        time.sleep(0.008)
                                                                        kk.inviteIntoGroup(op.param1,[op.param3])
                                                                        ky.acceptGroupInvitation(op.param1)
                                                                    except:
                                                                        try:
                                                                            kc.kickoutFromGroup(op.param1,[op.param2])
                                                                            time.sleep(0.008)
                                                                            kc.inviteIntoGroup(op.param1,[op.param3])
                                                                            ky.acceptGroupInvitation(op.param1)
                                                                        except:
                                                                            try:
                                                                                km.kickoutFromGroup(op.param1,[op.param2])
                                                                                time.sleep(0.008)
                                                                                km.inviteIntoGroup(op.param1,[op.param3])
                                                                                ky.acceptGroupInvitation(op.param1)
                                                                            except:
                                                                                try:
                                                                                    kb.kickoutFromGroup(op.param1,[op.param2])
                                                                                    time.sleep(0.008)
                                                                                    kb.inviteIntoGroup(op.param1,[op.param3])
                                                                                    ky.acceptGroupInvitation(op.param1)
                                                                                except:
                                                                                    try:
                                                                                        kn.kickoutFromGroup(op.param1,[op.param2])
                                                                                        time.sleep(0.008)
                                                                                        kn.inviteIntoGroup(op.param1,[op.param3])
                                                                                        ky.acceptGroupInvitation(op.param1)
                                                                                    except:
                                                                                        try:
                                                                                            ko.kickoutFromGroup(op.param1,[op.param2])
                                                                                            time.sleep(0.008)
                                                                                            ko.inviteIntoGroup(op.param1,[op.param3])
                                                                                            ky.acceptGroupInvitation(op.param1)
                                                                                        except:
                                                                                            try:
                                                                                                kw.kickoutFromGroup(op.param1,[op.param2])
                                                                                                time.sleep(0.008)
                                                                                                kw.inviteIntoGroup(op.param1,[op.param3])
                                                                                                ky.acceptGroupInvitation(op.param1)
                                                                                            except:
                                                                                                pass
                    return
        if op.type == 19:
            if Zmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                        random.choice(ABC).inviteIntoGroup(op.param1,[op.param3])
                        cl.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                            random.choice(ABC).inviteIntoGroup(op.param1,[op.param3])
                            ki.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                random.choice(ABC).inviteIntoGroup(op.param1,[op.param3])
                                kk.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                    random.choice(ABC).inviteIntoGroup(op.param1,[op.param3])
                                    kc.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                        random.choice(ABC).inviteIntoGroup(op.param1,[op.param3])
                                        km.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                            random.choice(ABC).inviteIntoGroup(op.param1,[op.param3])
                                            kb.acceptGroupInvitation(op.param1)
                                        except:
                                            try:
                                                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                                random.choice(ABC).inviteIntoGroup(op.param1,[op.param3])
                                                kn.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                                    random.choice(ABC).inviteIntoGroup(op.param1,[op.param3])
                                                    ko.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                                        random.choice(ABC).inviteIntoGroup(op.param1,[op.param3])
                                                        kw.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            G = random.choice(ABC).getGroup(op.param1)
                                                            G.preventedJoinByTicket = False
                                                            random.choice(ABC).updateGroup(G)
                                                            Ticket = random.choice(ABC).reissueGroupTicket(op.param1)
                                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            km.acceptGroupInvitationByTicket(op.param1,Ticket) 
                                                            kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kn.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kw.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            ky.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            G = random.choice(ABC).getGroup(op.param1)
                                                            G.preventedJoinByTicket = True
                                                            random.choice(ABC).updateGroup(G)
                                                            Ticket = random.choice(ABC).reissueGroupTicket(op.param1)
                                                        except:
                                                            try:
                                                                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                                                random.choice(ABC).inviteIntoGroup(op.param1,[op.param3])
                                                                ke.acceptGroupInvitation(op.param1)
                                                            except:
                                                                try:
                                                                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                                                    random.choice(ABC).inviteIntoGroup(op.param1,[op.param3])
                                                                    ky.acceptGroupInvitation(op.param1)
                                                                except:
                                                                    try:
                                                                        random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                                                        random.choice(ABC).inviteIntoGroup(op.param1,[op.param3])
                                                                        cl.acceptGroupInvitation(op.param1)
                                                                    except:
                                                                        try:
                                                                            random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                                                            random.choice(ABC).inviteIntoGroup(op.param1,[op.param3])
                                                                            ki.acceptGroupInvitation(op.param1)
                                                                        except:
                                                                            try:
                                                                                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                                                                random.choice(ABC).inviteIntoGroup(op.param1,[op.param3])
                                                                                kk.acceptGroupInvitation(op.param1)
                                                                            except:
                                                                                try:
                                                                                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                                                                    random.choice(ABC).inviteIntoGroup(op.param1,[op.param3])
                                                                                    kc.acceptGroupInvitation(op.param1)
                                                                                except:
                                                                                    try:
                                                                                        random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                                                                        random.choice(ABC).inviteIntoGroup(op.param1,[op.param3])
                                                                                        km.acceptGroupInvitation(op.param1)
                                                                                    except:
                                                                                        try:
                                                                                            random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                                                                            random.choice(ABC).inviteIntoGroup(op.param1,[op.param3])
                                                                                            kb.acceptGroupInvitation(op.param1)
                                                                                        except:
                                                                                            try:
                                                                                                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                                                                                random.choice(ABC).inviteIntoGroup(op.param1,[op.param3])
                                                                                                kn.acceptGroupInvitation(op.param1)
                                                                                            except:
                                                                                                pass
                    return

        if op.type == 55:
            if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                wait["blacklist"][op.param2] = True
                try:
                    ki.cancelGroupInvitation(op.param1,[op.param3])
                    ki.kickoutFromGroup(op.param1,[op.param2])
                except:
                    try:
                        kk.cancelGroupInvitation(op.param1,[op.param3])
                        kk.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            kc.cancelGroupInvitation(op.param1,[op.param3])
                            kc.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                km.cancelGroupInvitation(op.param1,[op.param3])
                                km.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    kb.cancelGroupInvitation(op.param1,[op.param3])
                                    kb.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        kn.cancelGroupInvitation(op.param1,[op.param3])
                                        kn.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            ko.cancelGroupInvitation(op.param1,[op.param3])
                                            ko.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            try:
                                                kw.cancelGroupInvitation(op.param1,[op.param3])
                                                kw.kickoutFromGroup(op.param1,[op.param2])
                                            except:
                                                try:
                                                    ke.cancelGroupInvitation(op.param1,[op.param3])
                                                    ke.kickoutFromGroup(op.param1,[op.param2])
                                                except:
                                                    try:
                                                        ky.cancelGroupInvitation(op.param1,[op.param3])
                                                        ky.kickoutFromGroup(op.param1,[op.param2])
                                                    except:
                                                        pass
#======================================================================================================#
                return

            if admin in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                        random.choice(ABC).findAndAddContactsByMid(op.param1,admin)
                        random.choice(ABC).inviteIntoGroup(op.param1,admin)
                    except:
                        pass

                return

            if staff in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                        random.choice(ABC).findAndAddContactsByMid(op.param1,staff)
                        random.choice(ABC).inviteIntoGroup(op.param1,staff)
                    except:
                        pass

                return

        if op.type == 55:
            try:
                if op.param1 in Setmain["ARreadPoint"]:
                   if op.param2 in Setmain["ARreadMember"][op.param1]:
                       pass
                   else:
                       Setmain["ARreadMember"][op.param1][op.param2] = True
                else:
                   pass
            except:
                pass

            if cctv['cyduk'][op.param1]==True:
                if op.param1 in cctv['point']:
                    Name = cl.getContact(op.param2).displayName
                    if Name in cctv['sidermem'][op.param1]:
                        pass
                    else:
                        cctv['sidermem'][op.param1] += "\n~ " + Name
                        siderMembers(op.param1, [op.param2])
                        contact = cl.getContact(op.param2)
                        #image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                        cl.sendImageWithURL(op.param1, image)                        
                        
        if op.type == 55:
            if op.param2 in wait["blacklist"]:
                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
            else:
                pass

        if op.type == 26:
           if wait["selfbot"] == True:
               msg = op.message
               if msg._from not in Bots:
                 if wait["talkban"] == True:
                   if msg._from in wait["Talkblacklist"]:
                      try:
                          random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
                      except:
                          try:
                              random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
                          except:
                              random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
               if msg._from not in Bots:
                 if wait["talkban"] == True:
                   if msg._from in wait["Talkblacklist"]:
                      try:
                          random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
                      except:
                          try:
                              random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
                          except:
                              random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention"] == True:
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           cl.sendMessage(msg.to, wait["Respontag"])
                           cl.sendMessage(msg.to, None, contentMetadata={"STKID":"136","STKPKGID":"1","STKVER":"100"}, contentType=7)
                           break
               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["Mentionkick"] == True:
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           cl.mentiontag(msg.to,[msg._from])
                           cl.sendMessage(msg.to, "Jangan tag saya....")
                           cl.kickoutFromGroup(msg.to, [msg._from])
                           break
               if msg.contentType == 7:
                 if wait["sticker"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,"「Cek ID Sticker」\n❧STKID : " + msg.contentMetadata["STKID"] + "\n❧STKPKGID : " + msg.contentMetadata["STKPKGID"] + "\n❧STKVER : " + msg.contentMetadata["STKVER"]+ "\n\n「Link Sticker」" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        path = cl.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        cl.sendMessage(msg.to,"❧Nama : " + msg.contentMetadata["displayName"] + "\n❧MID : " + msg.contentMetadata["mid"] + "\n❧Status Msg : " + contact.statusMessage + "\n❧Picture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        cl.sendImageWithURL(msg.to, image)

        if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 2:
               if msg.toType == 0:
                    to = receiver
               elif msg.toType == 2:
                    to = receiver
               if msg.contentType == 7:
                 if wait["sticker"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,"STKID : " + msg.contentMetadata["STKID"] + "\nSTKPKGID : " + msg.contentMetadata["STKPKGID"] + "\nSTKVER : " + msg.contentMetadata["STKVER"]+ "\n\n「Link Sticker」" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        path = cl.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        cl.sendMessage(msg.to,"❧Nama : " + msg.contentMetadata["displayName"] + "\n❧MID : " + msg.contentMetadata["mid"] + "\n❧Status Msg : " + contact.statusMessage + "\n❧Picture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        cl.sendImageWithURL(msg.to, image)
#ADD Bots
               if msg.contentType == 13:
                 if msg._from in admin:
                  if wait["addbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        cl.sendMessage(msg.to,"Contact itu sudah jadi anggota bot")
                        wait["addbots"] = True
                    else:
                        Bots.append(msg.contentMetadata["mid"])
                        wait["addbots"] = True
                        cl.sendMessage(msg.to,"Successfully Become ke anggota bot")
                 if wait["dellbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        Bots.remove(msg.contentMetadata["mid"])
                        cl.sendMessage(msg.to,"Successfully deleted dari anggota bot")
                    else:
                        wait["dellbots"] = True
                        cl.sendMessage(msg.to,"Contact itu bukan anggota bot Dpk")
#ADD STAFF
                 if msg._from in admin:
                  if wait["addstaff"] == True:
                    if msg.contentMetadata["mid"] in staff:
                        cl.sendMessage(msg.to,"Contact itu sudah jadi staff")
                        wait["addstaff"] = True
                    else:
                        staff.append(msg.contentMetadata["mid"])
                        wait["addstaff"] = True
                        cl.sendMessage(msg.to,"Successfully Become ke staff")
                 if wait["dellstaff"] == True:
                    if msg.contentMetadata["mid"] in staff:
                        staff.remove(msg.contentMetadata["mid"])
                        cl.sendMessage(msg.to,"Successfully deleted dari staff")
                        wait["dellstaff"] = True
                    else:
                        wait["dellstaff"] = True
                        cl.sendMessage(msg.to,"Contact itu bukan staff")
#ADD ADMIN
                 if msg._from in admin:
                  if wait["addmin"] == True:
                    if msg.contentMetadata["mid"] in admin:
                        cl.sendMessage(msg.to,"Contact admin")
                        wait["addmin"] = True
                    else:
                        admin.append(msg.contentMetadata["mid"])
                        wait["addmin"] = True
                        cl.sendMessage(msg.to,"Successfully Become ke admin")
                 if wait["delladmin"] == True:
                    if msg.contentMetadata["mid"] in admin:
                        admin.remove(msg.contentMetadata["mid"])
                        cl.sendMessage(msg.to,"Successfully deleted dari admin")
                    else:
                        wait["delladmin"] = True
                        cl.sendMessage(msg.to,"Contact itu bukan admin")
#ADD BLACKLIST
                 if msg._from in admin:
                  if wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendMessage(msg.to,"Contact itu sudah ada di blacklist")
                        wait["wblacklist"] = True
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = True
                        cl.sendMessage(msg.to,"Successfully Become ke blacklist user")
                  if wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendMessage(msg.to,"Successfully deleted dari blacklist user")
                    else:
                        wait["dblacklist"] = True
                        cl.sendMessage(msg.to,"Contact itu tidak ada di blacklist")
#TALKBAN
                 if msg._from in admin:
                  if wait["Talkwblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["Talkblacklist"]:
                        cl.sendMessage(msg.to,"Contact itu sudah ada di Talkban")
                        wait["Talkwblacklist"] = True
                    else:
                        wait["Talkblacklist"][msg.contentMetadata["mid"]] = True
                        wait["Talkwblacklist"] = True
                        cl.sendMessage(msg.to,"Successfully Become ke Talkban user")
                  if wait["Talkdblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["Talkblacklist"]:
                        del wait["Talkblacklist"][msg.contentMetadata["mid"]]
                        cl.sendMessage(msg.to,"Successfully deleted dari Talkban user")
                    else:
                        wait["Talkdblacklist"] = True
                        cl.sendMessage(msg.to,"Contact itu tidak ada di Talkban")
#UPDATE FOTO
               if msg.contentType == 1:
                 if msg._from in admin:
                    if Setmain["Addimage"] == True:
                        msgid = msg.id
                        fotoo = "https://obs.line-apps.com/talk/m/download.nhn?oid="+msgid
                        headers = cl.Talk.Headers
                        r = requests.get(fotoo, headers=headers, stream=True)
                        if r.status_code == 200:
                            path = os.path.join(os.path.dirname(__file__), 'dataPhotos/%s.jpg' % Setmain["Img"])
                            with open(path, 'wb') as fp:
                                shutil.copyfileobj(r.raw, fp)
                            cl.sendText(msg.to, "Successfully Become gambar")
                        Setmain["Img"] = {}
                        Setmain["Addimage"] = False

               if msg.toType == 2:
                 if msg._from in admin:
                   if settings["groupPicture"] == True:
                     path = cl.downloadObjectMsg(msg_id)
                     settings["groupPicture"] = False
                     cl.updateGroupPicture(msg.to, path)
                     cl.sendMessage(msg.to, "Successfully mengubah foto group")

               if msg.contentType == 1:
                   if msg._from in admin:
                       if mid in Setmain["ARfoto"]:
                            path = cl.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][mid]
                            cl.updateProfilePicture(path)
                            cl.sendMessage(msg.to,"Foto Successfully dirubah")

               if msg.contentType == 1:
                 if msg._from in admin:
                        if Amid in Setmain["ARfoto"]:
                            path = ki.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][Amid]
                            ki.updateProfilePicture(path)
                            ki.sendMessage(msg.to,"Foto Successfully dirubah")
                        elif Bmid in Setmain["ARfoto"]:
                            path = kk.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][Bmid]
                            kk.updateProfilePicture(path)
                            kk.sendMessage(msg.to,"Foto Successfully dirubah")
                        elif Cmid in Setmain["ARfoto"]:
                            path = kc.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][Cmid]
                            kc.updateProfilePicture(path)
                            kc.sendMessage(msg.to,"Foto Successfully dirubah")
                        elif Dmid in Setmain["ARfoto"]:
                            path = km.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][Dmid]
                            km.updateProfilePicture(path)
                            km.sendMessage(msg.to,"Foto Successfully dirubah")
                        elif Emid in Setmain["ARfoto"]:
                            path = kb.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][Emid]
                            kb.updateProfilePicture(path)
                            kb.sendMessage(msg.to,"Foto Successfully dirubah")
                        elif Fmid in Setmain["ARfoto"]:
                            path = kn.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][Fmid]
                            kn.updateProfilePicture(path)
                            kn.sendMessage(msg.to,"Foto Successfully dirubah")
                        elif Gmid in Setmain["ARfoto"]:
                            path = ko.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][Gmid]
                            ko.updateProfilePicture(path)
                            ko.sendMessage(msg.to,"Foto Successfully dirubah")
                        elif Hmid in Setmain["ARfoto"]:
                            path = kw.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][Hmid]
                            kw.updateProfilePicture(path)
                            kw.sendMessage(msg.to,"Foto Successfully dirubah")
                        elif Imid in Setmain["ARfoto"]:
                            path = ke.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][Imid]
                            ke.updateProfilePicture(path)
                            ke.sendMessage(msg.to,"Foto Successfully dirubah")
                        elif Jmid in Setmain["ARfoto"]:
                            path = ky.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][Jmid]
                            ky.updateProfilePicture(path)
                            ky.sendMessage(msg.to,"Foto Successfully dirubah")
                        elif Zmid in Setmain["ARfoto"]:
                            path = sw.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][Zmid]
                            sw.updateProfilePicture(path)
                            sw.sendMessage(msg.to,"Foto Successfully dirubah")

               if msg.contentType == 1:
                 if msg._from in admin:
                   if settings["changePicture"] == True:
                     path1 = ki.downloadObjectMsg(msg_id)
                     path2 = kk.downloadObjectMsg(msg_id)
                     path3 = kc.downloadObjectMsg(msg_id)
                     path4 = km.downloadObjectMsg(msg_id)
                     path5 = kb.downloadObjectMsg(msg_id)
                     path6 = kn.downloadObjectMsg(msg_id)
                     path7 = ko.downloadObjectMsg(msg_id)
                     path8 = kw.downloadObjectMsg(msg_id)
                     path9 = ke.downloadObjectMsg(msg_id)
                     path10 = ky.downloadObjectMsg(msg_id)
                     path11 = sw.downloadObjectMsg(msg_id)
                     settings["changePicture"] = False
                     ki.updateProfilePicture(path1)
                     ki.sendMessage(msg.to, "Successfully mengubah foto profile bot")
                     kk.updateProfilePicture(path2)
                     kk.sendMessage(msg.to, "Successfully mengubah foto profile bot")
                     kc.updateProfilePicture(path3)
                     kc.sendMessage(msg.to, "Successfully mengubah foto profile bot")
                     km.updateProfilePicture(path4)
                     km.sendMessage(msg.to, "Successfully mengubah foto profile bot")
                     kb.updateProfilePicture(path5)
                     kb.sendMessage(msg.to, "Successfully mengubah foto profile bot")
                     kn.updateProfilePicture(path6)
                     kn.sendMessage(msg.to, "Successfully mengubah foto profile bot")
                     ko.updateProfilePicture(path7)
                     ko.sendMessage(msg.to, "Successfully mengubah foto profile bot")
                     kw.updateProfilePicture(path8)
                     kw.sendMessage(msg.to, "Successfully mengubah foto profile bot")
                     ke.updateProfilePicture(path9)
                     ke.sendMessage(msg.to, "Successfully mengubah foto profile bot")
                     ky.updateProfilePicture(path10)
                     ky.sendMessage(msg.to, "Successfully mengubah foto profile bot")
                     sw.updateProfilePicture(path11)
                     sw.sendMessage(msg.to, "Successfully mengubah foto profile bot")

               if msg.contentType == 0:
                    if Setmain["autoRead"] == True:
                        cl.sendChatChecked(msg.to, msg_id)
                        ki.sendChatChecked(msg.to, msg_id)
                        kk.sendChatChecked(msg.to, msg_id)
                        kc.sendChatChecked(msg.to, msg_id)
                        km.sendChatChecked(msg.to, msg_id)
                        kb.sendChatChecked(msg.to, msg_id)
                        kn.sendChatChecked(msg.to, msg_id)
                        ko.sendChatChecked(msg.to, msg_id)
                        kw.sendChatChecked(msg.to, msg_id)
                        ke.sendChatChecked(msg.to, msg_id)
                        ky.sendChatChecked(msg.to, msg_id)
                        sw.sendChatChecked(msg.to, msg_id)
                    if text is None:
                        return
                    
                    else:
                        cmd = command(text)
                        if cmd == "h":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpMessage = help()
                               cl.sendMessage(msg.to, str(helpMessage))
                                                                                       
                        if cmd == "เปิดบอท":
                            if msg._from in admin:
                                wait["selfbot"] = True
                                cl.sendText(msg.to, "เปิดระบบทำงานคิก10ตัวแล้ว..")
                                
                        elif cmd == "ปิดบอท":
                            if msg._from in admin:
                                wait["selfbot"] = False
                                cl.sendText(msg.to, "ปิดระบบทำงานคิก10ตัวแล้ว")
                                            
                        elif cmd == "hb":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpMessage1 = helpbot()
                               cl.sendMessage(msg.to, str(helpMessage1))

                        elif cmd == "hg":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpMessage2 = helpgroup()
                               cl.sendMessage(msg.to, str(helpMessage2))

                        elif cmd == "set":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                md = "SELFBOT\n\n"
                                if wait["sticker"] == True: md+=" Sticker「 ✔ 」\n"
                                else: md+=" Sticker「 ✖ 」\n"
                                if wait["contact"] == True: md+=" Contact「 ✔ 」\n"
                                else: md+=" Contact「 ✖ 」\n"
                                if wait["talkban"] == True: md+=" Talkban「 ✔ 」\n"
                                else: md+=" Talkban「 ✖ 」\n"
                                if wait["Mentionkick"] == True: md+=" Notag「 ✔ 」\n"
                                else: md+=" Notag「 ✖ 」\n"
                                if wait["detectMention"] == True: md+=" Respon「 ✔ 」\n"
                                else: md+=" Respon「 ✖ 」\n"
                                if wait["autoJoin"] == True: md+=" Autojoin「 ✔ 」\n"
                                else: md+=" Autojoin「 ✖ 」\n"
                                if wait["autoAdd"] == True: md+=" Autoadd「 ✔ 」\n"
                                else: md+=" Autoadd「 ✖ 」\n"
                                if msg.to in welcome: md+=" Welcome「 ✔ 」\n"
                                else: md+=" Welcome「 ✖ 」\n"
                                if wait["autoLeave"] == True: md+=" Autoleave「 ✔ 」\n"
                                else: md+=" Autoleave「 ✖ 」\n"
                                if msg.to in protectqr: md+=" Protecturl「 ✔ 」\n"
                                else: md+=" Protecturl「 ✖ 」\n"
                                if msg.to in protectjoin: md+=" Protectjoin「 ✔ 」\n"
                                else: md+=" Protectjoin「 ✖ 」\n"
                                if msg.to in protectkick: md+=" Protectkick「 ✔ 」\n"
                                else: md+=" Protectkick「 ✖ 」\n"
                                if msg.to in protectinvite: md+=" Protectinvite「 ✔ 」\n"
                                else: md+=" Protectinvite「 ✖ 」\n"
                                if msg.to in protectcancel: md+=" Protectcancel「 ✔ 」\n"
                                else: md+=" Protectcancel「 ✖ 」\n"
                                if msg.to in protectantijs: md+=" js「 ✔ 」\n"
                                else: md+=" js「 ✖ 」\n"  
                                if msg.to in ghost: md+=" ผี「 ✔ 」\n"
                                else: md+=" ผี「 ✖ 」\n"                                   
                                cl.sendMessage(msg.to, md+"\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")

                        elif cmd == "creator" or text.lower() == 'ผส':
                            #if msg._from in admin:
                                cl.sendText(msg.to,"「 CREATOR 」") 
                                ma = ""
                                for i in creator:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "about" or cmd == "informasi":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sendMention(msg.to, sender, "「 Type Selfbot 」\n")
                               cl.sendMessage(msg.to, None, contentMetadata={'mid': mid}, contentType=13)

                        elif cmd == "me" or text.lower() == 'มี':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': mid}
                               cl.sendMessage1(msg)
 
                        elif text.lower() == "มิด":
                               cl.sendMessage(msg.to, msg._from)

                        elif ("มิด " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = cl.getContact(key1)
                               cl.sendMessage(msg.to, "Nama : "+str(mi.displayName)+"\nMID : " +key1)
                               cl.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)

                        elif ("ตัส " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = cl.getContact(key1)
                               cl.sendMessage(msg.to, "❧Nama : "+str(mi.displayName)+"\n❧Mid : " +key1+"\n❧Status Msg"+str(mi.statusMessage))
                               cl.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)
                               if "videoProfile='{" in str(cl.getContact(key1)):
                                   cl.sendVideoWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath)+'/vp.small')
                               else:
                                   cl.sendImageWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath))
                                    
                                
                        elif "ดึง " in msg.text:
                            if msg._from in admin:                                                                                                                                       
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]                                                                                                                                
                               targets = []
                               for x in key["MENTIONEES"]:                                                                                                                                  
                                   targets.append(x["M"])
                               for target in targets:                                                                                                                                       
                                   try:
                                      cl.findAndAddContactsByMid(target)
                                      cl.inviteIntoGroup(msg.to,[target])
                                   except:
                                       pass

                        elif cmd == "mybot":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Amid}
                               cl.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Bmid}
                               cl.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Cmid}
                               cl.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Dmid}
                               cl.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Emid}
                               cl.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Fmid}
                               cl.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Gmid}
                               cl.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Hmid}
                               cl.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Imid}
                               cl.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Jmid}
                               cl.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Zmid}
                               cl.sendMessage1(msg)

                        elif text.lower() == "ลบแชท":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               try:
                                   cl.removeAllMessages(op.param2)
                               except:
                                   pass

                        elif text.lower() == "ลบแชทคิก":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               try:
                                   ki.removeAllMessages(op.param2)
                                   kk.removeAllMessages(op.param2)
                                   kc.removeAllMessages(op.param2)
                                   km.removeAllMessages(op.param2)
                                   kb.removeAllMessages(op.param2)
                                   kn.removeAllMessages(op.param2)
                                   ko.removeAllMessages(op.param2)
                                   kw.removeAllMessages(op.param2)
                                   ke.removeAllMessages(op.param2)
                                   ky.removeAllMessages(op.param2)
                                   ki.sendText(msg.to,"Chat dibersihkan...")
                                   kk.sendText(msg.to,"Chat dibersihkan...")
                                   kc.sendText(msg.to,"Chat dibersihkan...")
                                   km.sendText(msg.to,"Chat dibersihkan...")
                                   kb.sendText(msg.to,"Chat dibersihkan...")
                                   kn.sendText(msg.to,"Chat dibersihkan...")
                                   ko.sendText(msg.to,"Chat dibersihkan...")
                                   kw.sendText(msg.to,"Chat dibersihkan...")
                                   ke.sendText(msg.to,"Chat dibersihkan...")
                                   ky.sendText(msg.to,"Chat dibersihkan...")
                               except:
                                   pass
                                
                        elif cmd == "addbot":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               try:
                                   cl.findAndAddContactsByMid(Amid)
                                   cl.findAndAddContactsByMid(Bmid)
                                   cl.findAndAddContactsByMid(Cmid)
                                   cl.findAndAddContactsByMid(Dmid)
                                   cl.findAndAddContactsByMid(Emid)
                                   cl.findAndAddContactsByMid(Fmid) 
                                   cl.findAndAddContactsByMid(Gmid)
                                   cl.findAndAddContactsByMid(Hmid)
                                   cl.findAndAddContactsByMid(Imid)
                                   cl.findAndAddContactsByMid(Jmid)
                                   cl.findAndAddContactsByMid(Zmid)                                                         
                                   ki.findAndAddContactsByMid(mid)                                                               
                                   ki.findAndAddContactsByMid(Cmid)
                                   ki.findAndAddContactsByMid(Dmid)
                                   ki.findAndAddContactsByMid(Emid)
                                   ki.findAndAddContactsByMid(Fmid)                                                              
                                   ki.findAndAddContactsByMid(Gmid)
                                   ki.findAndAddContactsByMid(Hmid)                                
                                   ki.findAndAddContactsByMid(Imid)
                                   ki.findAndAddContactsByMid(Jmid)
                                   ki.findAndAddContactsByMid(Zmid)
                                   kk.findAndAddContactsByMid(mid)                                                             
                                   kk.findAndAddContactsByMid(Bmid)
                                   kk.findAndAddContactsByMid(Dmid)
                                   kk.findAndAddContactsByMid(Emid)
                                   kk.findAndAddContactsByMid(Fmid)                                                              
                                   kk.findAndAddContactsByMid(Gmid)
                                   kk.findAndAddContactsByMid(Hmid)                                
                                   kk.findAndAddContactsByMid(Imid)
                                   kk.findAndAddContactsByMid(Jmid)
                                   kk.findAndAddContactsByMid(Zmid)
                                   kc.findAndAddContactsByMid(mid)                                
                                   kc.findAndAddContactsByMid(Bmid)                              
                                   kc.findAndAddContactsByMid(Dmid)
                                   kc.findAndAddContactsByMid(Emid)
                                   kc.findAndAddContactsByMid(Fmid)                                                              
                                   kc.findAndAddContactsByMid(Gmid)
                                   kc.findAndAddContactsByMid(Hmid)                                
                                   kc.findAndAddContactsByMid(Imid)
                                   kc.findAndAddContactsByMid(Jmid)
                                   kc.findAndAddContactsByMid(Zmid)
                                   km.findAndAddContactsByMid(mid)                                
                                   km.findAndAddContactsByMid(Bmid)
                                   km.findAndAddContactsByMid(Cmid)                                
                                   km.findAndAddContactsByMid(Emid)
                                   km.findAndAddContactsByMid(Fmid)                                                              
                                   km.findAndAddContactsByMid(Gmid)
                                   km.findAndAddContactsByMid(Hmid)                                
                                   km.findAndAddContactsByMid(Imid)
                                   km.findAndAddContactsByMid(Jmid)
                                   km.findAndAddContactsByMid(Zmid)
                                   kb.findAndAddContactsByMid(mid)                                
                                   kb.findAndAddContactsByMid(Bmid)
                                   kb.findAndAddContactsByMid(Cmid)
                                   kb.findAndAddContactsByMid(Dmid)                                
                                   kb.findAndAddContactsByMid(Fmid)                                                              
                                   kb.findAndAddContactsByMid(Gmid)
                                   kb.findAndAddContactsByMid(Hmid)                                
                                   kb.findAndAddContactsByMid(Imid)
                                   kb.findAndAddContactsByMid(Jmid)
                                   kb.findAndAddContactsByMid(Zmid)
                                   kn.findAndAddContactsByMid(mid)                                
                                   kn.findAndAddContactsByMid(Bmid)
                                   kn.findAndAddContactsByMid(Cmid)
                                   kn.findAndAddContactsByMid(Dmid)
                                   kn.findAndAddContactsByMid(Emid)
                                   kn.findAndAddContactsByMid(Fmid)                                                              
                                   kn.findAndAddContactsByMid(Gmid)
                                   kn.findAndAddContactsByMid(Hmid)                                
                                   kn.findAndAddContactsByMid(Imid)
                                   kn.findAndAddContactsByMid(Jmid)
                                   kn.findAndAddContactsByMid(Zmid)
                                   ko.findAndAddContactsByMid(mid)                                
                                   ko.findAndAddContactsByMid(Bmid)
                                   ko.findAndAddContactsByMid(Cmid)
                                   ko.findAndAddContactsByMid(Dmid)
                                   ko.findAndAddContactsByMid(Emid)
                                   ko.findAndAddContactsByMid(Fmid)                                                              
                                   ko.findAndAddContactsByMid(Gmid)
                                   ko.findAndAddContactsByMid(Hmid)                                
                                   ko.findAndAddContactsByMid(Imid)
                                   ko.findAndAddContactsByMid(Jmid)
                                   ko.findAndAddContactsByMid(Zmid)
                                   kw.findAndAddContactsByMid(mid)                                
                                   kw.findAndAddContactsByMid(Bmid)
                                   kw.findAndAddContactsByMid(Cmid)
                                   kw.findAndAddContactsByMid(Dmid)
                                   kw.findAndAddContactsByMid(Emid)
                                   kw.findAndAddContactsByMid(Fmid)                                                              
                                   kw.findAndAddContactsByMid(Gmid)
                                   kw.findAndAddContactsByMid(Hmid)                                
                                   kw.findAndAddContactsByMid(Imid)
                                   kw.findAndAddContactsByMid(Jmid)
                                   kw.findAndAddContactsByMid(Zmid)
                                   ke.findAndAddContactsByMid(mid)                                
                                   ke.findAndAddContactsByMid(Bmid)
                                   ke.findAndAddContactsByMid(Cmid)
                                   ke.findAndAddContactsByMid(Dmid)
                                   ke.findAndAddContactsByMid(Emid)
                                   ke.findAndAddContactsByMid(Fmid)                                                              
                                   ke.findAndAddContactsByMid(Gmid)
                                   ke.findAndAddContactsByMid(Hmid)                                
                                   ke.findAndAddContactsByMid(Imid)
                                   ke.findAndAddContactsByMid(Jmid)
                                   ke.findAndAddContactsByMid(Zmid) 
                                   ky.findAndAddContactsByMid(mid)                                
                                   ky.findAndAddContactsByMid(Bmid)
                                   ky.findAndAddContactsByMid(Cmid)
                                   ky.findAndAddContactsByMid(Dmid)
                                   ky.findAndAddContactsByMid(Emid)
                                   ky.findAndAddContactsByMid(Fmid)                                                              
                                   ky.findAndAddContactsByMid(Gmid)
                                   ky.findAndAddContactsByMid(Hmid)                                
                                   ky.findAndAddContactsByMid(Imid)
                                   ky.findAndAddContactsByMid(Jmid)
                                   ky.findAndAddContactsByMid(Zmid)
                                   sw.findAndAddContactsByMid(mid)                                
                                   sw.findAndAddContactsByMid(Bmid)
                                   sw.findAndAddContactsByMid(Cmid)
                                   sw.findAndAddContactsByMid(Dmid)
                                   sw.findAndAddContactsByMid(Emid)
                                   sw.findAndAddContactsByMid(Fmid)                                                              
                                   sw.findAndAddContactsByMid(Gmid)
                                   sw.findAndAddContactsByMid(Hmid)                                
                                   sw.findAndAddContactsByMid(Imid)
                                   sw.findAndAddContactsByMid(Jmid)                                                                                   
                                   cl.sendMessage(to,"Sucsess!!!")
                               except:
                                   cl.sendMessage(to,"Sucess! add all bots...Ok")

                        elif cmd.startswith("broadcast: "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sep = text.split(" ")
                               pesan = text.replace(sep[0] + " ","")
                               saya = cl.getGroupIdsJoined()
                               for group in saya:
                                   cl.sendMessage(group,"[ SELFBOT ]\n" + str(pesan))

                        elif text.lower() == "mykey":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "「Mykey」\nSetkey bot mu「 " + str(Setmain["keyCommand"]) + " 」")
                               
                        elif cmd.startswith("setkey "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   cl.sendMessage(msg.to, "Gagal mengganti key")
                               else:
                                   Setmain["keyCommand"] = str(key).lower()
                                   cl.sendMessage(msg.to, "「Setkey」\nSetkey diganti jadi「{}」".format(str(key).lower()))

                        elif text.lower() == "resetkey":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               Setmain["keyCommand"] = ""
                               cl.sendMessage(msg.to, "「Setkey」\nSetkey mu kembali ke awal")

                        elif cmd == "รี":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "ใช้เวลารีระบบ 3วิ กรุนารอซักครู่...")
                               Setmain["restartPoint"] = msg.to
                               cl.sendMessage(msg.to, "รีระบบเส็ดแล้ว...")
                               restartBot()
                            
                        elif cmd == "ออน":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               eltime = time.time() - mulai
                               bot = "Aktif " +waktu(eltime)
                               cl.sendMessage(msg.to,bot)
                            
                        elif cmd == "ginfo":
                          if msg._from in admin:
                            try:
                                G = cl.getGroup(msg.to)
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                cl.sendMessage(msg.to, "❧Bot Fams Grup Info\n\n❧Nama Group : {}".format(G.name)+ "\n❧ID Group : {}".format(G.id)+ "\n❧Pembuat : {}".format(G.creator.displayName)+ "\n❧Waktu Dibuat : {}".format(str(timeCreated))+ "\n❧Jumlah Member : {}".format(str(len(G.members)))+ "\n❧Jumlah Pending : {}".format(gPending)+ "\n❧Group Qr : {}".format(gQr)+ "\n❧Group Ticket : {}".format(gTicket))
                                cl.sendMessage(msg.to, None, contentMetadata={'mid': G.creator.mid}, contentType=13)
                                cl.sendImageWithURL(msg.to, 'http://dl.profile.line-cdn.net/'+G.pictureStatus)
                            except Exception as e:
                                cl.sendMessage(msg.to, str(e))
                      
                        elif cmd == "fiendlist":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = cl.getAllContactIds()
                               for i in gid:
                                   G = cl.getContact(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "╠ " + str(a) + ". " +G.displayName+ "\n"
                               cl.sendMessage(msg.to,"╔══[ FRIEND LIST ]\n║\n"+ma+"║\n╚══[ Total「"+str(len(gid))+"」Friends ]")

                        elif cmd == "รายชื่อกลุ่ม":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = cl.getGroupIdsJoined()
                               for i in gid:
                                   G = cl.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "╠ " + str(a) + ". " +G.name+ "\n"
                               cl.sendMessage(msg.to,"╔══[ GROUP LIST ]\n║\n"+ma+"║\n╚══[ Total「"+str(len(gid))+"」Groups ]")

                        elif cmd == "gruplist1":
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = ki.getGroupIdsJoined()
                               for i in gid:
                                   G = ki.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "╠ " + str(a) + ". " +G.name+ "\n"
                               ki.sendMessage(msg.to,"╔══[ GROUP LIST ]\n║\n"+ma+"║\n╚══[ Total「"+str(len(gid))+"」Groups ]")

                        elif cmd == "gruplist2":
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = kk.getGroupIdsJoined()
                               for i in gid:
                                   G = kk.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "╠ " + str(a) + ". " +G.name+ "\n"
                               kk.sendMessage(msg.to,"╔══[ GROUP LIST ]\n║\n"+ma+"║\n╚══[ Total「"+str(len(gid))+"」Groups ]")

                        elif cmd == "gruplist3":
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = kc.getGroupIdsJoined()
                               for i in gid:
                                   G = kc.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "╠ " + str(a) + ". " +G.name+ "\n"
                               kc.sendMessage(msg.to,"╔══[ GROUP LIST ]\n║\n"+ma+"║\n╚══[ Total「"+str(len(gid))+"」Groups ]")

                        elif cmd == "เปิดลิ้ง":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   X = cl.getGroup(msg.to)
                                   X.preventedJoinByTicket = False
                                   cl.updateGroup(X)
                                   cl.sendMessage(msg.to, "Url Opened")

                        elif cmd == "ปิดลิ้ง":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   X = cl.getGroup(msg.to)
                                   X.preventedJoinByTicket = True
                                   cl.updateGroup(X)
                                   cl.sendMessage(msg.to, "Url Closed")

                        elif cmd == "ลิ้ง":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   x = cl.getGroup(msg.to)
                                   if x.preventedJoinByTicket == True:
                                      x.preventedJoinByTicket = False
                                      cl.updateGroup(x)
                                   gurl = cl.reissueGroupTicket(msg.to)
                                   cl.sendMessage(msg.to, "Nama : "+str(x.name)+ "\nUrl grup : http://line.me/R/ti/g/"+gurl)

#===========BOT UPDATE============#
                        elif cmd == "upg":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if msg.toType == 2:
                                settings["groupPicture"] = True
                                cl.sendText(msg.to,"ส่งรู)มาค่ะ.....")

                        elif cmd == "upp":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                settings["changePicture"] = True
                                cl.sendText(msg.to,"ส่งรู)มาค่ะ.....")
                                
                        elif cmd == "up":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                Setmain["ARfoto"][mid] = True
                                cl.sendText(msg.to,"ส่งรูปมาค่ะ.....")
                                
                        elif cmd == "1up":
                            if msg._from in admin:
                                Setmain["ARfoto"][Amid] = True
                                ki.sendText(msg.to,"ส่งรูปมาค่ะ.....")
                                
                        elif cmd == "2up":
                            if msg._from in admin:
                                Setmain["ARfoto"][Bmid] = True
                                kk.sendText(msg.to,"ส่งรูปมาค่ะ.....")
                                
                        elif cmd == "3up":
                            if msg._from in admin:
                                Setmain["ARfoto"][Cmid] = True
                                kc.sendText(msg.to,"ส่งรูปมาค่ะ.....")
                                
                        elif cmd == "4up":
                            if msg._from in admin:
                                Setmain["ARfoto"][Dmid] = True
                                km.sendText(msg.to,"ส่งรูปมาค่ะ.....")
                                
                        elif cmd == "5up":
                            if msg._from in admin:
                                Setmain["ARfoto"][Emid] = True
                                kb.sendText(msg.to,"ส่งรูปมาค่ะ.....")
                                
                        elif cmd == "6up":
                            if msg._from in admin:
                                Setmain["ARfoto"][Fmid] = True
                                kn.sendText(msg.to,"ส่งรูปมาค่ะ.....")
                                
                        elif cmd == "7up":
                            if msg._from in admin:
                                Setmain["ARfoto"][Gmid] = True
                                ko.sendText(msg.to,"ส่งรูปมาค่ะ.....")
                                
                        elif cmd == "8up":
                            if msg._from in admin:
                                Setmain["ARfoto"][Hmid] = True
                                kw.sendText(msg.to,"ส่งรูปมาค่ะ.....")
                                
                        elif cmd == "9up":
                            if msg._from in admin:
                                Setmain["ARfoto"][Imid] = True
                                ke.sendText(msg.to,"ส่งรูปมาค่ะ.....")
                                
                        elif cmd == "10up":
                            if msg._from in admin:
                                Setmain["ARfoto"][Jmid] = True
                                ky.sendText(msg.to,"ส่งรูปมาค่ะ.....")

                        elif cmd == "ผีup":
                            if msg._from in admin:
                                Setmain["ARfoto"][Imid] = True
                                k12.sendText(msg.to,"ส่งรูปมาค่ะ.....")
                                
                        elif cmd == "gup":
                            if msg._from in admin:
                                Setmain["ARfoto"][Zmid] = True
                                sw.sendText(msg.to,"ส่งรูปมาค่ะ.....")

                        elif cmd.startswith("ชื่อ: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = cl.getProfile()
                                profile.displayName = string
                                cl.updateProfile(profile)
                                cl.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("ชื่อ1: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = ki.getProfile()
                                profile.displayName = string
                                ki.updateProfile(profile)
                                ki.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("ชื่อ2: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kk.getProfile()
                                profile.displayName = string
                                kk.updateProfile(profile)
                                kk.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("ชื่อ3: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kc.getProfile()
                                profile.displayName = string
                                kc.updateProfile(profile)
                                kc.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("ชื่อ4: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = km.getProfile()
                                profile.displayName = string
                                km.updateProfile(profile)
                                km.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("ชื่อ5: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kb.getProfile()
                                profile.displayName = string
                                kb.updateProfile(profile)
                                kb.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("ชื่อ6: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kn.getProfile()
                                profile.displayName = string
                                kn.updateProfile(profile)
                                kn.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("ชื่อ7: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = ko.getProfile()
                                profile.displayName = string
                                ko.updateProfile(profile)
                                ko.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("ชื่อ8: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kw.getProfile()
                                profile.displayName = string
                                kw.updateProfile(profile)
                                kw.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("ชื่อ9: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = ke.getProfile()
                                profile.displayName = string
                                ke.updateProfile(profile)
                                ke.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("ชื่อ10: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = ky.getProfile()
                                profile.displayName = string
                                ky.updateProfile(profile)
                                ky.sendMessage(msg.to,"Nama diganti jadi " + string + "")
              
                        elif cmd.startswith("ชื่อผี: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = sw.getProfile()
                                profile.displayName = string
                                sw.updateProfile(profile)
                                sw.sendMessage(msg.to,"Nama diganti jadi " + string + "")
#===========BOT UPDATE============#
                        elif cmd == "tag" or text.lower() == 'แทค':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               group = cl.getGroup(msg.to)
                               nama = [contact.mid for contact in group.members]
                               nm1, nm2, nm3, nm4,nm5,nm6,nm7,nm8,nm9,nm10,nm11,nm12,nm13,nm14,nm15, jml = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], len(nama)
                               if jml <= 20:
                                   mentionMembers(msg.to, nama)
                               if jml > 20 and jml < 40:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, len(nama)-1):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                               if jml > 40 and jml < 60:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, len(nama)-1):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                               if jml > 60 and jml < 80:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 59):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, len(nama)-1):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                               if jml > 80 and jml < 100:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 59):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 79):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, len(nama)-1):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                               if jml > 100 and jml < 120:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 59):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 79):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, 99):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                                   for n in range (100, len(nama)-1):
                                       nm6 += [nama[n]]
                                   mentionMembers(msg.to, nm6)
                               if jml > 120 and jml < 140:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 59):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 79):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, 99):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                                   for n in range (100, 119):
                                       nm6 += [nama[n]]
                                   mentionMembers(msg.to, nm6)
                                   for o in range (120, len(nama)-1):
                                       nm7 += [nama[o]]
                                   mentionMembers(msg.to, nm7)
                               if jml > 140 and jml < 160:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 59):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 79):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, 99):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                                   for n in range (100, 119):
                                       nm6 += [nama[n]]
                                   mentionMembers(msg.to, nm6)
                                   for o in range (120, 139):
                                       nm7 += [nama[o]]
                                   mentionMembers(msg.to, nm7)
                                   for p in range (140, len(nama)-1):
                                       nm8 += [nama[p]]
                                   mentionMembers(msg.to, nm8)
                               if jml > 160 and jml < 180:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 59):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 79):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, 99):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                                   for n in range (100, 119):
                                       nm6 += [nama[n]]
                                   mentionMembers(msg.to, nm6)
                                   for o in range (120, 139):
                                       nm7 += [nama[o]]
                                   mentionMembers(msg.to, nm7)
                                   for p in range (150, 159):
                                       nm8 += [nama[p]]
                                   mentionMembers(msg.to, nm8)
                                   for q in range (160, len(nama)-1):
                                       nm8 += [nama[q]]                                       
                                   mentionMembers(msg.to, nm9)
                               if jml > 160 and jml < 180:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 59):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 79):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, 99):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                                   for n in range (100, 119):
                                       nm6 += [nama[n]]
                                   mentionMembers(msg.to, nm6)
                                   for o in range (120, 139):
                                       nm7 += [nama[o]]
                                   mentionMembers(msg.to, nm7)
                                   for p in range (140, 159):
                                       nm8 += [nama[p]]
                                   mentionMembers(msg.to, nm8)
                                   for q in range (160, 179):
                                       nm9 += [nama[q]]
                                   mentionMembers(msg.to, nm9)
                                   for r in range (180, len(nama)-1):
                                       nm10 += [nama[r]]
                                   mentionMembers(msg.to, nm10)
                               if jml > 180 and jml < 200:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 59):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 79):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, 99):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                                   for n in range (100, 119):
                                       nm6 += [nama[n]]
                                   mentionMembers(msg.to, nm6)
                                   for o in range (120, 139):
                                       nm7 += [nama[o]]
                                   mentionMembers(msg.to, nm7)
                                   for p in range (140, 159):
                                       nm8 += [nama[p]]
                                   mentionMembers(msg.to, nm8)
                                   for q in range (160, 179):
                                       nm9 += [nama[q]]
                                   mentionMembers(msg.to, nm9)
                                   for r in range (180, 199):
                                       nm10 += [nama[r]]
                                   mentionMembers(msg.to, nm10)
                                   for s in range (200, len(nama)-1):
                                       nm11 += [nama[s]]
                                   mentionMembers(msg.to, nm11)
                               if jml > 200 and jml < 220:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 59):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 79):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, 99):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                                   for n in range (100, 119):
                                       nm6 += [nama[n]]
                                   mentionMembers(msg.to, nm6)
                                   for o in range (120, 139):
                                       nm7 += [nama[o]]
                                   mentionMembers(msg.to, nm7)
                                   for p in range (140, 159):
                                       nm8 += [nama[p]]
                                   mentionMembers(msg.to, nm8)
                                   for q in range (160, 179):
                                       nm9 += [nama[q]]
                                   mentionMembers(msg.to, nm9)
                                   for r in range (180, 199):
                                       nm10 += [nama[r]]
                                   mentionMembers(msg.to, nm10)
                                   for s in range (200, 219):
                                       nm11 += [nama[s]]
                                   mentionMembers(msg.to, nm11)
                                   for t in range (220, len(nama)-1):
                                       nm12 += [nama[t]]
                                   mentionMembers(msg.to, nm12)
                               if jml > 220 and jml < 239:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 59):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 79):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, 99):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                                   for n in range (100, 119):
                                       nm6 += [nama[n]]
                                   mentionMembers(msg.to, nm6)
                                   for o in range (120, 139):
                                       nm7 += [nama[o]]
                                   mentionMembers(msg.to, nm7)
                                   for p in range (140, 159):
                                       nm8 += [nama[p]]
                                   mentionMembers(msg.to, nm8)
                                   for q in range (160, 179):
                                       nm9 += [nama[q]]
                                   mentionMembers(msg.to, nm9)
                                   for r in range (180, 199):
                                       nm10 += [nama[r]]
                                   mentionMembers(msg.to, nm10)
                                   for s in range (200, 219):
                                       nm11 += [nama[s]]
                                   mentionMembers(msg.to, nm11)
                                   for t in range (220, 239):
                                       nm12 += [nama[t]]
                                   mentionMembers(msg.to, nm12)
                                   for u in range (240, len(nama)-1):
                                       nm13 += [nama[u]]
                                   mentionMembers(msg.to, nm13)
                               if jml > 240 and jml < 259:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 59):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 79):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, 99):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                                   for n in range (100, 119):
                                       nm6 += [nama[n]]
                                   mentionMembers(msg.to, nm6)
                                   for o in range (120, 139):
                                       nm7 += [nama[o]]
                                   mentionMembers(msg.to, nm7)
                                   for p in range (140, 159):
                                       nm8 += [nama[p]]
                                   mentionMembers(msg.to, nm8)
                                   for q in range (160, 179):
                                       nm9 += [nama[q]]
                                   mentionMembers(msg.to, nm9)
                                   for r in range (180, 199):
                                       nm10 += [nama[r]]
                                   mentionMembers(msg.to, nm10)
                                   for s in range (200, 219):
                                       nm11 += [nama[s]]
                                   mentionMembers(msg.to, nm11)
                                   for t in range (220, 239):
                                       nm12 += [nama[t]]
                                   mentionMembers(msg.to, nm12)
                                   for u in range (240, 259):
                                       nm13 += [nama[u]]
                                   mentionMembers(msg.to, nm13)
                                   for v in range (260, len(nama)-1):
                                       nm14 += [nama[v]]
                                   mentionMembers(msg.to, nm14)
                               if jml > 260 and jml < 279:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 59):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 79):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, 99):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                                   for n in range (100, 119):
                                       nm6 += [nama[n]]
                                   mentionMembers(msg.to, nm6)
                                   for o in range (120, 139):
                                       nm7 += [nama[o]]
                                   mentionMembers(msg.to, nm7)
                                   for p in range (140, 159):
                                       nm8 += [nama[p]]
                                   mentionMembers(msg.to, nm8)
                                   for q in range (160, 179):
                                       nm9 += [nama[q]]
                                   mentionMembers(msg.to, nm9)
                                   for r in range (180, 199):
                                       nm10 += [nama[r]]
                                   mentionMembers(msg.to, nm10)
                                   for s in range (200, 219):
                                       nm11 += [nama[s]]
                                   mentionMembers(msg.to, nm11)
                                   for t in range (220, 239):
                                       nm12 += [nama[t]]
                                   mentionMembers(msg.to, nm12)
                                   for u in range (240, 259):
                                       nm13 += [nama[u]]
                                   mentionMembers(msg.to, nm13)
                                   for v in range (260, 279):
                                       nm14 += [nama[v]]
                                   mentionMembers(msg.to, nm14)
                                   for w in range (280, len(nama)-1):
                                       nm15 += [nama[w]]
                                   mentionMembers(msg.to, nm15)
                               if jml > 280 and jml < 299:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 59):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 79):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, 99):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                                   for n in range (100, 119):
                                       nm6 += [nama[n]]
                                   mentionMembers(msg.to, nm6)
                                   for o in range (120, 139):
                                       nm7 += [nama[o]]
                                   mentionMembers(msg.to, nm7)
                                   for p in range (140, 159):
                                       nm8 += [nama[p]]
                                   mentionMembers(msg.to, nm8)
                                   for q in range (160, 179):
                                       nm9 += [nama[q]]
                                   mentionMembers(msg.to, nm9)
                                   for r in range (180, 199):
                                       nm10 += [nama[r]]
                                   mentionMembers(msg.to, nm10)
                                   for s in range (200, 219):
                                       nm11 += [nama[s]]
                                   mentionMembers(msg.to, nm11)
                                   for t in range (220, 239):
                                       nm12 += [nama[t]]
                                   mentionMembers(msg.to, nm12)
                                   for u in range (240, 259):
                                       nm13 += [nama[u]]
                                   mentionMembers(msg.to, nm13)
                                   for v in range (260, 279):
                                       nm14 += [nama[v]]
                                   mentionMembers(msg.to, nm14)
                                   for w in range (280, 299):
                                       nm15 += [nama[w]]
                                   mentionMembers(msg.to, nm15)
                                   for x in range (300, len(nama)-1):
                                       nm16 += [nama[x]]
                                   mentionMembers(msg.to, nm16)

                        elif cmd == "รายชื่อบอท":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ma = ""
                                a = 0
                                for m_id in Bots:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                cl.sendMessage(msg.to,"SELFBOT\n\n"+ma+"\nTotal「%s」 Bots" %(str(len(Bots))))

                        elif cmd == "รายชื่อแอดมิน":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ma = ""
                                mb = ""
                                mc = ""
                                a = 0
                                b = 0
                                c = 0
                                for m_id in owner:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                for m_id in admin:
                                    b = b + 1
                                    end = '\n'
                                    mb += str(b) + ". " +cl.getContact(m_id).displayName + "\n"
                                for m_id in staff:
                                    c = c + 1
                                    end = '\n'
                                    mc += str(c) + ". " +cl.getContact(m_id).displayName + "\n"
                                cl.sendMessage(msg.to,"SELFBOT\n\nSuper admin:\n"+ma+"\nAdmin:\n"+mb+"\nStaff:\n"+mc+"\nTotal「%s」 Anggota" %(str(len(owner)+len(admin)+len(staff))))

                        elif cmd == "set2":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ma = ""
                                mb = ""
                                mc = ""
                                md = ""
                                me = ""
                                mf = ""
                                a = 0
                                gid = protectqr
                                for group in gid:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getGroup(group).name + "\n"
                                gid = protectkick
                                for group in gid:
                                    a = a + 1
                                    end = '\n'
                                    mb += str(a) + ". " +cl.getGroup(group).name + "\n"
                                gid = protectjoin
                                for group in gid:
                                    a = a + 1
                                    end = '\n'
                                    md += str(a) + ". " +cl.getGroup(group).name + "\n"
                                gid = protectcancel
                                for group in gid:
                                    a = a + 1
                                    end = '\n'
                                    mc += str(a) + ". " +cl.getGroup(group).name + "\n"
                                gid = protectinvite
                                for group in gid:
                                    a = a + 1
                                    end = '\n'
                                    me += str(a) + ". " +cl.getGroup(group).name + "\n"
                                gid = protectantijs
                                for group in gid:
                                    a = a + 1
                                    end = '\n'
                                    mf += str(a) + ". " +cl.getGroup(group).name + "\n"
                                cl.sendMessage(msg.to,"SELFBOT\n\n「😈」 PROTECT URL :\n"+ma+"\n「😈」 PROTECT KICK :\n"+mb+"\n「😈」 PROTECT JOIN :\n"+md+"\n「😈」 PROTECT CANCEL:\n"+mc+"\n「😈」 PROTECT INVITE:\n"+me+"\n「😈」 PROTECT ANTIJS :\n"+mf+"\nTotal「%s」Grup diamankan" %(str(len(protectqr)+len(protectkick)+len(protectjoin)+len(protectcancel)+len(protectinvite)+len(protectantijs))))

                        elif cmd == "b":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ki.sendMessage(msg.to,responsename1)
                                kk.sendMessage(msg.to,responsename2)
                                kc.sendMessage(msg.to,responsename3)
                                km.sendMessage(msg.to,responsename4)
                                kb.sendMessage(msg.to,responsename5)
                                kn.sendMessage(msg.to,responsename6)
                                ko.sendMessage(msg.to,responsename7)
                                kw.sendMessage(msg.to,responsename8)
                                ke.sendMessage(msg.to,responsename9)
                                ky.sendMessage(msg.to,responsename10)
                                
                        elif cmd == "ดึงคิก":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                try:
                                    anggota = [Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid,Zmid]
                                    cl.inviteIntoGroup(msg.to, anggota)
                                    ki.acceptGroupInvitation(msg.to)
                                    kk.acceptGroupInvitation(msg.to)
                                    kc.acceptGroupInvitation(msg.to)
                                    km.acceptGroupInvitation(msg.to)
                                    kb.acceptGroupInvitation(msg.to)
                                    kn.acceptGroupInvitation(msg.to)
                                    ko.acceptGroupInvitation(msg.to)
                                    kw.acceptGroupInvitation(msg.to)
                                    ke.acceptGroupInvitation(msg.to)
                                    ky.acceptGroupInvitation(msg.to)
                                    sw.acceptGroupInvitation(msg.to)
                                    ky.sendMessage(msg.to, "พร้อมคุ้มกันเจ้านายค่ะ")
                                except:
                                    pass
                                
                        elif cmd == "js":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                try:
                                    ginfo = cl.getGroup(msg.to)
                                    cl.inviteIntoGroup(msg.to, [Zmid])
                                    cl.sendMessage(msg.to,"Grup 「"+str(ginfo.name)+"」 Aman Dari JS")
                                except:
                                    pass
    
                        elif cmd == "in":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                                km.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kb.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kn.acceptGroupInvitationByTicket(msg.to,Ticket)
                                ko.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kw.acceptGroupInvitationByTicket(msg.to,Ticket)
                                ke.acceptGroupInvitationByTicket(msg.to,Ticket)
                                ky.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = ky.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                ky.updateGroup(G)
                                ky.sendMessage(msg.to, "พร้อมคุ้มกันเจ้านายค่ะ ")

                        elif cmd == "out":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ki.leaveGroup(msg.to)
                                kk.leaveGroup(msg.to)
                                kc.leaveGroup(msg.to)
                                km.leaveGroup(msg.to)
                                kb.leaveGroup(msg.to)
                                kn.leaveGroup(msg.to)
                                ko.leaveGroup(msg.to)
                                kw.leaveGroup(msg.to)
                                ke.leaveGroup(msg.to)
                                ky.leaveGroup(msg.to)
                                sw.leaveGroup(msg.to)
                                
                        elif cmd == "bye":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                cl.sendText(msg.to, "Bye bye fams "+str(G.name))
                                cl.leaveGroup(msg.to)
                                
                        elif cmd == "ck":
                            if msg._from in admin or msg._from in owner:
                               try:cl.inviteIntoGroup(to, [mid]);has = "OK"
                               except:has = "NOT"
                               try:cl.kickoutFromGroup(to, [mid]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = "🔋██ full 100%"
                               else:sil = "🔌█▒ Low 0%"
                               if has1 == "OK":sil1 = "🔋██ full 100%"
                               else:sil1 = "🔌█▒ Low 0%"
                               cl.sendMessage(to, "Status:\n\n🔴Kick : {} \n🔴Invite : {}".format(sil1,sil))
                               try:ki.inviteIntoGroup(to, [Amid]);has = "OK"
                               except:has = "NOT"
                               try:ki.kickoutFromGroup(to, [Amid]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = "🔋██ full 100%"
                               else:sil = "🔌█▒ Low 0%"
                               if has1 == "OK":sil1 = "🔋██ full 100%"
                               else:sil1 = "🔌█▒ Low 0%"
                               ki.sendMessage(to, "Status:\n\n🔴Kick : {} \n🔴Invite : {}".format(sil1,sil))                               
                               try:kk.inviteIntoGroup(to, [Bmid]);has = "OK"
                               except:has = "NOT"
                               try:kk.kickoutFromGroup(to, [Bmid]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = "🔋██ full 100%"
                               else:sil = "🔌█▒. Low 0%"
                               if has1 == "OK":sil1 = "🔋██ full 100%"
                               else:sil1 = "🔌█▒ Low 0%"
                               kk.sendMessage(to, "Status:\n\n🔴Kick : {} \n🔴Invite : {}".format(sil1,sil))
                               try:kc.inviteIntoGroup(to, [Cmid]);has = "OK"
                               except:has = "NOT"
                               try:kc.kickoutFromGroup(to, [Cmid]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = "🔋██ full 100%"
                               else:sil = "🔌█▒. Low 0%"
                               if has1 == "OK":sil1 = "🔋██ full 100%"
                               else:sil1 = "🔌█▒ Low  0%"
                               kc.sendMessage(to, "Status:\n\n🔴Kick : {} \n🔴Invite : {}".format(sil1,sil))                               
                               try:km.inviteIntoGroup(to, [Dmid]);has = "OK"
                               except:has = "NOT"
                               try:km.kickoutFromGroup(to, [Dmid]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = "🔋██ full 100%"
                               else:sil = "🔌█▒ Low 0%"
                               if has1 == "OK":sil1 = "🔋██ full 100%"
                               else:sil1 = "🔌█▒ Low 0%"
                               km.sendMessage(to, "Status:\n\n🔴Kick : {} \n🔴Invite : {}".format(sil1,sil))                              
                               try:kb.inviteIntoGroup(to, [Emid]);has = "OK"
                               except:has = "NOT"
                               try:kb.kickoutFromGroup(to, [Emid]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = "🔋██ full 100%"
                               else:sil = "🔌█▒ Low 0%"
                               if has1 == "OK":sil1 = "🔋██ full 100%"
                               else:sil1 = "🔌█▒ Low 0%"
                               kb.sendMessage(to, "Status:\n\n🔴Kick : {} \n🔴Invite : {}".format(sil1,sil))
                               try:kn.inviteIntoGroup(to, [Fmid]);has = "OK"
                               except:has = "NOT"
                               try:kn.kickoutFromGroup(to, [Fmid]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = "🔋██ full 100%"
                               else:sil = "🔌█▒. Low 0%"
                               if has1 == "OK":sil1 = "🔋██ full 100%"
                               else:sil1 = "🔌█▒ Low 0%"
                               kn.sendMessage(to, "Status:\n\n🔴Kick : {} \n🔴Invite : {}".format(sil1,sil))
                               try:ko.inviteIntoGroup(to, [Gmid]);has = "OK"
                               except:has = "NOT"
                               try:ko.kickoutFromGroup(to, [Gmid]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = "🔋██ full 100%"
                               else:sil = "🔌█▒ Low 0%"
                               if has1 == "OK":sil1 = "🔋██ full 100%"
                               else:sil1 = "🔌█▒ Low 0%"
                               ko.sendMessage(to, "Status:\n\n🔴Kick : {} \n🔴Invite : {}".format(sil1,sil))                               
                               try:kw.inviteIntoGroup(to, [Hmid]);has = "OK"
                               except:has = "NOT"
                               try:kw.kickoutFromGroup(to, [Hmid]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = "🔋██ full 100%"
                               else:sil = "🔌█▒. Low 0%"
                               if has1 == "OK":sil1 = "🔋██ full 100%"
                               else:sil1 = "🔌█▒ Low 0%"
                               kw.sendMessage(to, "Status:\n\n🔴Kick : {} \n🔴Invite : {}".format(sil1,sil))
                               try:ke.inviteIntoGroup(to, [Imid]);has = "OK"
                               except:has = "NOT"
                               try:ke.kickoutFromGroup(to, [Imid]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = "🔋██ full 100%"
                               else:sil = "🔌█▒. Low 0%"
                               if has1 == "OK":sil1 = "🔋██ full 100%"
                               else:sil1 = "🔌█▒ Low  0%"
                               ke.sendMessage(to, "Status:\n\n🔴Kick : {} \n🔴Invite : {}".format(sil1,sil))                               
                               try:ky.inviteIntoGroup(to, [Jmid]);has = "OK"
                               except:has = "NOT"
                               try:ky.kickoutFromGroup(to, [Jmid]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = "🔋██ full 100%"
                               else:sil = "🔌█▒ Low 0%"
                               if has1 == "OK":sil1 = "🔋██ full 100%"
                               else:sil1 = "🔌█▒ Low 0%"
                               ky.sendMessage(to, "Status:\n\n🔴Kick : {} \n🔴Invite : {}".format(sil1,sil))

                        elif cmd == "a1":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = ki.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                ki.updateGroup(G)

                        elif cmd == "a2":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = kk.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                kk.updateGroup(G)

                        elif cmd == "a3":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = kc.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                kc.updateGroup(G)
                                
                        elif cmd == "a4":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                km.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = km.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                km.updateGroup(G)

                        elif cmd == "a5":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                kb.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = kb.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                kb.updateGroup(G)

                        elif cmd == "a6":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                kn.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = kn.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                kn.updateGroup(G)
                                
                        elif cmd == "a7":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                ko.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = ko.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                ko.updateGroup(G)

                        elif cmd == "a8":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                kw.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = kw.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                kw.updateGroup(G)

                        elif cmd == "a9":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                ke.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = ke.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                ke.updateGroup(G)
                                
                        elif cmd == "a10":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                ky.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = ky.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                ky.updateGroup(G)

                        elif cmd == "ผีมา":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                sw.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = sw.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                sw.updateGroup(G)

                        elif cmd == "ผีออก":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                sw.leaveGroup(msg.to)
                                
                        elif cmd == "bb" or cmd == "10":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ki.sendMessage(msg.to, "อยู่ค่ะเจ้านาย ")
                                kk.sendMessage(msg.to, "อยู่ค่ะเจ้านาย ")
                                kc.sendMessage(msg.to, "อยู่ค่ะเจ้านาย ")
                                km.sendMessage(msg.to, "อยู่ค่ะเจ้านาย ")
                                kb.sendMessage(msg.to, "อยู่ค่ะเจ้านาย ")
                                kn.sendMessage(msg.to, "อยู่ค่ะเจ้านาย ")
                                ko.sendMessage(msg.to, "อยู่ค่ะเจ้านาย ")
                                kw.sendMessage(msg.to, "อยู่ค่ะเจ้านาย ")
                                ke.sendMessage(msg.to, "อยู่ค่ะเจ้านาย ")
                                ky.sendMessage(msg.to, "อยู่ค่ะเจ้านาย ")

                        elif cmd == "sb":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                get_profile_time_start = time.time()
                                get_profile = cl.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                cl.sendMessage(msg.to, "Speed\n%.10f ms" % (get_profile_time/3))
                                get_profile_time_start = time.time()
                                get_profile = cl.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                ki.sendMessage(msg.to, "Speed\n%.10f ms" % (get_profile_time/3))
                                get_profile_time_start = time.time()
                                get_profile = cl.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                kk.sendMessage(msg.to, "Speed\n%.10f ms" % (get_profile_time/3))
                                get_profile_time_start = time.time()
                                get_profile = cl.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                kc.sendMessage(msg.to, "Speed\n%.10f ms" % (get_profile_time/3))
                                get_profile_time_start = time.time()
                                get_profile = cl.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                km.sendMessage(msg.to, "Speed\n%.10f ms" % (get_profile_time/3))
                                get_profile_time_start = time.time()
                                get_profile = cl.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                kb.sendMessage(msg.to, "Speed\n%.10f ms" % (get_profile_time/3))
                                get_profile_time_start = time.time()
                                get_profile = cl.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                kn.sendMessage(msg.to, "Speed\n%.10f ms" % (get_profile_time/3))
                                get_profile_time_start = time.time()
                                get_profile = cl.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                ko.sendMessage(msg.to, "Speed\n%.10f ms" % (get_profile_time/3))
                                get_profile_time_start = time.time()
                                get_profile = cl.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                kw.sendMessage(msg.to, "Speed\n%.10f ms" % (get_profile_time/3))
                                get_profile_time_start = time.time()
                                get_profile = cl.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                ke.sendMessage(msg.to, "Speed\n%.10f ms" % (get_profile_time/3))
                                get_profile_time_start = time.time()
                                get_profile = cl.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                ky.sendMessage(msg.to, "Speed\n%.10f ms" % (get_profile_time/3))

                        elif cmd == "speed" or cmd == "sp":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               start = time.time()
                               cl.sendMessage(msg.to, "ความเร็วอยู่ที่...")
                               elapsed_time = time.time() - start
                               cl.sendMessage(msg.to, "{} ms".format(str(elapsed_time)))

                        elif cmd == "speedbot" or cmd == "spb":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               start = time.time()
                               ki.sendMessage(msg.to, "Pusiiing...")
                               elapsed_time = time.time() - start
                               ki.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))
                               elapsed_time = time.time() - start
                               kk.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))
                               elapsed_time = time.time() - start
                               kc.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))
                               elapsed_time = time.time() - start
                               km.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))
                               elapsed_time = time.time() - start
                               kb.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))
                               elapsed_time = time.time() - start
                               kn.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))
                               elapsed_time = time.time() - start
                               ko.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))
                               elapsed_time = time.time() - start
                               kw.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))
                               elapsed_time = time.time() - start
                               ke.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))
                               elapsed_time = time.time() - start
                               ky.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))

                        elif cmd == "lurking on":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                 tz = pytz.timezone("Asia/Jakarta")
                                 timeNow = datetime.now(tz=tz)
                                 Setmain['ARreadPoint'][msg.to] = msg_id
                                 Setmain['ARreadMember'][msg.to] = {}
                                 cl.sendText(msg.to, "Lurking Successfully activated\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                            
                        elif cmd == "lurking off":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                 tz = pytz.timezone("Asia/Jakarta")
                                 timeNow = datetime.now(tz=tz)
                                 del Setmain['ARreadPoint'][msg.to]
                                 del Setmain['ARreadMember'][msg.to]
                                 cl.sendText(msg.to, "Lurking Successfully dinoaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                            
                        elif cmd == "lurkers":
                          if msg._from in admin:
                            if msg.to in Setmain['ARreadPoint']:
                                if Setmain['ARreadMember'][msg.to] != {}:
                                    aa = []
                                    for x in Setmain['ARreadMember'][msg.to]:
                                        aa.append(x)
                                    try:
                                        arrData = ""
                                        textx = "  [ Result {} member ]    \n\n  [ Lurkers ]\n1. ".format(str(len(aa)))
                                        arr = []
                                        no = 1
                                        b = 1
                                        for i in aa:
                                            b = b + 1
                                            end = "\n"
                                            mention = "@x\n"
                                            slen = str(len(textx))
                                            elen = str(len(textx) + len(mention) - 1)
                                            arrData = {'S':slen, 'E':elen, 'M':i}
                                            arr.append(arrData)
                                            tz = pytz.timezone("Asia/Jakarta")
                                            timeNow = datetime.now(tz=tz)
                                            textx += mention
                                            if no < len(aa):
                                                no += 1
                                                textx += str(b) + ". "
                                            else:
                                                try:
                                                    no = "[ {} ]".format(str(cl.getGroup(msg.to).name))
                                                except:
                                                    no = "  "
                                        msg.to = msg.to
                                        msg.text = textx+"\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]"
                                        msg.contentMetadata = {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}
                                        msg.contentType = 0
                                        cl.sendMessage1(msg)
                                    except:
                                        pass
                                    try:
                                        del Setmain['ARreadPoint'][msg.to]
                                        del Setmain['ARreadMember'][msg.to]
                                    except:
                                        pass
                                    Setmain['ARreadPoint'][msg.to] = msg.id
                                    Setmain['ARreadMember'][msg.to] = {}
                                else:
                                    cl.sendText(msg.to, "User kosong...")
                            else:
                                cl.sendText(msg.to, "Ketik lurking on dulu")

                        elif cmd == "sider on":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              try:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  cl.sendMessage(msg.to, "Cek sider activated\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                                  del cctv['point'][msg.to]
                                  del cctv['sidermem'][msg.to]
                                  del cctv['cyduk'][msg.to]
                              except:
                                  pass
                              cctv['point'][msg.to] = msg.id
                              cctv['sidermem'][msg.to] = ""
                              cctv['cyduk'][msg.to]=True

                        elif cmd == "sider off":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              if msg.to in cctv['point']:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  cctv['cyduk'][msg.to]=False
                                  cl.sendMessage(msg.to, "Cek sider deactivated\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                              else:
                                  cl.sendMessage(msg.to, "Sudak tidak aktif")

#===========Hiburan============#
                        elif cmd.startswith("sholat: "):
                          if msg._from in admin:
                             sep = text.split(" ")
                             location = text.replace(sep[0] + " ","")
                             with requests.session() as web:
                                  web.headers["user-agent"] = random.choice(settings["userAgent"])
                                  r = web.get("http://api.corrykalam.net/apisholat.php?lokasi={}".format(urllib.parse.quote(location)))
                                  data = r.text
                                  data = json.loads(data)
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  if data[1] != "Subuh : " and data[2] != "Dzuhur : " and data[3] != "Ashar : " and data[4] != "Maghrib : " and data[5] != "Isha : ":
                                         ret_ = "「Jadwal Sholat」"
                                         ret_ += "\n❧Lokasi : " + data[0]
                                         ret_ += "\n❧" + data[1]
                                         ret_ += "\n❧" + data[2]
                                         ret_ += "\n❧" + data[3]
                                         ret_ += "\n❧" + data[4]
                                         ret_ += "\n❧" + data[5]
                                         ret_ += "\n\nTanggal : " + datetime.strftime(timeNow,'%Y-%m-%d')
                                         ret_ += "\nJam : " + datetime.strftime(timeNow,'%H:%M:%S')
                                  cl.sendMessage(msg.to, str(ret_))

                        elif cmd.startswith("cuaca: "):
                          if msg._from in admin:
                            separate = text.split(" ")
                            location = text.replace(separate[0] + " ","")
                            with requests.session() as web:
                                web.headers["user-agent"] = random.choice(settings["userAgent"])
                                r = web.get("http://api.corrykalam.net/apicuaca.php?kota={}".format(urllib.parse.quote(location)))
                                data = r.text
                                data = json.loads(data)
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                if "result" not in data:
                                    ret_ = "「Status Cuaca」"
                                    ret_ += "\n❧Lokasi : " + data[0].replace("Temperatur di kota ","")
                                    ret_ += "\n❧Suhu : " + data[1].replace("Suhu : ","") + " C"
                                    ret_ += "\n❧Kelembaban : " + data[2].replace("Kelembaban : ","") + " %"
                                    ret_ += "\n❧Tekanan udara : " + data[3].replace("Tekanan udara : ","") + " HPa"
                                    ret_ += "\n❧Kecepatan angin : " + data[4].replace("Kecepatan angin : ","") + " m/s"
                                    ret_ += "\n\nTanggal : " + datetime.strftime(timeNow,'%Y-%m-%d')
                                    ret_ += "\nJam : " + datetime.strftime(timeNow,'%H:%M:%S')
                                cl.sendMessage(msg.to, str(ret_))

                        elif cmd.startswith("lokasi: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            location = msg.text.replace(separate[0] + " ","")
                            with requests.session() as web:
                                web.headers["user-agent"] = random.choice(settings["userAgent"])
                                r = web.get("http://api.corrykalam.net/apiloc.php?lokasi={}".format(urllib.parse.quote(location)))
                                data = r.text
                                data = json.loads(data)
                                if data[0] != "" and data[1] != "" and data[2] != "":
                                    link = "https://www.google.co.id/maps/@{},{},15z".format(str(data[1]), str(data[2]))
                                    ret_ = "「Info Lokasi」"
                                    ret_ += "\n❧Location : " + data[0]
                                    ret_ += "\n❧Google Maps : " + link
                                else:
                                    ret_ = "[Details Location] Error : Location not found"
                                cl.sendMessage(msg.to,str(ret_))

                        elif cmd.startswith("lirik: "):
                           if msg._from in admin:
                               sep = msg.text.split(" ")
                               search = msg.text.replace(sep[0] + " ","")
                               params = {'songname': search}
                               with requests.session() as web:
                                   web.headers["User-Agent"] = random.choice(settings["userAgent"])
                                   r = web.get("https://ide.fdlrcn.com/workspace/yumi-apis/joox?{}".format(urllib.parse.urlencode(params)))
                                   try:
                                      data = json.loads(r.text)
                                      for song in data:
                                          songs = song[5]
                                          lyric = songs.replace('ti:','Title - ')
                                          lyric = lyric.replace('ar:','Artist - ')
                                          lyric = lyric.replace('al:','Album - ')
                                          removeString = "[1234567890.:]"
                                          for char in removeString:
                                              lyric = lyric.replace(char,'')
                                          ret_ = "╔══[ Lyric ]"
                                          ret_ += "\n╠ Nama lagu : {}".format(str(song[0]))
                                          ret_ += "\n╠ Durasi : {}".format(str(song[1]))
                                          ret_ += "\n╠ Link : {}".format(str(song[3]))
                                          ret_ += "\n╚══[ Finish ]\n\nLirik nya :\n{}".format(str(lyric))
                                          cl.sendText(msg.to, str(ret_))
                                   except:
                                       cl.sendText(to, "Lirik Not found")
                            
                        elif cmd.startswith("music: "):
                           if msg._from in admin:
                              sep = msg.text.split(" ")
                              search = msg.text.replace(sep[0] + " ","")
                              params = {'songname': search}
                              with requests.session() as web:
                                  web.headers["User-Agent"] = random.choice(settings["userAgent"])
                                  r = web.get("https://ide.fdlrcn.com/workspace/yumi-apis/joox?{}".format(urllib.parse.urlencode(params)))
                                  try:
                                      data = json.loads(r.text)
                                      for song in data:
                                          ret_ = "╔══[ Music ]"
                                          ret_ += "\n╠ Nama lagu : {}".format(str(song[0]))
                                          ret_ += "\n╠ Durasi : {}".format(str(song[1]))
                                          ret_ += "\n╠ Link : {}".format(str(song[3]))
                                          ret_ += "\n╚══[ Waiting Audio ]"
                                      cl.sendText(msg.to, str(ret_))
                                      cl.sendText(msg.to, "Mohon bersabar musicnya lagi di upload")
                                      cl.sendAudioWithURL(msg.to, song[3])
                                  except:
                                      cl.sendText(to, "Musik Not found")

                        elif cmd.startswith("gimage: "):
                          if msg._from in admin:
                            sep = msg.text.split(" ")
                            search = msg.text.replace(sep[0] + " ","")
                            url = "https://api.xeonwz.ga/api/image/google?q={}".format(urllib.parse.quote(search))
                            with requests.session() as web:
                                web.headers["User-Agent"] = random.choice(settings["userAgent"])
                                r = web.get(url)
                                data = r.text
                                data = json.loads(data)
                                if data["data"] != []:
                                    start = timeit.timeit()
                                    items = data["data"]
                                    path = random.choice(items)
                                    a = items.index(path)
                                    b = len(items)
                                    cl.sendText(msg.to,"「Google Image」\nType : Search Image\nTime taken : %seconds" % (start))
                                    cl.sendImageWithURL(msg.to, str(path))

                        elif cmd.startswith("ytmp4: "):
                          if msg._from in admin:
                            try:
                                sep = msg.text.split(" ")
                                textToSearch = msg.text.replace(sep[0] + " ","")
                                query = urllib.parse.quote(textToSearch)
                                search_url="https://www.youtube.com/results?search_query="
                                mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}
                                sb_url = search_url + query
                                sb_get = requests.get(sb_url, headers = mozhdr)
                                soupeddata = BeautifulSoup(sb_get.content, "html.parser")
                                yt_links = soupeddata.find_all("a", class_ = "yt-uix-tile-link")
                                x = (yt_links[1])
                                yt_href =  x.get("href")
                                yt_href = yt_href.replace("watch?v=", "")
                                qx = "https://youtu.be" + str(yt_href)
                                vid = pafy.new(qx)
                                stream = vid.streams
                                best = vid.getbest()
                                best.resolution, best.extension
                                for s in stream:
                                    me = best.url
                                    hasil = ""
                                    title = "Judul [ " + vid.title + " ]"
                                    author = '\n\n❧Author : ' + str(vid.author)
                                    durasi = '\n❧Duration : ' + str(vid.duration)
                                    suka = '\n❧Likes : ' + str(vid.likes)
                                    rating = '\n❧Rating : ' + str(vid.rating)
                                    deskripsi = '\n❧Deskripsi : ' + str(vid.description)
                                cl.sendVideoWithURL(msg.to, me)
                                cl.sendText(msg.to,title+ author+ durasi+ suka+ rating+ deskripsi)
                            except Exception as e:
                                cl.sendText(msg.to,str(e))

                        elif cmd.startswith("ytmp3: "):
                          if msg._from in admin:
                            try:
                                sep = msg.text.split(" ")
                                textToSearch = msg.text.replace(sep[0] + " ","")
                                query = urllib.parse.quote(textToSearch)
                                search_url="https://www.youtube.com/results?search_query="
                                mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}
                                sb_url = search_url + query
                                sb_get = requests.get(sb_url, headers = mozhdr)
                                soupeddata = BeautifulSoup(sb_get.content, "html.parser")
                                yt_links = soupeddata.find_all("a", class_ = "yt-uix-tile-link")
                                x = (yt_links[1])
                                yt_href =  x.get("href")
                                yt_href = yt_href.replace("watch?v=", "")
                                qx = "https://youtu.be" + str(yt_href)
                                vid = pafy.new(qx)
                                stream = vid.streams
                                bestaudio = vid.getbestaudio()
                                bestaudio.bitrate
                                best = vid.getbest()
                                best.resolution, best.extension
                                for s in stream:
                                    shi = bestaudio.url
                                    me = best.url
                                    vin = s.url
                                    hasil = ""
                                    title = "Judul [ " + vid.title + " ]"
                                    author = '\n\n❧Author : ' + str(vid.author)
                                    durasi = '\n❧Duration : ' + str(vid.duration)
                                    suka = '\n❧Likes : ' + str(vid.likes)
                                    rating = '\n❧Rating : ' + str(vid.rating)
                                    deskripsi = '\n❧Deskripsi : ' + str(vid.description)
                                cl.sendImageWithURL(msg.to, me)
                                cl.sendAudioWithURL(msg.to, shi)
                                cl.sendText(msg.to,title+ author+ durasi+ suka+ rating+ deskripsi)
                            except Exception as e:
                                cl.sendText(msg.to,str(e))

                        elif cmd.startswith("profileig: "):
                          if msg._from in admin:
                            try:
                                sep = msg.text.split(" ")
                                instagram = msg.text.replace(sep[0] + " ","")
                                response = requests.get("https://www.instagram.com/"+instagram+"?__a=1")
                                data = response.json()
                                namaIG = str(data['user']['full_name'])
                                bioIG = str(data['user']['biography'])
                                mediaIG = str(data['user']['media']['count'])
                                verifIG = str(data['user']['is_verified'])
                                usernameIG = str(data['user']['username'])
                                followerIG = str(data['user']['followed_by']['count'])
                                profileIG = data['user']['profile_pic_url_hd']
                                privateIG = str(data['user']['is_private'])
                                followIG = str(data['user']['follows']['count'])
                                link = "❧Link : " + "https://www.instagram.com/" + instagram
                                text = "❧Name : "+namaIG+"\n❧Username : "+usernameIG+"\n❧Biography : "+bioIG+"\n❧Follower : "+followerIG+"\n❧Following : "+followIG+"\n❧Post : "+mediaIG+"\n❧Verified : "+verifIG+"\n❧Private : "+privateIG+"" "\n" + link
                                cl.sendImageWithURL(msg.to, profileIG)
                                cl.sendMessage(msg.to, str(text))
                            except Exception as e:
                                    cl.sendMessage(msg.to, str(e))

                        elif cmd.startswith("cekdate: "):
                          if msg._from in admin:
                            sep = msg.text.split(" ")
                            tanggal = msg.text.replace(sep[0] + " ","")
                            r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                            data=r.text
                            data=json.loads(data)
                            lahir = data["data"]["lahir"]
                            usia = data["data"]["usia"]
                            ultah = data["data"]["ultah"]
                            zodiak = data["data"]["zodiak"]
                            cl.sendMessage(msg.to,"❧I N F O R M A S I ❧\n\n"+"❧Date Of Birth : "+lahir+"\n❧Age : "+usia+"\n❧Ultah : "+ultah+"\n❧Zodiak : "+zodiak)

                        elif cmd.startswith("jumlah: "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                Setmain["ARlimit"] = num
                                cl.sendText(msg.to,"Total Spamtag Diubah Menjadi " +strnum)

                        elif cmd.startswith("spamcall: "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                wait["limit"] = num
                                cl.sendText(msg.to,"Total Spamcall Diubah Menjadi " +strnum)

                        elif cmd.startswith("spamtag "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                if 'MENTION' in msg.contentMetadata.keys()!=None:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key1 = key["MENTIONEES"][0]["M"]
                                    zx = ""
                                    zxc = " "
                                    zx2 = []
                                    pesan2 = "@a"" "
                                    xlen = str(len(zxc))
                                    xlen2 = str(len(zxc)+len(pesan2)-1)
                                    zx = {'S':xlen, 'E':xlen2, 'M':key1}
                                    zx2.append(zx)
                                    zxc += pesan2
                                    msg.contentType = 0
                                    msg.text = zxc
                                    lol = {'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}
                                    msg.contentMetadata = lol
                                    jmlh = int(Setmain["ARlimit"])
                                    if jmlh <= 1000:
                                        for x in range(jmlh):
                                            try:
                                                cl.sendMessage1(msg)
                                            except Exception as e:
                                                cl.sendText(msg.to,str(e))
                                    else:
                                        cl.sendText(msg.to,"Jumlah melebihi 1000")
                                        
                        elif cmd == "spamcall":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                             if msg.toType == 2:
                                group = cl.getGroup(to)
                                members = [mem.mid for mem in group.members]
                                jmlh = int(wait["limit"])
                                cl.sendMessage(msg.to, "Successfully mengundang {} undangan Call Grup".format(str(wait["limit"])))
                                if jmlh <= 100000:
                                  for x in range(jmlh):
                                     try:
                                        call.acquireGroupCallRoute(to)
                                        call.inviteIntoGroupCall(to, contactIds=members)
                                     except Exception as e:
                                        cl.sendText(msg.to,str(e))
                                else:
                                    cl.sendText(msg.to,"Jumlah melebihi batas")

                        elif 'Gif: ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              korban = msg.text.replace('Gif: ','')
                              korban2 = korban.split()
                              midd = korban2[0]
                              jumlah = int(korban2[1])
                              if jumlah <= 100000:
                                  for var in range(0,jumlah):
                                      cl.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      ki.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      kk.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      kc.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      km.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      kb.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      kn.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      ko.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      kw.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      ke.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      ky.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      k12.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      sw.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)

                        elif 'Spam: ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              korban = msg.text.replace('Spam: ','')
                              korban2 = korban.split()
                              midd = korban2[0]
                              jumlah = int(korban2[1])
                              if jumlah <= 100000:
                                  for var in range(0,jumlah):
                                      cl.sendMessage(midd, str(Setmain["ARmessage1"]))
                                      ki.sendMessage(midd, str(Setmain["ARmessage1"]))
                                      kk.sendMessage(midd, str(Setmain["ARmessage1"]))
                                      kc.sendMessage(midd, str(Setmain["ARmessage1"]))
                                      km.sendMessage(midd, str(Setmain["ARmessage1"]))
                                      kb.sendMessage(midd, str(Setmain["ARmessage1"]))
                                      kn.sendMessage(midd, str(Setmain["ARmessage1"]))
                                      ko.sendMessage(midd, str(Setmain["ARmessage1"]))
                                      kw.sendMessage(midd, str(Setmain["ARmessage1"]))
                                      ke.sendMessage(midd, str(Setmain["ARmessage1"]))
                                      ky.sendMessage(midd, str(Setmain["ARmessage1"]))

                        elif 'ID line: ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              msgs = msg.text.replace('ID line: ','')
                              conn = cl.findContactsByUserid(msgs)
                              if True:
                                  cl.sendMessage(msg.to, "http://line.me/ti/p/~" + msgs)
                                  cl.sendMessage(msg.to, None, contentMetadata={'mid': conn.mid}, contentType=13)

#===========Protection============#
                        elif 'Welcome ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Welcome ','')
                              if spl == 'on':
                                  if msg.to in welcome:
                                       msgs = "Welcome Msg activated"
                                  else:
                                       welcome.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Welcome Msg activated\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「activated」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in welcome:
                                         welcome.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Welcome Msg deactivated\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Welcome Msg sudah tidak aktif"
                                    cl.sendMessage(msg.to, "「deactivated」\n" + msgs)

                        elif 'Protecturl ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protecturl ','')
                              if spl == 'on':
                                  if msg.to in protectqr:
                                       msgs = "Protect url activated"
                                  else:
                                       protectqr.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Protect url activated\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「activated」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectqr:
                                         protectqr.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Protect url deactivated\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect url sudah tidak aktif"
                                    cl.sendMessage(msg.to, "「deactivated」\n" + msgs)

                        elif 'Protectkick ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protectkick ','')
                              if spl == 'on':
                                  if msg.to in protectkick:
                                       msgs = "Protect kick activated"
                                  else:
                                       protectkick.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Protect kick activated\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「activated」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectkick:
                                         protectkick.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Protect kick deactivated\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect kick sudah tidak aktif"
                                    cl.sendMessage(msg.to, "「deactivated」\n" + msgs)
                        elif 'Protectinvite ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protectinvite ','')
                              if spl == 'on':
                                  if msg.to in protectinvite:
                                       msgs = "Protect invite activated"
                                  else:
                                       protectinvite.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Protect invite activated\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「activated」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectinvite:
                                         protectinvite.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Protect invite deactivated\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect invite sudah tidak aktif"
                                    cl.sendMessage(msg.to, "「deactivated」\n" + msgs)           

                        elif 'Protectjoin ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protectjoin ','')
                              if spl == 'on':
                                  if msg.to in protectjoin:
                                       msgs = "Protect join activated"
                                  else:
                                       protectjoin.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Protect join activated\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「activated」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectjoin:
                                         protectjoin.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Protect join deactivated\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect join sudah tidak aktif"
                                    cl.sendMessage(msg.to, "「deactivated」\n" + msgs)

                        elif 'Protectcancel ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protectcancel ','')
                              if spl == 'on':
                                  if msg.to in protectcancel:
                                       msgs = "Protect cancel activated"
                                  else:
                                       protectcancel.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Protect cancel activated\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「activated」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectcancel:
                                         protectcancel.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Protect cancel deactivated\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect cancel sudah tidak aktif"
                                    cl.sendMessage(msg.to, "「deactivated」\n" + msgs)

                        elif 'js ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('js ','')
                              if spl == 'on':
                                  if msg.to in protectantijs:
                                       msgs = "JS activated"
                                  else:
                                       protectantijs.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Anti JS activated\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「activated」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectantijs:
                                         protectantijs.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Anti JS deactivated\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Anti JS Sudah Tidak Aktif"
                                    cl.sendMessage(msg.to, "「deactivated」\n" + msgs)
                                    
                        elif 'ผี ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('ผี ','')
                              if spl == 'on':
                                  if msg.to in ghost:
                                       msgs = "Ghost activated"
                                  else:
                                       ghost.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Ghost activated\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「activated」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in ghost:
                                         ghost.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Ghost deactivated\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Ghost Sudah Tidak Aktif"
                                    cl.sendMessage(msg.to, "「deactivated」\n" + msgs)                                    

                        elif 'Allpro ' in msg.text:
                           if msg._from in admin:                             
                              spl = msg.text.replace('Allpro ','')
                              if spl == 'on':
                                #if wait["allprotect"] == True:
                                  if msg.to in protectqr:
                                       msgs = ""
                                  else:
                                       protectqr.append(msg.to)
                                  if msg.to in protectkick:
                                      msgs = ""
                                  else:
                                      protectkick.append(msg.to)
                                  if msg.to in protectinvite:
                                      msgs = ""
                                  else:
                                      protectinvite.append(msg.to)
                                  if msg.to in protectantijs:
                                      msgs = ""
                                  else:
                                      protectantijs.append(msg.to)
                                  if msg.to in ghost:
                                      msgs = ""
                                  else:
                                      ghost.append(msg.to)                                      
                                  if msg.to in protectcancel:
                                      ginfo = cl.getGroup(msg.to)
                                      msgs = "Status : [ ON ]\nDi Group : " +str(ginfo.name)
                                      msgs += "\nSemua sudah activated"
                                  else:
                                      protectcancel.append(msg.to)
                                      ginfo = cl.getGroup(msg.to)
                                      msgs = "Status : [ ON ]\nDi Group : " +str(ginfo.name)
                                      msgs += "\nSemua protection activated"
                                  cl.sendMessage(msg.to, "「 Status Protection 」\n" + msgs)
                              elif spl == 'off':
                                 #if wait["allprotect"] == False:
                                    if msg.to in protectqr:
                                         protectqr.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectkick:
                                         protectkick.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectinvite:
                                         protectinvite.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectantijs:
                                         protectantijs.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in ghost:
                                         ghost.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectcancel:
                                         protectcancel.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Status : [ OFF ]\nDi Group : " +str(ginfo.name)
                                         msgs += "\nSemua protection dimatikan"
                                    else:
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Status : [ OFF ]\nDi Group : " +str(ginfo.name)
                                         msgs += "\nSemua protection dimatikan"
                                    cl.sendMessage(msg.to, "「 Status Protection 」\n" + msgs)

#===========KICKOUT============#
                        elif ("Gk " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Bots:
                                       try:
                                           G = cl.getGroup(msg.to)
                                           G.preventedJoinByTicket = False
                                           cl.updateGroup(G)
                                           invsend = 0
                                           Ticket = cl.reissueGroupTicket(msg.to)
                                           sw.acceptGroupInvitationByTicket(msg.to,Ticket)
                                           sw.kickoutFromGroup(msg.to, [target])
                                           sw.leaveGroup(msg.to)
                                           X = cl.getGroup(msg.to)
                                           X.preventedJoinByTicket = True
                                           cl.updateGroup(X)
                                       except:
                                           pass

                        elif ("Bk " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Bots:
                                       try:
                                           random.choice(ABC).kickoutFromGroup(msg.to, [target])
                                       except:
                                           pass
#KICKALL
                        elif "/mai" in msg.text:
                          if msg._from in admin:
                           if msg.toType == 2:
                              print("ok")
                              _name = msg.text.replace("kickall","")
                              gs = sw.getGroup(msg.to)
                              gs = sw.getGroup(msg.to)
                              gs = sw.getGroup(msg.to)
                              targets = []
                              for g in gs.members:
                                 if _name in g.displayName:
                                     targets.append(g.mid)
                              if targets == []:
                                 cl.sendText(msg.to,"Not found.")
                              else:
                                  for target in targets:
                                   if not target in admin and Bots:
                                      try:
                                          klist=[sw]
                                          kicker=random.choice(klist)
                                          kicker.kickoutFromGroup(msg.to,[target])
                                          print (msg.to,[g.mid])
                                      except Exception as e:
                                          break

                        elif text.lower() == '/คิกบิน':
                            if msg._from in admin:
                                if msg.toType == 2:
                                    gs = cl.getGroup(msg.to)
                                gs.preventedJoinByTicket = False
                                cl.updateGroup(gs)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                cl.acceptGroupInvitationByTicket(msg.to,Ticket)
                                ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                                km.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kb.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kn.acceptGroupInvitationByTicket(msg.to,Ticket)
                                ko.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kw.acceptGroupInvitationByTicket(msg.to,Ticket)
                                ke.acceptGroupInvitationByTicket(msg.to,Ticket)
                                ky.acceptGroupInvitationByTicket(msg.to,Ticket)
                                time.sleep(0.1)
                                targets = []
                                for g in gs.members:
                                    targets.append(g.mid)
                                targets.remove(mid)
                                if targets == []:
                                    cl.sendText(msg.to,"KICK OUT BYE")
                                else:
                                    for target in targets:
                                      if target not in Bots:
                                        try:
                                            klist=[ki,kk,kc,km,kb,kn,ko,kw,ke,ky]
                                            kicker=random.choice(klist)
                                            kicker.kickoutFromGroup(msg.to,[target])
                                            print (msg.to,[g.mid])
                                        except:
                                           pass
                        
#===========ADMIN ADD============#
                        elif ("ตั้งแอดมิน " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           admin.append(target)
                                           cl.sendMessage(msg.to,"❃ѕuccєєdєd Become admin")
                                       except:
                                           pass

                        elif ("ตั้งสตาฟ " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           staff.append(target)
                                           cl.sendMessage(msg.to,"❃ѕuccєєdєd Become staff")
                                       except:
                                           pass

                        elif ("บอทแอด " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           Bots.append(target)
                                           cl.sendMessage(msg.to,"❃ѕuccєєdєd Become bot")
                                       except:
                                           pass

                        elif ("ลบแอดมิน " in msg.text):
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Dpk:
                                       try:
                                           admin.remove(target)
                                           cl.sendMessage(msg.to,"❃ѕuccєєdєd menghapus admin")
                                       except:
                                           pass

                        elif ("ลบสตาฟ " in msg.text):
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Dpk:
                                       try:
                                           staff.remove(target)
                                           cl.sendMessage(msg.to,"❃ѕuccєєdєd menghapus admin")
                                       except:
                                           pass

                        elif ("บอทลบ " in msg.text):
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Dpk:
                                       try:
                                           Bots.remove(target)
                                           cl.sendMessage(msg.to,"Successfully deleted admin")
                                       except:
                                           pass

                        elif cmd == "admin:on" or text.lower() == 'เปิดแอดมิน':
                            if msg._from in admin:
                                wait["addadmin"] = True
                                cl.sendText(msg.to,"Send a contact...")

                        elif cmd == "admin:repeat" or text.lower() == 'ปิดแอดมิน':
                            if msg._from in admin:
                                wait["delladmin"] = True
                                cl.sendText(msg.to,"Send a contact...")

                        elif cmd == "staff:on" or text.lower() == 'เปิดสตาฟ':
                            if msg._from in admin:
                                wait["addstaff"] = True
                                cl.sendText(msg.to,"Send a contact...")

                        elif cmd == "staff:repeat" or text.lower() == 'ปิดสตาฟ':
                            if msg._from in admin:
                                wait["dellstaff"] = True
                                cl.sendText(msg.to,"Send a contact...")

                        elif cmd == "bot:on" or text.lower() == 'บอท on':
                            if msg._from in admin:
                                wait["addbots"] = True
                                cl.sendText(msg.to,"Send a contact...")

                        elif cmd == "bot:repeat" or text.lower() == 'บอท off':
                            if msg._from in admin:
                                wait["dellbots"] = True
                                cl.sendText(msg.to,"Send a contact...")

                        elif cmd == "refresh" or text.lower() == 'refresh':
                            if msg._from in admin:
                                wait["addadmin"] = False
                                wait["delladmin"] = False
                                wait["addstaff"] = False
                                wait["dellstaff"] = False
                                wait["addbots"] = False
                                wait["dellbots"] = False
                                wait["wblacklist"] = False
                                wait["dblacklist"] = False
                                wait["Talkwblacklist"] = False
                                wait["Talkdblacklist"] = False
                                cl.sendText(msg.to,"Successfully di Refresh...")

                        elif cmd == "contact admin" or text.lower() == 'คทแอดมิน':
                            if msg._from in admin:
                                ma = ""
                                for i in admin:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "contact staff" or text.lower() == 'คทสตาฟ':
                            if msg._from in admin:
                                ma = ""
                                for i in staff:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "contact bot" or text.lower() == 'contact bot':
                            if msg._from in admin:
                                ma = ""
                                for i in Bots:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

#===========COMMAND ON OFF============#
                        elif cmd == "notag on" or text.lower() == 'notag on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Mentionkick"] = True
                                cl.sendText(msg.to,"Notag activated")

                        elif cmd == "notag off" or text.lower() == 'notag off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["MentionKick"] = False
                                cl.sendText(msg.to,"Notag deactivated")

                        elif cmd == "contact on" or text.lower() == 'contact on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["contact"] = True
                                cl.sendText(msg.to,"Deteksi contact activated")

                        elif cmd == "contact off" or text.lower() == 'contact off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["contact"] = False
                                cl.sendText(msg.to,"Deteksi contact deactivated")

                        elif cmd == "respon on" or text.lower() == 'respon on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["detectMention"] = True
                                cl.sendText(msg.to,"Auto respon activated")

                        elif cmd == "respon off" or text.lower() == 'respon off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["detectMention"] = False
                                cl.sendText(msg.to,"Auto respon deactivated")

                        elif cmd == "autojoin on" or text.lower() == 'join on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoin"] = True
                                cl.sendText(msg.to,"Autojoin activated")

                        elif cmd == "autojoin off" or text.lower() == 'join off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoin"] = False
                                cl.sendText(msg.to,"Autojoin deactivated")

                        elif cmd == "autoleave on" or text.lower() == 'autoleave on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoLeave"] = True
                                cl.sendText(msg.to,"Autoleave activated")

                        elif cmd == "autoleave off" or text.lower() == 'autoleave off':
                          if wait["selfbot"] == False:
                            if msg._from in admin:
                                wait["autoLeave"] = False
                                cl.sendText(msg.to,"Autoleave deactivated")

                        elif cmd == "autoblock on" or text.lower() == 'autoblock on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoBlock"] = True
                                cl.sendText(msg.to,"「 Status Autoleave 」\nAutoleave has been activated")

                        elif cmd == "autoblock off" or text.lower() == 'autoblock off':
                          if wait["selfbot"] == False:
                            if msg._from in admin:
                                wait["autoBlock"] = False
                                cl.sendText(msg.to,"「 Status Autoleave 」\nAutoleave has been disabled")

                        elif cmd == "autoadd on" or text.lower() == 'autoadd on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoAdd"] = True
                                cl.sendText(msg.to,"Auto add activated")

                        elif cmd == "autoadd off" or text.lower() == 'autoadd off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoAdd"] = False
                                cl.sendText(msg.to,"Auto add deactivated")

                        elif cmd == "read on" or text.lower() == 'autoread on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoRead"] = True
                                cl.sendText(msg.to,"Auto add activated")

                        elif cmd == "read off" or text.lower() == 'autoread off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoRead"] = False
                                cl.sendText(msg.to,"Auto add deactivated")

                        elif cmd == "sticker on" or text.lower() == 'sticker on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["sticker"] = True
                                cl.sendText(msg.to,"Deteksi sticker activated")

                        elif cmd == "sticker off" or text.lower() == 'sticker off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["sticker"] = False
                                cl.sendText(msg.to,"Deteksi sticker deactivated")

                        elif cmd == "jointicket on" or text.lower() == 'เปิดมุดลิ้ง':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoinTicket"] = True
                                cl.sendText(msg.to,"Join ticket activated")

                        elif cmd == "jointicket off" or text.lower() == 'ปิดมุดลิ้ง':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoinTicket"] = False
                                cl.sendText(msg.to,"Autojoin Tiket deactivated")

#===========COMMAND BLACKLIST============#
                        elif ("ดำ " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           wait["Talkblacklist"][target] = True
                                           cl.sendMessage(msg.to,"Successfully Become blacklist")
                                       except:
                                           pass

                        elif ("ขาว " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del wait["Talkblacklist"][target]
                                           cl.sendMessage(msg.to,"Successfully deleted blacklist")
                                       except:
                                           pass

                        elif cmd == "talkban:on" or text.lower() == 'talkban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Talkwblacklist"] = True
                                cl.sendText(msg.to,"Send a contact...")

                        elif cmd == "untalkban:on" or text.lower() == 'untalkban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Talkdblacklist"] = True
                                cl.sendText(msg.to,"Send a contact...")

                        elif ("Ban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           wait["blacklist"][target] = True
                                           cl.sendMessage(msg.to,"Successfully Become blacklist")
                                       except:
                                           pass

                        elif ("Unban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del wait["blacklist"][target]
                                           cl.sendMessage(msg.to,"Successfully deleted blacklist")
                                       except:
                                           pass

                        elif cmd == "ban:on" or text.lower() == 'ban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["wblacklist"] = True
                                cl.sendText(msg.to,"Send a contact...")

                        elif cmd == "unban:on" or text.lower() == 'unban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["dblacklist"] = True
                                cl.sendText(msg.to,"Send a contact...")

                        elif cmd == "banlist" or text.lower() == 'รายชื่อดำ':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["blacklist"] == {}:
                                cl.sendMessage(msg.to,"Tidak ada blacklist")
                              else:
                                ma = ""
                                a = 0
                                for m_id in wait["blacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                cl.sendMessage(msg.to,"Blacklist User\n\n"+ma+"\nTotal「%s」Blacklist User" %(str(len(wait["blacklist"]))))

                        elif cmd == "talkbanlist" or text.lower() == 'talkbanlist':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["Talkblacklist"] == {}:
                                cl.sendMessage(msg.to,"Tidak ada Talkban user")
                              else:
                                ma = ""
                                a = 0
                                for m_id in wait["Talkblacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                cl.sendMessage(msg.to,"Famz__Botz Talkban User\n\n"+ma+"\nTotal「%s」Talkban User" %(str(len(wait["Talkblacklist"]))))

                        elif cmd == "blc" or text.lower() == 'bc':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["blacklist"] == {}:
                                    cl.sendMessage(msg.to,"Tidak ada blacklist")
                              else:
                                    ma = ""
                                    for i in wait["blacklist"]:
                                        ma = cl.getContact(i)
                                        cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "clearban" or text.lower() == 'cb':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              wait["blacklist"] = {}
                              ragets = cl.getContacts(wait["blacklist"])
                              mc = "「%i」User Blacklist" % len(ragets)
                              cl.sendMessage(msg.to,"Sukses membersihkan " +mc)

                        elif cmd.startswith("ผีดึง "):
                          if msg._from in admin:
                               sep = text.split(" ")
                               idnya = text.replace(sep[0] + " ","")
                               conn = sw.findContactsByUserid(idnya)
                               sw.findAndAddContactsByMid(conn.mid)
                               sw.inviteIntoGroup(msg.to,[conn.mid])
                               group = sw.getGroup(msg.to)
                               xname = sw.getContact(conn.mid)
                               zx = ""
                               zxc = ""
                               zx2 = []
                               xpesan = '「 Sukses Diinvite 」\nNama contact '
                               recky = str(xname.displayName)
                               pesan = ''
                               pesan2 = pesan+"@a\n"
                               xlen = str(len(zxc)+len(xpesan))
                               xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                               zx = {'S':xlen, 'E':xlen2, 'M':xname.mid}
                               zx2.append(zx)
                               zxc += pesan2
                               text = xpesan+ zxc + "ke grup " + str(group.name) +""
                               sw.sendMessage(receiver, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                
                        elif cmd == "เปิดเชิญ" or text.lower() == 'invite on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["invite"] = True
                                sendMention(msg.to, sender, "「 Status Invite 」\nUser ", "\nSilahkan kirim kontaknya,\nKetik invite off jika sudah slesai")

                        elif cmd == "ปิดเชิญ" or text.lower() == 'invite off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["invite"] = False
                                sendMention(msg.to, sender, "「 Status Invite 」\nUser ", " \nInvite via contact dinonaktifkan")
#===========COMMAND SET============#
                        elif 'Set pesan: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set pesan: ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal mengganti Pesan Msg")
                              else:
                                  wait["message"] = spl
                                  cl.sendMessage(msg.to, "「Pesan Msg」\nPesan Msg diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'Set welcome: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set welcome: ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal mengganti Welcome Msg")
                              else:
                                  wait["welcome"] = spl
                                  cl.sendMessage(msg.to, "「Welcome Msg」\nWelcome Msg diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'Set respon: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set respon: ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal mengganti Respon Msg")
                              else:
                                  wait["Respontag"] = spl
                                  cl.sendMessage(msg.to, "「Respon Msg」\nRespon Msg diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'Set spam: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set spam: ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal mengganti Spam")
                              else:
                                  Setmain["ARmessage1"] = spl
                                  cl.sendMessage(msg.to, "「Spam Msg」\nSpam Msg diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'Set sider: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set sider: ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal mengganti Sider Msg")
                              else:
                                  wait["mention"] = spl
                                  cl.sendMessage(msg.to, "「Sider Msg」\nSider Msg diganti jadi :\n\n「{}」".format(str(spl)))

                        elif text.lower() == "cek pesan":
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "「Pesan Msg」\nPesan Msg mu :\n\n「 " + str(wait["message"]) + " 」")

                        elif text.lower() == "cek welcome":
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "「Welcome Msg」\nWelcome Msg mu :\n\n「 " + str(wait["welcome"]) + " 」")

                        elif text.lower() == "cek respon":
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "「Respon Msg」\nRespon Msg mu :\n\n「 " + str(wait["Respontag"]) + " 」")

                        elif text.lower() == "cek spam":
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "「Spam Msg」\nSpam Msg mu :\n\n「 " + str(Setmain["ARmessage1"]) + " 」")

                        elif text.lower() == "cek sider":
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "「Sider Msg」\nSider Msg mu :\n\n「 " + str(wait["mention"]) + " 」")

#===========JOIN TICKET============#
                        elif "/ti/g/" in msg.text.lower():
                          if wait["selfbot"] == True:
                              if settings["autoJoinTicket"] == True:
                                 link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                                 links = link_re.findall(text)
                                 n_links = []
                                 for l in links:
                                     if l not in n_links:
                                        n_links.append(l)
                                 for ticket_id in n_links:
                                     group = cl.findGroupByTicket(ticket_id)
                                     cl.acceptGroupInvitationByTicket(group.id,ticket_id)
                                     cl.sendMessage(msg.to, "สวัสดีครับ : %s" % str(group.name))
                                     group1 = ki.findGroupByTicket(ticket_id)
                                     ki.acceptGroupInvitationByTicket(group1.id,ticket_id)
                                     ki.sendMessage(msg.to, "สวัสดีค่ะเรามาใหม่นะ : %s" % str(group.name))
                                     group2 = kk.findGroupByTicket(ticket_id)
                                     kk.acceptGroupInvitationByTicket(group2.id,ticket_id)
                                     kk.sendMessage(msg.to, "สวัสดีค่ะเรามาใหม่นะ : %s" % str(group.name))
                                     group3 = kc.findGroupByTicket(ticket_id)
                                     kc.acceptGroupInvitationByTicket(group3.id,ticket_id)
                                     kc.sendMessage(msg.to, "สวัสดีค่ะเรามาใหม่นะ : %s" % str(group.name))
                                     group4 = km.findGroupByTicket(ticket_id)
                                     km.acceptGroupInvitationByTicket(group4.id,ticket_id)
                                     km.sendMessage(msg.to, "สวัสดีค่ะเรามาใหม่นะ : %s" % str(group.name))
                                     group5 = kb.findGroupByTicket(ticket_id)
                                     kb.acceptGroupInvitationByTicket(group5.id,ticket_id)
                                     kb.sendMessage(msg.to, "สวัสดีค่ะเรามาใหม่นะ : %s" % str(group.name))
                                     group6 = kn.findGroupByTicket(ticket_id)
                                     kn.acceptGroupInvitationByTicket(group6.id,ticket_id)
                                     kn.sendMessage(msg.to, "สวัสดีค่ะเรามาใหม่นะ : %s" % str(group.name))
                                     group7 = ko.findGroupByTicket(ticket_id)
                                     ko.acceptGroupInvitationByTicket(group7.id,ticket_id)
                                     ko.sendMessage(msg.to, "สวัสดีค่ะเรามาใหม่นะ : %s" % str(group.name))
                                     group8 = kw.findGroupByTicket(ticket_id)
                                     kw.acceptGroupInvitationByTicket(group8.id,ticket_id)
                                     kw.sendMessage(msg.to, "สวัสดีค่ะเรามาใหม่นะ : %s" % str(group.name))
                                     group9 = ke.findGroupByTicket(ticket_id)
                                     ke.acceptGroupInvitationByTicket(group9.id,ticket_id)
                                     ke.sendMessage(msg.to, "สวัสดีค่ะเรามาใหม่นะ : %s" % str(group.name))
                                     group10 = ky.findGroupByTicket(ticket_id)
                                     ky.acceptGroupInvitationByTicket(group10.id,ticket_id)
                                     ky.sendMessage(msg.to, "สวัสดีค่ะเรามาใหม่นะ : %s" % str(group.name))
                                     group11 = sw.findGroupByTicket(ticket_id)
                                     sw.acceptGroupInvitationByTicket(group11.id,ticket_id)
                                     sw.sendMessage(msg.to, "สวัสดีค่ะเรามาใหม่นะ : %s" % str(group.name))

    except Exception as error:
        print (error)


while True:
    try:
        ops = poll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                poll.setRevision(op.revision)
                thread1 = threading.Thread(target=bot, args=(op,))#self.OpInterrupt[op.type], args=(op,)
                thread1.start()
                thread1.join()
    except Exception as e:
        pass
