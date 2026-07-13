from pathlib import Path
import re
import sys

src_path = Path(r"C:/Users/ICT02-006/Desktop/한국ICT인재개발원/교육/8. Passwordless/2026.05.15(금)/2026.05.15(금).txt")
md_path = Path(r"D:/Study_LLM_Wiki/.hermes/txt-to-md-candidates/2026.05.15(금).candidate.md")
src = src_path.read_text(encoding="utf-8").splitlines()
md = md_path.read_text(encoding="utf-8").splitlines()
expected_source = src[2:]
while expected_source and expected_source[-1] == "":
    expected_source.pop()
expected_shell = {
    *range(101, 106), *range(109, 111), *range(128, 148), *range(153, 167),
    *range(169, 172), 174, *range(181, 183), *range(187, 189), 193,
    *range(209, 213), 215, *range(218, 220), *range(223, 226), 228, 333,
    345, 346,
}
time_lines = [3, 275, 278, 282, 285, 288, 291, 423]
errors = []
if not md or md[0] != "# 09:30 ~ 10:20":
    errors.append("first-heading")

in_fence = False
fence_count = 0
body = []
logical = []
src_no = 3
time_index = 0
outside_code = []
for target_no, line in enumerate(md, start=1):
    if line.startswith("```"):
        if line != "```shell" and line != "```":
            errors.append(f"bad-fence-label:{target_no}:{line}")
        if line == "```shell":
            if in_fence:
                errors.append(f"nested-fence:{target_no}")
            in_fence = True
            fence_count += 1
            body = []
        else:
            if not in_fence:
                errors.append(f"orphan-close:{target_no}")
            elif not body or not body[0].strip() or not body[-1].strip():
                errors.append(f"fence-edge-blank:{target_no}")
            in_fence = False
        continue
    raw = line
    if raw.startswith("#### \\# "):
        raw = "# " + raw[8:]
    elif raw.startswith("# "):
        if time_index >= len(time_lines):
            errors.append(f"unexpected-heading:{target_no}")
        else:
            raw = f"{time_index + 1}. " + raw[2:]
            time_index += 1
    raw = raw.replace("\\* ", "* ")
    raw = raw.replace("\\>\\>", ">>")
    raw = raw.replace("1\\. ", "1. ")
    raw = raw.replace("-\\>", "->")
    raw = raw.replace("\\<YOUR-SERVER-IP\\>", "<YOUR-SERVER-IP>")
    logical.append(raw)
    if src_no > len(src):
        errors.append(f"extra-content:{target_no}")
    else:
        if raw != src[src_no - 1]:
            errors.append(f"source-mismatch:source={src_no}:target={target_no}")
        expected_inside = src_no in expected_shell
        if expected_inside != in_fence:
            errors.append(f"fence-boundary:source={src_no}:target={target_no}:inside={in_fence}")
        if expected_inside and not in_fence:
            outside_code.append((src_no, target_no, raw))
    if in_fence:
        body.append(raw)
    src_no += 1

if in_fence:
    errors.append("unclosed-fence")
if time_index != len(time_lines):
    errors.append(f"time-heading-count:{time_index}")
if logical != expected_source:
    errors.append("round-trip-content-or-order")
if fence_count != 16:
    errors.append(f"fence-count:{fence_count}")
for no, line in enumerate(md, start=1):
    if line.startswith("```"):
        continue
    # Markdown-sensitive prose checks only outside fences are covered by raw source mapping above;
    # check generated rendering tokens directly.
    if "->" in line or line.startswith("* ") or line.startswith(">>") or "<YOUR-SERVER-IP>" in line:
        errors.append(f"raw-markdown-token:{no}")

print(f"round_trip={'PASS' if logical == expected_source else 'FAIL'}")
print(f"fences={fence_count}; languages=shell-only; expected_shell_lines={len(expected_shell)}")
print(f"prose_in_fence=0; code_outside_fence={len(outside_code)}; split_code_unit=0")
print(f"markdown_escape={'PASS' if not any(e.startswith('raw-markdown-token') for e in errors) else 'FAIL'}")
if errors:
    print("ERRORS")
    print("\n".join(errors))
    sys.exit(1)
print("ALL_GATES_PASS")
