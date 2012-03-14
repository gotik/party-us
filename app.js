(function() {
  var app, express, io, nib, routes, stylus, users;

  express = require('express');

  stylus = require('stylus');

  nib = require('nib');

  routes = require('./routes');

  app = module.exports = express.createServer();

  app.configure(function() {
    app.set('views', __dirname + '/views');
    app.set('view engine', 'jade');
    app.use(express.bodyParser());
    app.use(express.methodOverride());
    app.use(express.cookieParser());
    app.use(stylus.middleware({
      src: __dirname + '/stylus',
      dest: __dirname + '/public',
      compile: function(str, path) {
        return stylus(str).set('filename', path).set('compress', true).use(nib())["import"]('nib');
      }
    }));
    app.use(app.router);
    return app.use(express.static(__dirname + '/public'));
  });

  app.configure('development', function() {
    return app.use(express.errorHandler({
      dumpExceptions: true,
      showStack: true
    }));
  });

  app.configure('production', function() {
    return app.use(express.errorHandler());
  });

  users = {};

  io = require('socket.io').listen(app);

  io.set('log level', 1);

  io.sockets.on('connection', function(socket) {
    socket.on('adduser', function(user) {
      if (users[user] === user) {
        return socket.emit('sign', {
          state: 0
        });
      } else {
        socket.user = user;
        users[user] = user;
        socket.emit('sign', {
          state: 1
        });
        return io.sockets.emit('update', users);
      }
    });
    return socket.on('disconnect', function() {
      delete users[socket.user];
      return io.sockets.emit('update', users);
    });
  });

  app.get('/', routes.index);

  app.listen(3000);

  console.log("Express server listening on port %d in %s mode", app.address().port, app.settings.env);

}).call(this);
