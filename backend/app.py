"""
Portfolio Backend API
Flask REST API untuk mengelola data portfolio dari database MySQL
"""

from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta
import os
import random
import string
from dotenv import load_dotenv
from functools import wraps

# Load environment variables
load_dotenv()

app = Flask(__name__)

# CORS Configuration
CORS(app, origins=[
    os.getenv('FRONTEND_URL', 'http://localhost:8080'),
    'http://127.0.0.1:8080',
    'https://yourdomain.com'
])

# Database Configuration
db_host = os.getenv('DB_HOST', 'localhost')
db_port = os.getenv('DB_PORT', '3306')
db_name = os.getenv('DB_NAME', 'portfolio_db')
db_user = os.getenv('DB_USER', 'root')
db_password = os.getenv('DB_PASSWORD', '')

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret-key')

db = SQLAlchemy(app)

# ==================== MODELS ====================

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(20), default='admin')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class EmergencyOTP(db.Model):
    __tablename__ = 'emergency_otps'
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), nullable=False)
    otp_code = db.Column(db.String(6), nullable=False)
    requested_at = db.Column(db.DateTime, default=datetime.utcnow)
    expires_at = db.Column(db.DateTime, nullable=False)
    is_used = db.Column(db.Boolean, default=False)

class VisitorLog(db.Model):
    __tablename__ = 'visitor_logs'
    
    id = db.Column(db.Integer, primary_key=True)
    ip_address = db.Column(db.String(45))
    user_agent = db.Column(db.String(255))
    path = db.Column(db.String(100), default='/')
    visited_at = db.Column(db.DateTime, default=datetime.utcnow)

class Profile(db.Model):
    __tablename__ = 'profiles'
    
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False, default='Full Name')
    title = db.Column(db.String(150), default='Full-Stack Developer & UI/UX Designer')
    bio = db.Column(db.Text)
    avatar_url = db.Column(db.String(255), default='')
    resume_url = db.Column(db.String(255), default='')
    github = db.Column(db.String(150), default='')
    linkedin = db.Column(db.String(150), default='')
    instagram = db.Column(db.String(150), default='')
    facebook = db.Column(db.String(150), default='')
    twitter = db.Column(db.String(150), default='')
    youtube = db.Column(db.String(150), default='')
    website = db.Column(db.String(150), default='')
    email = db.Column(db.String(120), default='admin@example.com')
    phone = db.Column(db.String(30), default='+62 800-000-0000')
    location = db.Column(db.String(100), default='City, Country')

class Experience(db.Model):
    __tablename__ = 'experiences'
    
    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String(100), nullable=False)
    position = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), default='Kerja')
    period = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text)
    order_index = db.Column(db.Integer, default=0)
    is_visible = db.Column(db.Boolean, default=True)

class Education(db.Model):
    __tablename__ = 'educations'
    
    id = db.Column(db.Integer, primary_key=True)
    institution = db.Column(db.String(120), nullable=False)
    degree = db.Column(db.String(100), nullable=False)
    major = db.Column(db.String(100))
    period = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text)
    type = db.Column(db.String(20), default='education')
    credential_url = db.Column(db.String(255), default='')
    is_visible = db.Column(db.Boolean, default=True)

class Skill(db.Model):
    __tablename__ = 'skills'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    category = db.Column(db.String(50), default='Technical')
    proficiency = db.Column(db.Integer, default=85)
    icon = db.Column(db.String(50), default='code')
    is_visible = db.Column(db.Boolean, default=True)

class Project(db.Model):
    __tablename__ = 'projects'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text)
    image_url = db.Column(db.String(255))
    demo_url = db.Column(db.String(255))
    github_url = db.Column(db.String(255))
    category = db.Column(db.String(50), default='Web App')
    tags = db.Column(db.String(200), default='Flask, Tailwind, MySQL')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    is_visible = db.Column(db.Boolean, default=True)

class ProjectImage(db.Model):
    __tablename__ = 'project_images'
    
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id', ondelete='CASCADE'), nullable=False)
    image_url = db.Column(db.String(255), nullable=False)
    
    project = db.relationship('Project', backref=db.backref('images', lazy=True, cascade='all, delete-orphan'))

class Message(db.Model):
    __tablename__ = 'messages'
    
    id = db.Column(db.Integer, primary_key=True)
    sender_name = db.Column(db.String(100), nullable=False)
    sender_email = db.Column(db.String(120), nullable=False)
    subject = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    is_read = db.Column(db.Boolean, default=False)

# ==================== HELPER FUNCTIONS ====================

def log_visitor(path):
    """Log visitor information"""
    try:
        ip = request.remote_addr
        user_agent = request.headers.get('User-Agent', '')[:255]
        
        log = VisitorLog(ip_address=ip, user_agent=user_agent, path=path)
        db.session.add(log)
        db.session.commit()
    except Exception as e:
        print(f"Error logging visitor: {e}")
        db.session.rollback()

def generate_otp(length=6):
    """Generate random OTP code"""
    return ''.join(random.choices(string.digits, k=length))

def admin_required(f):
    """Decorator for admin-only routes"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # In production, implement proper JWT authentication
        token = request.headers.get('Authorization')
        if not token or token != 'Bearer admin-token':
            return jsonify({'error': 'Unauthorized'}), 401
        return f(*args, **kwargs)
    return decorated_function

# ==================== PUBLIC ROUTES ====================

@app.route('/api/profile', methods=['GET'])
def get_profile():
    """Get portfolio profile data"""
    log_visitor('/api/profile')
    
    profile = Profile.query.first()
    if not profile:
        return jsonify({'error': 'Profile not found'}), 404
    
    return jsonify({
        'id': profile.id,
        'full_name': profile.full_name,
        'title': profile.title,
        'bio': profile.bio,
        'avatar_url': profile.avatar_url,
        'resume_url': profile.resume_url,
        'email': profile.email,
        'phone': profile.phone,
        'location': profile.location,
        'social': {
            'github': profile.github,
            'linkedin': profile.linkedin,
            'instagram': profile.instagram,
            'facebook': profile.facebook,
            'twitter': profile.twitter,
            'youtube': profile.youtube,
            'website': profile.website
        }
    })

@app.route('/api/experiences', methods=['GET'])
def get_experiences():
    """Get all visible experiences ordered by order_index"""
    log_visitor('/api/experiences')
    
    experiences = Experience.query.filter_by(is_visible=True).order_by(Experience.order_index).all()
    
    return jsonify([{
        'id': exp.id,
        'company': exp.company,
        'position': exp.position,
        'category': exp.category,
        'period': exp.period,
        'description': exp.description
    } for exp in experiences])

@app.route('/api/educations', methods=['GET'])
def get_educations():
    """Get all visible educations"""
    log_visitor('/api/educations')
    
    educations = Education.query.filter_by(is_visible=True).all()
    
    return jsonify([{
        'id': edu.id,
        'institution': edu.institution,
        'degree': edu.degree,
        'major': edu.major,
        'period': edu.period,
        'description': edu.description,
        'type': edu.type,
        'credential_url': edu.credential_url
    } for edu in educations])

@app.route('/api/skills', methods=['GET'])
def get_skills():
    """Get all visible skills grouped by category"""
    log_visitor('/api/skills')
    
    skills = Skill.query.filter_by(is_visible=True).all()
    
    # Group by category
    categories = {}
    for skill in skills:
        if skill.category not in categories:
            categories[skill.category] = []
        categories[skill.category].append({
            'id': skill.id,
            'name': skill.name,
            'proficiency': skill.proficiency,
            'icon': skill.icon
        })
    
    return jsonify(categories)

@app.route('/api/projects', methods=['GET'])
def get_projects():
    """Get all visible projects with images"""
    log_visitor('/api/projects')
    
    projects = Project.query.filter_by(is_visible=True).order_by(Project.created_at.desc()).all()
    
    result = []
    for project in projects:
        project_data = {
            'id': project.id,
            'title': project.title,
            'description': project.description,
            'content': project.content,
            'image_url': project.image_url,
            'demo_url': project.demo_url,
            'github_url': project.github_url,
            'category': project.category,
            'tags': project.tags.split(', ') if project.tags else [],
            'created_at': project.created_at.isoformat(),
            'images': [img.image_url for img in project.images]
        }
        result.append(project_data)
    
    return jsonify(result)

@app.route('/api/projects/<int:project_id>', methods=['GET'])
def get_project(project_id):
    """Get single project details"""
    log_visitor(f'/api/projects/{project_id}')
    
    project = Project.query.get(project_id)
    if not project:
        return jsonify({'error': 'Project not found'}), 404
    
    return jsonify({
        'id': project.id,
        'title': project.title,
        'description': project.description,
        'content': project.content,
        'image_url': project.image_url,
        'demo_url': project.demo_url,
        'github_url': project.github_url,
        'category': project.category,
        'tags': project.tags.split(', ') if project.tags else [],
        'created_at': project.created_at.isoformat(),
        'images': [img.image_url for img in project.images]
    })

# ==================== CONTACT FORM ====================

@app.route('/api/contact', methods=['POST'])
def submit_contact():
    """Submit contact message"""
    log_visitor('/api/contact')
    
    data = request.get_json()
    
    if not data:
        return jsonify({'error': 'No data provided'}), 400
    
    required_fields = ['sender_name', 'sender_email', 'subject', 'content']
    for field in required_fields:
        if field not in data or not data[field]:
            return jsonify({'error': f'{field} is required'}), 400
    
    try:
        message = Message(
            sender_name=data['sender_name'],
            sender_email=data['sender_email'],
            subject=data['subject'],
            content=data['content']
        )
        db.session.add(message)
        db.session.commit()
        
        # TODO: Send email notification using Resend or SMTP
        
        return jsonify({
            'success': True,
            'message': 'Message sent successfully!'
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# ==================== ADMIN ROUTES ====================

@app.route('/api/admin/messages', methods=['GET'])
@admin_required
def get_messages():
    """Get all messages (admin only)"""
    messages = Message.query.order_by(Message.created_at.desc()).all()
    
    return jsonify([{
        'id': msg.id,
        'sender_name': msg.sender_name,
        'sender_email': msg.sender_email,
        'subject': msg.subject,
        'content': msg.content,
        'created_at': msg.created_at.isoformat(),
        'is_read': msg.is_read
    } for msg in messages])

@app.route('/api/admin/messages/<int:message_id>/read', methods=['PUT'])
@admin_required
def mark_message_read(message_id):
    """Mark message as read (admin only)"""
    message = Message.query.get(message_id)
    if not message:
        return jsonify({'error': 'Message not found'}), 404
    
    message.is_read = True
    db.session.commit()
    
    return jsonify({'success': True})

@app.route('/api/admin/profile', methods=['PUT'])
@admin_required
def update_profile():
    """Update profile data (admin only)"""
    data = request.get_json()
    
    profile = Profile.query.first()
    if not profile:
        return jsonify({'error': 'Profile not found'}), 404
    
    # Update fields
    updatable_fields = ['full_name', 'title', 'bio', 'avatar_url', 'resume_url', 
                       'email', 'phone', 'location', 'github', 'linkedin', 
                       'instagram', 'facebook', 'twitter', 'youtube', 'website']
    
    for field in updatable_fields:
        if field in data:
            setattr(profile, field, data[field])
    
    db.session.commit()
    
    return jsonify({'success': True, 'message': 'Profile updated'})

@app.route('/api/admin/skills', methods=['POST'])
@admin_required
def create_skill():
    """Create new skill (admin only)"""
    data = request.get_json()
    
    required_fields = ['name', 'category', 'proficiency']
    for field in required_fields:
        if field not in data:
            return jsonify({'error': f'{field} is required'}), 400
    
    skill = Skill(
        name=data['name'],
        category=data.get('category', 'Technical'),
        proficiency=data.get('proficiency', 85),
        icon=data.get('icon', 'code'),
        is_visible=data.get('is_visible', True)
    )
    
    db.session.add(skill)
    db.session.commit()
    
    return jsonify({'success': True, 'id': skill.id}), 201

@app.route('/api/admin/skills/<int:skill_id>', methods=['DELETE'])
@admin_required
def delete_skill(skill_id):
    """Delete skill (admin only)"""
    skill = Skill.query.get(skill_id)
    if not skill:
        return jsonify({'error': 'Skill not found'}), 404
    
    db.session.delete(skill)
    db.session.commit()
    
    return jsonify({'success': True})

@app.route('/api/admin/projects', methods=['POST'])
@admin_required
def create_project():
    """Create new project (admin only)"""
    data = request.get_json()
    
    required_fields = ['title', 'description']
    for field in required_fields:
        if field not in data:
            return jsonify({'error': f'{field} is required'}), 400
    
    project = Project(
        title=data['title'],
        description=data['description'],
        content=data.get('content'),
        image_url=data.get('image_url'),
        demo_url=data.get('demo_url'),
        github_url=data.get('github_url'),
        category=data.get('category', 'Web App'),
        tags=', '.join(data.get('tags', [])),
        is_visible=data.get('is_visible', True)
    )
    
    db.session.add(project)
    db.session.commit()
    
    return jsonify({'success': True, 'id': project.id}), 201

@app.route('/api/admin/projects/<int:project_id>', methods=['PUT'])
@admin_required
def update_project(project_id):
    """Update project (admin only)"""
    data = request.get_json()
    
    project = Project.query.get(project_id)
    if not project:
        return jsonify({'error': 'Project not found'}), 404
    
    updatable_fields = ['title', 'description', 'content', 'image_url', 
                       'demo_url', 'github_url', 'category', 'tags', 'is_visible']
    
    for field in updatable_fields:
        if field in data:
            setattr(project, field, data[field])
    
    db.session.commit()
    
    return jsonify({'success': True})

@app.route('/api/admin/projects/<int:project_id>', methods=['DELETE'])
@admin_required
def delete_project(project_id):
    """Delete project (admin only)"""
    project = Project.query.get(project_id)
    if not project:
        return jsonify({'error': 'Project not found'}), 404
    
    db.session.delete(project)
    db.session.commit()
    
    return jsonify({'success': True})

# ==================== EMERGENCY OTP ====================

@app.route('/api/auth/request-otp', methods=['POST'])
def request_otp():
    """Request emergency OTP for login"""
    data = request.get_json()
    
    if not data or 'email' not in data:
        return jsonify({'error': 'Email is required'}), 400
    
    email = data['email']
    
    # Check if user exists
    user = User.query.filter_by(email=email).first()
    if not user:
        return jsonify({'error': 'User not found'}), 404
    
    # Generate OTP
    otp_code = generate_otp()
    expires_at = datetime.utcnow() + timedelta(minutes=10)
    
    # Invalidate previous OTPs
    EmergencyOTP.query.filter_by(email=email, is_used=False).update({'is_used': True})
    
    # Create new OTP
    otp = EmergencyOTP(
        email=email,
        otp_code=otp_code,
        expires_at=expires_at
    )
    
    db.session.add(otp)
    db.session.commit()
    
    # TODO: Send OTP via email using Resend or SMTP
    # For now, return OTP in response (only for development!)
    return jsonify({
        'success': True,
        'message': 'OTP generated (check console in development)',
        'otp_code': otp_code  # Remove in production!
    })

@app.route('/api/auth/verify-otp', methods=['POST'])
def verify_otp():
    """Verify OTP code"""
    data = request.get_json()
    
    if not data or 'email' not in data or 'otp_code' not in data:
        return jsonify({'error': 'Email and OTP code are required'}), 400
    
    email = data['email']
    otp_code = data['otp_code']
    
    # Find valid OTP
    otp = EmergencyOTP.query.filter_by(
        email=email,
        otp_code=otp_code,
        is_used=False
    ).first()
    
    if not otp:
        return jsonify({'error': 'Invalid or expired OTP'}), 401
    
    if otp.expires_at < datetime.utcnow():
        return jsonify({'error': 'OTP has expired'}), 401
    
    # Mark OTP as used
    otp.is_used = True
    db.session.commit()
    
    # Get user
    user = User.query.filter_by(email=email).first()
    
    return jsonify({
        'success': True,
        'message': 'OTP verified successfully',
        'user': {
            'id': user.id,
            'email': user.email,
            'role': user.role
        }
    })

# ==================== ERROR HANDLERS ====================

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Endpoint not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return jsonify({'error': 'Internal server error'}), 500

# ==================== INITIALIZE DATABASE ====================

def init_db():
    """Initialize database tables"""
    with app.app_context():
        db.create_all()
        print("Database tables created successfully!")

if __name__ == '__main__':
    init_db()
    
    port = int(os.getenv('PORT', 5000))
    debug = os.getenv('FLASK_ENV') == 'development'
    
    app.run(host='0.0.0.0', port=port, debug=debug)
