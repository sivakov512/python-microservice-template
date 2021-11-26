{ pkgs ? import <nixpkgs> {} }:

let
  stable = import (builtins.fetchTarball https://nixos.org/channels/nixos-21.05/nixexprs.tar.xz) {};
  unstable = import (builtins.fetchTarball https://nixos.org/channels/nixos-unstable/nixexprs.tar.xz) {};
in

let
  libraries = with stable; [ stdenv.cc.cc.lib ];

  pip-packages = packages: [
    packages.pip
    packages.poetry
    (packages.python-lsp-server.override {
      withAutopep8 = false;
      withFlake8 = false;
      withMccabe = false;
      withPycodestyle = false;
      withPydocstyle = false;
      withPyflakes = false;
      withPylint = false;
      withYapf = false;
    })
  ];
  python = unstable.python39.withPackages pip-packages;
in

stable.mkShell {
  buildInputs = [
    python
    stable.protobuf
    (unstable.go-migrate.overrideAttrs (attrs: { buildFlags = "-tags=postgres"; }))
  ]
  ++ libraries;

  PROTOC = "${pkgs.protobuf}/bin/protoc";
  PROTOC_INCLUDE = "${pkgs.protobuf}/include";

  LD_LIBRARY_PATH = pkgs.lib.makeLibraryPath libraries;

  POSTGRES_URL = "postgres://guest:guest@localhost:5432/guest?sslmode=disable";
}
