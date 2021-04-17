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
        <ul class="pagination-list">
          % if page > 2:
          <li><a href="/inventory/0" class="pagination-link">0</a></li>
          <li><span class="pagination-ellipsis">&hellip;</span></li>
          % end

          % if page > 0:
          <li><a href="/inventory/{{page - 1}}" class="pagination-link">{{page - 1}}</a></li>
          % end
          <li><a href="/inventory/{{page}}" class="pagination-link is-current" aria-current="page">{{page}}</a></li>
          % if page < pages_max:
          <li><a href="/inventory/{{page + 1}}" class="pagination-link">{{page + 1}}</a></li>

          <li><span class="pagination-ellipsis">&hellip;</span></li>
          <li><a href="/inventory/{{pages_max}}" class="pagination-link">{{pages_max}}</a></li>
          % end
        </ul>
      </nav>
   </div>
  </div>
</div>
% include('footer.tpl')
