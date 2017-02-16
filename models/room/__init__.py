class Room(object):
	"""."""
	room_count = 0

	def __init__(self, arg):
		room_name = arg["<room_name>"]
		Room.room_count += 1