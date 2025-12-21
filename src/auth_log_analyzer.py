#!/usr/bin/env python3
from __future__ import annotations

import sys
from pathlib import Path


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python src/auth_log_analyzer.py <path-to-auth.log>")
        return 2

    log_path = Path(sys.argv[1])

    if not log_path.exists():
        print(f"[ERROR] File not found: {log_path}")
        return 2

    lines = log_path.read_text(errors="ignore").splitlines()

    failed = sum(1 for line in lines if "Failed password" in line)
    invalid = sum(1 for line in lines if "Invalid user" in line)
    accepted = sum(1 for line in lines if "Accepted password" in line or "Accepted publickey" in line)

    print("=== SSH Auth Log Quick Summary ===")
    print(f"File: {log_path}")
    print(f"Total lines: {len(lines)}")
    print(f"Failed password: {failed}")
    print(f"Invalid user: {invalid}")
    print(f"Accepted (login success): {accepted}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
