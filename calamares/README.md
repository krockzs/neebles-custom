<!-- SPDX-FileCopyrightText: 2026 N.E.E.B.L.E.S. contributors
     SPDX-License-Identifier: CC0-1.0
-->

# N.E.E.B.L.E.S. Calamares

N.E.E.B.L.E.S. Calamares is the downstream Calamares source tree used to maintain the installer changes required by **N.E.E.B.L.E.S. OS**.

This repository is **not the original Calamares project** and does not claim authorship of Calamares. It preserves the upstream project history and maintains a small, isolated set of N.E.E.B.L.E.S.-specific modifications on top of it.

## Upstream Project

Calamares is developed by the **Calamares project and its contributors**.

Official upstream repository:

https://github.com/calamares/calamares

Full credit for the original architecture, source code, modules, documentation, and installer framework belongs to the Calamares developers and contributors.

N.E.E.B.L.E.E.S. OS uses Calamares as its installer framework and maintains only the modifications required for its own distribution.

Original copyright notices, licenses, authorship information, contributor history, and licensing files from upstream are intentionally preserved.

## Base Version

The current N.E.E.B.L.E.S. branch is based on:

- **Calamares:** `v3.3.14`
- **Upstream commit:** `21ea803527735cfaf54fa6059e71d1ef65004864`
- **N.E.E.B.L.E.S. branch:** `neebles-v3.3.14`

The upstream Git history is preserved below the N.E.E.B.L.E.S. changes so authorship and project provenance remain traceable.

N.E.E.B.L.E.S.-specific development begins after the upstream `v3.3.14` base.

## Why This Repository Exists

N.E.E.B.L.E.S. OS requires a few installer behaviors and visual adaptations that differ from the default Calamares implementation.

Rather than modifying the upstream project or mixing distribution-specific requirements into the Calamares repository, those changes are maintained here as a separate downstream codebase.

The goals are to:

- preserve the original Calamares project and its history;
- clearly separate upstream code from N.E.E.B.L.E.S.-specific changes;
- make every local modification auditable;
- preserve the exact source used to build the modified installer modules;
- allow the modules to be rebuilt in the future;
- keep N.E.E.B.L.E.S. OS reproducible;
- make future rebasing against newer Calamares versions possible.

# N.E.E.B.L.E.S. Modifications

The initial N.E.E.B.L.E.S. customization commit modifies **43 files** in total:

- `README.md`;
- 2 keyboard-module source files;
- 39 locale/timezone image assets;
- 1 partition-view source file.

No other Calamares source files were modified in the initial downstream baseline.

## 1. Explicit Keyboard Layout Configuration

Modified files:

```text
src/modules/keyboard/Config.cpp
src/modules/keyboard/Config.h
```

The keyboard module was extended so N.E.E.B.L.E.S. OS can explicitly provide:

```yaml
keyboardLayout:
keyboardVariant:
```

These values are read from the Calamares configuration and stored internally as:

```cpp
QString m_configuredLayout;
QString m_configuredVariant;
```

During keyboard-layout detection, Calamares now checks whether an explicit configuration was supplied before falling back to the existing `locale1` detection path.

Conceptually, the resolution order becomes:

```text
Explicit configured layout / variant
              ↓
       locale1 detection
              ↓
       existing fallback logic
```

This allows N.E.E.B.L.E.S. OS to preserve an explicitly selected or configured keyboard layout instead of having it immediately replaced by auto-detection.

The original Calamares behavior remains available whenever no explicit layout is configured.

## 2. Locale / Timezone Visual Customization

Modified directory:

```text
src/modules/locale/images/
```

The N.E.E.B.L.E.S. baseline replaces or customizes **39 image assets** used by the locale/timezone interface:

- `bg.png`;
- `pin.png`;
- all modified `timezone_*.png` map layers present in the commit.

These changes adapt the locale/timezone selector to the visual language of the N.E.E.B.L.E.S. installer.

The initial N.E.E.B.L.E.S. commit does **not** modify the Calamares locale or timezone-selection C++ logic. The locale change in this baseline is visual/assets-only.

## 3. Partition View Dark-Theme Adaptation

Modified file:

```text
src/modules/partition/gui/PartitionLabelsView.cpp
```

The partition visualization originally used hard-coded black and gray label colors. Those colors have poor contrast on the dark N.E.E.B.L.E.S. installer theme.

The label drawing colors were changed to:

```text
Primary text:   #F5F5F5
Secondary text: #A3A3A3
```

The affected `QPainter` pen values are used only for partition-label rendering.

No partitioning logic, filesystem behavior, disk operations, partition calculations, or partition-management semantics were changed by this modification.

## Slideshow integration used by N.E.E.B.L.E.S. OS

The Calamares source tree is only one part of the N.E.E.B.L.E.S. installer.

The executable slideshow helper used by the certified Calamares runtime is conserved by N.E.E.B.L.E.S. CUSTOM under:

```text
runtime/calamares/rootfs/usr/lib/neebles/neebles-calamares-slides
```

N.E.E.B.L.E.S. BUILD transports that certified helper into the productive Calamares domestic runtime under:

```text
/opt/neebles-build/calamares/rootfs/usr/lib/neebles/neebles-calamares-slides
```

N.E.E.B.L.E.S. OS remains the authority for mutable remote slideshow content.

Remote slideshow assets are maintained under:

```text
neebles-os/calamares/slides/
```

The runtime supports:

- PNG, JPG and JPEG images;
- MP4 video;
- numeric slots from 1 to 20;
- progressive preparation during installation;
- protection of the currently active slot;
- temporary-file downloads followed by atomic replacement;
- local fallback content when remote content is unavailable;
- remote content replacement without rebuilding the ISO.

A change to mutable remote media does not by itself require rebuilding the certified Calamares runtime.

A change to the slideshow helper implementation does require the corresponding CUSTOM runtime material and manifests to be updated before BUILD transports it again.

## Scope of the Changes

The original N.E.E.B.L.E.S. Calamares baseline was intentionally narrow and consisted of keyboard configuration behavior, locale/timezone presentation assets and partition-view theme adaptation.

The current downstream tree also contains installer reliability and runtime-integration changes introduced during the N.E.E.B.L.E.S. domestic-runtime work.

The currently relevant additional source changes include:

```text
src/libcalamaresui/ViewManager.cpp
src/modules/finished/Config.cpp
src/modules/finished/FinishedViewStep.cpp
src/modules/mount/main.py
src/modules/partition/jobs/ClearTempMountsJob.cpp
```

These changes provide:

- suppression of Back and Next controls when Calamares reaches its final page;
- explicit disabling of the final-page Next state;
- reboot through the system logind D-Bus interface with the configured shell command retained as fallback;
- Calamares target mounts under `/run/neebles/calamares/target`;
- cleanup support for both the current target-mount location and the historical temporary mount location.

The partition cleanup change affects temporary installer mount cleanup. It does not change disk-layout calculation or partition-selection semantics.

Distribution-specific configuration, branding, productive overlays and domestic runtime material remain outside the upstream Calamares architecture and are maintained by the corresponding N.E.E.B.L.E.S. authorities.

## Relationship With N.E.E.B.L.E.S. CUSTOM, BUILD and OS

The current installer architecture separates source, certified material, productive materialization and mutable OS content.

```text
N.E.E.B.L.E.S. CUSTOM
    Canonical modified Calamares source
    Certified Calamares packages
    Certified Calamares rootfs
    Calamares manifests
    Build-support material required for reproducible recompilation

N.E.E.B.L.E.S. BUILD
    Materializes the productive domestic runtime
    Transports certified CUSTOM material
    Applies productive ownership and privilege semantics
    Applies installer configuration overlays required by the Live system

N.E.E.B.L.E.S. OS
    Owns operating-system integration
    Owns mutable remote slideshow content
    Supplies the wider Live and installed-system environment
```

The productive Calamares runtime is materialized by BUILD at:

```text
/opt/neebles-build/calamares/
├── packages/
└── rootfs/
```

CUSTOM and BUILD are not expected to be byte-for-byte identical in every metadata field.

CUSTOM conserves and certifies source material.

BUILD may apply productive ownership, permissions and explicitly defined configuration overlays.

Content that is expected to remain identical is verified by size and SHA256 before the build is considered statically closed.

## Reproducible N.E.E.B.L.E.S. Calamares Build

The canonical source tree is:

```text
/home/thomyorke/NEEBLES/neebles-custom/calamares
```

The current build tree is:

```text
/home/thomyorke/NEEBLES/neebles-build/build-tools/calamares-current-build
```

The build directory must be writable by the normal development user.

CMake configuration and compilation are performed without elevated privileges.

Elevated privileges are reserved for operations that genuinely require writing productive BUILD material or preserving root-owned runtime metadata.

### KPMcore ABI requirement

The productive N.E.E.B.L.E.S. Calamares runtime currently provides:

```text
libkpmcore.so.12
libkpmcore.so.24.12.3
```

The Calamares partition module must therefore link against SONAME:

```text
libkpmcore.so.12
```

A host build against a newer KPMcore SONAME is not acceptable even when compilation succeeds.

The isolated development material is stored under:

```text
neebles-custom/build_deps/kpmcore12/rootfs
```

It is assembled from the Debian Trixie development package:

```text
libkpmcore-dev 24.12.3-2
```

and the corresponding certified runtime package:

```text
libkpmcore12 24.12.3-2
```

The development package provides the KPMcore headers and CMake package metadata.

The runtime package provides the actual ABI-12 shared library used by the linker.

Additional host development dependencies discovered during the current rebuild include:

```text
libkf6i18n-dev
libkf6widgetsaddons-dev
```

### Clean configuration

Remove an obsolete or root-owned build directory before reconfiguration:

```text
sudo rm -rf neebles-build/build-tools/calamares-current-build
mkdir -p neebles-build/build-tools/calamares-current-build
```

Configure against the isolated KPMcore 12 SDK:

```text
cmake \
    -S neebles-custom/calamares \
    -B neebles-build/build-tools/calamares-current-build \
    -G Ninja \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DWITH_QT6=ON \
    -DBUILD_TESTING=OFF \
    -DBUILD_SCHEMA_TESTING=OFF \
    -DKPMcore_DIR:PATH=/home/thomyorke/NEEBLES/neebles-custom/build_deps/kpmcore12/rootfs/usr/lib/x86_64-linux-gnu/cmake/KPMcore
```

A valid configuration must complete both the configure and generation phases and must discover the partition module.

### Compilation

```text
cmake --build \
    neebles-build/build-tools/calamares-current-build \
    --parallel 16
```

For an ABI-sensitive partition-only rebuild:

```text
cmake --build \
    neebles-build/build-tools/calamares-current-build \
    --target calamares_viewmodule_partition \
    --parallel 16
```

The resulting partition module must be checked before it is accepted:

```text
readelf -d neebles-build/build-tools/calamares-current-build/src/modules/partition/libcalamares_viewmodule_partition.so
```

The required dependency is:

```text
NEEDED libkpmcore.so.12
```

A result that depends on a different KPMcore SONAME must not be copied into CUSTOM or BUILD.

## Certified Calamares Material

The canonical certified runtime is conserved under:

```text
neebles-custom/runtime/calamares/
├── packages/
└── rootfs/
```

The current locally modified runtime artifacts include:

```text
rootfs/usr/lib/neebles/neebles-calamares-slides
rootfs/usr/lib/x86_64-linux-gnu/libcalamaresui.so.3.3.14
rootfs/usr/lib/x86_64-linux-gnu/calamares/modules/finished/libcalamares_viewmodule_finished.so
rootfs/usr/lib/x86_64-linux-gnu/calamares/modules/partition/libcalamares_viewmodule_partition.so
rootfs/usr/lib/x86_64-linux-gnu/calamares/modules/mount/main.py
```

After replacing runtime material, both the physical corpus and its manifests must be updated and validated.

The current manifest files are:

```text
calamares_current_manifest.json
runtime/manifests/calamares.rootfs.tsv
runtime/manifests/calamares.packages.tsv
```

Temporary build directories such as a rootfs-local `work/` tree are not certified runtime material and must never be included in these manifests.

## Transport Into BUILD

BUILD materializes the certified runtime under:

```text
neebles-build/config/includes.chroot/opt/neebles-build/calamares/
├── packages/
└── rootfs/
```

Certified binary and script content that is transported from CUSTOM must be checked by SHA256 and size.

BUILD owns productive filesystem metadata and may therefore use root ownership even when the corresponding conserved CUSTOM material is user-owned.

BUILD also owns productive Calamares configuration overlays.

Examples include:

```text
config/includes.chroot/etc/calamares/
config/includes.chroot/opt/neebles-build/calamares/rootfs/etc/calamares/
```

These configuration overlays must not be replaced by a blind rootfs synchronization.

The productive `finished.conf` currently uses:

```yaml
---
restartNowMode: user-checked
restartNowCommand: "systemctl -i reboot"
```

## Static Acceptance Gate

Before a Calamares build is considered statically closed, verify:

- source changes pass `git diff --check`;
- the clean build succeeds;
- the partition module requires `libkpmcore.so.12`;
- changed runtime artifacts are materialized into CUSTOM;
- CUSTOM runtime manifests describe the current physical corpus;
- no temporary work tree is included in the certified runtime;
- the current manifest contains no stale entries;
- transported BUILD artifacts match certified content by SHA256 and size;
- BUILD retains intended productive ownership and configuration overlays;
- no stale artifact SHA remains referenced by productive scripts or checks.

Static closure is not the same as runtime acceptance.

Final runtime acceptance requires testing the generated Live system and confirming installer navigation, slideshow behavior, mount cleanup, final-page behavior, reboot and successful boot of the installed system.

## Repository Relationship

The original Calamares repository remains separate from the N.E.E.B.L.E.S. repository.

Typical local remotes:

```text
upstream  https://github.com/calamares/calamares.git
origin    https://github.com/krockzs/neebles-calamares.git
```

N.E.E.B.L.E.S.-specific commits belong in this repository.

Changes must not be pushed to the upstream Calamares repository as though they were part of the original project.

If a future modification becomes generally useful outside N.E.E.B.L.E.S. OS, it can be evaluated independently for possible upstream contribution following the Calamares project's own contribution process.

## Attribution and Licensing

This repository contains substantial source code originating from Calamares.

**Calamares remains the work of the Calamares project and its contributors.**

N.E.E.B.L.E.S. claims authorship only for its own modifications and distribution-specific additions.

Existing upstream copyright notices, SPDX metadata, licenses, `AUTHORS`, `CONTRIBUTING.md`, `LICENSES/`, Git commit authorship, and contributor history must remain intact.

Nothing in this repository should be interpreted as transferring ownership of upstream Calamares code to N.E.E.B.L.E.S.

Please refer to the licensing information already included in the Calamares source tree for the licenses applicable to individual upstream components.

## Development Policy

When modifying this repository:

1. Keep N.E.E.B.L.E.S.-specific changes as small and isolated as practical.
2. Preserve upstream authorship and licensing information.
3. Document why a modification is necessary for N.E.E.B.L.E.S. OS.
4. Avoid changing unrelated upstream behavior.
5. Keep the upstream base traceable.
6. Prefer configuration and branding over source modification whenever Calamares already provides the required mechanism.
7. Maintain source compatibility and rebaseability where reasonably possible.

## Current N.E.E.B.L.E.S. Customization Baseline

Initial downstream customization:

```text
fed9b6b12ccf4e40c41d244d6f8f9c6d6a575be5
Add N.E.E.B.L.E.S. Calamares customizations
```

Upstream baseline:

```text
21ea803527735cfaf54fa6059e71d1ef65004864
Calamares v3.3.14
```

This provides a clear boundary between the upstream project and the N.E.E.B.L.E.S.-specific work.

---

## N.E.E.B.L.E.S.

**Nested Evolutionary Engine for Behavioral Language Emergent Systems**

N.E.E.B.L.E.S. OS is built by integrating existing open-source technologies with its own operating-system architecture, tooling, configuration, branding, and distribution-specific components.

Calamares is one of those upstream technologies, and its contribution to the N.E.E.B.L.E.S. OS installer is explicitly acknowledged here.
