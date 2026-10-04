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

## Controlled Calamares Qt 6.8.2 rebuild

This procedure is the canonical rebuild path for the N.E.E.B.L.E.S. Calamares ELF artifacts.

The host distribution is never a build authority.

Do not compile Calamares against host Qt, host KDE Frameworks or uncontrolled host development packages.

The controlled development world is:

```text
build_deps/
build_sysroot_6.8.2/
```

The productive runtime remains:

```text
runtime/calamares/packages/
runtime/calamares/rootfs/
```

### Controlled dependency provenance

Development packages must be acquired through the controlled Debian Trixie APT state:

```text
build_deps/apt-etc/sources.list
build_deps/apt-state/
build_deps/apt-cache/
```

Never use an unconstrained host apt download for this laboratory.

The controlled Calamares development closure established during the Qt 6.8.2 repair includes:

```text
libyaml-cpp-dev              0.8.0+dfsg-7
libkf6coreaddons-dev         6.13.0-1
extra-cmake-modules          6.13.0-1
libxkbcommon-dev             1.7.0-2
libkpmcore-dev               24.12.3-2
libkf6i18n-dev               6.13.0-1
libkf6config-dev             6.13.0-2
libkf6widgetsaddons-dev      6.13.0-1
libkf6configqml6             6.13.0-2
libkf6config-dev-bin         6.13.0-2
libkf6i18nlocaledata6        6.13.0-1
libkf6i18nqml6               6.13.0-1
gettext                      0.23.1-2
python3-dev                  3.13.5-1
python3.13-dev               3.13.5-2+deb13u5
libpython3-dev               3.13.5-1
libpython3.13-dev            3.13.5-2+deb13u5
pybind11-dev                 2.13.6-2
libexpat1-dev                2.8.3-1~deb13u1
zlib1g-dev                   1:1.3.dfsg+really1.3.1-1+b1
```

Ubuntu/Kubuntu KF6 6.24 and host Qt 6.10 material must never be mixed into this controlled sysroot.

### Canonical controlled source

```text
/work/calamares-neebles-source
```

### Configure

```text
sudo chroot build_sysroot_6.8.2 /usr/bin/env LANG=C.UTF-8 LC_ALL=C.UTF-8 /usr/bin/cmake -S /work/calamares-neebles-source -B /work/calamares-neebles-build -G Unix\ Makefiles -DCMAKE_BUILD_TYPE=Release -DWITH_QT6=ON -DWITH_PYTHON=ON -DWITH_PYBIND11=ON
```

Required configuration gate:

```text
Configuring done
Generating done
Build files have been written to:
WITH_PYTHON:BOOL=ON
WITH_PYBIND11:BOOL=ON
```

Python is a mandatory Calamares runtime interface in N.E.E.B.L.E.S.

A configure that silently disables Python is a hard failure.

### Build

```text
sudo chroot build_sysroot_6.8.2 /usr/bin/env LANG=C.UTF-8 LC_ALL=C.UTF-8 /usr/bin/cmake --build /work/calamares-neebles-build -j 12
```

The build must complete to 100 percent.

### Install stage

Never publish ELF files directly from the CMake build tree.

The build tree may contain a temporary RUNPATH such as:

```text
/work/calamares-neebles-build
```

Create a DESTDIR stage first:

```text
sudo rm -rf build_sysroot_6.8.2/work/calamares-neebles-stage
sudo chroot build_sysroot_6.8.2 /usr/bin/env DESTDIR=/work/calamares-neebles-stage /usr/bin/cmake --install /work/calamares-neebles-build
```

Only staged artifacts are candidates for productive publication.

### Mandatory ELF gate

The three N.E.E.B.L.E.S. Calamares artifacts are:

```text
usr/lib/libcalamaresui.so.3.3.14
usr/lib/calamares/modules/finished/libcalamares_viewmodule_finished.so
usr/lib/calamares/modules/partition/libcalamares_viewmodule_partition.so
```

Inspect every staged ELF with readelf before publication.

Required:

```text
Qt_6.8 present where applicable
Qt_6.10 absent
/work/calamares-neebles-build absent from RUNPATH and RPATH
```

Any Qt_6.10 requirement is a hard failure.

Any build-tree RUNPATH is a hard failure.

### Mandatory Python interface gate

The controlled build must additionally prove:

- staged `usr/lib/libcalamares.so.3.3.14` has `NEEDED libpython3.13.so.1.0`
- staged `usr/lib/libcalamaresui.so.3.3.14` does not contain `Python modules are not supported in this version of Calamares.`
- `PythonJobModule` is compiled as part of `libcalamaresui`

Python development material belongs to the controlled Debian Trixie laboratory.

Host Python development packages are never build authority.

### Productive publication

Publish only the three certified staged ELF artifacts into:

```text
runtime/calamares/rootfs/usr/lib/x86_64-linux-gnu/libcalamaresui.so.3.3.14
runtime/calamares/rootfs/usr/lib/x86_64-linux-gnu/calamares/modules/finished/libcalamares_viewmodule_finished.so
runtime/calamares/rootfs/usr/lib/x86_64-linux-gnu/calamares/modules/partition/libcalamares_viewmodule_partition.so
```

Required productive metadata:

```text
owner root:root
mode 0755
```

Never replace the complete runtime/calamares/rootfs with the install stage.

### Integrity manifests

After productive ELF publication update both integrity authorities:

```text
runtime/manifests/calamares.rootfs.tsv
calamares_current_manifest.json
```

calamares.rootfs.tsv describes rootfs material.

calamares_current_manifest.json describes the complete Calamares corpus and must preserve both packages and rootfs.

Never regenerate calamares_current_manifest.json from rootfs alone.

The final manifest gate must verify:

```text
component = calamares
version = 1.0
complete package membership preserved
packages/SHA256SUMS preserved
new ELF SHA256 values present
superseded ELF SHA256 values absent
```

### Portable laboratory seal

Whenever build_deps or build_sysroot_6.8.2 changes, regenerate:

```text
portable/esbirro/snapshots/build_deps.tar.zst
portable/esbirro/snapshots/build_sysroot_6.8.2.tar.zst
```

Then update portable/esbirro/manifest.json for each workspace:

```text
sha256
archive_bytes
source_stats.files
source_stats.directories
source_stats.symlinks
source_stats.bytes
```

A changed laboratory with stale snapshot SHA256 metadata is not a closed N.E.E.B.L.E.S. state.

### Absolute rebuild law

```text
controlled dependencies
-> controlled Qt 6.8.2 sysroot
-> configure
-> build
-> DESTDIR install stage
-> Qt and RUNPATH audit
-> publish exact ELF artifacts
-> regenerate integrity manifests
-> regenerate portable snapshots
-> update snapshot SHA256 metadata
-> materialize BUILD
-> real Live acceptance
```

The repository is authoritative.
Downloads is not authoritative.
The host is not authoritative.
A successful compilation alone is not certification.


## Boss Tray certification checkpoint — 2026-10-04

The Tray repair reinforced, rather than relaxed, Esbirro law.

The current accepted construction sequence for the Qt Tray Host is:

```text
controlled Boss source projection
    -> controlled Qt 6.8.2 CMake configure/build
    -> CMake install through DESTDIR
    -> installed-ELF audit
    -> release input
    -> domestic ELF transformation
    -> final client-data ELF verification
```

A successful CMake build is not sufficient publication authority. The CMake build-tree ELF must not be used directly as the release payload.

The 1.0.21 workflow source has therefore been prepared so the Tray Host release input comes from the DESTDIR-installed artifact. The final release verifier has also been extended to inspect the domestic Tray ELF inside `client-data.tar.gz`.

The controlled installed artifact showed no build-tree path leak. Its final domestic form uses the canonical interpreter and runtime library roots below:

```text
/opt/neebles/client/runtime/boss/rootfs
```

The Rust Boss backend change for Tray StatusNotifierItem behavior was built with the official Boss release command `cargo build --release --locked --bins` and completed successfully. Rust release build success is compile evidence only; Plasma interaction remains a runtime acceptance gate.

### Protected Launcher continuity

The previously repaired Launcher sequence remains authoritative:

```text
Build Plasma launcher plugin
    -> DESTDIR install
    -> certify-launcher-plugin-stage.py
    -> release-work/launcher-plugin-install
    -> materialize release
```

Do not reorder or bypass that chain while integrating Tray changes.

### Current stop point

Do not cut Boss 1.0.22 from this checkpoint. Resume with final integration, Plasma runtime acceptance and Test Module Point 10 in the next session.
