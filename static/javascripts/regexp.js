(function () {
  $('#substr').hide();
  $('#data-output').hide();
  $('input[type="text"]').val("")

  $('input[type="text"]').keypress(function (e) {
    if(e.which === 13) {
      $('#query-form').submit();
    }
  });

  $('#query-form').submit(function () {
    var opts = {
      query  : $('#regexp-query').val(),
      text   : $('textarea').val(),
      func   : $('#function > .active').attr('id'),
      substr : $('#substr').val() || ''
    };

    $.post('/regexp/query', opts, function (data) {
      var lines = JSON.parse(data);
      var out;

      if(opts.func === 'replace') {
        out = lines.join("<br />");
      }
      else {
        out = lines.map(function (e) {
          return e.join(' &#166; ');
        }).join("<br />");
      }

      $('#data-output').html(out).show();
    });

    return false;
  });

  $('#data-source > .button').click(function () {
    var id = $(this).attr('id');
    var new_text = function (txt) {
      var txt = txt || "";

      $('textarea').empty().val(txt);
    }

    $('#data-source > .active').removeClass('active');
    $(this).addClass('active');

    if(id === 'custom') {
      new_text('');
      $('textarea').focus();
    }
    else {
      $.get('/static/data/'+id, function (data) {
        new_text(data);
      });
    }
  });

  $('#function > .button').click(function () {
    var id = $(this).attr('id');

    $('#function > .active').removeClass('active');
    $(this).addClass('active');

    if(id === 'replace') {
      $('#substr').show();
    }
    else {
      $('#substr').hide();
    }
  });

  $('#data-source').find('#food-indices').click();
  $('#function').find('#findall').click();
})();
