% include('header.tpl', title=title)
<div class="columns">
  <div class="column">
    <div class="content">
      <div class="notification is-info">
      <p>Diese Tabelle zeigt L&auml;den in Marburg an, bei denen klar oder unklar ist, ob sie noch exisitieren.</p>
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
        <td>{{round(item["score"], 2)}}</td>
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

      <nav class="pagination is-small" role="navigation" aria-label="pagination">
        % if page == 0:
        <a class="pagination-previous" disabled>Vorherige</a>
        % else:
        <a href="/inventory/{{page - 1}}" class="pagination-previous">Vorherige</a>
        % end
        <a href="/inventory/{{page + 1}}" class="pagination-next">N&auml;chste</a>
      </nav>
   </div>
  </div>
</div>
% include('footer.tpl')
