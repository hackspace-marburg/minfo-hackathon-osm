% include('header.tpl', title=title)
<div class="columns">
  <div class="column">
    <div class="content">
      <div class="notification is-info">
      <p>Diese Tabelle zeigt L&auml;den in Marburg an, bei denen klar oder unklar ist, ob sie noch exisitieren.</p>
      </div>
      <table class="table is-striped">
      <thead>
        <tr>
        <th><abbr title="Position">#</abbr></th>
        <th>Gesch&auml;tsname</th>
        <th>Score</th>
        <th>Status</th>
        <th>Get HR involved</th>
        </tr>
      </thead>
      <tbody>
      % for item in items:
      <tr>
        <th><a href="https://www.openstreetmap.org/node/{{item["entry"].osm_id}}">{{item["entry"].osm_id}}</a></th>
        <td>{{item["entry"].tags.get("name", "N/A")}}</td>
        <td>{{round(calc_score(item["checks"]), 2)}}</td>
        <td>
          % if calc_score(item["checks"]) >= 0.75:
          <span class="tag is-success">Existiert</span>
          % else:
          <span class="tag is-danger">Geschlossen</span>
          % end
        </td>
        <td>
          % if "name" in item["entry"].tags:
          <a class="tags has-addons" href="/jodel/poll/osm:{{item["entry"].osm_id}}?city={{city}}&lat={{item["entry"].lat}}&lng={{item["entry"].lon}}&channel={{jodel_channel}}&message={{quote("Gibt es " + item["entry"].tags.get("name") + " noch? #frage")}}&poll_option=Ja&poll_option=Nein">
            <span class="tag is-warning">Jodel</span>
            <span class="tag is-dark">Ask</span>
          </a>
          % end
        </td>
      </tr>
      <tr>
        <th>&nbsp;</th>
        <td colspan="4">
          <div class="field is-grouped is-grouped-multiline">
            % for k, v in item["checks"].items():
            <div class="control">
              <div class="tags has-addons">
                <span class="tag is-light">{{k}}</span>
                % if not v:
                <span class="tag is-warning">N/A</span>
                % elif v >= 0.75:
                <span class="tag is-success">{{round(v, 2)}}</span>
                % else:
                <span class="tag is-danger">{{round(v, 2)}}</span>
                % end
              </div>
            </div>
            %end
          </div>
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

        % if page < pages_max:
        <a href="/inventory/{{page + 1}}" class="pagination-next">N&auml;chste</a>
        % else:
        <a class="pagination-next" disabled>N&auml;chste</a>
        % end

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
