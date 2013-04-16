#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Main access point to the kuklok prototype
'''

from bottle import request, redirect, route, run, template, static_file, default_app
from beaker.middleware import SessionMiddleware

session_opts = {
    'session.type': 'file',
    'session.cookie_expires': 3600,
    'session.data_dir': './session_data',
    'session.auto': True
}
app = SessionMiddleware(default_app(), session_opts)
errors = {
    'IndentationError' : u'Python jest wyczulony na wcięcia. Gdzieś jest nierówno!',
    'IndexError'       : u'Nie ma tylu elementów na tej liście',
    'ImportError'      : u'Chyba chcesz zaimportować moduł/bibliotekę, której nie ma',
    'KeyError'         : u'Jest gdzieś słownik, ale nie ma takiego kluczyka',
    'SyntaxError'      : u'Brakuje gdzieś przecinka, nawiasu albo szukamy literówek!',
    'ZeroDivisionError': u'La la la, nie dziel przez zero!',
    'NameError'        : u'Chyba próbujesz się zawołać zmienną, której nie ma',
    'AttributeError'   : u'To pudełko nie ma takiego śrubokręta',
    'EOFError'         : u'Hm... Sam nie wiem, co się podziało... Krzycz "POMOCY!"',
    'ReferenceError'   : u'Hm... Sam nie wiem, co się podziało... Krzycz "POMOCY!"',
    'SystemError'      : u'Hm... Sam nie wiem, co się podziało... Krzycz "POMOCY!"',
    'TypeError'        : u'Dajesz napis, myślisz liczba? Coś się posypało w typach pudełek',
    'ValueError'       : u'Hm... Sam nie wiem, co się podziało... Krzycz "POMOCY!"',
    'IOError'          : u'Hm... Sam nie wiem, co się podziało... Krzycz "POMOCY!"',
    'UnboundLocalError': u'Hm... Sam nie wiem, co się podziało... Krzycz "POMOCY!"',
}


@route('/')
def _main():
    return template('index')


# -------> CONSOLE
@route('/console')
def _console(code=None):
    return template('console', {'code': code or '# coding: utf-8\\n\\n'})

@route('/console/evaluate', method='POST')
def _console_eval():
    code = uni(request.POST.get('code', u''))

    return _evaluate(code)


# -------> NOTATKI
@route('/notes')
def _notes():
    return template('notes')

@route('/notes/<note_id:int>')
def _notes_code(note_id=0):
    code = open('notes/%03d.py' % note_id).read()
    code = code.replace('\n', '\\n').replace('"', '\\"')

    return _console(code)

# -------> TUTORIAL
@route('/tutorial')
def _tutorial():
    return template('tutorial')

@route('/tutorial/<ex_id:int>')
def _index(ex_id=1):
    code = open('exs/ex_%03d.py' % ex_id).read()
    code = code.replace('\n', '\\n').replace('"', '\\"')

    desc = u"Oczekiwany wynik to:\n" + \
           u"--------------------\n\n" + \
           open('exs/re_%03d.py' % ex_id).read().decode('utf-8')

    sol  = open('exs/sl_%03d.py' % ex_id).read().decode('utf-8')
    sol  = sol.replace('\n', '\\n').replace('"', '\\"')

    return template('exercise', {'code': code, 
                                 'desc': desc, 
                                 'sol' : sol,
                                 'ex_id': ex_id})

@route('/tutorial/evaluate/<re_id:int>', method='POST')
def _tutorial_eval(re_id):
    code = uni(request.POST.get('code', u''))
    result = _evaluate(code)

    if result['error']:
        return result
    else:
        user_result = result['value']
        solution = open('exs/re_%03d.py' % re_id).read().decode('utf-8')
        success  = solution == user_result

        if success:
            msg = u"Brawo!\n------\n\n%s"
        else:
            msg = u"Twój wynik to:\n--------------\n\n%s" + \
                  u"\n----------------\nPróbuj dalej!"
            result['error'] = True

        result['value'] = msg % user_result

        return result


# ---------> REGEXP SANDBOX
@route('/regexp', method='GET')
def _regexp():
    return template('regexp')

@route('/regexp/tutorial', method='GET')
def _regexp_tutorial():
    return template('regexp_tutorial')

@route('/regexp/query', method='POST')
def _query():
    import re
    import json as js

    query  = request.POST.get('query', '').decode('utf-8')
    text   = request.POST.get('text', '').decode('utf-8')
    func   = request.POST.get('func', '')
    substr = request.POST.get('substr', '')
    
    todo = {
        'findall': re.findall,
        'replace': lambda r, e: re.sub(r, substr, e),
        'split'  : re.split
    }[func]

    regexp = re.compile(query, re.UNICODE)
    # FIX Why the hell this if at the end of list comprehention?
    result = [todo(regexp, unicode(line)) for line in text.split('\n') if regexp.search(line)]
    
    return js.dumps(result, ensure_ascii=False)



# ------> EVALUATOR
def _evaluate(user_code):
    import StringIO
    import sys
    import traceback

    sysout  = sys.stdout
    userout = StringIO.StringIO()
    sys.stdout = userout

    line_number = -1

    try:
        code  = '# coding: utf-8\n'
        code += 'def __user_function():\n'
        code += user_code
        code += '\n'
        code += '__user_function()'

        exec code

        value = userout.getvalue()
        error = False
    except:
        exc_type, exc_value, exc_tb = sys.exc_info()
        tb = traceback.extract_tb(exc_tb)
        fname, line, func, source = tb.pop()

        error_name = exc_type.mro()[0].__name__
        error_desc = unicode(exc_value)

        if error_name == 'SyntaxError':
            try:
                # extra 2 at the end is for the eval wrapper overhead
                line_number = int(error_desc.strip(' )').rsplit(' ', 1).pop()) - 3
                error_desc  = u'invalid syntax'
            except ValueError:
                pass
        else:
            if func == '__user_function':
                line_number = line-3

        value = u"%s:\n\n!!! %s !!!" % (errors[error_name], error_desc)
        error = True
            

    return {
        'value': value,
        'error': error,
        'line_number': line_number
    }




# --------> STATIC FILES
@route('/static/<path:path>')
def _serve_files(path):
    '''
    Static files route
    '''
    return static_file(path, root='static/')


def uni(code):
    '''
    Take a code and make all strings unicodes
    '''
    import re

    def _uni(line):
        subs = []
        IN = False
        p = ''
        for i, c in enumerate(line):
            if c in ['"', "'"] and p != '\\':
                if not IN:
                    IN = True
                    ch = c
                    start = i
                elif c == ch:
                    subs.append(start)
                    ch = None
                    start = None
                    IN = False
            p = c

        splits = []
        last_stop = 0
        for start in subs+[len(line)]:
            splits.append(line[last_stop:start])
            last_stop = start

        # add an extra tab to wrap it into a function later on
        uni_line = '\t' + 'u'.join(splits)
        return re.sub(r"\buu(\"|')", "u\g<1>", uni_line)

    return '\n'.join(_uni(line) for line in code.split('\n'))

# -- run the app
if __name__ == '__main__':
    import sys

    if len(sys.argv) == 2 and sys.argv[1] == 'debug':
        run(app=app, host='localhost', port=8082, reloader=True)
    else:
        application = app

