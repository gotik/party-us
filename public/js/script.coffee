flag = false
node = {}
socket = io.connect '', {
	'reconnect': true
	'reconnection delay': 500
	'max reconnection attempts': 5
}

# Excuted when you signed
# if state = 0 nickname is already taken
# else you can continue
socket.on 'sign', (data) ->
	if data.state==0 
		$('#user').addClass 'rounded_error'
		node.err $('.box_login'), node.errors.EMPTY
	else
		$('#alert').hide 'slow'
		flag=true
		$('#container').hide 'slow', () ->
			$('#container').remove();
	$('#loading').hide()

# Executed when new users sign or leave
socket.on 'update', (data) ->
	if flag
		$('#users').empty()
		$.each data, (key, value) ->
			$('#users').append '<div class="user">' + key + '</div>'

# Namespace
node = {
	# Static values
	errors: {
		NICK_TAKEN : 'Nick taken :('
		EMPTY : '¬¬"'
	}

	# Initialize function
	init: () ->
		# Login button action
		$('#buttom').on 'click', (event) ->
			event.preventDefault()
			$('#loading').show()
			# If the nick you entered is empty fire error
			if $('#user').val().trim() == ''
				$('#user').addClass 'rounded_error'
				node.err $('.box_login'), node.errors.EMPTY
				$('#loading').hide()
			else
				$('#alert').hide 'slow'
				$('#user').removeClass 'rounded_error'
				socket.emit 'adduser', $('#user').val()

	# Function for manage the errors
	err: (obj, msg) ->
		$('#alert').html '<img src="/img/error.png" />'+msg
		$('#alert').show()
		for i in 5
			obj.animate({"left": '+=12'}, 80).animate({"left": '-=12'}, 80)
}

# Initialize all
$ ->
	node.init()