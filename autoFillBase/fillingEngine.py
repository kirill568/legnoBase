from instagram.agents import WebAgent, WebAgentAccount
from instagram.entities import Account

class findEngine():
	def __init__(self, entrys, keyWordsTown, keyWordsActivity, agent = 'kirillbalaev', password = 'Rbhbkk_2001', getFollowers = False):
		self.entrys = entrys
		self.agent = agent
		self.password = password
		self.getFollowers = getFollowers
		self.scaningPeoples = []
		self.sortingPeoples = []
		self.keyWordsTown = keyWordsTown
		self.keyWordsActivity = keyWordsActivity
		self.currentSortPeople = 0
		self.currentScanPeople = 0

	def recursiveScan(self, startScan = 0):
		for entry in self.entrys[startScan:]:
			try:
				self.scanPeoples(entry)
				self.currentScanPeople += 1
			except:
				print('error')
				# turned vpn
				self.playScanPeoples()
		return self.scaningPeoples

	def scanPeoples(self, entry):
		agent = WebAgentAccount(self.agent)
		agent.auth(self.password)
		account = Account(entry)
		agent.update(account)

		if self.getFollowers:
			followersCount = account.followers_count
			followsCount = account.follows_count

			follows = agent.get_follows(account, None, followsCount)[0]
			followers = agent.get_followers(account, None, followersCount)[0]

			self.scaningPeoples += follows + followers
			return
		else:
			followsCount = account.follows_count
			follows = agent.get_follows(account, None, followsCount)[0]

			self.scaningPeoples += follows
			return

	def sortPeoples(self, startSort = 0):
		agent = WebAgent()
		if startSort == 0:
			scaningPeoples = self.scaningPeoples
		else:
			scaningPeoples = self.scaningPeoples[startSort:]

		for people in scaningPeoples:
			try:
				account = Account(people)
				agent.update(account)
				biography = account.biography
				name = account.full_name
				infoAcc = biography + name
				print(people)
				if self.sortByTown(infoAcc.lower()) and self.sortByActivity(infoAcc.lower()):
					self.sortingPeoples.append(people)
				self.currentSortPeople += 1
			except:
				print('error')
				#turned vpn
				self.playSortPeoples()
		return self.sortingPeoples

	def sortByTown(self, string, counter = 0, length = 0):
		length = len(self.keyWordsTown)
		if string.find(self.keyWordsTown[counter]) != -1:
			return True
		if counter == length - 1:
			return False
		counter+=1
		return self.sortByTown(string, counter, length)

	def sortByActivity (self, string, counter = 0, length = 0):
		length = len(self.keyWordsActivity)
		if string.find(self.keyWordsActivity[counter]) != -1:
			return True
		if counter == length - 1:
			return False
		counter+=1
		return self.sortByActivity(string, counter, length)

	def playSortPeoples(self):
		return self.sortPeoples(startSort = self.currentSortPeople)

	def playScanPeoples(self):
		return self.recursiveScan(startScan = self.currentScanPeople)










		






