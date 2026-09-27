# Esbirro Portable Workspace

This directory preserves the development laboratory used by
the N.E.E.B.L.E.S. domestic authority and Esbirro work.

The repository is authoritative.

Downloads, temporary directories and machine-local state
must never be required to continue development.

## Snapshots

build_deps.tar.zst

Exact dependency workspace snapshot.

build_sysroot_6.8.2.tar.zst

Exact Qt 6.8.2 development sysroot and laboratory snapshot.

## Historical external material

archive/downloads-neebles.tar.zst

Preserves N.E.E.B.L.E.S. material that previously existed
outside the repositories in Downloads.

Downloads is therefore not an authoritative project location.

## Restore

Run:

python3 portable/esbirro/restore-workspace.py

The restore tool verifies SHA-256 before extraction.

## Deprecated material

Historical private-runtime source found inside old sysroot work
copies is preserved only as part of the exact sysroot snapshot.

It is not restored into the canonical Boss source tree and
does not regain architectural authority.
