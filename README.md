# Portfolio - Cinematic WebGL

Portfolio cinematic single-page dengan Three.js yang terhubung ke backend Flask API.

## 📁 Struktur Folder

```
/workspace/
├── backend/           # Flask REST API
│   ├── app.py        # Main application
│   ├── requirements.txt
│   ├── .env.example
│   └── README.md
│
├── frontend/         # Three.js Frontend
│   ├── index.html    # Single page application
│   ├── assets/       # Images & models
│   └── fonts/        # Custom fonts
│
└── database/         # SQL Schema (optional)
    └── schema.sql
```

## 🚀 Quick Start

### 1. Setup Database

```bash
mysql -u root -p < database/schema.sql
```

### 2. Setup Backend

```bash
cd backend
cp .env.example .env
# Edit .env dengan konfigurasi database Anda
pip install -r requirements.txt
python app.py
```

Backend berjalan di `http://localhost:5000`

### 3. Setup Frontend

Buka `frontend/index.html` di browser atau gunakan live server:

```bash
# Dengan Python
cd frontend
python -m http.server 8080

# Atau dengan Node.js
npx serve frontend
```

Frontend berjalan di `http://localhost:8080`

## 🔧 Configuration

### Backend (.env)

```env
DB_HOST=localhost
DB_PORT=3306
DB_NAME=portfolio_db
DB_USER=root
DB_PASSWORD=your_password
FRONTEND_URL=http://localhost:8080
SECRET_KEY=your-secret-key
```

### Frontend (index.html)

Edit `API_BASE_URL` di JavaScript:

```javascript
const API_BASE_URL = window.location.hostname === 'localhost' 
    ? 'http://localhost:5000/api' 
    : '/api';
```

## ✨ Features

### Frontend
- ✅ Cinematic Three.js background
- ✅ Scroll-driven camera movement
- ✅ Particle system dengan geometric shapes
- ✅ Custom cursor (desktop)
- ✅ Word-by-word text reveal
- ✅ Responsive design (mobile 390×844)
- ✅ Reduced motion support
- ✅ Dynamic content dari API
- ✅ Contact form terintegrasi

### Backend
- ✅ RESTful API endpoints
- ✅ CRUD operations untuk semua entities
- ✅ Contact form handler
- ✅ Emergency OTP authentication
- ✅ Visitor tracking
- ✅ CORS enabled
- ✅ Admin endpoints dengan auth

## 📡 API Integration

Frontend secara otomatis fetch data dari backend:

1. **Profile** → Hero section, About, Contact info
2. **Projects** → Projects grid
3. **Skills** → Skills categories dengan progress bars
4. **Contact Form** → Submit messages ke database

### Fallback Mode

Jika backend tidak tersedia, frontend menggunakan fallback content statis.

## 🎨 Customization

### Ganti Color Theme

Edit CSS variables di `frontend/index.html`:

```css
:root {
    --color-primary: #0a0a0a;
    --color-secondary: #1a1a2e;
    --color-accent: #00d9ff;
    --color-accent-secondary: #7c3aed;
}
```

### Update Content via API

Gunakan admin endpoints untuk update content:

```bash
curl -X PUT http://localhost:5000/api/admin/profile \
  -H "Authorization: Bearer admin-token" \
  -H "Content-Type: application/json" \
  -d '{"full_name":"Your Name","bio":"Your bio..."}'
```

## 🌐 Deployment

### Production Mode

1. **Backend:**
   - Set `FLASK_ENV=production`
   - Gunakan production database
   - Deploy dengan Gunicorn + nginx

2. **Frontend:**
   - Update `API_BASE_URL` ke production URL
   - Deploy ke Netlify/Vercel/GitHub Pages

### Environment Variables Production

```env
# Backend
DB_HOST=your-db-host.com
DB_PASSWORD=secure-password
FRONTEND_URL=https://yourdomain.com
SECRET_KEY=secure-random-key
FLASK_ENV=production
```

## 🧪 Testing

### Test API Endpoints

```bash
# Get profile
curl http://localhost:5000/api/profile

# Get projects
curl http://localhost:5000/api/projects

# Submit contact
curl -X POST http://localhost:5000/api/contact \
  -H "Content-Type: application/json" \
  -d '{"sender_name":"Test","sender_email":"test@test.com","subject":"Hi","content":"Hello"}'
```

## 📱 Mobile Testing

Test responsive design di browser DevTools:
- iPhone 12 Pro: 390 × 844
- iPad: 768 × 1024

## 🛠️ Troubleshooting

### Frontend tidak connect ke backend
- Pastikan backend running di port 5000
- Cek CORS configuration di `app.py`
- Verifikasi `API_BASE_URL` di frontend

### Database connection error
- Cek credentials di `.env`
- Pastikan MySQL service running
- Verifikasi database sudah dibuat

### Build errors
```bash
# Reinstall dependencies
pip install -r backend/requirements.txt --force-reinstall
```

## 📄 License

MIT License

## 🙏 Credits

Inspired by [Kage](https://github.com/MengTo/kage) by Meng To
