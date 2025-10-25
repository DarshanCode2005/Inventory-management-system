# Inventory Management System

A full-stack inventory management application built with FastAPI backend and React frontend, deployed on Render and Vercel.

## 🚀 Live Demo

- **Website**: [https://inventory-management-system-fronten-phi.vercel.app](https://inventory-management-system-fronten-phi.vercel.app)

## 📋 Features

### Core Functionality
- ✅ **Product Management**: Create, read, update, and delete products
- ✅ **Real-time Search**: Search products by ID, name, or description
- ✅ **Sorting**: Sort products by any column (ID, name, price, quantity)
- ✅ **Responsive Design**: Works on desktop, tablet, and mobile devices
- ✅ **Modern UI**: Clean, professional interface with gradient backgrounds
- ✅ **Error Handling**: Comprehensive error handling and user feedback
- ✅ **Auto-save**: Form validation and auto-dismiss notifications

### Technical Features
- ✅ **RESTful API**: FastAPI with automatic OpenAPI documentation
- ✅ **Database**: PostgreSQL with SQLAlchemy ORM
- ✅ **CORS Support**: Configured for cross-origin requests
- ✅ **Environment Variables**: Secure configuration management
- ✅ **Production Ready**: Deployed on cloud platforms

## 🏗️ Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   React Frontend│    │  FastAPI Backend│    │  PostgreSQL DB  │
│   (Vercel)      │◄──►│   (Render)      │◄──►│   (Render)      │
│                 │    │                 │    │                 │
│ • Product CRUD  │    │ • REST API      │    │ • Product Table │
│ • Search/Sort   │    │ • CORS Middleware│   │ • Auto Migrate  │
│ • Responsive UI │    │ • Error Handling│    │ • Sample Data   │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

## 🛠️ Tech Stack

### Backend
- **FastAPI** - Modern, fast web framework for building APIs
- **SQLAlchemy** - SQL toolkit and ORM
- **PostgreSQL** - Robust, open-source database
- **Pydantic** - Data validation using Python type annotations
- **Uvicorn** - ASGI server implementation
- **python-dotenv** - Environment variable management

### Frontend
- **React 18** - JavaScript library for building user interfaces
- **Axios** - HTTP client for API requests
- **CSS3** - Modern styling with gradients and animations
- **Create React App** - Build tooling and development server

### Deployment
- **Render** - Backend and database hosting
- **Vercel** - Frontend hosting and deployment
- **GitHub** - Version control and CI/CD

## 📁 Project Structure

```
fastapi-project/
├── 📁 frontend/                 # React frontend application
│   ├── 📁 public/              # Static assets
│   │   └── index.html          # HTML template
│   ├── 📁 src/                 # Source code
│   │   ├── App.js              # Main React component
│   │   ├── App.css             # Main styles
│   │   ├── index.js            # React entry point
│   │   └── index.css           # Global styles
│   ├── package.json            # Node.js dependencies
│   └── .gitignore              # Frontend git ignore
├── 📄 main.py                  # FastAPI application
├── 📄 models.py                # Pydantic models
├── 📄 database.py              # Database configuration
├── 📄 database_models.py       # SQLAlchemy models
├── 📄 requirements.txt         # Python dependencies
├── 📄 requirements-render.txt  # Render-specific dependencies
├── 📄 runtime.txt              # Python version specification
├── 📄 render.yaml              # Render deployment configuration
├── 📄 Procfile                 # Alternative deployment config
├── 📄 .env.example             # Environment variables template
├── 📄 .gitignore               # Git ignore rules
└── 📄 README.md                # This file
```

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- Node.js 16+
- PostgreSQL (for local development)
- Git

### Local Development

#### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd fastapi-project
```

#### 2. Backend Setup
```bash
# Create virtual environment
python -m venv myenv

# Activate virtual environment
# Windows:
myenv\Scripts\activate
# macOS/Linux:
source myenv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create .env file
cp .env.example .env
# Edit .env with your database credentials

# Run the backend
uvicorn main:app --reload
```

#### 3. Frontend Setup
```bash
cd frontend

# Install dependencies
npm install

# Start development server
npm start
```

#### 4. Access the Application
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- API Docs: http://localhost:8000/docs

## 🌐 Deployment

### Backend Deployment (Render)

#### Method 1: Using Blueprint (render.yaml)
1. Push code to GitHub
2. In Render: "New +" → "Blueprint"
3. Select your repository
4. Render will automatically create database and web service

#### Method 2: Manual Deployment
1. **Create PostgreSQL Database**:
   - Go to Render dashboard
   - "New +" → "PostgreSQL"
   - Name: `inventory-db`
   - Plan: Free
   - Create database

2. **Create Web Service**:
   - "New +" → "Web Service"
   - Connect GitHub repository
   - Settings:
     - Build Command: `pip install --upgrade pip && pip install -r requirements-render.txt --no-cache-dir`
     - Start Command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
   - Environment Variables:
     - `DATABASE_URL`: (from database service)
     - `ALLOWED_ORIGINS`: `https://your-frontend-url.vercel.app,http://localhost:3000`
     - `PYTHON_VERSION`: `3.11.0`

### Frontend Deployment (Vercel)

1. **Deploy to Vercel**:
   - Go to [vercel.com](https://vercel.com)
   - Import GitHub repository
   - Settings:
     - Framework: Create React App
     - Root Directory: `frontend`
     - Build Command: `npm run build`
     - Output Directory: `build`

2. **Set Environment Variables**:
   - In Vercel dashboard → Settings → Environment Variables
   - Add: `REACT_APP_API_URL` = `https://your-backend-url.onrender.com`

3. **Update Backend CORS**:
   - Update `ALLOWED_ORIGINS` in Render to include your Vercel URL

## 📚 API Documentation

### Base URL
```
https://your-backend-url.onrender.com
```

### Endpoints

#### Products
- `GET /products` - Get all products
- `GET /products/{id}` - Get product by ID
- `POST /products` - Create new product
- `PUT /products/{id}` - Update product
- `DELETE /products/{id}` - Delete product

#### Health Check
- `GET /` - API health check

### Example API Usage

#### Get All Products
```bash
curl https://your-backend-url/products/
```

#### Create Product
```bash
curl -X POST https://your-backend-url/products/ \
  -H "Content-Type: application/json" \
  -d '{
    "id": 1,
    "name": "Laptop",
    "description": "High-performance laptop",
    "price": 999.99,
    "quantity": 10
  }'
```

## 🗄️ Database Schema

### Product Table
```sql
CREATE TABLE product (
    id INTEGER PRIMARY KEY,
    name VARCHAR,
    description VARCHAR,
    price FLOAT,
    quantity INTEGER
);
```

### Sample Data
The application automatically initializes with sample products:
- Laptop ($999.99, Qty: 10)
- Smartphone ($699.99, Qty: 25)
- Headphones ($199.99, Qty: 50)
- Monitor ($399.99, Qty: 15)

## 🔧 Configuration

### Environment Variables

#### Backend (.env)
```env
# Database Configuration
DB_USER=postgres
DB_PASS=your_password
DB_HOST=localhost
DB_PORT=5432
DB_NAME=fastapiproj

# Alternative: Use DATABASE_URL for production
DATABASE_URL=postgresql://user:pass@host:port/dbname

# CORS Configuration
ALLOWED_ORIGINS=http://localhost:3000,https://your-frontend-url.vercel.app
```

#### Frontend (Vercel Environment Variables)
```env
REACT_APP_API_URL=https://your-backend-url.onrender.com
```

## 👨‍💻 Author

**Your Name**
- GitHub: [@yourusername](https://github.com/yourusername)
- LinkedIn: [Your LinkedIn](https://linkedin.com/in/yourprofile)

## 🙏 Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/) - The web framework used
- [React](https://reactjs.org/) - The frontend library used
- [Render](https://render.com/) - Backend and database hosting
- [Vercel](https://vercel.com/) - Frontend hosting
- [SQLAlchemy](https://www.sqlalchemy.org/) - Database ORM

## 📊 Project Status

- ✅ Backend API (FastAPI + PostgreSQL)
- ✅ Frontend UI (React)
- ✅ Database Integration
- ✅ CRUD Operations
- ✅ Search and Sort
- ✅ Responsive Design
- ✅ Production Deployment
- ✅ CORS Configuration
- ✅ Error Handling
- ✅ Environment Configuration
