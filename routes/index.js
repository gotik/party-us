(function() {
  var namedefault;

  namedefault = 'juan';

  exports.index = function(req, res) {
    return res.render('index', {
      title: 'Party Us',
      user: namedefault + Math.ceil(Math.random() * 1000)
    });
  };

}).call(this);
