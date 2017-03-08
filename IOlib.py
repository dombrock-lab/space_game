class IO:
	def say(self,text):
		print text

	def command(self):
		cmd = raw_input("cmd: ")
		return cmd

	def ask(self,question):
		self.say(question)
		answer = self.command()
		return answer

#io = IO()

#io.say("Welcome")
#name = io.ask("What is your name?")
#io.say("Hi "+name)