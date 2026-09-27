#!/usr/bin/env python3

from pathlib import Path
import subprocess


ROOT = (
    Path(__file__).resolve().parent.parent
    / "runtime/boss/rootfs"
)

ORIGIN = chr(36) + "ORIGIN"

RULES = {
    ROOT
    / "usr/lib/x86_64-linux-gnu/libproxy.so.1":
        ORIGIN + "/libproxy",

    ROOT
    / "usr/lib/x86_64-linux-gnu/libproxy"
    / "libpxbackend-1.0.so":
        ORIGIN + "/..",
}


def run(args):
    subprocess.run(
        [str(item) for item in args],
        check=True,
    )


def output(args):
    return subprocess.check_output(
        [str(item) for item in args],
        text=True,
    ).strip()


def main():
    failures = 0

    for target, expected in RULES.items():
        if not target.is_file():
            print(
                "MISSING ::",
                target,
            )

            failures += 1
            continue

        run([
            "patchelf",
            "--force-rpath",
            "--set-rpath",
            expected,
            target,
        ])

        actual = output([
            "patchelf",
            "--print-rpath",
            target,
        ])

        print(
            "TARGET ::",
            target,
        )

        print(
            "RPATH ::",
            actual,
        )

        if actual != expected:
            print(
                "CHECK :: FAIL"
            )

            failures += 1
        else:
            print(
                "CHECK :: OK"
            )

    print(
        "FAILURES ::",
        failures,
    )

    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
