def create_counter(num):
	counter = {'value': num}
        
	def up():
		counter['value'] += 1
		return counter['value']
	def down():
		counter['value'] -= 1
		return counter['value']
	return {'up':up ,'down': down}
