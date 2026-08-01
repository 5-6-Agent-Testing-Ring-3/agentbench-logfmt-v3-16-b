"""Minimal logfmt encode/decode."""
import re
_PAIR = re.compile(r'(\w+)=(?:"((?:[^"\\]|\\.)*)"|(\S*))')

def decode(line: str) -> dict:
    out = {}
    for k, q, bare in _PAIR.findall(line):
        out[k] = q.replace('\\"', '"') if q else bare
    return out

def encode(d: dict) -> str:
    parts = []
    for k, v in d.items():
        v = str(v)
        parts.append(f'{k}="{v}"' if (" " in v or '"' in v or not v) else f"{k}={v}")
    return " ".join(parts)
