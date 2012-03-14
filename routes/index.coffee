# GET home page

# static value
namedefault = 'juan'

exports.index = (req, res) ->
	res.render 'index', {
		title: 'Party Us'
		user: namedefault+Math.ceil(Math.random()*1000)
	}