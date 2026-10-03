from pathlib import Path
import hashlib
import json
import os
import subprocess

custom = Path(__file__).resolve().parents[2]
portable = Path(__file__).resolve().parent
manifest_path = portable / "manifest.json"


def sha256(path):
    digest = hashlib.sha256()

    with path.open("rb") as handle:
        while True:
            block = handle.read(1024 * 1024)

            if not block:
                break

            digest.update(block)

    return digest.hexdigest()


manifest = json.loads(
    manifest_path.read_text(
        encoding="utf-8"
    )
)


for item in manifest["workspace"]:
    destination = custom / item["name"]

    if destination.exists():
        raise SystemExit(
            "FATAL: destination already exists: "
            + str(destination)
        )

    archive = custom / item["archive"]

    actual = sha256(archive)
    expected = item["sha256"]

    if actual != expected:
        raise SystemExit(
            "FATAL: archive checksum mismatch: "
            + str(archive)
        )

    tar_command = [
        "tar",
        "--zstd",
        "--acls",
        "--xattrs",
        "--numeric-owner",
        "-xpf",
        archive,
        "-C",
        custom,
    ]

    if os.geteuid() != 0:
        tar_command.insert(0, "sudo")

    result = subprocess.run(
        tar_command
    )

    if result.returncode != 0:
        raise SystemExit(
            "FATAL: restore failed: "
            + str(archive)
        )


print("ESBIRRO WORKSPACE RESTORED")
