# N.E.E.B.L.E.S. CUSTOM

N.E.E.B.L.E.S. CUSTOM is the certified domestic runtime, construction-material and portability repository of the N.E.E.B.L.E.S. ecosystem.

It isolates runtime material from the Linux installation used to build or execute the project.

## Responsibilities

- certified Boss runtime corpus
- certified Calamares runtime corpus
- package and rootfs manifests
- shared module material namespaces
- module package-membership manifests
- module material-integrity manifests
- canonical domestic construction declarations
- runtime relocation and normalization tooling
- controlled development sysroots
- portable Esbirro laboratory snapshots

## Boss runtime

The canonical Boss runtime lives below:

```text
runtime/boss/
```

Runtime ELF files may be normalized so their dependency lookup remains relocatable inside the domestic corpus.

## Module material world

CUSTOM owns the canonical shared source territory for future module material:

```text
runtime/modules/packages/
runtime/modules/rootfs/
```

The physical source pool is shared. Material is not duplicated merely because more than one module requires it.

Module identity remains data. CUSTOM does not require one physical package pool per module.

## Module declarative manifests

The canonical module manifest namespace is:

```text
runtime/manifests/modules/
```

Two distinct contracts are intentionally preserved.

Package membership:

```text
<module_id>.packages.tsv
```

The package-membership TSV carries exactly:

```text
package
version
arch
filename
sha256
```

Material integrity:

```text
<module_id>.manifest.json
```

The integrity manifest carries the module identity, version and required material entries. Entry integrity uses the established N.E.E.B.L.E.S. inventory semantics:

```text
path
type
mode
size      # files
sha256    # files
target    # symlinks
```

The laws are:

```text
membership != integrity

required package membership
    -> <module_id>.packages.tsv

required material integrity
    -> <module_id>.manifest.json

shared source material
    -> runtime/modules/

observed image/runtime pool
    -> /opt/neebles-build/modules
```

A requested module is certified only against the material it declares. Unrelated material belonging to other modules in the shared pool is not an error.

For required DEBs, the package selector and integrity manifest must agree on filename membership and SHA256.

## Construction declarations

CUSTOM owns the canonical declarative source truth for domestic construction.

Construction declarations live under:

```text
runtime/construction/
```

Each declaration is identified by the safe filename:

```text
<subject>.json
```

CUSTOM owns declaration semantics.

BUILD may materialize these files but does not interpret their construction meaning.

Boss consumes declarations generically and projects them into its existing domestic workspace execution primitive.

The declaration contract remains technology-agnostic: Boss does not learn compiler identity, package-manager identity, framework identity or module-specific build logic.

An empty construction namespace is valid.

Real module declarations are introduced only when the corresponding module integration stage begins.

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

## Architectural boundary

CUSTOM and Esbirro own module construction, domestication and certification semantics.

Lifecycle does not talk to Esbirro.

Lifecycle does not domesticate runtimes.

Lifecycle does not validate module technology.

Boss governs generic execution and explicit authority; it does not become the owner of CUSTOM construction semantics.
