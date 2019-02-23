# TexConverter

## Purpose
make markdown that be able to show markdown math in github from your markdown file

## Usage

Just Type in folder that has TexConverter.py

```console
python TexConverter.py \path\...\filename.tex.md
```

it will change .tex.md file to .md file

- in .tex.md file
```markdown
$$ f(x) = 2x + 3 $$
Parameter : $x$
```

$$ f(x) = 2x +3 $$
Parameter : $x$

- in .md file
```markdown
$ <img src="https://latex.codecogs.com/gif.latex?f(x)=2x+3">
Parameter : <img src="https://latex.codecogs.com/gif.latex?x">
```

<p style="text-align:center;"><img src="https://latex.codecogs.com/gif.latex?f(x)=2x+3"></p>

Parameter : <img src="https://latex.codecogs.com/gif.latex?x">
