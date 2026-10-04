# N.E.E.B.L.E.S. Esbirro Portable Workspace

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

Domestic runtime manifests expose worlds to generic consumers.

Boss runtime manifests are built during Boss release from Boss world contracts and the pinned CUSTOM rootfs.

Module runtime manifests may live directly in CUSTOM when they describe the shared module material authority.

The important rule is:

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

CUSTOM/Esbirro currently supports a shared module material model.

```text
runtime/modules/packages/
runtime/modules/rootfs/
runtime/manifests/modules/
```

Two distinct truths are preserved:

```text
membership
    -> <module_id>.packages.tsv

integrity
    -> <module_id>.manifest.json
```

These contracts must not be collapsed.

The package pool is shared and cumulative.

Uninstall does not erase unrelated or reusable domestic package material.

---

# Current Test Module world

The current reference module uses:

```text
47 certified DEBs
modules.python3.13-tk
```

The world includes Python 3.13, native libraries, Tcl/Tk and graphical dependencies needed by the current reference runtime.

This does not make Python/Tk an Esbirro law.

It is one certified world.

Future modules may request different worlds.

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

Esbirro does not become Lifecycle.

Lifecycle does not talk directly to an "Esbirro daemon".

Instead:

```text
Esbirro/CUSTOM prepares certified declarations/worlds/material
    -> Boss reads declarative authority
    -> Boss performs generic governed execution
```

That separation is deliberate.

---

# Esbirro and Calamares

Calamares consumes controlled Esbirro build/runtime material.

Calamares does not become Boss.

Boss does not become Calamares.

Both can depend on the same controlled domestic authority without collapsing their architectures.

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

# Current release boundary

Latest published Boss:

```text
1.0.22
```

Next Boss release:

```text
1.0.23
```

Before 1.0.23 is cut, the new CUSTOM revision must contain the current certified material/declarations and be pinned immutably by the Boss release workflow.

Fresh Live remains the final system acceptance frontier.

---

# Final law

Esbirro exists so N.E.E.B.L.E.S. can keep growing new worlds, tools and technologies **without turning Boss into a pile of technology-specific branches**.

> **Esbirro domesticates and certifies. CUSTOM preserves the truth. OS supplies platform authority. Boss governs generic execution. BUILD materializes the system.**
