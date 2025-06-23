class QuizBrain:
	def __init__(self, q_lis):
		self.question_no = 0
		self.question_list = q_lis
		self.score = 0

	def next_question(self):
		current_question = self.question_list[self.question_no]
		self.question_no += 1
		user_answer = input(f"Q. {self.question_no}: {current_question.text}(True/False): ")
		# current_question.answer is correct answer stored in list
		self.check_answer(current_question.ans, user_answer)

	def check_answer(self, correct_answer, user_answer):
		if user_answer.lower() == correct_answer.lower():
			print("You got it right!")
			self.score += 1

		else:
			print("That's Wrong")
		print(f"Correct answer was : {correct_answer}")
		print(f"Your current score is : {self.score}/{self.question_no}")

	def still_have_questions(self):
		return self.question_no < len(self.question_list)
