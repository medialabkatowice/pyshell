;(function ($) {
    var code_mirror = CodeMirror(document.getElementById('editor'), {
        value        : __code,
        mode         : "python",
        indentUnit   : 4,
        lineNumbers  : true,
        lineWrapping : true,
        autofocus    : true
    });
    code_mirror.setCursor(2, 0);

    // arm ctrl+enter as a submit shortcut
    $(document).keydown(function (e) { 
      if(e.ctrlKey && e.keyCode == 13) {

        var code = code_mirror.getValue();
        var ex_id = $(this).attr('data-ex_id');

        // validate if user doesn't want to import dengerous modules
        var dengerous = code.split('\n').filter(function (line) {
            var modules = ['sys', 'os'].filter(function (e) {
                var rx = new RegExp("\\s*(from|import).+\\b"+e+"\\b");
                return rx.test(line);
            });
            return modules.length !== 0;
        });

        if(dengerous.length !== 0) {
            alert("Nie wolno importować modułów os i sys!");
        }
        else {
            // execute the code
            $.post('/console/evaluate', {'code': code}, function (data) {
                $('#results').empty()
                             .removeClass('error')
                             .html(data['value'])
                             .addClass(data.error ? 'error' : '')
                $('.CodeMirror-linenumber').removeClass('error');
                if(data.line_number !== -1) {
                    $('.CodeMirror-linenumber:eq('+data.line_number+')').addClass('line-error');
                }
            });
        }
      }
    });

})(jQuery);
