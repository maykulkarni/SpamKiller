from django.shortcuts import render
from django.http import HttpResponse
import json
import imaplib
import email
from email.parser import HeaderParser
from models import MailTable
import models
from django.views.generic import ListView
import os
from sklearn.externals import joblib
import numpy
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import Pipeline
from sklearn.naive_bayes import MultinomialNB
# # encoding=utf8  
import sys  

reload(sys)  
sys.setdefaultencoding('utf8')

# Create your views here.
usrname = ""
mail = imaplib.IMAP4_SSL('imap.gmail.com')
def home(request):
	if request.method=='GET':
		return render(request, "index.html", {})
	if request.method=='POST':
		print request
		print "Post request received"
		for key, value in request.POST.items():
			print key + " : " + value
		return HttpResponse(json.dumps("POST req reply from home"),content_type="application/json")

def login_request(request):
	print os.getcwd()
	global usrname
	global mail
	if request.method=='GET':
		print "get received at login_request"
		return HttpResponse(json.dumps("success"), content_type="application/json")
	if request.method=='POST':	
		print "post received in login_request"
		uname = request.POST['uname']
		passwd = request.POST['pass']
		print uname + " " + passwd
		try:
			mail.login("mayurkulkarni012@gmail.com", 'uzumakinaruto1')
			print "Logged in as %r !" % usrname
			usrname += uname;
			return HttpResponse("OK")
		except imaplib.IMAP4.error:
			print "Login failed." + str(imaplib.IMAP4.error)
			return HttpResponse("NOK")

def show_splash(request):
	return render(request, "SplashScreen.html")

def get_first_text_block(email_message_instance):
    maintype = email_message_instance.get_content_maintype()
    if maintype == 'multipart':
        for part in email_message_instance.get_payload():
            if part.get_content_maintype() == 'text':
                return part.get_payload()
    elif maintype == 'text':
        return email_message_instance.get_payload()



def landing_page(request):
	# str = unicode(str, errors='ignore')
	mail.select('inbox')
	result, data = mail.uid('search', None, "ALL")
	# clf_spam_ham = joblib.load('pipeline_clf_svm_largeIP.pkl')
	# clf_multinomial = joblib.load('MultinomialNB_dump.pkl')
	i = len(data[0].split())
	for x in range(i, i-10, -1):
		status, data = mail.fetch(x, '(RFC822)')
		email_msg = email.message_from_string(data[0][1])
		if email_msg.is_multipart():
			for part in email_msg.walk():
				if part.get_content_type() == "text/plain":
					body = part.get_payload(decode=True).decode("quoted-printable")
					body = body.replace('\n', '<br />\n')

		else:
			body = email_msg.get_payload(decode=True).decode("quoted-printable")
		if body is None	:
			body = "None"
		# classification = clf_multinomial.predict([body.decode('utf-8', 'ignore')])
		# category = clf_spam_ham.predict([body.decode('utf-8', 'ignore')])
		rec = MailTable(mid = x, subject = email_msg['subject'], sender = email_msg['from'], mail=body.decode('utf-8', 'ignore'), category = 'category', classification = 'classification')
		rec.save()
	return render(request, "landing_page.html", {})
	
# def actualfun():
# 	mail.select('inbox')
# 	result, data = mail.uid('search', None, "ALL")
# 	clf_spam_ham = joblib.load('pipeline_clf_svm_largeIP.pkl')
# 	clf_multinomial = joblib.load('MultinomialNB_dump.pkl')
# 	i = len(data[0].split())
# 	for x in range(i, i-10, -1):
# 		status, data = mail.fetch(x, '(RFC822)')
# 		email_msg = str(email.message_from_string(data[0][1])).decode("quoted-printable")
# 		if email_msg.is_multipart():
# 			for part in email_msg.walk():
# 				if part.get_content_type() == "text/plain":
# 					body = part.get_payload(decode=True) ALTER TABLE classifier_mailtable MODIFY COLUMN mail VARCHAR(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL;

# 		else:
# 			body = email_msg.get_payload(decode=True)
# 		if body is None:
# 			body = "None"
# 		classification = clf_multinomial.predict([body])
# 		category = clf_spam_ham.predict([body])
# 		rec = MailTable(mid = x, subject = email_msg['subject'], sender = email_msg['from'], mail=body, category = category, classification = classification)
# 		rec.save()
# 	return render(request, "landing_page.html", {})

def get_context():
	senders = []
	mids = []
	subjs = []
	category = []
	classification = []
	for p in MailTable.objects.raw('SELECT * from classifier_mailtable order by mid DESC'):
		senders.append(p.sender)
		mids.append(p.mid)
		subjs.append(p.subject)
		category.append(p.category)
		classification.append(p.classification)
 #'/home/ubuntu/gigit_mayur/static/static_dirs'
	context = {
	'sender0' : senders[0],
	'sender1' : senders[1],
	'sender2' : senders[2],
	'sender3' : senders[3],
	'sender4' : senders[4],
	'sender5' : senders[5],
	'sender6' : senders[6],
	'sender7' : senders[7],
	'sender8' : senders[8],
	'sender9' : senders[9],

	'mid0' : mids[0],
	'mid1': mids[1],
	'mid2' : mids[2],
	'mid3' : mids[3],
	'mid4' : mids[4],
	'mid5' : mids[5],
	'mid6' : mids[6],
	'mid7' : mids[7],
	'mid8' : mids[8],
	'mid9' : mids[9],

	'subj0' : subjs[0],
	'subj1' : subjs[1],
	'subj2' : subjs[2],
	'subj3' : subjs[3],
	'subj4' : subjs[4],
	'subj5' : subjs[5],
	'subj6' : subjs[6],
	'subj7' : subjs[7],
	'subj8' : subjs[8],
	'subj9' : subjs[9],

	'classification0' : classification[0],
	'classification1' : classification[1],
	'classification2' : classification[2],
	'classification3' : classification[3],
	'classification4' : classification[4],
	'classification5' : classification[5],
	'classification6' : classification[6],
	'classification7' : classification[7],
	'classification8' : classification[8],
	'classification9' : classification[9],

	'category0' : category[0],
	'category1' : category[1],
	'category2' : category[2],
	'category3' : category[3],
	'category4' : category[4],
	'category5' : category[5],
	'category6' : category[6],
	'category7' : category[7],
	'category8' : category[8],
	'category9' : category[9],
	}

	return context

def inbox(request):
	
	return render(request, "inbox.html", get_context())

def get_mail(request):
	print "url is : " + request.build_absolute_uri()
	mid_ = request.build_absolute_uri()[32:]	
	print "mid is : " + str(mid_)
	ans = MailTable.objects.raw('SELECT * from classifier_mailtable where mid = ' + mid_)
	print str(ans[0].mid) + " " + ans[0].subject + " " + ans[0].sender
	return HttpResponse("<h1> htllo </h1>" )

def show_mail(request):
	print "url is : " + request.build_absolute_uri()
	mid_ = request.build_absolute_uri()[32:]	
	print "mid is : " + str(mid_)
	ans = MailTable.objects.raw('SELECT * from classifier_mailtable where mid = ' + mid_)
	context = {
	'mid_' :  str(ans[0].mid),
	'to_' : "me",
	'subject_' : ans[0].subject, 
	'sender_' : ans[0].sender,
	'body_' : str(ans[0].mail)
	}
	return render(request, "show_mail.html", context)

def svm(request):

	return render(request, "svm.html", get_context())

def category(request):

	return render(request, "category.html", get_context())