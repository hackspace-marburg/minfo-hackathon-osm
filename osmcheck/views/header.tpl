<!DOCTYPE html>
<html>
<head>
  <title>{{title}}</title>
  <link rel="stylesheet" href="/static/bulma.css"/>
  <meta name="viewport" content="width=device-width,initial-scale=1.0">
</head>
<body>
<div class="container">
<nav class="navbar" role="navigation" aria-label="main navigation">
  <div class="navbar-brand">
    <a class="navbar-item" href="/">
      <strong>{{title}}</strong>
    </a>

  <div id="navbarBasicExample" class="navbar-menu">
    <div class="navbar-start">
      <a class="navbar-item" href="/inventory/0">
       Inventar
      </a>

      <a class="navbar-item" href="/analysis">
       Analyse
      </a>

      <div class="navbar-item has-dropdown is-hoverable">
        <a class="navbar-link">
          Mehr
        </a>

        <div class="navbar-dropdown">
          <a href="https://github.com/hackspace-marburg/minfo-hackathon-osm" class="navbar-item">
            &Uuml;ber das Projekt
          </a>
          <a href="https://github.com/hackspace-marburg/minfo-hackathon-osm/issues" class="navbar-item">
            Fehler melden
          </a>
        </div>
      </div>
    </div>

    </div>
  </div>
</nav>

<section class="section">
