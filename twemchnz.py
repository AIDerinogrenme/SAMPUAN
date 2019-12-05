import mechanize
tw = mechanize.Browser()
tw.set_handle_robots(False)
tw.addheaders=[('User-agent','Chrome')]
tw_girisi = 'https://mobile.twitter.com/login'
user = raw_input('kullanýcý:')
pas = raw_input('þifre :')
tw.open(tw_girisi)
tw.select_form(nr=0)
tw["session[username_or_email]"] = user
tw['session[password]'] = pas
send = tw.submit()
print send.geturl()