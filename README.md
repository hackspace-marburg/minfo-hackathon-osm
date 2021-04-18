# *klopf*

`*klopf*` is a light-weight automated query software for requesting the statuses of commerce shops in Marburg, Germany.
This was written for the [MInfo Hackathon](https://matheinfo.github.io/hackathon/).


## Queries

It queries shops based on [Open Street Map API](https://wiki.openstreetmap.org/wiki/API) and verifies them with the following resources:

- Timestamps used in OSM
- Websites linked in OSM
- OSM tags indicating a closed store
- [Gelbe Seiten](https://www.gelbeseiten.de/)
- [HERE Places API](https://developer.here.com/documentation/places/dev_guide/topics/what-is.html)
- Jodel API
- [Lieferando](https://www.lieferando.de/)


## Installing

You either install the dependencies in `requirements.txt` and skip directly to Running … or use Nix:

```
$ nix-shell -p chromedriver chromium
$ nix-build machnix.nix
```

## Running

Running with Nix is as easy as:

```
python -m osmcheck.web_ui
python -m osmcheck.check_mr
```


## Mirror

To create a read-only mirror, use `wget`.
There is also a mirror available [online](https://0x21.biz/klopf/).

```
wget \
  --mirror \
  --convert-links \
  --page-requisites \
  --adjust-extension \
  --exclude-directories='jodel/*' \
  'http://[::1]:8161/'
```
