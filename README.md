<div align="center">

<a href="https://spoolmojo.com"><img src="assets/banner.svg" alt="SpoolMojo — if you can dream it, we can print it" width="100%"/></a>

<br/><br/>

<img src="https://img.shields.io/badge/🌐_live-spoolmojo.com-FF5E5B?style=for-the-badge&labelColor=241E3D" alt="spoolmojo.com"/>
<img src="https://img.shields.io/badge/stack-HTML_+_Three.js-00CECB?style=for-the-badge&labelColor=241E3D" alt="Stack"/>
<img src="https://img.shields.io/badge/build-none_needed-FFED66?style=for-the-badge&labelColor=241E3D" alt="No build"/>
<img src="https://img.shields.io/badge/backend-zero-7B61FF?style=for-the-badge&labelColor=241E3D" alt="No backend"/>

<br/><br/>

**[🖨️ What We Make](#️-what-we-make)** &nbsp;·&nbsp;
**[🔄 How It Works](#-how-it-works)** &nbsp;·&nbsp;
**[🎨 Brand Kit](#-brand-kit)** &nbsp;·&nbsp;
**[🚀 Run & Deploy](#-run--deploy)** &nbsp;·&nbsp;
**[🛠️ Customize](#️-customize)**

<img src="assets/wave.svg" width="100%" alt=""/>

</div>

## 🖨️ What We Make

<table align="center">
  <tr>
    <td align="center" width="25%">🎁<br/><b>Personalized Gifts</b><br/><sub>keepsakes nobody else can give</sub></td>
    <td align="center" width="25%">🏠<br/><b>Home Décor</b><br/><sub>planters, lamps, wall art</sub></td>
    <td align="center" width="25%">🧸<br/><b>Toys & Games</b><br/><sub>articulated critters & puzzles</sub></td>
    <td align="center" width="25%">💻<br/><b>Desk Accessories</b><br/><sub>organizers that tame chaos</sub></td>
  </tr>
  <tr>
    <td align="center">📱<br/><b>Holders & Mounts</b><br/><sub>custom-fit to your gear</sub></td>
    <td align="center">🔧<br/><b>Spare Parts</b><br/><sub>discontinued? we reprint it</sub></td>
    <td align="center">🚀<br/><b>Prototypes</b><br/><sub>sketch → sample, fast</sub></td>
    <td align="center">🎨<br/><b>Your Wild Idea</b><br/><sub>we love a challenge</sub></td>
  </tr>
</table>

<div align="center"><img src="assets/wave.svg" width="100%" alt=""/></div>

## 🔄 How It Works

<div align="center">

| &nbsp;&nbsp;1️⃣&nbsp;&nbsp; | &nbsp;&nbsp;2️⃣&nbsp;&nbsp; | &nbsp;&nbsp;3️⃣&nbsp;&nbsp; | &nbsp;&nbsp;4️⃣&nbsp;&nbsp; |
|:---:|:---:|:---:|:---:|
| **Dream It** | **Design It** | **Make It** | **Love It** |
| sketch, photo, or just words | 3D model + preview tweaks | printed & hand-finished | packed & shipped to you |

</div>

```mermaid
flowchart LR
  A([💭 Dream It]) --> B([✏️ Design It]) --> C([🖨️ Make It]) --> D([📦 Love It])
  A -.->|quote form| E([✉️ hello@spoolmojo.com])
```

<div align="center"><img src="assets/wave.svg" width="100%" alt=""/></div>

## 🎨 Brand Kit

<div align="center">

| Swatch | Name | Hex | Role |
|:---:|---|---|---|
| ![coral](https://img.shields.io/badge/-%20%20%20%20-FF5E5B?style=flat-square) | Coral | `#FF5E5B` | Primary CTA, brand accent |
| ![teal](https://img.shields.io/badge/-%20%20%20%20-00CECB?style=flat-square) | Teal | `#00CECB` | Secondary buttons |
| ![yellow](https://img.shields.io/badge/-%20%20%20%20-FFED66?style=flat-square) | Yellow | `#FFED66` | Kicker / highlights |
| ![purple](https://img.shields.io/badge/-%20%20%20%20-7B61FF?style=flat-square) | Purple | `#7B61FF` | Accents, rim light |
| ![ink](https://img.shields.io/badge/-%20%20%20%20-241E3D?style=flat-square) | Ink | `#241E3D` | Text, borders, dark band |
| ![cream](https://img.shields.io/badge/-%20%20%20%20-FFF8F0?style=flat-square) | Cream | `#FFF8F0` | Page background |

**Fonts:** [Baloo 2](https://fonts.google.com/specimen/Baloo+2) (headings) · [Nunito](https://fonts.google.com/specimen/Nunito) (body)

</div>

<div align="center"><img src="assets/wave.svg" width="100%" alt=""/></div>

## 🚀 Run & Deploy

One self-contained file. No build step, no dependencies to install.

```bash
open index.html                 # macOS — just open it
python3 -m http.server 8080     # or serve it → http://localhost:8080
```

<details>
<summary><b>🌍 Deploy to spoolmojo.com</b></summary>
<br/>

Any static host works — the site is a single `index.html` (Three.js loads from cdnjs):

1. Push this repo to GitHub → enable **Pages**, or drag the folder into **Netlify** / **Cloudflare Pages** / **Vercel**.
2. Point the `spoolmojo.com` DNS at the host.
3. Done. There is nothing else.

</details>

<details>
<summary><b>✉️ How the quote form works</b></summary>
<br/>

Client-side only: submit opens the visitor's mail app via `mailto:` with the project details pre-filled, addressed to `hello@spoolmojo.com`. No server, no data stored.

Upgrade path when volume grows: point the handler at Formspree / Basin, or a tiny serverless function.

</details>

<details>
<summary><b>🌀 What the 3D hero draws</b></summary>
<br/>

A Three.js filament spool — dark flanges, layered torus windings, a loose filament tail — with drag/touch spin, idle momentum, and five clickable filament colors that recolor the windings live.

</details>

<div align="center"><img src="assets/wave.svg" width="100%" alt=""/></div>

## 🛠️ Customize

<details>
<summary><b>Change brand colors</b></summary>
<br/>

Edit the `:root` block at the top of `index.html`:

```css
:root{
  --coral:#FF5E5B; --teal:#00CECB; --yellow:#FFED66;
  --purple:#7B61FF; --ink:#241E3D; --cream:#FFF8F0;
}
```

Update the hero swatch `data-c` values if the filament presets should match.

</details>

<details>
<summary><b>Add gallery photos</b></summary>
<br/>

Replace the placeholder `.g-tile` divs with real prints:

```html
<img class="g-tile" src="assets/prints/planter-01.jpg" alt="Custom planter"/>
```

and restyle `.g-tile` to `object-fit:cover`.

</details>

<details>
<summary><b>Point the form at a different inbox</b></summary>
<br/>

In the submit handler at the bottom of `index.html`, change the `mailto:` address — and keep the helper text under the button in sync.

</details>

<details>
<summary><b>📋 Launch checklist</b></summary>
<br/>

- [ ] Real gallery photos once first prints ship
- [ ] Favicon + Open Graph tags for link previews
- [ ] Hamburger menu for mobile section links
- [ ] `prefers-reduced-motion` fallback for blobs & auto-spin
- [ ] Form backend (Formspree) when mailto gets limiting

</details>

<br/>

<div align="center">

<img src="assets/wave.svg" width="100%" alt=""/>

### Spool<span>**Mojo**</span>

*Custom products & gifts, made with mojo.*

**[spoolmojo.com](https://spoolmojo.com)** · **[hello@spoolmojo.com](mailto:hello@spoolmojo.com)**

<sub>© 2026 SpoolMojo · All ideas welcome</sub>

</div>
