# N.E.E.B.L.E.S. CUSTOM

**CUSTOM classic — Boss / Calamares controlled material authority**

**Autoridad vigente:** CUSTOM classic preserva el material domestico certificado de **Boss y Calamares**. La familia CUSTOM V2 se ocupa del material de módulos. Este README no determina la version actual de Boss ni sus dependencias de modulo.

**Mapa de documentación (leer segun la autoridad que se investiga):**

- `README_CUSTOM.md` — material clasico Boss/Calamares, Qt controlado y metadatos efectivos.
- `README_CUSTOM_V2.md` — paquetes Essential, deltas, RootFS, mundos y Construction de módulos.
- `portable/esbirro/README.md` — laboratorio, restauración, autoridad, certificación y lore del Esbirro.
- `neebles-boss/README.md` — Governor, MaterialBinding, RuntimeLease, transacciones y release de Boss.
- `neebles-test-module/README.md` — tutorial de desarrollo de módulos y consumidor de referencia.

Los tres primeros documentos se encuentran en este repositorio; los otros dos en repositorios independientes. Los pins y versiones se verifican en manifiestos y releases reales, no mediante fechas antiguas del README.

N.E.E.B.L.E.S. CUSTOM preserves controlled physical material and integrity truth used by the classic Boss and Calamares domestic paths.

> **CUSTOM classic is not CUSTOM V2. Boss/Calamares material remains classic; module domestic material belongs to CUSTOM V2.**

---

## Fotografía de integración — 28-10-2026

CUSTOM classic continúa siendo la autoridad de material controlado **Boss/Calamares**, sin convertirse en un pool de dependencias de módulos. La integración seleccionada en el ecosistema utiliza **Boss 2.0.8**, **Secrets 1.0.7** y **Connect 1.0.2**; los paquetes de Connect y sus RootFS pertenecen exclusivamente a **CUSTOM V2**. En particular, el DEB Q06 de LibVNCClient fue incorporado al delta de Connect, **no** al corpus classic.

La publicación documental de este README no regenera, reempaqueta ni certifica materiales. Para la selección vigente de fuentes, consultar `runtime/construction/neebles-connect.json`, los manifiestos de CUSTOM V2 y `neebles-boss/registry/modules.json`. La prueba de dos monitores y persistencia de equipos fue comunicada por el operador en el Ryzen el 28-10-2026; esa evidencia de consumidor no altera el alcance de CUSTOM classic.

---

## Hard boundary: CUSTOM classic != CUSTOM V2

The repository may physically contain both families of material, but their architectural identities are distinct.

```text
CUSTOM classic
    -> Boss domestic runtime corpus
    -> Calamares domestic runtime corpus
    -> controlled Qt/build material used by those paths

CUSTOM V2
    -> module Essential layer
    -> module package deltas
    -> module membership/integrity manifests
    -> module runtime/world/construction material
```

Changes in the separate CUSTOM V2 module-material architecture do not redefine CUSTOM classic. Do not modify classic Boss/Calamares material merely to compensate for a module-material problem.

---

## Responsibilities

CUSTOM classic owns:

- certified Boss runtime corpus;
- certified Calamares runtime corpus;
- classic package/rootfs inventories;
- certified effective installed metadata for those corpora;
- controlled Qt 6.8.2 development/build material;
- Esbirro portable snapshots used to restore controlled laboratories;
- reproducible Boss/Calamares build and certification material.

CUSTOM classic does **not** own:

- CUSTOM V2 module package semantics;
- module Essential/delta composition;
- Boss MaterialBinding;
- Boss RuntimeLease;
- Boss governance or Lifecycle state;
- module runtime IPC;
- OS platform authority semantics;
- BUILD image-composition semantics;
- module UI behavior;
- Registry installed state.

---

# Effective installed metadata

CUSTOM manifests describe the certified effective filesystem state for the corpus they own.

For a manifest entry, `mode` is the mode expected in the effective runtime, not necessarily the raw mode stored in an upstream package.

Therefore:

```text
package payload metadata
    != necessarily
certified effective installed metadata

CUSTOM manifest
    = certified effective runtime truth
```

A materializer must verify type/integrity before applying privileged metadata.

CUSTOM classic remains the material authority for its Boss/Calamares corpora.

---

# Domestic corpora

Canonical classic runtime territories include:

```text
runtime/boss/
runtime/calamares/
```

Boss and Calamares remain separate domestic corpora.

Module material under the same repository is not a third classic corpus; it belongs to the separately documented CUSTOM V2 architecture.

---

# Controlled Boss runtime

The Boss release pipeline consumes a pinned CUSTOM classic revision/material set as required by the release workflow.

The controlled Boss runtime source includes:

```text
runtime/boss/rootfs
runtime/manifests/boss.rootfs.tsv
boss_current_manifest.json
```

The Boss domestic runtime manifest is materialized during release from Boss contracts plus the pinned classic CUSTOM runtime corpus.

CUSTOM classic supplies the controlled physical material; Boss release tooling produces the versioned Boss runtime package.

The separate CUSTOM V2 module-material architecture does not redefine this classic corpus.

---

# Controlled Calamares runtime

Calamares remains independent from Boss.

Canonical classic material includes:

```text
runtime/calamares/packages
runtime/calamares/rootfs
runtime/manifests/calamares.packages.tsv
runtime/manifests/calamares.rootfs.tsv
calamares_current_manifest.json
```

The controlled Qt 6.8.2 world remains the build authority.

Host Qt is not build authority.

The separate CUSTOM V2 module-material architecture does not redefine the Calamares corpus.

---

# Controlled Qt 6.8.2 world

The controlled Qt 6.8.2 sysroot/laboratory remains authoritative for current N.E.E.B.L.E.S. Qt consumers that use the classic path.

Do not compile against arbitrary host Qt/KF development packages.

Controlled development territory includes:

```text
build_deps/
build_sysroot_6.8.2/
```

Host Qt 6.10 material must not leak into controlled Qt 6.8.2 outputs.

Publication candidates must come from controlled build/install stages and pass the corresponding ELF/runtime/integrity gates.

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

Esbirro can serve both architectural families while preserving their boundary:

```text
Esbirro + CUSTOM classic
    -> Boss / Calamares controlled material

Esbirro + CUSTOM V2
    -> module material/world engineering and certification
```

Sharing a certification laboratory does not merge the ownership models.

---

# Filesystem-boundary ownership

CUSTOM classic owns controlled material, not OS permission semantics.

OS owns the filesystem-boundary implementation and platform authority.

Boss consumes explicit supplied/granted authority.

```text
CUSTOM classic
    -> controlled physical material truth

OS
    -> boundary provider and platform authority

Boss
    -> governed generic consumption
```

CUSTOM classic must not be mutated to compensate for an OS boundary defect.

---

# BUILD relationship

BUILD may carry image-side materialized copies of CUSTOM classic corpora.

BUILD must preserve byte/integrity parity and must not reinterpret CUSTOM semantics.

The existence of a BUILD copy does not transfer material authority away from CUSTOM classic.

CUSTOM V2 module material is governed by its own README and contracts.

---

# Repository authority

The repository is authoritative.

Downloads is not authoritative.

Machine-local temporary work is not authoritative.

The host is not build authority.

A successful compilation alone is not certification.

---

# Current integration boundary

CUSTOM classic remains on its established Boss/Calamares architecture.

This README intentionally does not track module-development point numbering. Module material, Essential/delta composition, module manifests, MaterialBinding and RuntimeLease belong to the separately documented CUSTOM V2 + Boss module-runtime architecture.

Updates to CUSTOM V2 do not imply changes to CUSTOM classic unless a concrete Boss/Calamares material requirement independently changes.

Release preparation for Boss or Calamares must always be audited from the then-current repository, workflow and pinned-material truth.

---

# Architectural boundary

The final classic law is:

> **CUSTOM classic preserves certified Boss/Calamares material. CUSTOM V2 preserves certified module material. They may share repository territory and Esbirro engineering infrastructure, but they are not the same architectural authority.**
