# Portfolio Backend & Frontend

Full-stack portfolio application dengan cinematic WebGL frontend dan Flask REST API backend.

## 📁 Struktur Project

```
portfolio/
├── backend/           # Flask REST API
│   ├── app.py        # Main application
│   ├── .env.example  # Environment variables template
│   └── requirements.txt
├── frontend/         # Three.js WebGL UI
│   ├── index.html    # Single page application
│   ├── assets/       # Images & models
│   └── fonts/        # Custom fonts
└── README.md         # This file
```

## 🚀 Quick Start

### 1. Setup Backend

```bash
cd backend

# Install dependencies
pip install -r requirements.txt

# Copy environment file
cp .env.example .env

# Edit .env dengan konfigurasi database Anda
# Lihat bagian "Environment Configuration" di bawah

# Jalankan server
python app.py
```

Backend akan berjalan di `http://localhost:5000`

### 2. Setup Frontend

```bash
cd frontend

# Menggunakan Python HTTP Server
python -m http.server 8080

# Atau menggunakan Node.js (jika ada)
npx serve .
```

Frontend akan berjalan di `http://localhost:8080`

## 🔧 Environment Configuration

### Backend (.env)

**Opsi 1: TiDB/Cloud MySQL (Recommended)**
```env
DATABASE_URL=mysql+pymysql://user:password@host:port/dbname?ssl_ca=/path/to/ca.pem
SECRET_KEY=your-secret-key-here
FLASK_ENV=development
RESEND_API_KEY=re_xxxxxxxxxxxxx
SENDER_EMAIL=onboarding@resend.dev
PERSONAL_EMAIL=admin@example.com
CLOUDINARY_CLOUD_NAME=your_cloud
CLOUDINARY_API_KEY=your_key
CLOUDINARY_API_SECRET=your_secret
FRONTEND_URL=http://localhost:8080
```

**Opsi 2: Local MySQL**
```env
DB_HOST=localhost
DB_PORT=3306
DB_NAME=portfolio_db
DB_USER=root
DB_PASSWORD=your_password
SECRET_KEY=your-secret-key-here
FLASK_ENV=development
FRONTEND_URL=http://localhost:8080
```

## 📡 API Endpoints

### Public Endpoints
- `GET /api/profile` - Portfolio profile data
- `GET /api/experiences` - Work experiences
- `GET /api/educations` - Education history
- `GET /api/skills` - Skills grouped by category
- `GET /api/projects` - All projects
- `GET /api/projects/<id>` - Single project
- `POST /api/contact` - Submit contact message

### Admin Endpoints (Requires Auth)
- `GET /api/admin/messages` - Get all messages
- `PUT /api/admin/messages/<id>/read` - Mark as read
- `PUT /api/admin/profile` - Update profile
- `POST /api/admin/skills` - Create skill
- `DELETE /api/admin/skills/<id>` - Delete skill
- `POST /api/admin/projects` - Create project
- `PUT /api/admin/projects/<id>` - Update project
- `DELETE /api/admin/projects/<id>` - Delete project

### Authentication
- `POST /api/auth/request-otp` - Request OTP
- `POST /api/auth/verify-otp` - Verify OTP

## 🗄️ Database Setup

Jalankan schema SQL untuk membuat tabel:

```bash
mysql -u root -p portfolio_db < ../database/schema.sql
```

Atau copy paste schema dari file `database/schema.sql` ke MySQL client Anda.

## 🎨 Features

### Backend
- ✅ RESTful API dengan Flask
- ✅ MySQL/TiDB integration via SQLAlchemy
- ✅ CORS support untuk frontend terpisah
- ✅ Email notifications via Resend API
- ✅ OTP authentication untuk admin
- ✅ Contact form handler
- ✅ Visitor tracking
- ✅ Environment-based configuration

### Frontend
- ✅ Cinematic WebGL dengan Three.js
- ✅ Scroll-driven animations
- ✅ Dynamic content dari API backend
- ✅ Responsive design (mobile + desktop)
- ✅ Custom cursor (desktop)
- ✅ Reduced motion support
- ✅ 5 sections: Hero, About, Projects, Skills, Contact

## 🌐 Deployment

### Production Checklist

1. **Backend:**
   - Set `FLASK_ENV=production`
   - Gunakan production database
   - Setup SSL/HTTPS
   - Configure Gunicorn/uWSGI
   - Setup reverse proxy (nginx)

2. **Frontend:**
   - Update API_BASE_URL di `index.html`
   - Build optimization (minify HTML/CSS/JS)
   - Deploy ke static hosting (Netlify/Vercel/GitHub Pages)

3. **Database:**
   - Backup data
   - Enable SSL connection
   - Setup firewall rules
   - Monitor performance

### GitHub Pages Deployment

```bash
# Frontend
cd frontend
# Upload ke GitHub repository
# Enable GitHub Pages di Settings
```

## 🧪 Testing

Test API dengan cURL:

```bash
# Get profile
curl http://localhost:5000/api/profile

# Get skills
curl http://localhost:5000/api/skills

# Submit contact
curl -X POST http://localhost:5000/api/contact \
  -H "Content-Type: application/json" \
  -d '{"sender_name":"Test","sender_email":"test@test.com","subject":"Hi","content":"Hello"}'
```

## 🛠️ Troubleshooting

### Database Connection Error
- Pastikan MySQL service running
- Cek credentials di `.env`
- Verifikasi database sudah dibuat
- Untuk TiDB: pastikan SSL CA path benar

### CORS Error
- Pastikan `FRONTEND_URL` di `.env` sesuai
- Tambahkan origin frontend ke list CORS di `app.py`

### API Not Loading
- Cek console browser untuk errors
- Pastikan backend running di port 5000
- Verify API endpoints dengan curl/postman

## 📝 License

MIT License
