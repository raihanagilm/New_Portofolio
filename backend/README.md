# Portfolio Backend API

Flask REST API backend untuk mengelola data portfolio dari database MySQL.

## 📋 Prerequisites

- Python 3.8+
- MySQL/TiDB database
- pip (Python package manager)

## 🚀 Installation

1. **Clone repository dan masuk ke folder backend:**
```bash
cd backend
```

2. **Buat virtual environment (opsional tapi disarankan):**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# atau
venv\Scripts\activate  # Windows
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Setup environment variables:**
```bash
cp .env.example .env
```

Edit file `.env` dan sesuaikan konfigurasi database Anda:
```env
DB_HOST=localhost
DB_PORT=3306
DB_NAME=portfolio_db
DB_USER=root
DB_PASSWORD=your_password
FRONTEND_URL=http://localhost:8080
SECRET_KEY=your-secret-key-here
```

5. **Jalankan database migration (jika belum ada):**
```bash
mysql -u root -p portfolio_db < ../database/schema.sql
```

## 🎯 Running the Server

```bash
python app.py
```

Server akan berjalan di `http://localhost:5000`

## 📡 API Endpoints

### Public Endpoints

#### Get Profile
```http
GET /api/profile
```

#### Get Experiences
```http
GET /api/experiences
```

#### Get Educations
```http
GET /api/educations
```

#### Get Skills (grouped by category)
```http
GET /api/skills
```

#### Get All Projects
```http
GET /api/projects
```

#### Get Single Project
```http
GET /api/projects/<id>
```

#### Submit Contact Message
```http
POST /api/contact
Content-Type: application/json

{
  "sender_name": "John Doe",
  "sender_email": "john@example.com",
  "subject": "Project Inquiry",
  "content": "Hello, I'd like to discuss..."
}
```

### Admin Endpoints (Requires Authentication)

Semua endpoint admin memerlukan header:
```http
Authorization: Bearer admin-token
```

#### Get All Messages
```http
GET /api/admin/messages
```

#### Mark Message as Read
```http
PUT /api/admin/messages/<id>/read
```

#### Update Profile
```http
PUT /api/admin/profile
Content-Type: application/json

{
  "full_name": "Your Name",
  "title": "Your Title",
  "bio": "Your bio...",
  "email": "your@email.com"
}
```

#### Create Skill
```http
POST /api/admin/skills
Content-Type: application/json

{
  "name": "React.js",
  "category": "Frontend",
  "proficiency": 90,
  "icon": "react"
}
```

#### Delete Skill
```http
DELETE /api/admin/skills/<id>
```

#### Create Project
```http
POST /api/admin/projects
Content-Type: application/json

{
  "title": "Project Name",
  "description": "Short description",
  "content": "Detailed content",
  "category": "Web App",
  "tags": ["React", "Node.js"],
  "demo_url": "https://...",
  "github_url": "https://..."
}
```

#### Update Project
```http
PUT /api/admin/projects/<id>
```

#### Delete Project
```http
DELETE /api/admin/projects/<id>
```

### Authentication Endpoints

#### Request Emergency OTP
```http
POST /api/auth/request-otp
Content-Type: application/json

{
  "email": "admin@example.com"
}
```

#### Verify OTP
```http
POST /api/auth/verify-otp
Content-Type: application/json

{
  "email": "admin@example.com",
  "otp_code": "123456"
}
```

## 🔐 Security Notes

**PENTING:** Dalam production:
1. Ganti `admin-token` dengan JWT authentication yang proper
2. Jangan return OTP code di response (hanya untuk development)
3. Gunakan HTTPS
4. Implement rate limiting
5. Sanitasi semua input user

## 🗄️ Database Schema

Backend menggunakan schema yang sama dengan database SQL yang disediakan. Tabel yang digunakan:
- `users` - Admin users
- `profiles` - Portfolio profile data
- `experiences` - Work experiences
- `educations` - Education history
- `skills` - Technical skills
- `projects` - Portfolio projects
- `project_images` - Project images
- `messages` - Contact form messages
- `emergency_otps` - OTP codes for login
- `visitor_logs` - Analytics

## 🧪 Testing with cURL

Test get profile:
```bash
curl http://localhost:5000/api/profile
```

Test submit contact form:
```bash
curl -X POST http://localhost:5000/api/contact \
  -H "Content-Type: application/json" \
  -d '{"sender_name":"Test","sender_email":"test@test.com","subject":"Hi","content":"Hello"}'
```

## 📦 Deployment

### Production Setup

1. Set `FLASK_ENV=production`
2. Gunakan production database server
3. Setup reverse proxy (nginx/Apache)
4. Gunakan WSGI server (Gunicorn/uWSGI)
5. Enable HTTPS
6. Setup proper logging

### Gunicorn Example
```bash
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

## 🛠️ Troubleshooting

### Database Connection Error
- Pastikan MySQL service running
- Cek credentials di `.env`
- Verifikasi database sudah dibuat

### CORS Error
- Pastikan `FRONTEND_URL` di `.env` sesuai dengan URL frontend
- Tambahkan origin frontend ke list di `app.py`

### Module Not Found
```bash
pip install -r requirements.txt
```

## 📝 License

MIT License
