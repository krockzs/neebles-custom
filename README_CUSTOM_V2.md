# N.E.E.B.L.E.S. CUSTOM V2

**Module domestic-material authority**

**Current integration status (2026-10-05):** **Point 1 CLOSED / GREEN.** CUSTOM V2 now represents the certified module-material model consumed by Boss through permanent package pools, persistent MaterialBinding and ephemeral RuntimeLease. The legacy productive shared module-rootfs model is retired. **Point 2 remains pending. No new Boss release is claimed here.**

CUSTOM V2 is the certified domestic material, world and module-construction truth for N.E.E.B.L.E.S. modules.

> **CUSTOM V2 declares and certifies WHAT module material exists. Boss governs HOW that certified material is authenticated, bound to an installed module and executed.**

---

# Hard boundary: CUSTOM V2 != CUSTOM classic

CUSTOM V2 is specifically the module-material architecture.

```text
CUSTOM classic
    -> Boss runtime corpus
    -> Calamares runtime corpus
    -> classic controlled build material

CUSTOM V2
    -> module package material
    -> Essential global layer
    -> per-module deltas
    -> module membership/integrity manifests
    -> module domestic runtime/world truth
    -> module Construction declaration truth
```

A module-material failure must not be "fixed" by mutating CUSTOM classic unless independent evidence proves a classic-corpus defect.

---

# Responsibilities

CUSTOM V2 owns:

- exact Essential package membership;
- exact Essential material integrity;
- exact per-module package-delta membership;
- exact per-module material integrity;
- certified reusable `.deb` source material;
- module domestic runtime/world payloads;
- module Construction declarations and references;
- module material metadata required by Boss Preinstall;
- source truth consumed by module recovery verification.

CUSTOM V2 does **not** own:

- Boss MaterialBinding persistence semantics;
- Boss RuntimeLease lifetime;
- Boss transaction semantics;
- Lifecycle state/execution semantics;
- module runtime IPC;
- OS platform authority semantics;
- BUILD image-composition semantics;
- module private technology or UI behavior;
- CUSTOM classic Boss/Calamares corpus semantics.

---

# Canonical module material layout

The Point 1 source model is:

```text
runtime/modules/packages/essentials/*.deb
runtime/modules/packages/*.deb

runtime/manifests/modules/essentials.packages.tsv
runtime/manifests/modules/essentials.manifest.json

runtime/manifests/modules/<module_id>.packages.tsv
runtime/manifests/modules/<module_id>.manifest.json

runtime/modules/domestic-runtime.json
```

The productive model does **not** require one persistent composed `runtime/modules/rootfs/` as module runtime truth.

---

# Essential is a real global layer

Essential is shared certified module-runtime material.

It is **not**:

- a fake module;
- a module identity;
- a per-module duplicate;
- a convenience rootfs snapshot that each module owns independently.

Its contracts are:

```text
runtime/manifests/modules/essentials.packages.tsv
runtime/manifests/modules/essentials.manifest.json
```

The current Point 1 certification records:

```text
Essential packages    59 DEBs
Essential entries     3538
```

A module delta can rely on Essential while remaining declaratively separate from it.

---

# Per-module delta

Each module owns only the certified material that is not already part of the global Essential layer.

For module identity `<module_id>`:

```text
package membership
    -> runtime/manifests/modules/<module_id>.packages.tsv

material integrity
    -> runtime/manifests/modules/<module_id>.manifest.json
```

The permanent law remains:

```text
membership != integrity
```

The membership TSV answers:

> Which exact package payloads belong to this layer?

The integrity manifest answers:

> Which exact filesystem objects and metadata must this certified layer produce?

For every required `.deb`, package identity/version/architecture/filename/SHA truth must remain coherent across the certified contracts.

---

# Current Test Module material

The reference Test Module is now represented as a delta over Essential:

```text
Essential layer         59 certified DEBs
Test Module delta       32 certified DEBs
```

Point 1 physical certification observed:

```text
Essential entries       3538
Test Module entries     2210
compatible overlap      16 directories
file/symlink collisions 0
```

The combined layers executed the reference Python/Tk world successfully during certification:

```text
Python 3.13.5
_tkinter / Tcl 8.6
unresolved ELF dependencies: 0
```

Python/Tk remains reference-module technology, not a CUSTOM V2 architectural law.

---

# Domestic runtime worlds

CUSTOM V2 publishes module runtime/world truth generically.

Current reference world:

```text
modules.python3.13-tk
```

The world can describe executable/native-library/runtime-path requirements without forcing Boss to understand the technology name.

Boss consumes the world through generic runtime authority and Workspace contracts.

Future module worlds may be introduced without recompiling Boss when the existing generic capability set is sufficient.

---

# Construction declarations

CUSTOM V2 owns the module-side Construction declaration truth consumed by Boss.

Canonical declaration source territory remains:

```text
runtime/construction/
```

Declarations remain declarative and may describe:

- runtime authority;
- world;
- execution mode;
- desktop-session requirement;
- fixed read-only authority;
- dynamic read-only authority;
- writable authority;
- proc/dev/tmp mounts;
- working directory;
- arguments.

The reference Test Module declaration currently contains:

```text
init
fetch
checkout
open-runtime
```

The first three remain finite Boss-runtime construction steps. `open-runtime` uses:

```text
runtime_authority: modules.runtime
world: modules.python3.13-tk
execution: persistent
session: true
```

The module declares the WHAT. Boss supplies the generic HOW.

---

# Preinstall contract with Boss

Preinstall is Boss behavior over CUSTOM V2 truth.

The productive sequence is:

```text
Boss resolves/authenticates the selected CUSTOM V2 revision
    -> validates Essential membership + integrity
    -> validates module-delta membership + integrity
    -> validates the module runtime manifest payload
    -> ensures exact Essential DEBs in the permanent Essential pool
    -> ensures exact module-delta DEBs in the permanent module pool
    -> produces MaterialBindingInput
```

Preinstall does **not** publish a global composed module rootfs.

Preinstall does **not** make the module download/materialize its own dependencies.

---

# Permanent package-cache law

The installed system keeps verified `.deb` material as a cumulative reusable arsenal.

```text
/opt/neebles-build/modules/packages/essentials/
    -> Essential pool

/opt/neebles-build/modules/packages/
    -> module-delta pool
```

For a required package:

```text
existing file + correct SHA
    -> reuse

missing required file
    -> obtain exact certified payload

existing file + wrong SHA
    -> reject
```

Uninstall does not erase the permanent package arsenal.

A later module may reuse already-present certified packages.

---

# MaterialBinding relationship

MaterialBinding is **Boss-owned persistent state** built from authenticated CUSTOM V2 truth.

CUSTOM V2 supplies the authoritative inputs; Boss persists which exact certified material belongs to the installed module.

The binding ties together:

```text
module identity
installed module version
CUSTOM V2 revision
Essential authority blobs
module-delta authority blobs
runtime manifest payload
```

The `.deb` files are not duplicated into the binding; they remain in permanent pools.

This prevents an installed module from silently drifting to unrelated later module-material metadata.

---

# RuntimeLease relationship

RuntimeLease is **Boss-owned ephemeral execution state**.

When `modules.runtime` executes, Boss uses the active MaterialBinding to create an independent temporary runtime:

```text
MaterialBinding
    -> new lease territory
    -> materialize Essential + module delta
    -> lease/rootfs
    -> authenticated domestic-runtime.json
    -> generic Workspace execution
```

The lease exists for the real lifetime of the process and disappears on drop.

Concurrent executions receive independent leases.

CUSTOM V2 therefore does not publish a mutable global user-side runtime rootfs as execution truth.

---

# Productive user-side territories

CUSTOM V2 material is consumed into these Boss-owned territories:

```text
/opt/neebles-build/modules/packages/essentials/
    -> permanent Essential DEBs

/opt/neebles-build/modules/packages/
    -> permanent module-delta DEBs

/opt/neebles-build/modules/material/<module-id>/
    -> persistent authenticated MaterialBinding

/opt/neebles-build/modules/runtime-leases/
    -> ephemeral per-execution runtime territories
```

The following is legacy and must not be restored as the productive model:

```text
/opt/neebles-build/modules/rootfs
shared mutable domestic-runtime.json
```

---

# Esbirro relationship

Esbirro is the engineering/certification workspace used to domesticate and certify CUSTOM V2 module material.

```text
Esbirro
    -> discovers/builds/domesticates/certifies exact module material
    -> produces sealed declarations/manifests/package truth

CUSTOM V2
    -> preserves that certified truth in the repository

Boss
    -> authenticates and consumes it generically
```

Esbirro may evolve new worlds and authorities without forcing Boss to gain technology-specific branches.

---

# Recovery relationship

Dynamic module recovery consumes CUSTOM V2 truth rather than assuming every file under a shared pool belongs to one module.

For a module subset, the authoritative contracts remain:

```text
runtime/manifests/modules/<module_id>.packages.tsv
runtime/manifests/modules/<module_id>.manifest.json
```

Unrelated reusable material in permanent pools is not, by itself, an error.

Essential is a separate global layer and must be verified as such rather than disguised as module-owned material.

---

# Repository authority

The repository is authoritative.

Downloads is not authoritative.

Machine-local temporary work is not authoritative.

The host is not build authority.

A successful compilation alone is not certification.

---

# Point 1 closure and Point 2 boundary

Point 1 is **CLOSED / GREEN**.

The architecture now fixed is:

```text
CUSTOM V2 Essential + module delta truth
    -> Boss Preinstall
    -> permanent verified package pools
    -> persistent MaterialBinding
    -> modules.runtime
    -> ephemeral RuntimeLease
    -> generic Workspace
```

Point 1 intentionally removed the productive legacy bridge based on a persistent shared rootfs/shared mutable runtime manifest.

**Point 2 remains pending.** Before moving fully into Point 2, documentation and repository cleanup/audit are completed and the intended source state is committed/pushed.

Release preparation/publication occurs after Point 2 closes. This README does not invent a next release number.

Fresh Live remains a later integrated acceptance gate and is not falsely claimed by Point 1.

---

# Architectural laws

- Boss knows the generic HOW; module/CUSTOM V2 declare the WHAT.
- Essential is a global layer, not a fake module.
- Module deltas do not re-own Essential material.
- Membership and integrity remain separate contracts.
- Preinstall guarantees authenticated material before module operation.
- DEB pools are permanent/reusable arsenal.
- MaterialBinding is persistent installed-module material identity.
- RuntimeLease is ephemeral execution state.
- `modules.installed_runtime` remains separate from `modules.runtime`.
- Workspace remains generic and does not learn MaterialBinding/RuntimeLease semantics.
- No shared persistent module rootfs or mutable global module runtime manifest may return for convenience.

> **CUSTOM V2 certifies module material once; Boss binds that truth to the installed module and reconstructs only the runtime needed for each execution.**
