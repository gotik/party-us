
# Error 404

exports.not_found = (res) ->
	res.render '404', {
		locals: {
			
		}
		layout: false
		status: 404
	}

# GET home page.

# static value
namedefault = 'user'

exports.index = (req, res) ->
	res.render 'index', {
		title: 'Party Us'
		user: namedefault+Math.ceil(Math.random()*1000)
	}