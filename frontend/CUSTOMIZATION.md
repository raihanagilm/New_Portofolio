# Customization Guide for Cinematic WebGL Portfolio

This guide provides detailed instructions for customizing every aspect of your portfolio.

## 🎨 Quick Start: Theme Presets

### Option 1: Tech/Developer (Default)
```css
:root {
    --color-primary: #0a0a0a;
    --color-secondary: #1a1a2e;
    --color-accent: #00d9ff;
    --color-accent-secondary: #7c3aed;
    --color-text: #f5f5f5;
}
```

### Option 2: Creative Designer
```css
:root {
    --color-primary: #1a1a1a;
    --color-secondary: #2d2d2d;
    --color-accent: #ff6b6b;
    --color-accent-secondary: #ffd93d;
    --color-text: #ffffff;
}
```

### Option 3: Photographer
```css
:root {
    --color-primary: #0d0d0d;
    --color-secondary: #1f1f1f;
    --color-accent: #ff8c42;
    --color-accent-secondary: #e63946;
    --color-text: #f1f1f1;
}
```

### Option 4: Minimalist
```css
:root {
    --color-primary: #ffffff;
    --color-secondary: #f0f0f0;
    --color-accent: #000000;
    --color-accent-secondary: #333333;
    --color-text: #1a1a1a;
}
```

---

## 📝 Content Replacement Checklist

### 1. Personal Information
Search and replace in `index.html`:
- `Full Name` → Your name
- `Full-Stack Developer & Tech Enthusiast` → Your title
- `admin@example.com` → Your email
- `+62 800-000-0000` → Your phone
- `City, Country` → Your location

### 2. Social Links
Replace `#` with your actual URLs:
```html
<a href="https://github.com/yourusername" class="contact-btn">GitHub</a>
<a href="https://linkedin.com/in/yourname" class="contact-btn">LinkedIn</a>
<a href="https://instagram.com/yourhandle" class="contact-btn">Instagram</a>
```

### 3. Bio Section
Update the paragraph text in `#about`:
```html
<div class="bio">
    <p>Your first paragraph here...</p>
    <p>Your second paragraph here...</p>
</div>
```

### 4. Projects
Each project card contains:
- Title (`<h3 class="project-title">`)
- Description (`<p class="project-description">`)
- Tags (`.tag` spans)
- Links (`.project-link` anchors)

Copy/paste the `<article class="project-card">` block to add more projects.

### 5. Skills
Each skill category has:
- Category name (`<h3>`)
- Skill items with progress bars

Adjust the `--progress` inline style for each skill bar:
```html
<div class="skill-progress" style="--progress: 92%"></div>
```

---

## 🎬 Three.js Scene Customization

### Adjust Particle Count
```javascript
const CONFIG = {
    particleCount: 2000,  // Increase for denser effect, decrease for performance
    // ...
};
```

### Change Camera Speed
```javascript
const CONFIG = {
    cameraSpeed: 0.0008,  // Higher = faster camera movement
    // ...
};
```

### Modify Fog Density
```javascript
const CONFIG = {
    fogDensity: 0.02,  // Higher = thicker fog, less visibility
    // ...
};
```

### Add Custom 3D Objects

For developers - add code visualization:
```javascript
function createCodeBlocks() {
    const geometry = new THREE.BoxGeometry(0.5, 0.5, 0.5);
    const material = new THREE.MeshPhongMaterial({
        color: 0x00d9ff,
        wireframe: true
    });
    
    for (let i = 0; i < 50; i++) {
        const cube = new THREE.Mesh(geometry, material);
        cube.position.set(
            (Math.random() - 0.5) * 100,
            (Math.random() - 0.5) * 100,
            (Math.random() - 0.5) * 50
        );
        scene.add(cube);
    }
}
```

For designers - add art installations:
```javascript
function createArtPieces() {
    const torusKnot = new THREE.TorusKnotGeometry(1, 0.3, 100, 16);
    const material = new THREE.MeshPhongMaterial({
        color: 0xff6b6b,
        metalness: 0.8,
        roughness: 0.2
    });
    const mesh = new THREE.Mesh(torusKnot, material);
    scene.add(mesh);
}
```

For photographers - add gallery frames:
```javascript
function createPhotoFrames() {
    const frameGeometry = new THREE.BoxGeometry(3, 2, 0.1);
    const material = new THREE.MeshPhongMaterial({
        color: 0xffffff,
        opacity: 0.8,
        transparent: true
    });
    
    for (let i = 0; i < 10; i++) {
        const frame = new THREE.Mesh(frameGeometry, material);
        frame.position.set(
            (Math.random() - 0.5) * 80,
            (Math.random() - 0.5) * 40,
            -20
        );
        scene.add(frame);
    }
}
```

---

## 🖼️ Adding Foreground Images

1. Create WebP images with transparent backgrounds
2. Place in `/assets` folder
3. Add HTML before closing `</body>` tag:

```html
<div class="foreground">
    <img src="assets/laptop.webp" 
         alt="" 
         style="position: absolute; bottom: 0; left: 0; width: 100%; max-height: 30vh; object-fit: contain;">
</div>
```

Recommended images:
- Laptop/computer silhouette
- Desk setup
- Tools relevant to your profession
- Abstract shapes matching your brand

---

## ⌨️ Typography Changes

### Change Font Family

1. Update Google Fonts link in `<head>`:
```html
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
```

2. Update CSS variable:
```css
:root {
    --font-family: 'Poppins', sans-serif;
}
```

### Adjust Font Sizes

```css
:root {
    --font-size-hero: clamp(3rem, 8vw, 6rem);      /* Main title */
    --font-size-title: clamp(2rem, 5vw, 4rem);     /* Section titles */
    --font-size-subtitle: clamp(1.25rem, 3vw, 2rem); /* Subtitles */
    --font-size-body: clamp(1rem, 2vw, 1.25rem);   /* Body text */
}
```

---

## 🎯 Camera Path Customization

The camera follows a path based on scroll position. Modify in `animate()`:

```javascript
function animate() {
    // Current: Linear descent
    const targetCameraY = 10 - scrollProgress * 50;
    const targetCameraZ = 30 - scrollProgress * 20;
    
    // Alternative: Spiral path
    // const targetCameraY = Math.sin(scrollProgress * Math.PI * 4) * 20;
    // const targetCameraZ = 30 - scrollProgress * 30;
    // const targetCameraX = Math.cos(scrollProgress * Math.PI * 4) * 20;
    
    // Alternative: Zigzag
    // const targetCameraY = 10 - scrollProgress * 50;
    // const targetCameraZ = 30 - scrollProgress * 20 + Math.sin(scrollProgress * 10) * 5;
}
```

---

## 📱 Mobile Optimization

### Adjust Section Height
```css
:root {
    --spacing-section: clamp(80vh, 100vh, 120vh);  /* Reduce for mobile */
}
```

### Reduce Particle Count on Mobile
```javascript
const isMobile = window.innerWidth < 768;
const CONFIG = {
    particleCount: isMobile ? 800 : 2000,
    // ...
};
```

---

## ♿ Accessibility Improvements

### Keyboard Navigation
Already implemented via semantic HTML. Test with Tab key.

### Screen Reader Support
All interactive elements have `aria-label` attributes.

### Reduced Motion
Automatically disabled when user prefers reduced motion:
```css
@media (prefers-reduced-motion: reduce) {
    /* All animations minimized */
}
```

---

## 🚀 Performance Tips

### For Slower Devices
1. Reduce particle count to 1000
2. Lower renderer pixel ratio:
```javascript
renderer.setPixelRatio(Math.min(window.devicePixelRatio, 1.5));
```

### Optimize Images
- Use WebP format
- Compress to < 200KB each
- Use appropriate dimensions (max 1920px width)

### Lazy Load Sections
Already implemented via IntersectionObserver.

---

## 🎨 Advanced: Custom Shaders

For advanced users, add custom shaders to particles:

```javascript
const shaderMaterial = new THREE.ShaderMaterial({
    uniforms: {
        time: { value: 0 },
        color: { value: new THREE.Color(0x00d9ff) }
    },
    vertexShader: `
        uniform float time;
        void main() {
            vec3 pos = position;
            pos.y += sin(time + pos.x) * 0.5;
            gl_Position = projectionMatrix * modelViewMatrix * vec4(pos, 1.0);
        }
    `,
    fragmentShader: `
        uniform vec3 color;
        void main() {
            gl_FragColor = vec4(color, 0.8);
        }
    `
});
```

---

## 📊 Analytics Integration

Add Google Analytics or other tracking before `</head>`:

```html
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=GA_MEASUREMENT_ID"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'GA_MEASUREMENT_ID');
</script>
```

---

## 🎭 Easter Eggs & Interactions

Add click interactions:

```javascript
document.addEventListener('click', (e) => {
    // Create particle burst at click position
    createParticleBurst(e.clientX, e.clientY);
});

function createParticleBurst(x, y) {
    // Implementation for particle explosion effect
}
```

---

## ✅ Pre-Launch Checklist

- [ ] Replace all placeholder content
- [ ] Update social media links
- [ ] Test on multiple devices
- [ ] Check accessibility (screen reader, keyboard nav)
- [ ] Verify all external links work
- [ ] Optimize images
- [ ] Test reduced motion preference
- [ ] Add analytics if needed
- [ ] Set up custom domain (optional)
- [ ] Submit to search engines

---

**Need help?** Open an issue on GitHub or check the documentation at [threejs.org](https://threejs.org/docs/).
