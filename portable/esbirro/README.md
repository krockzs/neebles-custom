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


---

# Lore canónico del Esbirro Goblin — lenguaje de colaboración

> **Este capítulo es una adición narrativa y de vocabulario.** Todo el README técnico anterior se conserva íntegro. El lore ayuda a conversar, diseñar casts, entender diagnósticos y mantener continuidad entre chats y máquinas; **no sustituye** los contratos, el código, las autoridades ni la certificación actual.
>
> **Fuente histórica:** *N.E.E.B.L.E.S. — Esbirro Goblin, Dossier Maestro de Arquitectura, Autoridad, Domesticación y Lore*, baseline documental 27-09-2026 (post-Stage 8). Ese baseline es histórico, no una declaración del estado técnico vigente. Ante discrepancias operativas manda el código y la documentación técnica actual; el significado narrativo aquí recogido se conserva como vocabulario de trabajo.

## El personaje y la cadena de mando

**Sr. Neebles** es la autoridad narrativa máxima: manda y fija la doctrina. **Esbirro Goblin**, también llamado el Goblin o el Goblin de los Elfos, es su segundo a bordo, el **Espía de Asalto Informador**: observa, interroga, persigue, custodia y regresa con testimonios. Su condición de segundo a bordo **no le otorga autoridad ilimitada**.

```text
                      SR. NEEBLES
                 autoridad máxima
                         |
                    fija la ley
                         v
                    ESBIRRO GOBLIN
            segundo a bordo / espía de asalto
                         |
             +-----------+-----------+
             |           |           |
             v           v           v
          ELFTOWN      GHETTOS     PRÓFUGOS
          observa      custodia     persigue
             |           |           |
             +-----------+-----------+
                         |
                         v
                    TESTIMONIOS
                         |
                         v
                 VUELVE AL MANDO
```

En las conversaciones de N.E.E.B.L.E.S., esto es una **metáfora operativa de rol**, distinta del vocabulario estratégico de Arsenal y Municiones utilizado en Lifecycle. El lore permite preguntar qué vio el Goblin, qué elfo interrogó, qué mueble falta, dónde está el prófugo, qué barrotes se cruzaron, qué ventanilla se solicitó y qué llave autoriza abrirla.

## Diccionario de Elftown

| Palabra del lore | Sentido dentro del mundo | Traducción técnica original |
| --- | --- | --- |
| **Sr. Neebles** | Autoridad suprema que dicta la doctrina | Autoridad narrativa máxima del ecosistema |
| **Esbirro Goblin** | Segundo a bordo, espía, interrogador, custodio | Agente de observación, domesticación, resolución, transporte y certificación, gobernado por autoridades explícitas |
| **Goblin / espía** | Investiga sin asumir que lo observado es legal | Observación ELF, observación doméstica y pruebas; evidence/findings |
| **Elftown** | Lugar narrativo donde se observan los elfos | Área de observación y conocimiento de objetos ELF |
| **Elfo** | Criatura que el Goblin examina | **Objeto ELF** inspeccionado, ejecutable o biblioteca ELF |
| **Casa** | Hogar físico donde vive el mundo domesticado | Domestic root / runtime root materializado |
| **Ghetto** | Mundo controlado donde habitan los elfos | Entorno runtime separado de las dependencias implícitas del Linux anfitrión |
| **Muebles** | Todo lo que la casa necesita para ser habitable | Ejecutables, bibliotecas, helpers, loaders, rutas de datos, rutas runtime y otros recursos del mundo |
| **Barrotes** | Límites del Ghetto: impiden fugas | Filesystem boundary y reglas de containment del domestic world |
| **Ventanilla** | Abertura reglada para relacionarse con el exterior | Interfaz externa **explícita** concedida mediante authority |
| **Llave** | Permiso que permite abrir una ventanilla precisa | Grant explícito; no aparece automáticamente por encontrar un recurso |
| **Prófugo** | Rastro o habitante que escapa o falta en su casa | Referencia sin resolver, escapante o perseguida recursivamente |
| **Poder** | Algo que el Goblin sabe hacer | Capacidad genérica implementada |
| **Hechizo / spell** | Forma de invocar un poder bajo una ley | Invocación declarativa reusable y comprobable |
| **Grimorio** | Libro de leyes y conocimiento de los mundos | Catálogo declarativo de worlds y semánticas de resolución |
| **Cast / casteo** | El acto de lanzar el hechizo | Invocación controlada o probe forense bajo una ley declarada |
| **Testimonio** | Lo que el Goblin informa después de investigar | Observation/evidence conservada |
| **Penqueo** | El Goblin rechaza un cast incorrecto | Rechazo estructurado por contrato, ley o input inválido |
| **Cuarta Pared** | El Goblin advierte algo que no era la pregunta principal | Finding lateral relevante que, por sí solo, no altera PASS/FAIL |

**Distinciones que jamás se deben confundir:** una **Casa** es el root materializado; el **Ghetto** es el mundo controlado; los **Barrotes** son las reglas que lo contienen. Los **Muebles** no son solamente dependencias `.so`: incluyen también los ejecutables, intérpretes, helpers, loaders, datos y rutas necesarias. Un **Elfo** es un objeto ELF particular, no el nombre de todo el rootfs. Una **Ventanilla** no es una **Llave**: la primera es la interfaz y la segunda el grant que autoriza usarla.

## El Ghetto: la casa, los muebles y sus barrotes

```text
+---------------------------------------------------------+
|                       GHETTO                            |
|                 (mundo controlado)                       |
|                                                         |
|  CASA /                                                |
|    usr/          muebles: ELF, ejecutables y recursos   |
|    lib/          muebles: bibliotecas y loaders         |
|    etc/          muebles: datos/config autorizados      |
|    var/          muebles y writable grants controlados  |
|                                                         |
|  BARROTES: las rutas internas pertenecen a ESTA casa    |
+----------------------------+----------------------------+
                             |
                        VENTANILLA
                             |
                       LLAVE / GRANT
                             |
                             v
                       LINUX ANFITRIÓN
```

El objetivo no es simular aislamiento mientras se resuelve lo que falta en el host. **Un elfo no puede huir al Linux de turno para conseguir muebles por debajo de la mesa.** Una ruta hallada físicamente en el anfitrión no se convierte en mueble autorizado. Encontrar un objeto, resolverlo, transportarlo y recibir permiso para usarlo son hechos diferentes.

El Goblin puede observar recursos exteriores, pero **observación no significa concesión**. Las Ventanillas se abren únicamente mediante autoridades exactas. Los Barrotes evitan los escapes de rutas, enlaces y resoluciones; una comunicación exterior necesaria debe tener su propia Ventanilla y Llave declaradas.

## La investigación de un elfo y la persecución de prófugos

El Goblin no pregunta solamente «¿se ejecuta?». Interroga la estructura del ELF y devuelve hechos:

1. **Ve al Elfo.** Inspecciona el binario real; observa `PT_INTERP`, `DT_NEEDED` y `RPATH/RUNPATH`.
2. **Escucha su testimonio.** Preserva lo observado como evidencia. Ver un `DT_NEEDED` **no** significa que ya esté resuelto.
3. **Persigue a sus contactos.** Busca los `NEEDED` únicamente en los lugares y las autoridades declaradas para ese mundo.
4. **Sigue a los prófugos recursivamente.** No basta con la primera capa: persigue dependencias transitivas, ramas y ciclos hasta cerrar el árbol.
5. **Distingue los senderos.** `RPATH` y `RUNPATH` no significan lo mismo; el contexto heredado y su orden importan.
6. **Revisa los Barrotes.** Rechaza referencias que escapan de la Casa, rutas ilegales, enlaces que salen del Ghetto y dependencias ausentes cuando son obligatorias.
7. **Vuelve con su Testimonio.** Informa evidencia y hallazgos laterales sin confundirlos automáticamente con un juicio de certificación.

```text
ELFO RAÍZ
   |-- PT_INTERP ------> observar ------> resolver dentro del mundo
   |-- DT_NEEDED[] ----> frontera de búsqueda ----> prófugos
   |                                                |
   |                                          cierre recursivo
   +-- RPATH/RUNPATH -> búsqueda y herencia bajo reglas exactas
                                                    |
                                                    v
                                      TODO DENTRO DEL GHETTO
```

**Lore del cierre:** el Goblin considera prófugo tanto lo que falta como lo que intenta escapar; una persecución bien hecha no se detiene en el primer `DT_NEEDED` encontrado. También sabe que observar una fuga y tener autoridad para corregirla no son la misma cosa.

## Poderes, hechizos, grimorio y escuelas

Un **Poder** implementa una capacidad genérica. Un **Hechizo** la formula como invocación declarativa. El **Grimorio** guarda vocabulario y mundos; los **targets** vinculan valores lógicos con rutas relativas dentro de la Casa; un **cast** ejerce la pregunta de forma controlada.

El Dossier Maestro histórico documentó **32 hechizos únicos, 40 inserciones de hechizos y 233 casos declarativos** en **siete escuelas**. Estas cifras pertenecen al censo del dossier de septiembre de 2026 y **no son un conteo automático del árbol actual**.

| Escuela (nombre canónico) | Área interrogada en el lore |
| --- | --- |
| `allowed_session_inputs` | Qué puede y qué no puede entrar por las ventanillas de sesión |
| `data_paths` | Qué datos/muebles son requeridos, opcionales o inalcanzables |
| `environment` | Qué lleva el proceso en su mochila de entorno; cómo se sella |
| `executable` | A qué elfo/ejecutable se invoca, con qué argumentos y autoridad |
| `helpers` | Qué ayudantes físicos pertenecen a la Casa |
| `library_paths` | Dónde se esconden dependencias ELF; búsqueda, herencia y persecución recursiva |
| `runtime_paths` | Rutas y referencias del mundo que pueden transportarse sin capturar el host |

Artefactos mencionados por el dossier (referencias históricas de contrato; su ubicación actual debe verificarse en el repositorio):

```text
domesticacion-elfica.schema.json
    -> vocabulario de las siete escuelas y tipos de valor

domesticacion-elfica.grimorio.json
    -> identidades de worlds y asociaciones lógicas

domesticacion-elfica.targets.json
    -> valores lógicos -> targets relativos dentro de la Casa

testings/domesticacion/manifest.json
    -> runner, leyes, matrices y referencias a contratos
```

El Dossier describe hechizos como `boss.elf_interpreter_observation`, `boss.elf_interpreter_resolution`, `boss.elf_needed_observation`, `boss.elf_needed_resolution`, `boss.elf_recursive_closure`, `boss.recursive_closure_certification`, `boss.search_authority_grants`, `boss.world_reference_resolution`, `boss.path_contract`, `boss.physical`, `boss.process_environment` y `boss.runtime_authority`. Esos nombres identifican **capacidades genéricas**, no reglas especiales para Python, Qt ni un módulo determinado. El catálogo histórico completo y sus matrices pertenecen al Dossier y a los contratos del repositorio.

## Las tres capas del juicio del Goblin

```text
                 OBSERVACIÓN
                     |
                   hechos
                     v
                  EVIDENCIA
                     |
             +-------+-------+
             |               |
             v               v
          AUTHORITY       SENTENCIA
         ¿quién puede     ¿cumple la ley?
          usar qué?       PASS / ERROR /
                          required / optional /
                          domestic / escape
```

**Auditoría**: encuentra un hecho, conserva evidencia y puede reportar un finding sin convertirlo en fracaso. **Certificación**: compara la evidencia con la ley declarada y puede producir un ERROR. **Cuarta Pared**: durante un cast que pregunta por X, el Goblin advierte Y, lo informa como finding y **no modifica por ello** el PASS/FAIL de X. Una investigación de Y puede requerir otro cast.

**Ley cardinal del Esbirro:**

```text
AVAILABLE != REGISTERED != GRANTED != USED
```

Que exista un mueble no entrega una Llave. Que una authority esté disponible no significa que haya sido registrada. Que esté registrada no significa que se haya concedido, y que se haya concedido no implica su uso. El Esbirro puede tener poderes, pero no autoentregarse autoridad.

## Buen casteo, Penqueo y nuevas leyes

Un **buen cast** es una pregunta técnica bajo un hechizo existente, con entradas, mundo y autoridad explícitos:

```text
PREGUNTA -> HECHIZO EXISTENTE -> AUTHORITY EXACTA
         -> EVIDENCIA -> JUICIO
```

Un **mal cast** intenta forzar un verde introduciendo excepciones, cambiando la ley para el caso particular o buscando silenciosamente en el host:

```text
RESULTADO DESEADO -> PARCHE ESPECÍFICO -> HOST FALLBACK -> GREEN FALSO
```

Si el Goblin **penquea** un cast, el diagnóstico debe investigar antes de tocar código: ¿falló la realidad física, el sensor, el cast, la ley, la authority, su registro/grant, o el operador? **Un RED no demuestra por sí solo que falte una capacidad nueva.**

Para crear un nuevo hechizo:

1. Observar el problema real y formular la **ley genérica**, no un parche para ese producto.
2. Buscar primero si un hechizo existente ya responde la pregunta.
3. Solo si falta un Poder, definir la semántica nueva en el engine dueño de ella.
4. Declarar el hechizo, sus opciones y casos en la escuela correcta.
5. Obtener un RED controlado cuando corresponda; implementar y certificar fixtures y realidad física.
6. Dejar el poder reusable para casos X, Y, Z y módulos futuros.

Para crear una nueva **Llave** (authority), el dueño de la semántica declara su descriptor; OS/BUILD suministran autoridad de plataforma donde corresponda; Boss autentica, registra y concede **el grant exacto**. Ningún cast puede inventar permisos por detectar una ruta disponible.

## El Esbirro y los futuros módulos N.E.E.B.L.E.S.

Cuando un módulo necesita su entorno, el Goblin ayuda a identificar los Elfos, sus Muebles y la Casa requerida; certifica los caminos de búsqueda y denuncia a los Prófugos. Los Barrotes aíslan el mundo del Linux anfitrión. Si se necesita comunicación, se declara una Ventanilla y se solicita la Llave apropiada.

El módulo nuevo no debe obligar a codificar un nuevo «Boss Python», «Boss Node», «Boss Qt» o una rama particular para su tecnología. **El objetivo narrativo y técnico es que los poderes del Esbirro y los contratos de Boss sean reusables**.

La discusión actual sobre manifiestos Multi-RootFS de propiedad del módulo y un campo `domination` **sigue siendo diseño**, no una sintaxis que este capítulo declare implementada. No convertir nombres del lore en campos obligatorios del parser ni desplazar la responsabilidad de Preinstall por inferencia. El README técnico anterior continúa describiendo su baseline; el lore aquí añadido explica cómo hablamos de Casas, Ghettos, Elfos, Muebles y autoridad.

## Leyes de continuidad del lore

- **El Goblin observa; la ley juzga.** No confundir testimonio con autorización ni con sentencia.
- **Un Elfo no se fuga al host.** No hay fallback silencioso fuera del world/grant declarado.
- **La Casa no es la ciudad.** Los Muebles que requiere deben estar domesticados y autorizados.
- **Los Barrotes son reales.** Los paths, symlinks, búsquedas y referencias no deben escapar del Ghetto.
- **La Ventanilla requiere Llave.** Toda interfaz externa necesita concesión explícita.
- **Los Prófugos se persiguen hasta el cierre recursivo.** No abandonar dependencias transitivas.
- **Un Poder no pertenece a un incidente.** Los nuevos hechizos representan leyes reusables.
- **La Cuarta Pared conserva hallazgos laterales.** No contamina automáticamente el resultado principal.
- **El Penqueo es evidencia de un rechazo, no licencia para parchear.** Primero se determina qué falló.
- **Esbirro vuelve al mando con Testimonios.** Su trabajo debe seguir siendo explicable, auditable y transportable entre máquinas y conversaciones.

> **Identidad conservada:** Sr. Neebles dicta la doctrina. Esbirro Goblin, su segundo a bordo, espía Elftown, custodia los Ghettos, persigue Prófugos y vuelve con Testimonios. Los Elfos habitan una Casa con sus Muebles; los Barrotes impiden la fuga; las Ventanillas solo se abren con Llaves. El Grimorio guarda los Hechizos, y un buen cast pregunta primero por la ley.
