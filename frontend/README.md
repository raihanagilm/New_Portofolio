# Cinematic WebGL Portfolio

A cinematic, single-page WebGL portfolio inspired by [Kage](https://github.com/MengTo/kage), built with Three.js for smooth scroll-driven storytelling.

## ✨ Features

- **Scroll-Driven Camera Movement**: Continuous 3D camera path controlled by scroll position
- **Procedural Particle Environment**: 2000+ animated particles with color gradients
- **Floating Geometric Shapes**: Wireframe icosahedrons, octahedrons, and torus shapes
- **Custom Cursor**: Interactive cursor with hover states (desktop only)
- **Text Reveal Animations**: Character-by-character text reveal on scroll
- **Responsive Design**: Optimized for desktop and mobile (390×844 minimum)
- **Reduced Motion Support**: Respects user's motion preferences
- **5 Scroll Chapters**: Hero, About, Projects, Skills, Contact

## 🎨 Customization Guide

### 1. Color Palette

Edit CSS variables in the `<style>` section:

```css
:root {
    /* Tech/Developer Theme */
    --color-primary: #0a0a0a;
    --color-secondary: #1a1a2e;
    --color-accent: #00d9ff;
    --color-accent-secondary: #7c3aed;
    --color-text: #f5f5f5;
    
    /* Creative Theme */
    --color-primary: #1a1a1a;
    --color-secondary: #2d2d2d;
    --color-accent: #ff6b6b;
    --color-accent-secondary: #ffd93d;
    --color-text: #ffffff;
    
    /* Photographer Theme */
    --color-primary: #0d0d0d;
    --color-secondary: #1f1f1f;
    --color-accent: #ff8c42;
    --color-accent-secondary: #e63946;
    --color-text: #f1f1f1;
}
```

### 2. Three.js Configuration

Edit the `CONFIG` object in the JavaScript section:

```javascript
const CONFIG = {
    cameraSpeed: 0.0008,      // Camera movement speed
    particleCount: 2000,       // Number of particles
    colors: {
        primary: 0x0a0a0a,
        secondary: 0x1a1a2e,
        accent: 0x00d9ff,
        accentSecondary: 0x7c3aed
    },
    fogDensity: 0.02,          // Atmospheric fog density
    bloomStrength: 0.5         // Post-processing bloom
};
```

### 3. Typography

Change the font family in CSS:

```css
:root {
    --font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    
    /* Font sizes are responsive using clamp() */
    --font-size-hero: clamp(3rem, 8vw, 6rem);
    --font-size-title: clamp(2rem, 5vw, 4rem);
    --font-size-subtitle: clamp(1.25rem, 3vw, 2rem);
}
```

### 4. Content Replacement

Update content directly in the HTML:

- **Hero Section**: Change name and title in `#hero`
- **About Section**: Update bio text in `#about`
- **Projects**: Modify project cards in `#projects`
- **Skills**: Edit skill categories and progress bars in `#skills`
- **Contact**: Update email and social links in `#contact`

### 5. 3D Background Scene

To customize the 3D scene for different professions:

#### For Developers:
```javascript
// Add code-like structures
function createCodeVisualization() {
    // Create floating code blocks or binary digits
}
```

#### For Designers:
```javascript
// Add creative studio elements
function createArtInstallations() {
    // Create abstract geometric sculptures
}
```

#### For Photographers:
```javascript
// Add gallery space elements
function createGallerySpace() {
    // Create picture frames or camera equipment
}
```

### 6. Camera Path

Modify the camera movement in the `animate()` function:

```javascript
function animate() {
    // Adjust target positions based on scroll
    const targetCameraY = 10 - scrollProgress * 50;
    const targetCameraZ = 30 - scrollProgress * 20;
    
    // Smooth interpolation
    camera.position.y += (targetCameraY - camera.position.y) * CONFIG.cameraSpeed;
    camera.position.z += (targetCameraZ - camera.position.z) * CONFIG.cameraSpeed;
}
```

### 7. Foreground Images

Add WebP images with alpha channels at the bottom of viewport:

```html
<div class="foreground">
    <img src="assets/laptop.webp" alt="" style="position: absolute; bottom: 0; left: 0; width: 100%;">
</div>
```

## 📁 File Structure

```
portfolio/
├── index.html          # Main HTML file with inline CSS/JS
├── assets/             # Folder for images and models
│   └── (add your .webp files here)
└── fonts/              # Folder for custom fonts
    └── (add your font files here)
```

## 🚀 Deployment

### GitHub Pages

1. Push to GitHub repository
2. Go to Settings > Pages
3. Select branch: `main` and folder: `/portfolio`
4. Your site will be live at `https://username.github.io/repository/portfolio/`

### Netlify

1. Drag and drop the `portfolio` folder to Netlify Drop
2. Or connect GitHub repository for automatic deployments

### Vercel

```bash
npm i -g vercel
cd portfolio
vercel
```

## 📱 Responsive Breakpoints

- **Desktop**: 1400px+ (full experience)
- **Tablet**: 768px - 1399px (adjusted layout)
- **Mobile**: 390px - 767px (single column)
- **Small Mobile**: < 390px (minimal layout)

## ♿ Accessibility

- Semantic HTML5 with ARIA labels
- Reduced motion support via `prefers-reduced-motion`
- Keyboard navigation support
- Screen reader friendly
- High contrast text

## ⚡ Performance

- 60fps animation target
- Lazy loading for sections
- Optimized particle count
- Efficient scroll listeners
- Minimal external dependencies (only Three.js)

## 🎯 Browser Support

- Chrome/Edge (latest)
- Firefox (latest)
- Safari (latest)
- Mobile browsers (iOS Safari, Chrome Mobile)

## 📝 License

MIT License - Feel free to use for personal or commercial projects.

## 🙏 Credits

- Inspired by [Kage by Meng To](https://github.com/MengTo/kage)
- Three.js library from [threejs.org](https://threejs.org)
- Inter font from Google Fonts

---

**Ready to customize?** Open `index.html` and start editing the configuration and content to match your personal brand!
