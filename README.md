# N.E.E.B.L.E.S. CUSTOM

**Current integration status: Point 8 GREEN / CLOSED. Boss contract CLOSED. Point 10 dynamic Test Module integration IN PROGRESS.**

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

## Filesystem boundary continuity

The 2026-10-03 Live validation exposed an OS-side filesystem-boundary defect while Boss consumed CUSTOM domestic material.

The failure occurred when an explicitly authorized external file such as:

```text
/etc/resolv.conf
```

had to be projected into a destination that did not yet exist inside the domestic runtime.

The previous OS boundary provider attempted to manufacture that destination by copying the complete domestic top-level directory into a temporary staging tree. For `/etc/resolv.conf`, this meant traversing the full domestic `/etc`.

That behavior was invalid for the N.E.E.B.L.E.S. authority model because the domestic corpus can legitimately contain root-only material such as:

```text
/etc/sudoers.d/README
/etc/ssl/private
```

A normal user must not need read access to unrelated domestic material merely to receive one explicitly authorized external file.

The corrected OS provider no longer copies domestic top-level trees.

For an existing domestic top-level whose requested destination leaf does not yet exist, the provider now composes a temporary overlay:

```text
domestic top-level
    -> --overlay-src

temporary writable overlay
    -> --tmp-overlay

authorized external resource
    -> explicit bind onto the requested destination
```

For `/etc/resolv.conf`, the effective shape is conceptually:

```text
CUSTOM domestic rootfs /etc
    -> overlay lower source

temporary /etc overlay
    -> transient mountpoint creation

host /etc/resolv.conf
    -> explicit read-only authority grant
    -> /etc/resolv.conf inside the boundary
```

The fix is owned by N.E.E.B.L.E.S. OS, not CUSTOM.

Canonical OS fix commit:

```text
b3bd0896cdf5b03ee79f485ebdbe39b49362ed43
Fix filesystem boundary mountpoint staging
```

The important ownership rule remains unchanged:

```text
CUSTOM
    -> owns certified domestic material truth

OS
    -> owns platform filesystem-boundary implementation
    -> projects explicitly supplied authority

Boss
    -> consumes authority generically
    -> does not copy or reinterpret CUSTOM material
```

This fix required no mutation of the CUSTOM domestic corpus, package manifests, effective installed metadata, Esbirro snapshots or controlled construction worlds.

The Live validation confirmed the corrected chain:

```text
AuthoritySupply
    -> platform.filesystem_boundary
    -> OS boundary provider
    -> domestic boss.git / boss.curl
    -> GitHub registry resolution
    -> Test Module discovery
```

The architectural law is therefore explicit:

```text
authority by mount composition
    !=
authority by domestic-tree duplication
```

A boundary consumer must never duplicate a domestic directory merely to create a missing mountpoint.

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
POINT 7 CUSTOM V2                    GREEN / CLOSED
POINT 8 BOSS FINAL GATE              GREEN / CLOSED
POINT 9 TEST MODULE ADAPTATION       CLOSED / INTEGRATED
POINT 10 DYNAMIC CERTIFICATION       IN PROGRESS
BOSS CONTRACT                        CLOSED
CUSTOM MATERIAL MODEL                UNCHANGED
OS FILESYSTEM BOUNDARY FIX           GREEN / VALIDATED IN LIVE
TEST MODULE INSTALLATION             GREEN
TEST MODULE DYNAMIC SURFACES         IN PROGRESS
```

Test Module has already adapted to the existing CUSTOM/Esbirro contract and remains a consumer/template of the closed Boss architecture.

Its installation path has now been validated in Live through the real remote registry and CUSTOM preinstall flow.

The current dynamic certification front is no longer a CUSTOM redesign task. Remaining work belongs to runtime/surface integration such as module runtime registration, tray-provider execution, launcher projection, UI/config surfaces and shared state synchronization.

CUSTOM must remain stable unless new evidence shows a defect in its own certified material truth, package membership, material integrity or construction declarations.
