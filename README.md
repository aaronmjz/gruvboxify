# gruvboxify

Easily convert any image to the **Gruvbox color palette** (dark or light) — straight from your terminal.

<div>
  <img src="https://raw.githubusercontent.com/aaronmjz/gruvboxify/master/input.jpg" alt="Input Image" width="503" style="display: inline-block; margin-right: 20px;"/>
  <img src="https://raw.githubusercontent.com/aaronmjz/gruvboxify/master/output_dark.jpg" alt="Gruvboxified Dark Output" width="503" style="display: inline-block;"/>
</div>

## Installation

Clone the repository and install it locally:

```bash
git clone https://github.com/aaronmjz/gruvboxify.git
cd gruvboxify
pip install .
```

## Usage

Basic usage:

```bash
gruvboxify <input_image> <output_image>
```

By default, it uses the **dark Gruvbox theme**.

### Optional: Specify a Theme

You can also choose between the **dark** and **light** variants:

```bash
gruvboxify <input_image> <output_image> --theme dark
```
or
```bash
gruvboxify <input_image> <output_image> --theme light
```

---

## Example

Convert a photo to Gruvbox **dark** palette:

```bash
gruvboxify myphoto.jpg myphoto_gruvbox_dark.png --theme dark
```

Convert a photo to Gruvbox **light** palette:

```bash
gruvboxify myphoto.jpg myphoto_gruvbox_light.png --theme light
```
