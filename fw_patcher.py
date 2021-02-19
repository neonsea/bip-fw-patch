#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# Amazfit Bip Firmware Patcher (fw_patcher)

import sys
from pathlib import Path

FW_START_ADDRESS = 0x8008000


def _fatal(line, line_num, patchfile, error):
    print(f"ERROR: {error} on line {line_num} in {patchfile}:")
    print(f"    {line.rstrip()}")
    sys.exit(-1)


def main(argv):
    if len(argv) < 3:
        print("fw_patcher v0.2 by x27, neonsea")
        print(f"Usage: {argv[0]} <fw_file> <patch_file_0> ...<patch_file_n>")
        sys.exit(2)

    with open(argv[1], "rb") as content:
        fw = bytearray(content.read())
        content.close()

    bytesPatched = 0
    for patch in argv[2:]:
        with open(patch, "r") as f:
            lines = f.readlines()

        for line_count, line in enumerate(lines):
            line_count = line_count + 1
            arr = line.split("#")
            if len(arr[0].strip()) == 0:
                continue

            arr = arr[0].split()
            if len(arr) != 3:
                _fatal(line, line_count, patch, "Wrong number of arguments")

            address = int(arr[0], 16)
            if len(fw) + FW_START_ADDRESS < address < FW_START_ADDRESS:
                _fatal(line, line_count, patch, "Address out of range")

            before = bytes.fromhex(arr[1])
            after = bytes.fromhex(arr[2])
            if len(before) != len(after):
                _fatal(line, line_count, patch, "Check and patch data size mismatch")

            offset = address - FW_START_ADDRESS
            for i in range(len(before)):
                if fw[offset + i] != before[i]:
                    _fatal(line, line_count, patch, "FW and check data mismatch")

                if fw[offset + i] == after[i]:
                    continue
                fw[offset + i] = after[i]
                bytesPatched = bytesPatched + 1

    if bytesPatched == 0:
        print("No patch data found")
        sys.exit(-2)

    filename = Path(argv[1]).stem + "_patched" + Path(argv[1]).suffix
    with open(filename, "wb") as content:
        content.write(fw)

    print(f"Created {filename}")
    print(f"Applied patches: {bytesPatched} bytes")


if __name__ == "__main__":
    main(sys.argv)
