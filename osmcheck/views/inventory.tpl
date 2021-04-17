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
        <th>Score</th>
        <th>Status</th>
        </tr>
      </thead>
      <tbody>
      % for item in items:
      <tr>
        <th><a href="https://www.openstreetmap.org/node/{{item["entry"].osm_id}}">{{item["entry"].osm_id}}</a></th>
        <td>{{item["entry"].tags.get("name", "N/A")}}</td>
        <td>{{item["score"]}}</td>
        <td>
          % if item["score"] > 0.75:
          <span class="tag is-success">Existiert</span>
          % else:
          <span class="tag is-danger">Geschlossen</span>
          % end
        </td>
      </tr>
      %end
      </tbody>
      </table>
   </div>
  </div>
</div>
% include('footer.tpl')
