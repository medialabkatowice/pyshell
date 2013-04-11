<br />
<div class="row">
  <div class="twelve columns">

    <div class="row">
      <div class="twelve columns">
        <div id="data-source">
          <div id="food-indices" class="left button">Indeksy cen żywności</div>
          <div id="wikipedia" class="left button">Edycje Wikipedii</div>
          <div id="slaskie" class="left button">Rejestr zabytków</div>
          <div id="custom" class="active left button">Dowolny tekst</div>
        </div>
      </div>
    </div>


    <div class="row">
      <div class="twelve columns">
        <textarea id="data-panel"></textarea>
      </div>
    </div>


    <div class="row">
      <div class="twelve columns">
        <div id="function">
          <div id="findall" class="active left button">wyszukaj</div>
          <div id="replace" class="left button">zamień</div>
          <div id="split" class="left button">podziel</div>
        </div>
      </div>
    </div>


    <div class="row">
      <div class="twelve columns">
        <form id="query-form">
          <input type="text" id="regexp-query" />
          <input type="text" id="substr" />
        </form>

      </div>
    </div>


    <div class="row">
      <div class="twelve columns">
        <pre id="data-output"></pre>
      </div>
    </div>

  </div>
</div>

%rebase base js='regexp.js'
