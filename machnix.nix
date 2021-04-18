let
  nixpkgs = import (builtins.fetchTarball {
    url = "https://github.com/NixOS/nixpkgs/archive/294d1925af6462e55c76b49624b983036f0093b9.tar.gz";
    sha256 = "0x0aafl20c087vhs2mmzga20bmafsn93p271ddc9lvjsgbny80wd";
  });

  mach-nix = import (builtins.fetchGit {
    url = "https://github.com/DavHau/mach-nix/";
    ref = "refs/tags/3.2.0";
  }) {
    pkgs = nixpkgs { };

    python = "python39";
  };
in
mach-nix.mkPython {
  requirements = ''
    beautifulsoup4
    waitress
    bottle
    overpass
    requests
    selenium
    textdistance[Levenshtein]
  '';

  packagesExtra = [
    "https://github.com/hackspace-marburg/jodel_api/tarball/poll-options"
    "https://github.com/patx/pickledb/tarball/master"
  ];

  providers.shapely = "nixpkgs";
}
