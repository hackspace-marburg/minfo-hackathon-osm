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
  requirements = builtins.readFile ./requirements.txt;
}
