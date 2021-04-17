% include('header.tpl', title=title)
<div class="columns">
  <div class="column">
    <div class="content">
      <div class="notification is-info">
      <p>Diese Tabelle zeigt L&auml;den an, bei denen unklar ist, ob sie noch exisitieren.</p>
      </div>
      <table class="table">
      <thead>
        <tr>
        <th><abbr title="Position">#</abbr></th>
        <th>Gesch&auml;tsname</th>
        <th>Adresse</th>
        <th>Score</th>
        <th>Aktion</th>
        </tr>
      </thead>
      <tbody>
      <tr>
        <th>1</th>
        <td>Sefa's D&ouml;ner und Pizzahaus</td>
        <td>Am Gr&uuml;n 1, 35037 Marburg</td>
        <td>1.0</td>
        <td>
          <button class="button is-success is-light">Existiert</button>
          <button class="button is-danger is-light">Geschlossen</button>
        </td>
      </tr>
       <tr>
        <th>1</th>
        <td>Sefa's D&ouml;ner und Pizzahaus</td>
        <td>Am Gr&uuml;n 1, 35037 Marburg</td>
        <td>1.0</td>
       <td>
          <button class="button is-success is-light">Existiert</button>
          <button class="button is-danger is-light">Geschlossen</button>
        </td>
      </tr>
      </tbody>
      </table>
   </div>
  </div>
</div>
% include('footer.tpl')
