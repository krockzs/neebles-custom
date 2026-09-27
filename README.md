# N.E.E.B.L.E.S. CUSTOM

N.E.E.B.L.E.S. CUSTOM is the certified domestic runtime and portability repository of the N.E.E.B.L.E.S. ecosystem.

It isolates runtime material from the Linux installation used to build or execute the project.

## Responsibilities

- certified Boss runtime corpus
- certified Calamares runtime corpus
- package and rootfs manifests
- runtime relocation and normalization tooling
- controlled development sysroots
- portable Esbirro laboratory snapshots

## Boss runtime

The canonical Boss runtime lives below:

```text
runtime/boss/
```

Runtime ELF files may be normalized so their dependency lookup remains relocatable inside the domestic corpus.

## Esbirro portability

The portable Esbirro development laboratory lives below:

```text
portable/esbirro/
```

The repository preserves exact snapshots of the heavyweight development workspace through Git LFS.

A workstation Downloads directory is not an authoritative N.E.E.B.L.E.S. location.

The restore entrypoint is:

```text
python3 portable/esbirro/restore-workspace.py
```

`build_deps/` and `build_sysroot_6.8.2/` remain local materialized workspaces and are ignored by normal Git tracking.

The repository is authoritative.
