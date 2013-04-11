;(function ($) {
    var code_mirror = CodeMirror(document.getElementById('editor'), {
        value       : __ex_code,
        mode        :  "python",
        indentUnit  : 4,
        lineNumbers : true,
        lineWrapping: true,
        autofocus   : true
    });
    var code_solution = CodeMirror(document.getElementById('solution'), {
        value       : __ex_sol,
        mode        :  "python",
        indentUnit  : 4,
        lineNumbers : true,
        lineWrapping: true,
        autofocus   : false,
        readOnly    : true
    });


    $(document).keydown(function (e) { 
      if(e.ctrlKey && e.keyCode == 13) {
        var code = code_mirror.getValue();
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
            $.post('/tutorial/evaluate/'+__ex_id, {'code': code}, function (data) {
                $('#results').empty()
                             .removeClass('error')
                             .html(data['value'])
                             .addClass(data.error ? 'error' : 'great-success')
                $('.CodeMirror-linenumber').removeClass('error');
                if(data.line_number !== -1) {
                    $('.CodeMirror-linenumber:eq('+data.line_number+')').addClass('line-error');
                }
            });
        }
      }
    });

})(jQuery);
