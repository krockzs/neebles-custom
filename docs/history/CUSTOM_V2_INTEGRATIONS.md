# N.E.E.B.L.E.S. CUSTOM V2 — Integraciones historicas

> ARCHIVO HISTORICO. Preserva el texto de integraciones anteriores tal como figuraba en `README_CUSTOM_V2.md` antes de reorganizarlo en 2026-10-14. Ninguna version, SHA o promesa de pruebas de este archivo prevalece sobre los manifiestos vigentes. No ejecutar una receta antigua sin revalidar su material.


## Integración Test Module 1.2.11 — material y fuente alineados; pruebas físicas pendientes

- Fuente inmutable: `krockzs/neebles-test-module` commit `3def2f0d0d97e57aae9e26fec33386e63df5b16d` (Test Module `1.2.11`).
- Construction `fetch` y `checkout` seleccionan exactamente ese commit.
- Ambos manifiestos del módulo declaran `1.2.11` sin modificar sus 2.242 entradas, hashes ni permisos.
- Permanecen intactos los 59 DEB Essential, los 32 DEB delta, el mundo `modules.python3.13-tk`, los cinco steps y los grants declarativos.
- Boss `1.0.55` instalado en Ryzen según reporte del operador. La instalación real de Test Module `1.2.11`, el cambio de idioma en vivo y el inicio automático de Tray requieren validación física posterior.
- Boss Registry `registry/modules.json` se alineará por separado; este commit CUSTOM no actualiza el catálogo.

---

## Integracion Test Module 1.2.9 (fuentes coordinadas; aceptacion instalada pendiente)

- Fuente inmutable del modulo: `4a8ba8d018de50f86191235f22c9b9aa41cdeabb`.
- Construction `fetch` y `checkout` utilizan ese mismo SHA; Boss `registry/modules.json` selecciona 1.2.9.
- Dos manifiestos CUSTOM V2 indican 1.2.9, sin cambiar ninguna de las 2.242 entradas ni los paquetes/RootFS `python3.13-tk`.
- Boss 1.0.53 Uninstall se mantiene intacto. El controlador `systemd-user` es retirado durante Uninstall por contrato.
- En esta version el finalizador de sesion KDE `scripts/complete-desktop-install.py` es EXPLICITO: la UI de Boss no lo ejecuta automaticamente.
- Pruebas unitarias del modulo: 24/24; ciclo real Update/Uninstall/Reinstall/Tray en Ryzen sigue pendiente.

---


## Integración Test Module 1.2.7 (fuentes, sin aceptación instalada)

- Fuente publicada: `krockzs/neebles-test-module` commit `5db32c4fdec61564415839851c18c092896e11bc`.
- `runtime/construction/test-module.json` apunta a ese SHA inmutable en `fetch` y `checkout`.
- Los dos manifiestos CUSTOM V2 de Test Module declaran versión `1.2.7`; se preservan exactamente las 2.242 entradas certificadas y sus hashes.
- Se conservan los DEB Essential/delta, RootFS `python3.13-tk`, mundos, autoridades y steps de ejecución. No se modifica CUSTOM clásico.
- El Tray ahora sigue `runtime_state` y `open_available` de Governor. El cambio de unidad systemd de 1.2.6 a 1.2.7 requiere una migración explícita durante la actualización instalada.
- Esta alineación de fuentes no afirma aceptación tras actualización, reinicio ni pruebas visuales en Ryzen.

---

**Module domestic-material authority**

**Current integration status (2026-10-08):** **Point 1 CLOSED / GREEN. Point 2 CLOSED / GREEN at source level.** CUSTOM V2 represents the certified module-material model consumed by Boss through permanent package pools, persistent MaterialBinding and ephemeral RuntimeLease. Point 2 additionally certifies persistent Tray behavior through module-owned Construction using the same generic runtime/material authority model. The current Test Module 1.2.3 Construction fetch/checkout is aligned to the published module-source revision `308fbf186aa9dc2a2201862f993809799a987fd0`. The legacy productive shared module-rootfs model and direct host-provider execution model are retired. **Fresh Live and installed-system acceptance remain pending. Boss v1.0.32 has been published; this source alignment does not claim Fresh Live acceptance.**

CUSTOM V2 is the certified domestic material, world and module-construction truth for N.E.E.B.L.E.S. modules.

## Current Multi-RootFS integration — Boss 1.0.34

The current Test Module source revision is
`b36b3ed73a0db7b099a9e61e938e303482fea4f8`.

The canonical CUSTOM Construction recipe is
`runtime/construction/test-module.json`, which pins that source revision
for both `fetch` and `checkout`.

The Construction contract declares the named RootFS `python3.13-tk`
in world `modules.python3.13-tk`. Both `open-runtime` and
`tray-provider` select that RootFS explicitly.

The 59 Essential DEBs and 32 Test Module delta DEBs retain their
certified membership data. The module material manifest's 2,242 entries
match the corresponding Test Module manifest; the latter additionally
declares its RootFS identity.

Boss 1.0.34 candidate build completed successfully in GitHub Actions
(run `38087115867`). The candidate is not a published stable release,
and VM installation, update, rollback and Fresh Live acceptance
remain pending.

The CAST30 source pin and earlier release-status statements below are
historical records, not the current integration selector.

---

## CAST30 — Test Module 1.2.3 source pin (pre-publication)

The immutable source commit `308fbf186aa9dc2a2201862f993809799a987fd0`
contains the module-owned Open-window Close / IPC unregister repair. CUSTOM V2
only aligns `fetch` and `checkout` to that commit and changes the installed
module material-manifest version metadata from `1.2.2` to `1.2.3`. Its 2,242
material entries, 32-DEB module delta, 59-DEB global Essential layer,
Python/Tk world and controlled Construction runtime authorities are unchanged.

The module reports the authenticated session end to Boss, which owns the
canonical `runtime_dead` state/event for every declared Open Surface. CUSTOM V2
does not implement UI/Tray/Launcher synchronization and must not duplicate it.
This source change requires publication under a new immutable CUSTOM revision
and later Boss Registry/Preinstall pin alignment before Fresh Live acceptance.
Passing JSON/source checks does not certify installed-system behavior.

> **CUSTOM V2 declares and certifies WHAT module material exists. Boss governs HOW that certified material is authenticated, bound to an installed module and executed.**

---
