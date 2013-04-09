<!DOCTYPE html>

<!-- paulirish.com/2008/conditional-stylesheets-vs-css-hacks-answer-neither/ -->
<!--[if lt IE 7]> <html class="no-js lt-ie9 lt-ie8 lt-ie7" lang="en"> <![endif]-->
<!--[if IE 7]>    <html class="no-js lt-ie9 lt-ie8" lang="en"> <![endif]-->
<!--[if IE 8]>    <html class="no-js lt-ie9" lang="en"> <![endif]-->
<!--[if gt IE 8]><!--> <html class="no-js" lang="en"> <!--<![endif]-->
<head>
  <meta charset="utf-8" />

  <!-- Set the viewport width to device width for mobile -->
  <meta name="viewport" content="width=device-width" />

  <title>PyShell</title>
  
  <!-- Included CSS Files (Compressed) -->
  <link rel="stylesheet" href="/static/stylesheets/foundation.css">
  <link rel="stylesheet" href="/static/stylesheets/app.css">

  <link href='http://fonts.googleapis.com/css?family=Ubuntu:300&subset=latin,latin-ext' rel='stylesheet' type='text/css'>
  <link href='http://fonts.googleapis.com/css?family=PT+Mono&subset=latin,latin-ext' rel='stylesheet' type='text/css'>

  <script src="/static/javascripts/modernizr.foundation.js"></script>

  <!-- code mirror -->
  <script src="/static/codemirror/lib/codemirror.js"></script>
  <link rel="stylesheet" href="/static/codemirror/lib/codemirror.css">
  <script src="/static/codemirror/mode/python/python.js"></script>

  <!-- IE Fix for HTML5 Tags -->
  <!--[if lt IE 9]>
    <script src="http://html5shiv.googlecode.com/svn/trunk/html5.js"></script>
  <![endif]-->

</head>
<body>

  %include
  
  
  <!-- Included JS Files (Compressed) -->
  <script src="/static/javascripts/foundation.min.js"></script>

  <!-- Initialize JS Plugins -->
  <script src="/static/javascripts/app.js"></script>

  %if js:
  <!-- User defined JS -->
  <script src="/static/javascripts/{{js}}"></script>
  %end
</body>
</html>
