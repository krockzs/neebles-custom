# N.E.E.B.L.E.S. Esbirro Portable Workspace

**Current integration status (2026-10-08):** Point 1 and Point 2 are CLOSED/GREEN at source level. Esbirro preserves the separate CUSTOM classic and CUSTOM V2 material-authority models. CAST30 changes Boss governance/presentation, not the certified Esbirro/Qt 6.8.2 material. Release-build, Fresh Live and installed-system acceptance remain separate pending gates.

Esbirro is the controlled domestic engineering and certification authority of the N.E.E.B.L.E.S. ecosystem.

This directory preserves the portable development laboratory used to create, certify and restore controlled worlds, runtime material and construction authority.

> **The repository is authoritative. The host is not authoritative. Downloads is not authoritative. Successful compilation alone is not certification.**

---

# Dual-life model

Esbirro intentionally lives in two contexts.

```text
Esbirro outside the running OS
    -> invents / certifies new worlds
    -> gains new spells
    -> gains new authorities
    -> prepares domestic material
    -> restores controlled laboratories
    -> performs controlled builds
    -> certifies outputs

Esbirro inside the N.E.E.B.L.E.S. ecosystem
    -> supplies already-certified material/worlds
    -> serves Boss Construction
    -> serves Boss domestic runtime
    -> serves Calamares controlled material
```

The authority is one.

The deployment/use contexts are two.

This is what allows Esbirro to evolve without forcing Boss to gain a language-specific branch for every future module or technology.

---

# Portable snapshots

Current portable laboratory snapshots include:

```text
build_deps.tar.zst
build_sysroot_6.8.2.tar.zst
```

`build_deps.tar.zst` preserves the controlled dependency workspace.

`build_sysroot_6.8.2.tar.zst` preserves the controlled Qt 6.8.2 development sysroot/laboratory.

Historical external material may be preserved under:

```text
archive/
```

but historical material does not regain architectural authority merely because it was archived.

---

# Restore

Canonical restore entrypoint:

```text
python3 portable/esbirro/restore-workspace.py
```

The restore path verifies SHA256 before extraction.

A restored workspace must match the portable manifest.

---

# Authority model

Esbirro does not grant runtime permission merely because a binary exists.

It participates in the broader N.E.E.B.L.E.S. law:

```text
material exists
    !=
authority is granted
```

Esbirro certifies controlled material/world truth.

OS owns platform AuthoritySupply.

Boss authenticates supplied authority and creates explicit grants.

---

# Worlds

A world is a declarative identity for a controlled execution/runtime environment.

Examples include Boss infrastructure worlds and module worlds.

Current module example:

```text
modules.python3.13-tk
```

A world may describe:

- executable;
- native library paths;
- runtime paths;
- other future categories.

The consuming Boss code resolves the world generically.

Boss must not need:

```text
boss.python
boss.node
boss.java
```

merely because new module technologies appear.

---

# Construction powers

Domestic Construction is declarative.

CUSTOM stores declarations under:

```text
runtime/construction/
```

A step may declare:

```text
runtime_authority
world
execution
session
readonly
dynamic_readonly
writable
mounts
chdir
arguments
```

These are construction facts.

Boss executes them through its generic workspace capability.

Esbirro/CUSTOM owns the construction declaration truth; Lifecycle does not become Esbirro.

---

## Execution modes

Construction supports explicit execution modes:

```text
foreground
persistent
```

`foreground` is appropriate for finite build/setup steps.

`persistent` is appropriate for a long-lived runtime that must continue after Lifecycle returns.

Persistent execution is a generic Boss execution behavior, not a Test Module special case.

---

## Session authority

Construction may request:

```text
session: true
```

That request does not mean "inherit host environment".

It means Boss must obtain the certified desktop-session interface from OS authority and project only authorized resources such as:

- desktop UID/GID;
- session bus;
- X11 socket;
- Wayland socket;
- Xauthority file;
- runtime directory metadata.

The runtime is then entered under the intended desktop identity.

---

## Dynamic read-only authority

Construction can request a strict dynamic subpath from a supplied authority.

Conceptually:

```text
authority root
    + validated source subpath
    -> exact read-only projection
```

This avoids hardcoding individual module install directories inside Boss.

---

# Runtime manifests

Domestic runtime manifests expose named worlds to generic consumers.

Boss infrastructure runtime manifests remain part of the classic Boss release material path.

Module runtime truth belongs to CUSTOM V2. For module execution, the important relationship is now:

```text
world identity
    -> authenticated CUSTOM V2 runtime manifest payload
    -> persistent Boss MaterialBinding for the installed module
    -> fresh Boss RuntimeLease
    -> generic resolver / Workspace
```

Esbirro certifies the declarations and material that make this possible; Esbirro does not own the runtime lease lifetime.

The permanent rule remains:

```text
world identity
    -> declarative material mapping
    -> generic resolver
```

not:

```text
technology name
    -> Boss source branch
```

---

# Module material powers

Module domestic material belongs to **CUSTOM V2**, not to CUSTOM classic.

The current certified source layout is:

```text
runtime/modules/packages/essentials/*.deb
runtime/modules/packages/*.deb
runtime/manifests/modules/essentials.packages.tsv
runtime/manifests/modules/essentials.manifest.json
runtime/manifests/modules/<module_id>.packages.tsv
runtime/manifests/modules/<module_id>.manifest.json
runtime/modules/domestic-runtime.json
```

Two material layers are intentionally distinct:

```text
Essential
    -> global reusable base required by module runtimes
    -> not a fake module

module delta
    -> only material specific to the consuming module
    -> must not re-own Essential merely because it needs it
```

Membership and integrity remain separate truths:

```text
package membership
    -> *.packages.tsv

material integrity
    -> *.manifest.json
```

The source `.deb` arsenal is cumulative and reusable. The productive user system preserves verified package pools, **not** one persistent composed rootfs.

Esbirro/CUSTOM V2 certifies material truth. Boss Preinstall authenticates and caches it. Boss MaterialBinding persists which certified truth belongs to the installed module. Boss RuntimeLease composes Essential + module delta only for the lifetime of an execution.

The following model is obsolete and must not return:

```text
runtime/modules/rootfs/ as one productive persistent shared module rootfs
    -> published to /opt/neebles-build/modules/rootfs
    -> mutable shared domestic-runtime.json
```

---

# Current Test Module world

The current reference module uses:

```text
world: modules.python3.13-tk
Essential layer: 59 certified DEBs
Test Module delta: 32 certified DEBs
```

Physical certification during Point 1 observed:

```text
Essential material entries       3538
Test Module delta entries        2210
compatible overlap               16 directories
file/symlink collisions          0
```

The combined Essential + Test Module material executed Python 3.13.5 and `_tkinter` / Tcl 8.6 with no unresolved ELF dependencies in the certification path.

This does **not** make Python/Tk an Esbirro law. It is one certified world and one reference module delta.

Future modules may consume the same Essential material, extend it through a different delta, or use entirely different worlds without requiring technology-specific branches in Boss.

---

# Boss infrastructure worlds

Boss-owned infrastructure tools remain Boss worlds.

Examples include:

```text
boss.git
boss.setpriv
```

The physical executable is drawn from the certified Boss domestic runtime.

Host executable discovery is not a fallback authority.

`boss.setpriv` is used by session-aware workspace execution to enter the certified desktop identity before the boundary command executes.

---

# Controlled Qt 6.8.2 world

The controlled Qt 6.8.2 sysroot remains the build authority for current N.E.E.B.L.E.S. Qt consumers.

Do not compile against arbitrary host Qt/KF development packages.

Current controlled development territory:

```text
build_deps/
build_sysroot_6.8.2/
```

Host Qt 6.10 material must not leak into controlled Qt 6.8.2 outputs.

---

## Calamares controlled rebuild

Canonical source:

```text
/work/calamares-neebles-source
```

Configure/build/install must happen inside the controlled sysroot.

Publication candidates must come from a DESTDIR install stage, not directly from a CMake build tree.

Required gates include:

- Qt 6.8 symbols where applicable;
- no Qt 6.10 dependency;
- no build-tree RUNPATH leak;
- expected Python 3.13 interface;
- certified final metadata.

Only exact certified artifacts are published into the productive Calamares rootfs.

---

# Boss Qt consumers

The same construction law applies to Boss Qt outputs.

Protected order:

```text
controlled Boss source projection
    -> controlled CMake configure/build
    -> DESTDIR install
    -> installed artifact audit
    -> release materialization
    -> domestic transformation
    -> final release verification
```

This applies to components such as:

- Boss UI;
- Installer;
- auth agent where applicable;
- Launcher plugin;
- Tray Host.

A successful build-tree executable is not release authority.

---

# Rust boundary

Boss Rust release binaries are built by the Boss release workflow with the pinned Rust toolchain.

Current release policy uses:

```text
Rust 1.98.1
cargo build --release --locked --bins
```

The static bootstrap runtime resolver is built for musl.

Rust source compilation does not occur "inside Esbirro" merely because Esbirro supplies the controlled Qt/material world.

Keep those authorities distinct.

---

# Portable seal

Whenever controlled laboratory material changes, regenerate the corresponding snapshots and update:

```text
portable/esbirro/manifest.json
```

including:

```text
sha256
archive_bytes
source_stats.files
source_stats.directories
source_stats.symlinks
source_stats.bytes
```

A changed workspace with stale snapshot metadata is not a closed state.

---

# Absolute construction law

```text
controlled source
    -> controlled dependencies/world
    -> configure
    -> build
    -> install/stage
    -> integrity / ELF / runtime audit
    -> publish exact certified material
    -> regenerate manifests when material changes
    -> seal portable workspace when laboratory changes
    -> materialize consuming system
    -> real runtime acceptance
```

---

# Esbirro and Boss

Esbirro does not become Lifecycle, MaterialBinding or RuntimeLease.

Lifecycle does not talk directly to an "Esbirro daemon".

Instead:

```text
Esbirro / CUSTOM classic
    -> certifies Boss/Calamares controlled material where applicable

Esbirro / CUSTOM V2
    -> certifies module Essential + delta + manifests/worlds/declarations

Boss
    -> authenticates declared authority
    -> persists installed module material identity through MaterialBinding
    -> creates ephemeral RuntimeLease when modules.runtime executes
    -> performs generic governed execution
```

That separation is deliberate. Material certification authority and runtime ownership remain distinct.

---

# Esbirro and Calamares

Calamares consumes **CUSTOM classic** controlled build/runtime material.

Calamares does not become Boss.

Boss does not become Calamares.

CUSTOM V2 module material must not be confused with the classic Calamares/Boss corpus merely because both are domesticated through Esbirro-controlled processes.

The controlled Qt 6.8.2 laboratory and classic Calamares path remain unchanged by Point 1.

---

# Adding a new world

The intended pattern for future work is:

```text
1. define the required world/material outside Boss
2. domesticate and certify exact dependencies
3. publish declarative world/runtime truth
4. expose required authority through existing generic contracts
5. add/adjust module Construction declaration
6. test through Boss generic execution
7. only add a new Boss capability if the required HOW is genuinely new
```

A new module technology alone is not sufficient reason to modify Boss.

---

# Adding a new authority

New authorities must be explicit, narrow and auditable.

Before introducing one, answer:

- who owns its semantics?
- what exact source/root can it expose?
- read-only or writable?
- static or dynamic subpath?
- who supplies the descriptor?
- who authenticates it?
- who grants it?
- which generic consumer needs it?

Do not smuggle authority through host environment or filesystem presence.

---

# Current integration boundary

Point 1 is closed for the module-material architecture:

```text
Essential global layer
    + module delta
    -> permanent verified DEB pools
    -> persistent Boss MaterialBinding
    -> ephemeral per-execution RuntimeLease
```

The previous shared persistent module-rootfs model is no longer authoritative.

**Point 2 is CLOSED/GREEN at source level.** CUSTOM V2 and Boss document the module-owned persistent Tray Construction path. Source closure is not publication or installed-system acceptance.

No "next Boss release" number is asserted by this README. Version/release truth must be read from the repository again when the release phase actually begins.

Fresh Live remains a later integrated system-acceptance frontier; Point 1 source/material certification does not falsely claim it.

---

# Final law

Esbirro exists so N.E.E.B.L.E.S. can keep growing new worlds, tools and technologies **without turning Boss into a pile of technology-specific branches**.

> **Esbirro domesticates and certifies. CUSTOM preserves the truth. OS supplies platform authority. Boss governs generic execution. BUILD materializes the system.**
