<br />
<div class="row">
  <div class="twelve columns">

    <div class="row">
      <div class="four columns">
        <p id="info">Naciśnij Ctrl+Enter by uruchomić program</p>
      </div>
    </div>
    
    <div class="row">
      <div class="twelve columns">
        <div id="editor">
        </div>
      </div>
    </div>
    
    <br />
    
    <div class="row">
      <div class="six columns left">
        <pre id="results"></pre>
      </div>
      <div class="six columns left">
        <pre id="desc">{{!desc}}</pre>
      </div>
    </div>

    <br />

    <div class="row">
      <div class="twelve columns">
        <h5>Przykładowe rozwiązanie</h5>
        <div id="solution">
        </div>
      </div>
    </div>
    
  </div>
</div>

<br />
<div class="row">
  <div class="twelve columns">
  </div>
</div>

<script>
  var __ex_code = "{{!code}}";
  var __ex_sol  = "{{!sol}}";
  var __ex_id   = {{ex_id}};
</script>

%rebase base js='exercise.js'
