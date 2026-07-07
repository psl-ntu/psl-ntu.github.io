# Parallel Systems Lab (PSL) @ NTU

Source for our [lab website](https://psl-ntu.github.io). Built with
[Hugo](https://gohugo.io) and deployed to GitHub Pages.

## Run and test locally

You need **Hugo v0.163.1 or newer**.

```sh
# macOS
brew install hugo

# then, from the repo root:
hugo server -D
```

Open <http://localhost:1313/>. The site live-reloads as you save files.

## Deploying

Just push to Github. A GitHub Actions workflow
(`.github/workflows/hugo.yaml`) builds the site and publishes it to
<https://psl-ntu.github.io> automatically. There is no manual build/upload step.

---

## Guide for students: update your photo and links

Everything about you lives in `content/people.md`, in the **Students** section.
Each person is one `<div class="person">` block:

```html
<div class="person">
  <img class="headshot" src="/static/images/people/placeholder.svg" alt="Your Name">
  <div class="p-body">
    <div class="p-name"><a>Your Name</a></div>
    <div class="p-role">Ph.D. Student</div>
  </div>
</div>
```

### 1. Add your photo

1. Add a **square** photo (e.g. 400×400) to `static/static/images/people/`,
   named like `your-name.jpg`.
2. Change your `<img ... src>` from the placeholder to your file:
   ```html
   <img class="headshot" src="/static/images/people/your-name.jpg" alt="Your Name">
   ```

### 2. Link your name to your homepage

Add an `href` to the `<a>` tag around your name — LinkedIn, Google Scholar, or a
personal site. Add `target="_blank"` to make it open in a new tab:

```html
<div class="p-name"><a href="https://www.linkedin.com/in/your-handle" target="_blank">Your Name</a></div>
```

### 3. Add yourself (new member)

Copy an existing `<div class="person">` block, paste it inside the
`<div class="people">` container, and update the name, role, photo, and link.

### 4. Preview and submit

Run `hugo server -D` and open <http://localhost:1313/people/> to check it looks
right, then commit and push (or open a pull request). The live site updates a
minute or two after your change lands on `main`.

---



## How the site is organized

| Path | What it holds |
|------|---------------|
| `content/_index.md` | Home page: headline + **News** list (edit the bullet list at the bottom) |
| `content/research.md` | Research / projects page |
| `content/publications.md` | Publications page (renders `data/publications.yaml`) |
| `content/people.md` | People page (PI + students) |
| `content/teaching.md`, `content/join.md` | Teaching and Join Us pages |
| `data/publications.yaml` | The publication list — **edit this to add/change papers** |
| `data/research_areas.yaml` | The three research-area cards on the home page |
| `static/static/images/people/` | Headshots |
| `static/static/pub/papers/` | Paper PDFs |
| `static/css/psl.css` | Site styling |
| `hugo.yaml` | Site config (title, menu, footer) |

### Adding a publication

Add an entry to the top of `papers:` in `data/publications.yaml`:

```yaml
  - title: "Paper Title"
    authors: "First Author, Chen Wang, ..."
    venue: "SC"          # short venue name shown on the chip
    year: 2026
    tags: [parallel-io, gpu]
    # award: "Best Paper"        # optional
    # highlight: true            # optional: also feature it on the home page
    # summary: "1-2 sentences..." # shown on the home page when highlighted
    links:
      doi: "https://doi.org/..."     # or an IEEE Xplore / ACM DL page
      arxiv: "https://arxiv.org/abs/..."
      pdf: "static/pub/papers/your-file.pdf"   # PDFs go in static/static/pub/papers/
      code: "https://github.com/..."
```

Buttons render only for the links you provide. The paper title links to the
first available of `doi`, `arxiv`, `pdf`, `project`, `code`.

### Updating the News feed

Edit the bullet list at the bottom of `content/_index.md`. Newest first.
