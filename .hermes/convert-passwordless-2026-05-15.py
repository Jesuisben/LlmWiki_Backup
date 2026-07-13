from pathlib import Path

src = Path(r"C:/Users/ICT02-006/Desktop/한국ICT인재개발원/교육/8. Passwordless/2026.05.15(금)/2026.05.15(금).txt")
out = Path(r"D:/Study_LLM_Wiki/.hermes/txt-to-md-candidates/2026.05.15(금).candidate.md")
out.parent.mkdir(parents=True, exist_ok=True)

shell_ranges = [
    (101, 105), (109, 110), (128, 147), (153, 166), (169, 171),
    (174, 174), (181, 182), (187, 188), (193, 193), (209, 212),
    (215, 215), (218, 219), (223, 225), (228, 228), (333, 333), (345, 346),
]

def in_shell(line_no: int) -> bool:
    return any(start <= line_no <= end for start, end in shell_ranges)

def escape_prose(text: str, line_no: int) -> str:
    if line_no == 1:
        return ""
    if line_no in {3, 275, 278, 282, 285, 288, 291, 423}:
        return "# " + text[3:]
    if text.startswith("# "):
        return "#### \\# " + text[2:]
    if text.startswith("* "):
        text = "\\* " + text[2:]
    if text.startswith(">>"):
        text = "\\>\\>" + text[2:]
    if line_no == 307:
        text = "1\\. " + text[3:]
    text = text.replace("->", "-\\>")
    text = text.replace("<YOUR-SERVER-IP>", "\\<YOUR-SERVER-IP\\>")
    return text

lines = src.read_text(encoding="utf-8").splitlines()
result = []
active = False
for no, raw in enumerate(lines, start=1):
    should_fence = in_shell(no)
    if should_fence and not active:
        result.append("```shell")
        active = True
    if not should_fence and active:
        result.append("```")
        active = False
    if no in {1, 2}:
        continue
    result.append(raw if should_fence else escape_prose(raw, no))
if active:
    result.append("```")
while result and result[-1] == "":
    result.pop()
out.write_text("\n".join(result) + "\n", encoding="utf-8")
print(out)
print(f"source_lines={len(lines)} target_lines={len(result)} fences={len(shell_ranges)}")
