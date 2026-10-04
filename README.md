# N.E.E.B.L.E.S. CUSTOM

**Current integration status (2026-10-04):** certified domestic material model active; Test Module package/material world populated; generic Construction and runtime-world integration source-certified; next integrated Boss 1.0.23 / BUILD / ISO pass pending.

N.E.E.B.L.E.S. CUSTOM is the certified domestic material, construction, world and portability repository of the N.E.E.B.L.E.S. ecosystem.

CUSTOM is the canonical owner of controlled physical material and its integrity truth.

> **CUSTOM certifies what exists. Boss governs how declared capabilities are consumed. OS owns platform authority. BUILD materializes the image.**

---

## Responsibilities

CUSTOM owns:

- certified Boss runtime corpus;
- certified Calamares runtime corpus;
- package inventories;
- rootfs inventories;
- effective installed metadata;
- shared module package material;
- shared module rootfs material;
- per-module package-membership TSVs;
- per-module material-integrity manifests;
- domestic runtime manifests/worlds;
- domestic Construction declarations;
- controlled development sysroots;
- Esbirro portable snapshots;
- reproducible build/certification material.

CUSTOM does not own:

- Boss governance;
- Lifecycle state;
- module runtime IPC;
- OS platform authority semantics;
- image composition;
- module UI behavior;
- Registry installed state.

---

# Effective installed metadata

CUSTOM manifests describe the certified effective filesystem state.

For a manifest entry, `mode` is the mode expected in the effective runtime, not necessarily the raw mode stored in an upstream `.deb`.

Therefore:

```text
package payload metadata
    != necessarily
certified effective installed metadata

CUSTOM manifest
    = certified effective runtime truth
```

A materializer must verify type/integrity before applying privileged metadata.

CUSTOM remains the only owner of that metadata truth.

---

# Domestic corpora

Canonical domestic runtime territories include:

```text
runtime/boss/
runtime/calamares/
runtime/modules/
```

Boss and Calamares remain separate domestic corpora.

Module material uses a shared source pool.

---

# Module material world

Canonical shared module material:

```text
runtime/modules/packages/
runtime/modules/rootfs/
```

The pool is shared.

There is no physical package pool per module.

Module identity is declarative data.

---

## Package membership

Per-module package membership lives in:

```text
runtime/manifests/modules/<module_id>.packages.tsv
```

The canonical columns are:

```text
package
version
arch
filename
sha256
```

This file answers:

> Which exact package payloads are required by this module?

---

## Material integrity

Per-module material integrity lives in:

```text
runtime/manifests/modules/<module_id>.manifest.json
```

Entries may describe:

```text
path
type
mode
size
sha256
target
```

This file answers:

> Which exact material must exist after domestic materialization?

---

## Permanent law

```text
membership != integrity
```

And:

```text
required package membership
    -> <module_id>.packages.tsv

required material integrity
    -> <module_id>.manifest.json

shared source material
    -> runtime/modules/

observed installed/runtime pool
    -> /opt/neebles-build/modules
```

For required `.deb` files, selector membership and integrity manifest SHA256 must agree.

---

# Current Test Module material

The current Test Module domestic material contains:

```text
47 certified DEBs
2812 integrity-manifest entries
```

The module world provides the Python 3.13 + Tk runtime required by the current reference implementation.

This is **reference-module material**, not a law that future modules must use Python or Tk.

---

# Domestic runtime worlds

CUSTOM may publish materialized domestic runtime manifests that expose named worlds.

Current module world:

```text
modules.python3.13-tk
```

It declares categories for:

- executable;
- native library paths;
- runtime paths.

Current resolved material includes:

```text
usr/bin/python3.13
usr/lib/x86_64-linux-gnu
usr/lib/python3.13
usr/lib/tcltk
usr/share/tcltk
```

Boss consumes world identity generically.

Boss does not know that `modules.python3.13-tk` is Python/Tk by hardcoded source logic.

Future worlds can be introduced without recompiling Boss when the existing generic authority contract is sufficient.

---

# Construction declarations

CUSTOM owns canonical domestic Construction source truth.

Declarations live under:

```text
runtime/construction/
```

Each declaration is identified by:

```text
<subject>.json
```

A Construction declaration may describe:

- runtime authority;
- world;
- execution mode;
- desktop-session requirement;
- fixed readonly authority;
- dynamic readonly authority;
- writable authority;
- proc/dev/tmp mounts;
- working directory;
- arguments.

Boss consumes declarations generically.

CUSTOM owns the declaration meaning and material references.

BUILD transports declarations opaquely.

---

## Current Test Module construction

The Test Module declaration contains four steps:

```text
init
fetch
checkout
open-runtime
```

The first three use:

```text
runtime_authority: boss.runtime
world: boss.git
execution: foreground
session: false
```

`open-runtime` uses:

```text
runtime_authority: modules.runtime
world: modules.python3.13-tk
execution: persistent
session: true
```

and requests:

```text
boss.modules.ipc
modules.installed_runtime
```

The module runtime itself does not perform Preinstall or materialization.

Boss does.

---

# Preinstall ownership

Preinstall is not module code and not CUSTOM execution.

Correct ownership:

```text
Module
    -> declares requirement

CUSTOM
    -> owns package membership + integrity + source material

Boss
    -> executes Preinstall
    -> verifies/reuses/downloads required DEBs
    -> materializes required module rootfs
```

CUSTOM does not turn the Test Module into an apt/dpkg installer.

---

## Shared package-cache law

The module `.deb` pool is cumulative.

```text
existing file + correct SHA
    -> reuse

missing required file
    -> obtain exact certified payload

existing file + wrong SHA
    -> reject
```

Uninstall does not remove shared package material.

There is no productive package refcount or ownership garbage collection.

---

# Esbirro

The portable Esbirro laboratory lives under:

```text
portable/esbirro/
```

Its detailed operating law is documented in:

```text
portable/esbirro/README.md
```

Esbirro is the domestic engineering/certification authority that can evolve new worlds, construction capabilities, spells and authorities outside the running OS, while supplying already-domesticated material/authority into Boss and Calamares.

One truth; two use contexts:

```text
outside the OS
    -> research, certification, new worlds, new authorities, build laboratories

inside the ecosystem
    -> already-certified material/worlds consumed by Boss/Calamares
```

External Esbirro evolution must not force Boss to learn each module technology.

---

# Controlled Boss runtime

The Boss release pipeline consumes a pinned CUSTOM revision.

The controlled Boss runtime source includes:

```text
runtime/boss/rootfs
runtime/manifests/boss.rootfs.tsv
boss_current_manifest.json
```

The Boss domestic runtime manifest itself is materialized during release from Boss contracts plus the pinned CUSTOM rootfs.

CUSTOM supplies the material; release tooling produces the versioned Boss runtime package.

---

# Controlled Calamares runtime

Calamares remains independent from Boss.

Canonical material includes:

```text
runtime/calamares/packages
runtime/calamares/rootfs
runtime/manifests/calamares.packages.tsv
runtime/manifests/calamares.rootfs.tsv
calamares_current_manifest.json
```

The controlled Qt 6.8.2 world remains the build authority.

Host Qt is not build authority.

---

# Filesystem-boundary ownership

CUSTOM owns domestic material.

OS owns the filesystem-boundary implementation.

Boss consumes the explicit authority.

Therefore:

```text
CUSTOM
    -> material truth

OS
    -> boundary provider and platform authority

Boss
    -> generic consumption
```

CUSTOM must not be mutated to compensate for an OS boundary defect.

---

# BUILD relationship

BUILD may carry image-side materialized copies of CUSTOM-owned corpora and declarations.

BUILD must not reinterpret:

- Construction semantics;
- package membership semantics;
- manifest integrity semantics;
- module technology;
- CUSTOM permission truth.

When BUILD copies CUSTOM material, byte/integrity parity must remain provable.

---

# Recovery relationship

`neebles-check --module <module_id>` consumes dynamic CUSTOM truth:

```text
runtime/manifests/modules/<module_id>.packages.tsv
runtime/manifests/modules/<module_id>.manifest.json
```

It checks only the requested module's required subset.

Unrelated shared material is not an error.

---

# Repository authority

The repository is authoritative.

Downloads is not authoritative.

Machine-local temporary work is not authoritative.

The host is not build authority.

A successful compilation is not certification.

---

# Current release boundary

Latest published Boss release:

```text
1.0.22
```

Next planned Boss release:

```text
1.0.23
```

Before Boss 1.0.23 is cut:

- Test Module must be committed and pinned;
- CUSTOM Construction must reference the new immutable Test Module commit;
- CUSTOM runtime worlds/manifests must be coherent;
- CUSTOM must be committed to an immutable revision;
- Boss 1.0.23 workflow must pin that exact CUSTOM revision;
- BUILD must materialize the updated OS/CUSTOM source truth;
- Fresh Live acceptance remains required.

---

# Architectural boundary

CUSTOM and Esbirro own domestic material/construction certification semantics.

Lifecycle does not domesticate runtimes.

Lifecycle does not validate module technology.

Boss does not become a package manager or compiler interpreter.

The final law is:

> **Declare exact material and exact worlds once, certify them in CUSTOM/Esbirro, and let generic Boss machinery consume them without module-specific source branches.**
