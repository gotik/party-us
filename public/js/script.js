(function() {
  var flag, node, socket;

  flag = false;

  node = {};

  socket = io.connect('', {
    'reconnect': true,
    'reconnection delay': 500,
    'max reconnection attempts': 5
  });

  socket.on('sign', function(data) {
    if (data.state === 0) {
      $('#user').addClass('rounded_error');
      node.err($('.box_login'), node.errors.EMPTY);
    } else {
      $('#alert').hide('slow');
      flag = true;
      $('#container').hide('slow', function() {
        return $('#container').remove();
      });
    }
    return $('#loading').hide();
  });

  socket.on('update', function(data) {
    if (flag) {
      $('#users').empty();
      return $.each(data, function(key, value) {
        return $('#users').append('<div class="user">' + key + '</div>');
      });
    }
  });

  socket.on('handle', function(data) {
    return $('#' + data.obj[0]).css({
      'left': data.obj[1] + 'px',
      'top': data.obj[2] + 'px'
    });
  });

  node = {
    errors: {
      NICK_TAKEN: 'Nick taken :(',
      EMPTY: '¬¬"'
    },
    init: function() {
      return $('#buttom').on('click', function(event) {
        event.preventDefault();
        $('#loading').show();
        if ($('#user').val().trim() === '') {
          $('#user').addClass('rounded_error');
          node.err($('.box_login'), node.errors.EMPTY);
          return $('#loading').hide();
        } else {
          $('#alert').hide('slow');
          $('#user').removeClass('rounded_error');
          return socket.emit('adduser', $('#user').val());
        }
      });
    },
    err: function(obj, msg) {
      var i, _i, _len, _ref, _results;
      $('#alert').html('<img src="/img/error.png" />' + msg);
      $('#alert').show();
      _ref = 5;
      _results = [];
      for (_i = 0, _len = _ref.length; _i < _len; _i++) {
        i = _ref[_i];
        _results.push(obj.animate({
          "left": '+=12'
        }, 80).animate({
          "left": '-=12'
        }, 80));
      }
      return _results;
    }
  };

  $(function() {
    return node.init();
  });

}).call(this);
