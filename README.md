# N.E.E.B.L.E.S. CUSTOM

**Current integration status: Point 8 GREEN / CLOSED. Boss contract CLOSED.**

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

## Effective installed metadata

CUSTOM manifests describe the certified effective filesystem state of domestic material.

For each manifest entry, `mode` represents the mode that the file or directory must have in the effective installed runtime. It is not necessarily the raw mode stored inside an upstream package payload.

This distinction is intentional. A Debian package may ship a file with one payload mode and establish a different effective runtime mode from its maintainer scripts during package configuration. When N.E.E.B.L.E.S. domesticates that package by extracting controlled material rather than executing the original package installation transaction, CUSTOM preserves the effective installed metadata explicitly in its manifest.

Therefore:

```text
package payload metadata
    != necessarily
certified effective installed metadata

CUSTOM manifest mode
    = certified effective installed runtime mode
```

Consumers and materializers must not infer privileged runtime modes from the raw package archive alone.

A materializer must verify declared file integrity before applying manifest-declared metadata. A file whose type, size, SHA256 or symlink target does not match the certified manifest must not receive privileged metadata.

CUSTOM remains the canonical owner of this metadata truth. BUILD may materialize it, but BUILD must not maintain an independent hard-coded permission truth for the same domestic corpus.

## Boss runtime

The canonical Boss runtime lives below:

```text
runtime/boss/
```

Runtime ELF files may be normalized so their dependency lookup remains relocatable inside the domestic corpus.

## Module material world

CUSTOM owns the canonical shared source territory for module material:

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

Point 9 is now the next integration front. Test Module may be introduced there as real module material, but it must adapt to the closed Boss contract rather than redefine CUSTOM, Esbirro or Boss architecture.

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

Point 8 did not require changes to the CUSTOM material model, portable Esbirro laboratory or controlled Qt 6.8.2 world. The final Boss audit reused the existing CUSTOM-controlled material and confirmed that no second domestic execution engine or host-derived authority was needed.

## Architectural boundary

CUSTOM and Esbirro own module construction, domestication and certification semantics.

Lifecycle does not talk to Esbirro.

Lifecycle does not domesticate runtimes.

Lifecycle does not validate module technology.

Boss governs generic execution and explicit authority; it does not become the owner of CUSTOM construction semantics.


## Point 8 continuity

Point 8 globally certified the Boss contract without requiring source changes in N.E.E.B.L.E.S. CUSTOM.

The Point 7 ownership model remains canonical:

```text
CUSTOM
    -> certified domestic material
    -> module package membership
    -> module material integrity
    -> domestic construction declarations
    -> controlled Esbirro / world Modules material

OS
    -> platform authority semantics

BUILD
    -> image-side materialization and external recovery

Boss
    -> governed generic execution and explicit authority consumption
```

The Esbirro census remains:

```text
34 unique spells
42 spell insertions
250 declarative cases
```

Point 8 added no new spell and no second domestic-construction engine. `boss.workspace_execution` remains the generic governed execution primitive.

## Current handoff

```text
POINT 7 CUSTOM V2               GREEN / CLOSED
POINT 8 BOSS FINAL GATE         GREEN / CLOSED
BOSS CONTRACT                   CLOSED
CUSTOM SOURCE CHANGE IN POINT 8 NONE REQUIRED
TEST MODULE                     NEXT: POINT 9 ADAPTATION
```

Test Module may be unfrozen when Point 9 begins. Its material, package membership, integrity manifest and construction declaration must adapt to the existing CUSTOM/Esbirro contract; it does not become an architecture driver.
