# Assignment 2: The Research Trail

## How to run

```bash
pip install pandas openpyxl
python index.py
```

---

## Results

| Question          | Answer                         |
| ----------------- | ------------------------------ |
| Most citations    | Rania Dib — 662                |
| Most funded field | Computer Vision — $510,000 CAD |
| Earliest active   | Amr Hassan — joined 2006       |

Left join: 83 rows · Inner join: 49 rows · Lost: 34

---

## Hardest part

Keeping `clean_funding()` returning a DataFrame not a number,
and choosing left over inner join without losing researchers.

---

## What the data says

Half the researchers have no funding.
Computer Vision dominates in both output and money.
Half the papers are closed access — ironic given the hidden manifesto.
