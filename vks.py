import vk_api
import datetime # работа с датой и временем
import time

while True:
	vk = vk_api.VkApi(token="643865e1e2d7b54006996f31cde903f84c537ba528b446dbeebcbb3e10a3455b46391fb093fd0ce01c195")

	delta = datetime.timedelta(hours=3, minutes=0) 
	t = (datetime.datetime.now(datetime.timezone.utc) + delta)

	nowtime = t.strftime("%H:%M")
	nowdate = t.strftime("%d.%m.%Y")

	on = vk.method("friends.getOnline")
	counted = len(on)

	vk.method("status.set", {"text": nowtime + " * " + nowdate + " * " + "Друзей онлайн: " + str(counted)})
	time.sleep(30) 
